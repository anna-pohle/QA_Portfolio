from pages.auth_page import AuthPage
from testdata_config import AuthData
from system_config import EXTENDED_TIMEOUT


def test_create_account_and_login(browser_page):
    #erfolgreiche Registrierung eines neuen Users

    #Arrange
    auth_page = AuthPage(browser_page)
    new_user = AuthData.NEW_USER

    #Act & Assert 1
    auth_page.create_account(**new_user)
    assert "auth" in browser_page.url, "Nicht auf der Auth-Seite!"

    #Act & Assert 2
    auth_page.login(
            email=new_user["email"],
            password=new_user["password"])
    # prüfen ob sich die URL zur startseite ändert:
    auth_page.page.wait_for_url("https://grocerymate.masterschool.com/", timeout=EXTENDED_TIMEOUT)

    assert "auth" not in browser_page.url, "Sollte nicht mehr auf Auth-Seite sein"