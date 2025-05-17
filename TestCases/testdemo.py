# import pytest
# import allure
# import os
# from playwright.sync_api import expect
# from dotenv import load_dotenv
# from PageObjects.LoginPage import LoginPage
# from PageObjects.HomePage import HomePage
# from Util.generateLogs import LogGenerator
#
# load_dotenv()
#
#
# class TestDemo:
#     logger = LogGenerator.loggen()
#
#     @allure.title("Verify price sorting from high to low")
#     @allure.description("Test sorting functionality in inventory page")
#     @allure.feature("Inventory Management")
#     @allure.story("Price Sorting Validation")
#     @pytest.mark.parametrize("sort_option,expected_text", [
#         ("Price (high to low)", "Price (high to low)"),
#         ("Price (low to high)", "Price (low to high)")
#     ], ids=["high_to_low", "low_to_high"])
#     def test_price_sorting(self, setup, sort_option, expected_text):
#         self.page = setup
#
#         with allure.step("Login to application"):
#             self._perform_login()
#
#         with allure.step("Verify home page elements"):
#             self._verify_homepage_elements()
#
#         with allure.step(f"Apply {sort_option} filter"):
#             self._apply_price_filter(sort_option, expected_text)
#
#     def _perform_login(self):
#         self.logger.info("Navigating to base URL")
#         self.page.goto(os.getenv("BASE_URL"))
#
#         self.logger.info("Executing login sequence")
#         (LoginPage(self.page)
#          .enterUsername(os.getenv("STANDARD_USER"))
#          .enterPassword(os.getenv("PASSWORD"))
#          .clickLogin())
#
#         expect(self.page).to_have_url(f"{os.getenv('BASE_URL')}/inventory.html")
#
#     def _verify_homepage_elements(self):
#         hp = HomePage(self.page)
#         try:
#             expect(hp.logo).to_be_visible(timeout=5000)
#             allure.attach(
#                 self.page.screenshot(type="png"),
#                 name="homepage-verified",
#                 attachment_type=allure.attachment_type.PNG
#             )
#         except AssertionError as error:
#             self._capture_failure("homepage-verification", error)
#             raise
#
#     def _apply_price_filter(self, sort_option, expected_text):
#         hp = HomePage(self.page)
#         try:
#             with allure.step("Select filter from dropdown"):
#                 hp.select_filter_dropdown(sort_option)
#
#             with allure.step("Verify active filter"):
#                 expect(hp.active_filter).to_have_text(expected_text, timeout=3000)
#
#             allure.attach(
#                 self.page.screenshot(type="png"),
#                 name=f"after-{sort_option.replace(' ', '-')}-filter",
#                 attachment_type=allure.attachment_type.PNG
#             )
#
#             with allure.step("Validate price sorting"):
#                 prices = hp.get_product_prices()
#                 if "high" in sort_option.lower():
#                     assert prices == sorted(prices, reverse=True),
#                     "Prices not in descending order"
#             else:
#             assert prices == sorted(prices),
#             "Prices not in ascending order"
#
# except (AssertionError, Exception) as error:
# self._capture_failure("filter-application", error)
# raise
#
#
# def _capture_failure(self, step_name, error):
#     self.logger.error(f"Failure during {step_name}: {str(error)}")
#     screenshot_path = f"failure_{step_name}_{os.getpid()}.png"
#     self.page.screenshot(path=screenshot_path)
#     allure.attach.file(
#         screenshot_path,
#         name=step_name,
#         attachment_type=allure.attachment_type.PNG
#     )