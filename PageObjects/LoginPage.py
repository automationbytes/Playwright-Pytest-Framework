from playwright.sync_api import Page

class LoginPage:
    username_selector = '#user-name'         # CSS selector for ID
    password_selector = '[name="password"]'  # CSS attribute selector
    login_button_selector = '[name="login-button"]'

    def __init__(self, page: Page):
        self.page = page

    def enterUsername(self, user: str) -> None:
        self.page.locator(self.username_selector).fill(user)

    def enterPassword(self, password: str) -> None:
        self.page.locator(self.password_selector).fill(password)

    def clickLogin(self) -> None:
        self.page.locator(self.login_button_selector).click()