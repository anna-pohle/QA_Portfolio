from pages.base_page import EXTENDED_TIMEOUT


def test_create_account(auth_page):
    test_data = {"email":"palimmm@web.de", "password":"pommes", "name":"didi"}

    #methode create account nutzen
    auth_page.create_account(test_data["email"], test_data["password"], test_data["name"])

    #methode login nutzen
    auth_page.login(test_data["email"], test_data["password"])

    # prüfen ob sich die URL zur startseite ändert
    auth_page.page.wait_for_url("https://grocerymate.masterschool.com/", timeout=EXTENDED_TIMEOUT)