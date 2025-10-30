from playwright.sync_api import sync_playwright
from pages.authentification_page import AuthPage
import pytest


@pytest.fixture
#öffne browser & stelle ein page Objekt zur Verfügung
def browser_page():
    with sync_playwright() as playwright:
        #öffne browser
        browser = playwright.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()

        #stelle page zur Verfügung
        yield page
        #aufräumen: browser wieder schließen
        browser.close()

@pytest.fixture
# Nimm das Page-Objekt & mach daraus eine fertige AuthPage
def auth_page(browser_page):
    return AuthPage