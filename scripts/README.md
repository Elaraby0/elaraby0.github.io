# Google Scholar citation refresh

`python3 scripts/update_scholar.py` validates the public Ahmed Elaraby profile and
reads the **Citations / All** metric. The output in `data/scholar.json` includes the
last successful verification time. Both About pages render the count with
`{{< scholar-citations >}}`, using Arabic or English wording as appropriate.
The verification time remains in the data file and is not displayed on the site.

The existing Pages workflow checks once daily at **04:17 UTC**, and on a manual
workflow run on `master`. A successful refresh is committed to `master` before
that same workflow builds and deploys it. Normal code pushes do not fetch Scholar.
Only the refresh job has repository write permission. It refuses a stale branch
head and never force-pushes. No GitHub changes occur when this script runs locally.

`--allow-stale` retains the previous count **and its original verification time**
when Scholar blocks requests, changes markup, or cannot be reached. It emits a
workflow warning. A missing/invalid cache is an error. This is a best-effort daily
check, not a live connection; it makes one bounded request and does not bypass
CAPTCHAs. GitHub may delay scheduled runs or disable them after 60 days without
repository activity. Successful daily refresh commits normally provide activity;
extended fetch failures may require re-enabling the workflow in Actions.

Run the focused checks with:

```sh
python3 -m unittest discover -s tests -p 'test_update_scholar.py'
```

This workflow becomes active only after the user-approved changes are pushed to
the default branch. The local preview does not activate the schedule.
