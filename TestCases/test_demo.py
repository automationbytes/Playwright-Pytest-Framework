# # import pytest
# # from selenium import webdriver
# #
# # from PageObjects.LoginPage import LoginPage
# # from PageObjects.HomePage import HomePage
# # from Util.generateLogs import LogGenerator
# # from Util.readConfig import readConfig
# #
# #
# #
# # class TestDemo:
# #     logger = LogGenerator.loggen()
# #
# #     @pytest.fixture()
# #     def login(self,setup):
# #         self.logger.info("------------Pre Step-----------------")
# #         self.driver = setup
# #         self.driver.maximize_window()
# #         self.driver.implicitly_wait(int(readConfig.getConfig("commoninfo","timeout")))
# #         self.logger.info("------------URL Launch-----------------")
# #         self.driver.get(readConfig.getConfig("commoninfo","baseURL"))
# #         lp = LoginPage(self.driver)
# #         lp.enterUsername(readConfig.getConfig("commoninfo","username"))
# #         lp.enterPassword(readConfig.getConfig("commoninfo","password"))
# #         lp.clickLogin()
# #
# #
# #     def test_dropdown_high2low(self,login):
# #         self.logger.info("------------Home Launch-----------------")
# #         hp = HomePage(self.driver)
# #         if hp.verifyLogo():
# #             assert True
# #         else:
# #             self.driver.save_screenshot("logo.png")
# #         self.logger.info("------------Filter dropdown-----------------")
# #         hp.selectFilterDropdown("Price (high to low)")
# #
# #
#
#
# import pytest
# from playwright.sync_api import expect
# from PageObjects.LoginPage import LoginPage
# from PageObjects.HomePage import HomePage
# from Util.generateLogs import LogGenerator
# from Util.readConfig import readConfig
#
# import pytest
# from playwright.sync_api import expect
# from PageObjects.LoginPage import LoginPage
# from PageObjects.HomePage import HomePage
# from Util.generateLogs import LogGenerator
# from Util.readConfig import readConfig
#
#
# class TestDemo:
#     logger = LogGenerator.loggen()
#
#     @pytest.fixture()
#     def login(self, setup):
#         self.logger.info("------------Pre Step-----------------")
#         self.page = setup
#         self.logger.info("------------Set Viewport-----------------")
#         self.page.set_viewport_size({"width": 1920, "height": 1080})
#
#         self.logger.info("------------URL Launch-----------------")
#         self.page.goto(readConfig.getConfig("commoninfo", "baseURL"))
#
#         self.logger.info("------------Perform Login-----------------")
#         lp = LoginPage(self.page)
#         lp.enterUsername(readConfig.getConfig("commoninfo", "username"))
#         lp.enterPassword(readConfig.getConfig("commoninfo", "password"))
#         lp.clickLogin()
#
#         yield  # Teardown will happen after test completion
#
#     def test_dropdown_high2low(self, login):
#         self.logger.info("------------Home Launch-----------------")
#         hp = HomePage(self.page)
#
#         self.logger.info("------------Verify Logo-----------------")
#         try:
#             assert hp.verifyLogo(), "Logo verification failed"
#         except AssertionError:
#             self.page.screenshot(path="logo.png")
#             raise
#
#         self.logger.info("------------Filter dropdown-----------------")
#         hp.selectFilterDropdown("Price (high to low)")
#
#         # Add verification for sorting if needed
#         # Example: expect(hp.first_item).to_have_text("Expected Item")

import pytest
from playwright.sync_api import expect
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from Util.generateLogs import LogGenerator
from Util.readConfig import readConfig
import allure


class TestDemo:
    logger = LogGenerator.loggen()

    @pytest.fixture()
    def login(self, setup):
        """Fixture to perform login and setup test environment"""
        self.logger.info("------------Pre Step-----------------")
        self.page = setup

        # Set consistent viewport size
        self.logger.info("------------Set Viewport-----------------")
        self.page.set_viewport_size({"width": 1920, "height": 1080})

        # Navigation and login
        self.logger.info("------------URL Launch-----------------")
        self.page.goto(readConfig.getConfig("commoninfo", "baseURL"))

        self.logger.info("------------Perform Login-----------------")
        lp = LoginPage(self.page)
        lp.enterUsername(readConfig.getConfig("commoninfo", "username"))
        lp.enterPassword(readConfig.getConfig("commoninfo", "password"))
        lp.clickLogin()

        # Verify successful login
        expect(self.page).to_have_url(f"{readConfig.getConfig('commoninfo', 'baseURL')}inventory.html")

        yield  # Teardown happens after test completion

    @allure.title("Verify Price Sorting from High to Low")
    @allure.description("Test validation of price sorting functionality")
    def test_dropdown_high2low(self, login):
        """Test case for price sorting validation"""
        self.logger.info("------------Home Launch-----------------")
        hp = HomePage(self.page)

        with allure.step("Verify application logo"):
            try:
                # Use Playwright's built-in assertions
                expect(hp.logo).to_be_visible()
                allure.attach(
                    self.page.screenshot(type='png'),
                    name='logo-verification',
                    attachment_type=allure.attachment_type.PNG
                )
            except AssertionError as error:
                self.logger.error("Logo verification failed")
                allure.attach(
                    self.page.screenshot(type='png'),
                    name='logo-failure',
                    attachment_type=allure.attachment_type.PNG
                )
                raise error

        with allure.step("Select price filter and validate sorting"):
            # Select the dropdown option
            hp.selectFilterDropdown("Price (high to low)")

            # Verify active filter selection
            expect(hp.active_filter).to_have_text("Price (high to low)")

            # Get and validate prices
            prices = hp.get_product_prices()
            assert prices == sorted(prices, reverse=True), \
                "Prices not sorted in descending order"

            # Attach evidence
            allure.attach(
                self.page.screenshot(type='png'),
                name='after-sorting',
                attachment_type=allure.attachment_type.PNG
            )