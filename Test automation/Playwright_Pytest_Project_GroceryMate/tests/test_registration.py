from framework.pages.auth_page import AuthPage
from framework.dataclasses.data_object_user import User
from framework.dataclasses.test_data import TestUsers
from framework.system_config import BASE_URL

def test_create_account(browser_page):
    """
    Testet erfolgreiche Registrierung eines neuen Users
    1. Neuen User anlegen
    2. Account registrieren
    3. mit diesem Account anmelden
    4. innerhalb der Methode prüfen, ob Toast angezeigt wird, dass die Registrierung erfolgreich war
    """
    # Arrange
    auth_page = AuthPage(browser_page)
    new_user = User.generate_new_user()
    success_toast = browser_page.locator("text=Registration successful")

    # Act: Account erstellen (navigiert intern zur auth-page) & Assert (intern: success-toast)
    auth_page.create_account(new_user)

def test_login(browser_page):
    """
    Testet erfolgreichen Login mit existierendem User
    1. navigiert zur Login-Seite
    2. loggt sich mit einem existierenden User an
    """

    #Arrange
    auth_page = AuthPage(browser_page)
    existing_user = TestUsers.EXISTING

    #Act:
    auth_page.go_to_login()
    homepage = auth_page.login(existing_user)

    # Assert: prüfen ob die Homepage geladen wird
    assert homepage.is_loaded(), f"Erwartete URL: {BASE_URL}, aktuelle URL: {homepage.page.url}"
