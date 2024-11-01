import allure
import pytest

from workflows.web_flows import WebFlows


@pytest.mark.usefixtures('init_revenue_share')
class Test_Revenue_Share:
    @allure.title("Test01: Bonus Task - Verify the date of each airdrop")
    @allure.description(
        "This test will verify the list that contains the date of each airdrop is sorted in descending order")
    def test_verify_date_of_each_airdrop(self):
        date_value_format = []
        WebFlows.get_dates_of_airdrop(date_value_format, "%B, %Y")
        WebFlows.verify_dates_of_airdrop(date_value_format, True)
