from selenium.webdriver import ActionChains, Keys
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        try:
            self.browser.get(self.browser.url)
        except Exception:
            raise WebDriverException()
        return self

    def element_is_displayed(self, locator):
        try:
            check_locator = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(locator)).is_displayed()
            if check_locator is True:
                return check_locator
            else:
                raise AssertionError(f"'Элемент не отобразился, локатор:' {locator}")
        except TimeoutException:
            raise AssertionError(f"'Элемент не отобразился, локатор:' {locator}")

    def element_is_selected(self, locator):
        try:
            check_locator = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(locator)).is_selected()
            if check_locator is True:
                return check_locator
            else:
                raise AssertionError(f"'Элемент не выбран, локатор:' {locator}")
        except TimeoutException:
            raise AssertionError(f"'Элемент не выбран, локатор:' {locator}")

    def compare_text(self, locator, compared_text):
        try:
            text_from_locator = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator)).text
            return text_from_locator == compared_text
        except TimeoutException:
            raise AssertionError(f"'Текст не сходится' {locator}")

    def click(self, element):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(element)).click()

    def _input(self, locator, value):
        element = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)
        return self

    def scroll_to_element_item(self, element):
        locator = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(element))
        ActionChains(self.browser).scroll_to_element(locator).perform()

    def compare_name_itmes_on_pages(self, locator1, locator2):
        try:
            text_from_1st_place = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator1))
            text_from_2nd_place = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator2))
            if text_from_1st_place.text == text_from_2nd_place.text:
                pass
            else:
                raise AssertionError(f"'Текст не сходится' {locator1, locator2}")

        except TimeoutException:
            raise AssertionError(f"'Текст не сходится' {locator1, locator2}")

    def collect_1st_currency_to_compare_price(self, locator1):
        price_from_1st_currency = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(locator1)).text
        return price_from_1st_currency

    def collect_2nd_currency_to_compare_price(self, locator2):
        price_from_2nd_currency = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(locator2)).text
        return price_from_2nd_currency

    def press_enter_btn_in_alert(self, browser):
        alert = WebDriverWait(browser, 2).until(EC.alert_is_present())
        alert.accept()
        return self
