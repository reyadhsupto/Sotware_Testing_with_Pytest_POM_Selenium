import pytest
import os
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ChromeOptions,FirefoxOptions
from selenium import webdriver

@pytest.fixture(params=['chrome','firefox'], scope='class')
def init_driver(request):
    if request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument('--headless=new')
        driver = webdriver.Chrome(options=options)
        # driver = webdriver.Chrome()


    if request.param == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        # driver = webdriver.Firefox()

    
    request.cls.driver = driver
    driver.implicitly_wait(10)
    driver.delete_all_cookies()

    yield
    driver.quit()

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call" and rep.failed:
#         screenshots_dir = f"E:\Internship\SDET_selenium\Sotware_Testing_with_Pytest_POM_Selenium\Screenshots"
#         try:
#             os.makedirs(screenshots_dir)
#         except FileExistsError:
#             pass
#         screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
#         driver = item.cls.driver
#         driver.save_screenshot(screenshot_path)
#         print(f"\nScreenshot saved as: {screenshot_path}")