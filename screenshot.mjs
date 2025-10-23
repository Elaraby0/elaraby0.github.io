import puppeteer from "puppeteer";

const url = process.argv[2];
const browser = await puppeteer.launch({ headless: "new" });
const page = await browser.newPage();
await page.goto(url, { waitUntil: "networkidle0", timeout: 60000 });
const el = await page.$("figure.entry-cover");
if (el) {
  await el.screenshot({ path: "cover.png" });
  const bbox = await el.boundingBox();
  console.log("Bounding box:", bbox);
} else {
  console.log("No entry-cover figure found");
}
await browser.close();
