import test_cases.conftest as conf
from page_objects.web_objects.hord_staking_page import HordStakingPage
from page_objects.web_objects.revenue_share_page import RevenueSharePage

# Objects
hord_staking_page = None
revenue_share_page = None


class ManagePages:

    @staticmethod
    def init_hord():
        globals()['hord_staking_page'] = HordStakingPage(conf.driver)

    @staticmethod
    def init_revenue_share():
        globals()['revenue_share_page'] = RevenueSharePage(conf.driver)
