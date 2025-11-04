from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.store_page import StorePage

@pytest.fixture
def logged_in_user(page):
    # Eingeloggter User
    login_page = AuthPage(page)
    login_page.login("user@test.com", "password")
    return page

def test_buy_product(logged_in_user):
    """
checkout_page = CheckoutPage(BasePage)
    .goto_store()
    .add_to_cart()
    .click_cart()
    .checkout())
    """