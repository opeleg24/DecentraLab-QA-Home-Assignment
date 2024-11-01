import allure
import pytest
from smart_assertions import verify_expectations

import utilities.manage_pages as page
from utilities.common_ops import get_data
from workflows.web_flows import WebFlows, FAQSSections


@pytest.mark.usefixtures("init_hord")
class Test_Hord:

    @allure.title("Test01: Task 2 - Verify sidebar is expanded")
    @allure.description(
        "This test will verify the side bar is displayed by checking the class attribute & the expected value")
    def test_verify_side_bar_displayed(self):
        side_bar_attribute_value = WebFlows.get_side_bar_attribute()
        WebFlows.verify_side_bar_displayed(get_data("EXPECTED_STRING"), side_bar_attribute_value)

    @allure.title("Test02: Task 2 - Verify collapsing the sidebar")
    @allure.description(
        "This test will verify the side bar has collapsed by checking the class attribute & the expected value")
    def test_click_side_bar_expand_button(self):
        WebFlows.click_side_bar_expand_button()
        side_bar_attribute_value = WebFlows.get_side_bar_attribute()
        WebFlows.verify_side_bar_not_displayed(side_bar_attribute_value, get_data("EXPECTED_STRING"))

    @allure.title("Test03: Task 2 - Verify FSQ section")
    @allure.description("This test will verify the FSQ section:"
                        "1: Check if the number of FAQS is equal to the number of expected FAQS"
                        "2: Check if the FAQ text is not displayed"
                        "3: Check if the FAQ text equals the expected value")
    def test_verify_fsq_section(self):
        WebFlows.move_to_footer_section()
        # Check if both have exactly same number of values
        if len(page.hord_staking_page.get_faqs_section()) == len(FAQSSections):
            for faq, (key, value) in zip(page.hord_staking_page.get_faqs_section(), FAQSSections.items()):
                WebFlows.check_if_element_not_displayed(faq)
                WebFlows.click_faq_button(faq)
                WebFlows.check_if_element_equals_expected_value(faq, key, value)
        else:
            print("The number of FAQS is not equal to the number of expected FAQS")

        verify_expectations()
