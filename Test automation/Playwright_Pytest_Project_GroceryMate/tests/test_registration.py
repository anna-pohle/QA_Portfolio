from pages.auth_page import AuthPage
from tests.testdata_config import AuthData
from system_config import BASE_URL

def test_create_account(browser_page):
    """
    Testet erfolgreiche Registrierung eines neuen Users
    1. Neuen User anlegen
    2. Account registrieren
    3. mit diesem Account anmelden
    4. Prüfen, ob Toast angezeigt wird, dass die Registrierung erfolgreich war
    """
    # Arrange
    auth_page = AuthPage(browser_page)
    new_user = AuthData.new_user()

    # Act: Account erstellen (navigiert intern zur auth-page)
    auth_page.create_account(
        email=new_user.email,
        password=new_user.password,
        name=new_user.name
    )

    # Assert
    success_toast = browser_page.locator("text=Registration successful")
    success_toast.wait_for(state="visible")
    assert success_toast.is_visible(), "Success-Toast nicht angezeigt!"

def test_login(browser_page):
    """
    Testet erfolgreichen Login mit existierendem User
    1. navigiert zur Login-Seite
    2. loggt sich mit einem existierenden User an
    """

    #Arrange
    auth_page = AuthPage(browser_page)
    existing_user = AuthData.EXISTING_USER

    #Act:
    auth_page.go_to_login()
    homepage = auth_page.login(existing_user.email, existing_user.password)

    # Assert: prüfen ob die Homepage geladen wird
    homepage.page.wait_for_url(BASE_URL)
    assert homepage.page.url == BASE_URL, f"Erwartete URL: {BASE_URL}, aktuelle URL: {homepage.page.url}"
