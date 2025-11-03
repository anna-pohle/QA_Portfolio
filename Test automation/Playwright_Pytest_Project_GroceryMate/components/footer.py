class Footer:

    def __init__(self, page):
        self.page = page
        self.auth_button = page.locator("")
        self.login_button = page.locator("")
        self.register_button = page.locator("")
        self.logout_button = page.locator("")

    def click_logout(self):
        self.logout_button.click()
        from pages.auth_page import AuthPage
        return AuthPage(self.page)
