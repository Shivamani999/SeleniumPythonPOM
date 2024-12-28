import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        chrome_opt = webdriver.ChromeOptions()
        # chrome_opt.add_argument("--start-maximized")
        chrome_opt.add_argument("--ignore-certificate-errors")
        service = Service("D:/chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=chrome_opt)

    elif browser_name == "firefox":
        service = Service("D:/chromedriver.exe")
        driver = webdriver.Firefox(service=service)

    elif browser_name == "edge":
        service = Service("D:/msedgedriver.exe")
        driver = webdriver.Edge(service=service)

    elif browser_name == "safari":
        service = Service("D:/chromedriver.exe")
        driver = webdriver.Safari(service=service)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
