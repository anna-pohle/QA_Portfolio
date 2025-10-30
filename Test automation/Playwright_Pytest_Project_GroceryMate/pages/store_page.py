from pages.base_page import BasePage, DEFAULT_TIMEOUT

def StorePage(BasePage):
    URL = "https://grocerymate.masterschool.com/"

    def navigate(self):
        self.navigate(self.URL)

    def __init__(self, page):
        super().__init__(page)
