from selenium.webdriver.common.by import By
from Page_Objects.BasePage import BasePage


class MainPage(BasePage):
    BTN_SEARCH = (By.CSS_SELECTOR, ".btn-lg")
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, "[onclick$=\"(\'43\');\"] .fa-shopping-cart")
    NAME_ITEM_ON_PAGE = (By.CSS_SELECTOR, ".caption > h4 > a")
    NAME_ITEM_IN_CART = (By.CSS_SELECTOR, ".text-left > a")
    BTN_OPEN_CART = (By.CSS_SELECTOR, ".btn-inverse")

    DOLLAR_PRICE = (By.CSS_SELECTOR, ":nth-child(1) > div > .caption > p.price")
    EURO_PRICE = (By.CSS_SELECTOR, ":nth-child(1) > div > .caption > p.price")
    BTN_CHANGE_CURRENCY = (By.CSS_SELECTOR, ".btn-link > .hidden-xs")
    EURO_CURRENCY_SELECTOR = (By.CSS_SELECTOR, ".currency-select[name = 'EUR']")
    EURO_SIGN = (By.CSS_SELECTOR, "strong")
    def open(self):
        self.open_page()
        return self

    def is_element_displayed_btn_search(self):
        self.element_is_displayed(self.BTN_SEARCH)
        return self.BTN_SEARCH

    def scroll_to_item(self):
        self.scroll_to_element_item(self.BTN_ADD_TO_CART)

    def click_btn_add_to_cart(self):
        self.click(self.BTN_ADD_TO_CART)

    def click_btn_open_cart(self):
        self.click(self.BTN_OPEN_CART)

    def compare_text_page_and_cart(self):
        self.compare_name_itmes_on_pages(self.NAME_ITEM_ON_PAGE, self.NAME_ITEM_IN_CART)

    def compare_currency_price_main(self):
        self.scroll_to_element_item(self.DOLLAR_PRICE)
        currency_1 = self.collect_1st_currency_to_compare_price(self.DOLLAR_PRICE)
        self.click(self.BTN_CHANGE_CURRENCY)
        self.click(self.EURO_CURRENCY_SELECTOR)
        self.scroll_to_element_item(self.EURO_PRICE)
        currency_2 = self.collect_2nd_currency_to_compare_price(self.EURO_PRICE)
        if currency_1 != currency_2:
            pass
        else:
            raise AssertionError(f"'Цена не изменилась' {currency_1, currency_2}")

    def change_currency_main(self):
        self.click(self.BTN_CHANGE_CURRENCY)
        self.click(self.EURO_CURRENCY_SELECTOR)

    def check_euro_sign_in_header(self):
        self.compare_text(self.EURO_SIGN, "€")
