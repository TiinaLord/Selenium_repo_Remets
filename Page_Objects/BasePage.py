from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__

    @allure.step("Открытие страницы {url}")
    def open_page(self, url):
        self.logger.debug("%s: Opening url: %s" % (self.class_name, url))
        try:
            self.browser.get(self.browser.url)
        except Exception:
            raise WebDriverException()
        return self

    @allure.step("Отображение элемента {locator}")
    def element_is_displayed(self, locator):
        self.logger.debug("%s: FInding display element: %s" % (self.class_name, str(locator)))
        try:
            check_locator = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(locator)).is_displayed()
            if check_locator is True:
                return check_locator
            else:
                raise AssertionError(f"'Элемент не отобразился, локатор:' {locator}")
        except TimeoutException:
            raise AssertionError(f"'Элемент не отобразился, локатор:' {locator}")

    @allure.step("Элемент выбран {locator}")
    def element_is_selected(self, locator):
        self.logger.debug("%s: Checking element is selected: %s" % (self.class_name, str(locator)))
        try:
            check_locator = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(locator)).is_selected()
            if check_locator is True:
                return check_locator
            else:
                raise AssertionError(f"'Элемент не выбран, локатор:' {locator}")
        except TimeoutException:
            raise AssertionError(f"'Элемент не выбран, локатор:' {locator}")

    @allure.step("Сравнение текста {compared_text}")
    def compare_text(self, locator, compared_text):
        self.logger.debug("%s: Comparing text: %s" % (self.class_name, compared_text))
        try:
            text_from_locator = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator)).text
            return text_from_locator == compared_text
        except TimeoutException:
            raise AssertionError(f"'Текст не сходится' {locator}")

    @allure.step("Клик {element}")
    def click(self, element):
        self.logger.debug("%s: Clicking element: %s" % (self.class_name, str(element)))
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(element)).click()

    @allure.step("Ввод {locator}, {value}")
    def _input(self, locator, value):
        self.logger.debug("%s: Input text: %s" % (self.class_name, str(locator)))
        element = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)
        return self

    @allure.step("Скролл к элементу")
    def scroll_to_element_item(self, element):
        self.logger.debug("%s: Scrolling to element: %s" % (self.class_name, str(element)))
        locator = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(element))
        ActionChains(self.browser).scroll_to_element(locator).perform()

    @allure.step("Cравнение названий элементов {locator1}, {locator2}")
    def compare_name_itmes_on_pages(self, locator1, locator2):
        self.logger.debug("%s: Comparing name_titles: %s" % (self.class_name, locator1, locator2))
        try:
            text_from_1st_place = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator1))
            text_from_2nd_place = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator2))
            if text_from_1st_place.text == text_from_2nd_place.text:
                pass
            else:
                raise AssertionError(f"'Текст не сходится' {locator1, locator2}")

        except TimeoutException:
            raise AssertionError(f"'Текст не сходится' {locator1, locator2}")

    @allure.step("Collect 1st currency- {locator1}")
    def collect_1st_currency_to_compare_price(self, locator1):
        self.logger.debug("%s: Collecting 1st locator currency: %s" % (self.class_name, locator1))
        price_from_1st_currency = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(locator1)).text
        return price_from_1st_currency

    @allure.step("{Collect 2nd currency {locator2}")
    def collect_2nd_currency_to_compare_price(self, locator2):
        self.logger.debug("%s: Collecting 2nd locator currency: %s" % (self.class_name, locator2))
        price_from_2nd_currency = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(locator2)).text
        return price_from_2nd_currency

    @allure.step("Press enter")
    def press_enter_btn_in_alert(self, browser):
        self.logger.debug("%s: Pressing Enter: %s" % (self.class_name, browser))
        alert = WebDriverWait(browser, 2).until(EC.alert_is_present())
        alert.accept()
        return self
