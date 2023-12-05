from selenium.webdriver.common.by import By
from Page_Objects.BasePage import BasePage


class AdminPage_Profile(BasePage):
    CONTENT = (By.CSS_SELECTOR, "#content")
    PANEL_BODY = (By.CSS_SELECTOR, ".panel-body")
    SIGN_OUT_BTN = (By.CSS_SELECTOR, ".fa-sign-out")

    CATALOG_BTN = (By.CSS_SELECTOR, "#menu-catalog > a")
    PRODUCTS_BTN = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2) > a")
    ADD_NEW_BTN = (By.CSS_SELECTOR, "div > a > i")

    GENERAL_PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name1")
    GENERAL_PRODUCT_META_TAG = (By.CSS_SELECTOR, "#input-meta-title1")
    GO_TO_DATA_LABEL = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2)")
    DATA_MODEL = (By.CSS_SELECTOR, "#input-model")
    SAVE_BTN = (By.CSS_SELECTOR, "div.page-header > div button")
    ALERT_SUCCESS_ADD_ITEM = (By.CSS_SELECTOR, "div.alert.alert-success")

    CHECK_BOX_SELECTOR = (By.CSS_SELECTOR, " tbody > tr:nth-child(1) > td:nth-child(1) > input[type=checkbox]")
    DELETE_ITEM_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-danger")
    ALERT_SUCCESS_DELETE_ITEM = (By.CSS_SELECTOR, ".alert-dismissible")
    def is_element_displayed_on_page(self):
        self.element_is_displayed(self.CONTENT)
        self.element_is_displayed(self.PANEL_BODY)

    def click_sign_out(self):
        self.click(self.SIGN_OUT_BTN)
        return self.SIGN_OUT_BTN

    def open_catalog(self):
        self.click(self.CATALOG_BTN)
        return self.CATALOG_BTN

    def open_products(self):
        self.click(self.PRODUCTS_BTN)
        return self.PRODUCTS_BTN

    def add_new_item(self):
        self.click(self.ADD_NEW_BTN)
        self._input(self.GENERAL_PRODUCT_NAME, "Google Pixel 8 Pro")
        self._input(self.GENERAL_PRODUCT_META_TAG, "Google Pixel 8 Pro")
        self.click(self.GO_TO_DATA_LABEL)
        self._input(self.DATA_MODEL, "Google Pixel")
        self.click(self.SAVE_BTN)
        self.compare_text(self.ALERT_SUCCESS_ADD_ITEM, "Success: You have modified products!")

    def click_checkbox(self):
        self.click(self.CHECK_BOX_SELECTOR)

    def delete_item(self):
        self.click(self.DELETE_ITEM_BUTTON)
        self.press_enter_btn_in_alert(self.browser)

    def check_alert_deleted_items(self):
        self.compare_text(self.ALERT_SUCCESS_DELETE_ITEM, "Success: You have modified products!")
