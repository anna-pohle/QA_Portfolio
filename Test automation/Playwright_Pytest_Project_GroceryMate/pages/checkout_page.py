from pages.base_page import BasePage

class CheckoutPage(BasePage):
    URL = "https://grocerymate.masterschool.com/checkout"

    def navigate(self):
        self.navigate(self.URL)

    def __init__(self, page):
        super().__init__(page)
