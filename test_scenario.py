from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


def test_log_in_out_admin(browser):
    browser.get(browser.url + "/admin")
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-control[name='username']"))).send_keys("user")
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-control[name='password']"))).send_keys("bitnami")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary"))).click()
    assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                        "#content"))).is_displayed() is True, "Не отображается контент страницы после перехода в кабинет"
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fa-sign-out"))).click()
    assert wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".panel-body"))).is_displayed() is True, "Не отображается окно входа в учетную запись"
    assert wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".btn-primary"))).is_displayed() is True, "Не отображается кнопка лоигна"


def test_add_item_from_main_page(browser):
    wait = WebDriverWait(browser, 2)
    scroll_to_button = browser.find_element(By.CSS_SELECTOR, "[onclick$=\"(\'43\');\"] .fa-shopping-cart")
    ActionChains(browser)\
        .scroll_to_element(scroll_to_button)\
        .perform()
    name_card_of_item = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".caption > h4 > a")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[onclick$=\"(\'43\');\"] .fa-shopping-cart"))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-inverse"))).click()
    name_card_of_item_in_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-left > a")))
    assert name_card_of_item.text == name_card_of_item_in_cart.text, "Название товара не совпадают на карточке и в корзине"


def test_change_currency_check_prices_main_page(browser):
    wait = WebDriverWait(browser, 2)
    scroll_to_dollar_price = browser.find_element(By.CSS_SELECTOR, ":nth-child(1) > div > .caption > p.price")
    ActionChains(browser)\
        .scroll_to_element(scroll_to_dollar_price)\
        .perform()
    dollar_price = browser.find_element(By.CSS_SELECTOR, ":nth-child(1) > div > .caption > p.price").text

    scroll_to_change_currency = browser.find_element(By.CSS_SELECTOR, ".btn-link > .hidden-xs")
    ActionChains(browser)\
        .scroll_to_element(scroll_to_change_currency)\
        .perform()
    scroll_to_change_currency.click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".currency-select[name = 'EUR']"))).click()

    scroll_to_euro_price = browser.find_element(By.CSS_SELECTOR, ":nth-child(1) > div > .caption > p.price")
    ActionChains(browser)\
        .scroll_to_element(scroll_to_euro_price)\
        .perform()
    euro_price = browser.find_element(By.CSS_SELECTOR, ":nth-child(1) > div > .caption > p.price").text
    assert dollar_price != euro_price, "Цены в разных валютах не изменились"


def test_change_currency_check_prices_catalog(browser):
    browser.get(browser.url + "/desktops")
    wait = WebDriverWait(browser, 2)
    dollar_price = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > .caption > .price > .price-new"))).text

    scroll_to_change_currency = browser.find_element(By.CSS_SELECTOR, ".btn-link > .hidden-xs")
    ActionChains(browser)\
        .scroll_to_element(scroll_to_change_currency)\
        .perform()
    scroll_to_change_currency.click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".currency-select[name = 'EUR']"))).click()

    euro_price = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ":nth-child(2) > .caption > .price > .price-new"))).text
    assert dollar_price != euro_price, "Цены в разных валютах не изменились"


