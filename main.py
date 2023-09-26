from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    print(page.locator("xpath=//div[@class='login_password']").inner_text().split('\n')[1])