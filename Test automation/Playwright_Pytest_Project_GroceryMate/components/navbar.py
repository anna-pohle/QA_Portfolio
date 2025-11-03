class Navbar:
    def __init__(self, page):
        self.page = page
        self.store_button = page.locator("")
        self.home_button = page.locator("")


    def click_store(self):
        self.store_button.click()
        from pages.store_page import StorePage
        return StorePage(self.page)

    def click_home(self):
        self.home_button.click()
        from pages.home_page import HomePage
        return HomePage(self.page)