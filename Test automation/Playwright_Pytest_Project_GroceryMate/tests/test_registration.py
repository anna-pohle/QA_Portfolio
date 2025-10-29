from playwright.sync_api import sync_playwright
from pages.authentification_page import AuthPage


def test_create_account():
    with sync_playwright() as playwright:
        # browser starten
        browser = playwright.chromium.launch(headless=False, slow_mo=50)

        # page object erstellen
        page = browser.new_page()

        # authPage erstellen/'aktivieren'
        auth_page = AuthPage(page)

        #methode create account nutzen

        #methode login nutzen

        # prüfen ob sich die URL zur startseite ändert