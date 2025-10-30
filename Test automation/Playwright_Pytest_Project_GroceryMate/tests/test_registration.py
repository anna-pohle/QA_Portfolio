from pkg_resources import CHECKOUT_DIST

from pages.authentification_page import AuthPage
from pages.base_page import EXTENDED_TIMEOUT
from pages.store_page import StorePage


def test_create_account(browser_page):
    test_data = {"email":"palimmm3@web.de", "password":"pommes1", "name":"didi1"}

    auth_page = AuthPage(browser_page)
    auth_page.login(test_data["email"], test_data["password"])

    homepage = HomePage(browser_page)
    homepage.gotoStore()
    storepage = StorePage(browser_page)
    storepage.addtoCart()
    storepage.clickCart()
    checkoutpage = CheckoutPage(browser_page)
    checkoutpage.checkout()

    # prüfen ob sich die URL zur startseite ändert
    auth_page.page.wait_for_url("https://grocerymate.masterschool.com/", timeout=EXTENDED_TIMEOUT)
