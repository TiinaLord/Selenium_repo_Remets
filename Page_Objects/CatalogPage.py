from selenium.webdriver.common.by import By
from Page_Objects.BasePage import BasePage


class CatalogPage(BasePage):
    DESK_TITLE = (By.CSS_SELECTOR, "h2")
    TEXT_DESKTOPS = "Desktops"

    DOLLAR_PRICE = (By.CSS_SELECTOR, ":nth-child(2) > .caption > .price > .price-new")
    EURO_PRICE = (By.CSS_SELECTOR, ":nth-child(2) > .caption > .price > .price-new")
    BTN_CHANGE_CURRENCY = (By.CSS_SELECTOR, ".btn-link > .hidden-xs")
    EURO_CURRENCY_SELECTOR = (By.CSS_SELECTOR, ".currency-select[name = 'EUR']")

    def open(self, browser):
        url = browser.get(browser.url + "/desktops")
        return url

    def get_text(self):
        self.compare_text(locator=self.DESK_TITLE, compared_text=self.TEXT_DESKTOPS)

    def compare_currency_price_product(self):
        currency_1 = self.collect_1st_currency_to_compare_price(self.DOLLAR_PRICE)
        self.click(self.BTN_CHANGE_CURRENCY)
        self.click(self.EURO_CURRENCY_SELECTOR)
        currency_2 = self.collect_2nd_currency_to_compare_price(self.EURO_PRICE)
        if currency_1 != currency_2:
            pass
        else:
            raise AssertionError(f"'Цена не изменилась' {currency_1, currency_2}")

