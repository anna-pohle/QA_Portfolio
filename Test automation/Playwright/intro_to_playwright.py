from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #launch Chromium based browser
    browser = playwright.chromium.launch(headless=False, slow_mo=5000)

   # Open new Page
    page = browser.new_page()

    # Navigate to URL
    page.goto("https://playwright.dev/python")

    #Locate element
    docs_button = page.get_by_role("link", name="Docs")

    #click Element
    docs_button.click()

    browser.close()
