from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page_menu_availability_button_search(browser):
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-lg")))
    btn_search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-lg"))).is_displayed()
    assert btn_search is True, "Кнопка не найдена"


def test_catalog_desktops_title_page(browser):
    browser.get(browser.url + "/desktops")
    wait = WebDriverWait(browser, 1)
    desk_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2")))
    assert desk_title.text == "Desktops", "Текст неверный или отсутствует"


def test_page_item_title(browser):
    browser.get(browser.url + "/desktops/canon-eos-5d")
    wait = WebDriverWait(browser, 1)
    item_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))
    assert item_title.text == "Canon EOS 5D", "Текст неверный или отсутствует"


def test_login_btn_is_displayed(browser):
    browser.get(browser.url + "/admin")
    wait = WebDriverWait(browser, 1)
    check_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary"))).is_displayed()
    assert check_btn is True, "Кнопка не найдена (отсутствует)"


def test_register_page_radio_is_selected(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 1)
    check_radio = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".radio-inline > input[value='0']"))).is_selected()
    assert check_radio is True, "Кнопка Нет не выбрана"
