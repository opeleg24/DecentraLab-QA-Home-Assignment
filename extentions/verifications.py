import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert


class Verifications:

    @staticmethod
    @allure.step("Verifying equals")
    def verify_equals(actual, expected):
        assert actual == expected, f"Expected: {expected}, but got: {actual}"

    @staticmethod
    @allure.step("Verifying equals using smart assertions")
    def verify_soft_assert_equals(actual, expected, message=None):
        soft_assert(actual == expected,
                    f"Issue with value of {message}, expected result: {expected}, but got: {actual}")

    @staticmethod
    @allure.step("Verifying text using smart assertions")
    def verify_text_not_in_value(text, value):
        assert value not in text, f"The text {value} appears in the text: {text}"

    @staticmethod
    @allure.step("Verifying text")
    def verify_text_in_value(string, value):
        assert string in value, f"The string {string} is not in the value: {value}"

    @staticmethod
    @allure.step("Verifying element is not displayed")
    def is_not_displayed(elem: WebElement):
        soft_assert(not elem.is_displayed(), f"{elem.text} is displayed, but it should not be.")

    @staticmethod
    @allure.step("Verifying element is displayed")
    def is_displayed(elem: WebElement):
        soft_assert(elem.is_displayed(), f"{elem.text} is not displayed")
