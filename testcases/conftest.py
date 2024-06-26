import pytest
import platform

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

# def pytest_html_configure_metadata(metadata):
#     metadata['Project Name'] = 'nopCommerce Automation Testing'
#     metadata['Python Version'] = platform.python_version()  # Replace with your Python version
#     metadata['Tester'] = "Reyad Hassan"

# # It is a hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nopCommerce Automation Testing'
#     config._metadata['Python Version'] = platform.python_version()
#     config._metadata['Tester'] = 'Reyad Hassan'  # Replace 'Your Name' with the actual tester's name

# # It is a hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)


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