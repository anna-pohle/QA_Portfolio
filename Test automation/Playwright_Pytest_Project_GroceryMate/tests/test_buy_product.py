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