from selenium.webdriver.common.by import By

side_bar_toggle = (By.CSS_SELECTOR, "[class='sidebar-toggle-wrapper']")
side_bar_expand_button = (By.XPATH, "//div[@class='sidebar-toggle-wrapper hovered']/div[1]")
side_bar = (By.TAG_NAME, "aside")
faqs_section = (By.CSS_SELECTOR, "[class='faq-wrapper'] [class='flex-1'] [class*='faq-item-wrapper']")
faq_button = (By.CSS_SELECTOR, "[class='pointer']")
faq_text = (By.CSS_SELECTOR, "article span")
footer = (By.TAG_NAME, "footer")
faq_buttons_for_wait = (
    By.CSS_SELECTOR, "[class='faq-wrapper'] [class='flex-1'] [class*='faq-item-wrapper'] [class='pointer']")
faq_texts_for_wait = (
    By.CSS_SELECTOR, "[class='faq-wrapper'] [class='flex-1'] [class*='faq-item-wrapper'] article span")


class HordStakingPage:
    def __init__(self, driver):
        self.driver = driver

    def get_side_bar_toggle(self):
        return self.driver.find_elements(side_bar_toggle[0], side_bar_toggle[1])

    def get_side_bar_expand_button(self):
        return self.driver.find_element(side_bar_expand_button[0], side_bar_expand_button[1])

    def get_side_bar(self):
        return self.driver.find_element(side_bar[0], side_bar[1])

    def get_faqs_section(self):
        return self.driver.find_elements(faqs_section[0], faqs_section[1])

    def get_footer(self):
        return self.driver.find_element(footer[0], footer[1])
