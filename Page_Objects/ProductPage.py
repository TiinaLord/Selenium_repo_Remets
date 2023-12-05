from selenium.webdriver.common.by import By
from Page_Objects.BasePage import BasePage


class ProductPage(BasePage):
    ITEM_TITLE = (By.CSS_SELECTOR, "h1")
    TEXT_ITEM_DESKTOPS = "Canon EOS 5D"

    def open(self, browser):
        url = browser.get(browser.url + "/desktops/canon-eos-5d")
        return url

    def get_text(self):
        self.compare_text(locator=self.ITEM_TITLE, compared_text=self.TEXT_ITEM_DESKTOPS)
