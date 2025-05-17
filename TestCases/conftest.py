import pytest
from playwright.sync_api import sync_playwright
from Util.generateLogs import LogGenerator

logger = LogGenerator.loggen()


def pytest_addoption(parser):
    parser.addoption(
        "--app-headed",  # Changed from --headed
        action="store_true",
        help="Run tests in headed mode (visible browser)"
    )
    parser.addoption(
        "--app-browser",  # Changed from "--browser"
        action="store",
        default="chrome",
        help="Choose the browser: chrome, edge or firefox"
    )


@pytest.fixture(scope="function")
def browser(request):
    return request.config.getoption("--app-browser")  # Updated

#
# @pytest.fixture(scope="function")
# def setup(request, browser):
#     headed = request.config.getoption("--app-headed")  # Updated
#
#     with sync_playwright() as playwright:
#         if browser == "chrome":
#             browser_instance = playwright.chromium.launch(
#                 channel="chrome",
#                 headless=not headed  # 👈 Toggle based on flag
#             )
#         elif browser == "edge":
#             browser_instance = playwright.chromium.launch(
#                 channel="msedge",
#                 headless=not headed  # 👈 Toggle based on flag
#             )
#         elif browser == "firefox":
#             browser_instance = playwright.firefox.launch(
#                 headless=not headed  # 👈 Toggle based on flag
#             )
#         else:
#             raise ValueError(f"Unsupported browser: {browser}")
#
#         # Create browser context and page
#         context = browser_instance.new_context()
#         page = context.new_page()
#
#         logger.info(f"Initialized {browser} browser session")
#         yield page
#
#         # Cleanup
#         logger.info("Closing browser resources")
#         context.close()
#         browser_instance.close()


@pytest.fixture(scope="function")
def setup(request, browser):
    headed = request.config.getoption("--app-headed")

    # Add debug logging
    logger.info(f"Browser: {browser}, Headed mode: {headed}")

    with sync_playwright() as playwright:
        # Common launch parameters
        launch_args = {
            "headless": not headed,
            "slow_mo": 500  # Add slow motion for better visibility
        }

        if browser == "chrome":
            browser_instance = playwright.chromium.launch(
                **launch_args
            )
        elif browser == "edge":
            browser_instance = playwright.chromium.launch(
                channel="msedge",
                **launch_args
            )
        elif browser == "firefox":
            browser_instance = playwright.firefox.launch(
                **launch_args
            )
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        # Create context with larger viewport
        context = browser_instance.new_context(
            viewport={"width": 1600, "height": 1200}
        )
        page = context.new_page()

        logger.info(f"Created new page in {browser} browser")
        yield page

        # Cleanup
        logger.info("Closing browser context")
        context.close()
        logger.info("Closing browser instance")
        browser_instance.close()