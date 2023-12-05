from selenium.webdriver.common.by import By
from Page_Objects.BasePage import BasePage


class AdminPage(BasePage):
    CHECK_BTN = (By.CSS_SELECTOR, ".btn-primary")
    ADMIN_LOGIN = (By.CSS_SELECTOR, ".form-control[name='username']")
    ADMIN_PASSWORD = (By.CSS_SELECTOR, ".form-control[name='password']")


    LOGIN_CRED = "user"
    PASSWORD_CRED = "bitnami"

    def open(self, browser):
        url = browser.get(browser.url + "/admin")
        return url

    def is_element_displayed_check_btn(self):
        self.element_is_displayed(self.CHECK_BTN)
        return self.CHECK_BTN

    def input_creds(self):
        self._input(self.ADMIN_LOGIN, self.LOGIN_CRED)
        self._input(self.ADMIN_PASSWORD, self.PASSWORD_CRED)

    def click_log_in_button(self):
        self.click(self.CHECK_BTN)
        return self.CHECK_BTN
