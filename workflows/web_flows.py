from datetime import datetime

import allure

import utilities.manage_pages as page
from extentions.ui_actions import UiActions
from extentions.verifications import Verifications
from page_objects.web_objects import hord_staking_page
from utilities.common_ops import read_json_file, get_data
from utilities.common_ops import wait, For


class WebFlows:

    @staticmethod
    @allure.step("Get the attribute of the side bar")
    def get_side_bar_attribute():
        class_attribute_value = UiActions.get_attribute(page.hord_staking_page.get_side_bar(), "class")
        return class_attribute_value

    @staticmethod
    @allure.step("Verify the side bar is displayed - expended indication appears in the class attribute")
    def verify_side_bar_displayed(value_expected_string, value_actual):
        Verifications.verify_text_in_value(value_expected_string, value_actual)

    @staticmethod
    @allure.step("Click on the Side Bar Expand Button")
    def click_side_bar_expand_button():
        UiActions.move_to_element(page.hord_staking_page.get_side_bar_toggle()[1])
        UiActions.click(page.hord_staking_page.get_side_bar_expand_button())

    @staticmethod
    @allure.step("Verify the side bar is not displayed - expended indication doesn't appear in the class attribute")
    def verify_side_bar_not_displayed(value_expected_string, value_actual):
        Verifications.verify_text_not_in_value(value_expected_string, value_actual)

    @staticmethod
    @allure.step("Move to the footer section")
    def move_to_footer_section():
        UiActions.move_to_element(page.hord_staking_page.get_footer())

    @staticmethod
    @allure.step("Check if the element is not displayed (text of the FAQ)")
    def check_if_element_not_displayed(faq):
        Verifications.is_not_displayed(faq.find_element_by_css_selector(hord_staking_page.faq_text[1]))

    @staticmethod
    @allure.step("wait & click faq button")
    def click_faq_button(faq):
        wait(For.ELEMENT_IS_CLICKABLE, hord_staking_page.faq_buttons_for_wait)
        UiActions.click(faq.find_element_by_css_selector(hord_staking_page.faq_button[1]))

    @staticmethod
    @allure.step(
        "wait & Check if the element equals the expected value & print the result (key & value of expected result in json)")
    def check_if_element_equals_expected_value(faq, key, value):
        wait(For.ELEMENT_DISPLAYED, hord_staking_page.faq_texts_for_wait)
        Verifications.verify_soft_assert_equals(UiActions.get_text(
            faq.find_element_by_css_selector(hord_staking_page.faq_text[1])), value, key)

    @staticmethod
    @allure.step("Get each one of the air drops dates")
    def get_dates_of_airdrop(date_value_format, date_format):
        for date in page.revenue_share_page.get_date_of_each_airdrop():
            date_value_format.append(datetime.strptime(UiActions.get_text(date), date_format))

    @staticmethod
    @allure.step("Verify that the date of each airdrop is sorted in descending order")
    def verify_dates_of_airdrop(date_value_format, sorted_direction):
        Verifications.verify_equals(date_value_format, sorted(date_value_format, reverse=sorted_direction))


FAQSSections = read_json_file(get_data('FAQJsonData'))
