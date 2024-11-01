from selenium.webdriver.common.by import By

date_of_each_airdrop = (By.CSS_SELECTOR, "[class*='epoch-conainer'] span:last-child")


class RevenueSharePage:
    def __init__(self, driver):
        self.driver = driver

    def get_date_of_each_airdrop(self):
        return self.driver.find_elements(date_of_each_airdrop[0], date_of_each_airdrop[1])
