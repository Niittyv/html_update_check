from playwright.sync_api import sync_playwright
from pathlib import Path

url = "https://en.wikipedia.org/wiki/Power_of_10"

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto(url, wait_until="domcontentloaded")
    print(page.title())

    html = page.content()
    Path("remote.html").write_text(html, encoding="utf-8")

    browser.close()