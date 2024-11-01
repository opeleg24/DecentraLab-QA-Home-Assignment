import allure
import pytest
import selenium.webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.common_ops import get_data, get_time_stamp
from utilities.manage_pages import ManagePages

driver = None
actions = None


@pytest.fixture(scope='class')
def init_hord(request):
    globals()['driver'] = get_web_driver()
    driver = globals()['driver']
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('WaitTime')))
    driver.get(get_data('UrlHordApp'))
    request.cls.driver = driver
    globals()['actions'] = ActionChains(driver)
    actions = globals()['actions']
    request.cls.actions = actions
    ManagePages.init_hord()
    yield
    # time.sleep(2)
    driver.quit()


@pytest.fixture(scope='class')
def init_revenue_share(request):
    globals()['driver'] = get_web_driver()
    driver = globals()['driver']
    driver.get(get_data('UrlRevenueShare'))
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    globals()['actions'] = ActionChains(driver)
    actions = globals()['actions']
    request.cls.actions = actions
    ManagePages.init_revenue_share()

    yield
    # time.sleep(2)
    driver.quit()


def get_web_driver():
    web_driver = get_data('Browser')
    if web_driver.lower() == 'chrome':
        driver = get_chrome_driver()
    elif web_driver.lower() == 'firefox':
        driver = get_firefox_driver()
    elif web_driver.lower() == 'edge':
        driver = get_edge_driver()
    else:
        driver = None
        raise Exception('Unsupported web driver')
    return driver


def get_chrome_driver():
    chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
    return chrome_driver


def get_firefox_driver():
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return ff_driver


def get_edge_driver():
    edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install())
    return edge_driver


def pytest_exception_interact(node, call, report):
    if report.failed:
        image = get_data('ScreenshotPath') + 'screen_' + str(get_time_stamp()) + '.png'
        globals()['driver'].get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
