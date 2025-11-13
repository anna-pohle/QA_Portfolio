from playwright.sync_api import sync_playwright
from framework.system_config import BROWSER_CONFIG
import pytest


@pytest.fixture
#öffne browser & stelle ein page Objekt zur Verfügung
def browser_page():
    with sync_playwright() as playwright:
        #öffne Browser
        browser = playwright.chromium.launch(**BROWSER_CONFIG)
        page = browser.new_page()

        #stelle page zur Verfügung
        yield page
        #aufräumen: browser wieder schließen
        browser.close()

