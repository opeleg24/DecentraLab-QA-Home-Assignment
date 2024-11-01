import allure
from selenium.webdriver.remote.webelement import WebElement

import test_cases.conftest as conf


class UiActions:

    @staticmethod
    @allure.step("Clicking element")
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    @allure.step("Getting text")
    def get_text(elem: WebElement):
        return elem.text

    @staticmethod
    @allure.step("Getting attribute")
    def get_attribute(elem: WebElement, attribute):
        return elem.get_attribute(attribute)

    @staticmethod
    @allure.step("Move to element")
    def move_to_element(elem: WebElement):
        conf.actions.move_to_element(elem).perform()
