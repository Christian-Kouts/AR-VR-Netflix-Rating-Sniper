from playwright.sync_api import sync_playwright
import os

user_data_dir = 'C:\\Users\\chris\\AppData\\Local\\Microsoft\\Edge\\User Data'

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir=user_data_dir,
        channel="msedge",
        headless=False
    )


    page = browser.new_page()
    page.wait_for_timeout(1000)
    page.goto("https://www.netflix.com/browse")
    page.wait_for_timeout(1000)

    for i in range(1,5):

        row_selector = f'div#row-{i}'  # Create the row selector dynamically
        row_element = page.locator(row_selector)
        row_element.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        page.screenshot(path=f"netflix_row_{i}_screenshot.png")

    browser.close()