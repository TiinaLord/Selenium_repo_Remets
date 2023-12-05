from selenium.webdriver.common.by import By
from Page_Objects.BasePage import BasePage


class RegisterPage(BasePage):
    CHECK_RADIO = (By.CSS_SELECTOR, ".radio-inline > input[value='0']")

    F_NAME = (By.CSS_SELECTOR, "#input-firstname")
    L_NAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    TEL = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    POLICY_CHECKBOX = (By.CSS_SELECTOR, "input[type=checkbox]")
    CONTINUE_BTN = (By.CSS_SELECTOR, ".btn-primary")
    SUCCESS_CREATE_ACC = (By.CSS_SELECTOR, "#content > h1")

    def open(self, browser):
        url = browser.get(browser.url + "/index.php?route=account/register")
        return url

    def is_element_displayed_check_radio(self):
        self.element_is_selected(self.CHECK_RADIO)
        return self.CHECK_RADIO

    def input_personal_data(self):
        self._input(self.F_NAME, "George")
        self._input(self.L_NAME, "McTucker")
        self._input(self.EMAIL, "georgemctucker@gmail.com")
        self._input(self.TEL, "786688686")
        self._input(self.PASSWORD, "Right123")
        self._input(self.PASSWORD_CONFIRM, "Right123")

    def agree_with_policy(self):
        self.click(self.POLICY_CHECKBOX)

    def press_continue_btn(self):
        self.click(self.CONTINUE_BTN)

    def check_success_create_acc(self):
        self.compare_text(self.SUCCESS_CREATE_ACC, "Your Account Has Been Created!")
