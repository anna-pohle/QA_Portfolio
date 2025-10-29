from playwright.sync_api import sync_playwright
from pages.authentification_page import AuthPage


def test_create_account():
    test_data = {"email":"", "password":"", "name":""}
    with sync_playwright() as playwright:
        # browser starten
        browser = playwright.chromium.launch(headless=False, slow_mo=50)

        # page object erstellen
        page = browser.new_page()

        # authPage erstellen/'aktivieren'
        auth_page = AuthPage(page)

        #methode create account nutzen
        auth_page.create_account(test_data["email"], test_data["password"], test_data["name"])

        #methode login nutzen
        auth_page.login()

        # prüfen ob sich die URL zur startseite ändert
        assert page.url == "https://grocerymate.masterschool.com/