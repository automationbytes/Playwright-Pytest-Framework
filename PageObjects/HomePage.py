from playwright.sync_api import Page

class HomePage:
    appLogo_selector = "//div[text()='Swag Labs']"
    filter_selector = "//select[@data-test='product-sort-container']"
    openMenu_selector = '#react-burger-menu-btn'
    logOut_selector = "//a[text()='Logout']"

    def __init__(self, page: Page):
        self.page = page

    def verifyLogo(self) -> bool:
        return self.page.locator(self.appLogo_selector).is_visible()

    def selectFilterDropdown(self, value: str) -> None:
        self.page.locator(self.filter_selector).select_option(label=value)

    def clickLogout(self) -> None:
        self.page.locator(self.openMenu_selector).click()
        self.page.locator(self.logOut_selector).click()