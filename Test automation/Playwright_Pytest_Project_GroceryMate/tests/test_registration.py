import pytest

from pages.auth_page import AuthPage
from tests.testdata_config import AuthData
from system_config import BASE_URL


def test_create_account_and_login(browser_page):
    """
    erfolgreiche Registrierung eines neuen Users + anschließender Login
    1. Neuen User anlegen
    2. Account registrieren
    3. mit diesem Account anmelden
    4. Prüfen ob Homepage geladen wird
    """

    #Arrange
    auth_page = AuthPage(browser_page)
    new_user = AuthData.new_user()

    #Act: Account erstellen (navigiert intern zur auth-page)
    auth_page.create_account(
        email=new_user.email,
        password=new_user.password,
        name= new_user.name
    )

    #Act: Login (ist nach create_account weiterhin auf Auth-Seite)
    homepage = auth_page.login(
            email=new_user.email,
            password=new_user.password
    )

    # Assert: prüfen ob die Homepage geladen wird
    homepage.page.wait_for_url(BASE_URL)
    assert homepage.page.url == BASE_URL, f"Erwartete URL: {BASE_URL}, aktuelle URL: {homepage.page.url}"


