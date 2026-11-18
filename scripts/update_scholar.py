#!/usr/bin/env python3
"""Refresh one public Scholar profile; never replace verified data on failure."""

import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from urllib.request import Request, urlopen

PROFILE_ID = "dFUfLfAAAAAJ"
PROFILE_URL = f"https://scholar.google.com/citations?user={PROFILE_ID}&hl=en"
PROFILE_NAME = "Ahmed Elaraby"
DEFAULT_OUTPUT = Path(__file__).resolve().parents[1] / "data" / "scholar.json"


class ProfileParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.name_parts = []
        self.name_depth = 0
        self.name_count = 0
        self.table_depth = 0
        self.table_count = 0
        self.table_closed = False
        self.rows = []
        self.row = None
        self.cell = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "div":
            if attrs.get("id") == "gsc_prf_in":
                self.name_count += 1
                self.name_depth = 1
            elif self.name_depth:
                self.name_depth += 1
        if tag == "table":
            if attrs.get("id") == "gsc_rsb_st":
                self.table_count += 1
                self.table_depth = 1
            elif self.table_depth:
                self.table_depth += 1
        if self.table_depth == 1:
            if tag == "tr":
                self.row = []
            elif tag in ("td", "th") and self.row is not None:
                self.cell = []

    def handle_data(self, data):
        if self.name_depth:
            self.name_parts.append(data)
        if self.table_depth == 1 and self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if tag == "div" and self.name_depth:
            self.name_depth -= 1
        if self.table_depth == 1:
            if tag in ("td", "th") and self.cell is not None:
                self.row.append(" ".join("".join(self.cell).split()))
                self.cell = None
            elif tag == "tr" and self.row is not None:
                self.rows.append(self.row)
                self.row = None
        if tag == "table" and self.table_depth:
            self.table_depth -= 1
            if not self.table_depth:
                self.table_closed = True


def parse_citations(html):
    parser = ProfileParser()
    parser.feed(html)
    parser.close()
    name = " ".join("".join(parser.name_parts).split())
    if parser.name_count != 1 or name != PROFILE_NAME:
        raise ValueError("Expected Scholar profile identity was not found")
    if parser.table_count != 1 or not parser.table_closed or parser.table_depth:
        raise ValueError("Complete Scholar metrics table was not found")
    headers = [row for row in parser.rows if row.count("All") == 1]
    if len(headers) != 1:
        raise ValueError("Unambiguous all-time metrics column was not found")
    column = headers[0].index("All")
    if column == 0:
        raise ValueError("Metrics table has no row-label column")
    metrics = {}
    for label in ("Citations", "h-index", "i10-index"):
        rows = [row for row in parser.rows if row and row[0] == label]
        if len(rows) != 1 or len(rows[0]) != len(headers[0]):
            raise ValueError(f"Missing or malformed {label} row")
        value = rows[0][column]
        if not re.fullmatch(r"(?:0|[1-9][0-9]*|[1-9][0-9]{0,2}(?:,[0-9]{3})+)", value):
            raise ValueError(f"Invalid {label} count")
        metrics[label] = int(value.replace(",", ""))
    if (metrics["Citations"] < metrics["h-index"] ** 2
            or metrics["Citations"] < 10 * metrics["i10-index"]):
        raise ValueError("Scholar citation count is inconsistent with its indices")
    return metrics["Citations"]


def fetch_html():
    request = Request(PROFILE_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=30) as response:
        if response.status != 200:
            raise ValueError(f"Unexpected HTTP status: {response.status}")
        payload = response.read(2_000_001)
        if len(payload) > 2_000_000:
            raise ValueError("Unexpectedly large Scholar response")
        return payload.decode(response.headers.get_content_charset() or "utf-8")


def parse_timestamp(value):
    timestamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if timestamp.tzinfo is None:
        raise ValueError("Verification timestamp must include a timezone")
    return timestamp


def read_verified(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if (data.get("profile_id") != PROFILE_ID
            or data.get("profile_url") != PROFILE_URL
            or data.get("name") != PROFILE_NAME
            or type(data.get("citations")) is not int
            or data["citations"] < 0):
        raise ValueError("Stored Scholar data is invalid")
    parse_timestamp(data["checked_at"])
    return data


def refresh(path, fetcher=fetch_html, now=None):
    previous = read_verified(path) if path.exists() else None
    citations = parse_citations(fetcher())
    checked = now or datetime.now(timezone.utc)
    if checked.tzinfo is None:
        raise ValueError("Verification timestamp must include a timezone")
    if previous and checked < parse_timestamp(previous["checked_at"]):
        raise ValueError("Refusing to replace newer verified data with an older reading")
    data = {
        "profile_id": PROFILE_ID,
        "profile_url": PROFILE_URL,
        "name": PROFILE_NAME,
        "citations": citations,
        "checked_at": checked.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as handle:
            temporary = Path(handle.name)
            json.dump(data, handle, indent=2)
            handle.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()
    return data


def main(argv=None):
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    cli.add_argument("--allow-stale", action="store_true", help="Allow a build to retain valid cached data if refresh fails")
    args = cli.parse_args(argv)
    try:
        data = refresh(args.output)
    except Exception as error:
        print(f"Scholar refresh failed: {type(error).__name__}: {error}", file=sys.stderr)
        if args.allow_stale:
            try:
                data = read_verified(args.output)
            except Exception:
                return 1
            print(f"::warning::Retaining {data['citations']} citations, last verified {data['checked_at']}.")
            return 0
        return 1
    print(f"Verified {data['citations']} citations at {data['checked_at']}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
