from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from framework.pages.base_page import BasePage
    from framework.pages.home_page import HomePage


class CheckoutPage(BasePage):
    URL = "https://grocerymate.masterschool.com/checkout"

    def navigate(self, URL): #-> CheckoutPage:
        # Option, die Seite direkt via URL aufzurufen
        self.navigate(self.URL)
        return CheckoutPage(self.page)

    def __init__(self, page):
        super().__init__(page)

        #Locators
        self.street_input = page.get_by_placeholder("Street Address")
        self.city_input = page.get_by_placeholder("City")
        self.postal_code_input = page.get_by_placeholder("Postal Code")
        self.card_number_input = page.get_by_placeholder("Card number")
        self.name_on_card_input = page.get_by_placeholder("Name on card")
        self.expiration_input = page.get_by_placeholder("Expiration")
        self.cvv_input = page.get_by_placeholder("Cvv")
        self.buy_now_button = page.get_by_role("button", name="Buy now")

    def fill_address(self, street: str, city: str, postal_code: str): #-> CheckoutPage:
        # Füllt die Adressfelder aus
        self.street_input.fill(street)
        self.city_input.fill(city)
        self.postal_code_input.fill(postal_code)
        return CheckoutPage(self.page)

    def fill_payment(self, card_number: str, name_on_card: str, expiration: str, cvv: str): #-> CheckoutPage:
        # Füllt die Zahlungsfelder aus
        self.card_number_input.fill(card_number)
        self.name_on_card_input.fill(name_on_card)
        self.expiration_input.fill(expiration)
        self.cvv_input.fill(cvv)
        return CheckoutPage(self.page)


    def complete_checkout(self, address_data: dict, payment_data: dict) -> HomePage:
        # Füllt alle Felder aus und schließt Checkout ab
        self.fill_address(**address_data)
        self.fill_payment(**payment_data)
        self.buy_now_button.click()
        return HomePage(self.page)