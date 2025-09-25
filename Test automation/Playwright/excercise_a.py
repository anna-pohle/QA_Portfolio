#Exercises Based on playwright_excercise_a_sourcecode.py

from playwright.sync_api import sync_playwright
from playwright_excercise_a_sourcecode import html_content


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3000)
    page = browser.new_page()

    page.set_content(html_content)


    """
    # Exercise 1 — Click the Login Button
    # Goal: Click the Login button using a role locator.
    """
    login_button = page.get_by_role("button", name="Login")

    #to keep my script running for this exercise
    login_button.evaluate("button => button.addEventListener('click', e => e.preventDefault())")

    login_button.click()


    """
    Exercise 2 — Fill Email and Password
    Goal: Use label locators to fill:
    Email: student@example.com
    Password: Password123
    """
    fields_to_fill = {
        "Email": "student@example.com",
        "Password": "Password123"
    }

    for label, value in fields_to_fill.items():
        page.get_by_label(label).fill(value)


    """
    Exercise 3 — Fill Search Box
    Playwright Exercise 2
    Goal: Use placeholder locator to fill the search input with:
    "Playwright Guide"
    """
    search_box = page.get_by_placeholder("Search products…")
    search_box.fill("Playwright Guide")


    """
    Exercise 4 — Click Sign Up
    Goal: Click the Sign Up button using a role locator.
    """
    signup_btn = page.get_by_role("button", name="Sign Up")
    signup_btn.click()

    """
    Exercise 5 — Click Links
    Goal: Use text locators to click the About Us link in the header navigation.
    """
    about_link = page.get_by_text("About Us")
    about_link.click()


    """
    Exercise 6 — Click Images
    Goal: Click the Company Logo and Cart Icon using alt text locators.
    """
    company_logo = page.get_by_alt_text("Company Logo")
    # works only with real webpage/real image:
    # company_logo.click

    cart_icon = page.get_by_alt_text("Cart Icon")
    # works only with real webpage/real image:
    # cart_icon.click


    """
    Exercise 7 — Combined Actions (Challenge)
    """
    # 1. Fill email and password (label locators)
    # 2. Click Login button (role locator)
    # 3. Fill search input (placeholder locator)
    # 4. Click Search button (role locator)
    # 5. Click Cart Icon (alt text locator)

    browser.close()

print("Script completed!")