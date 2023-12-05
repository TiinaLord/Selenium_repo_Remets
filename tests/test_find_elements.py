from Page_Objects.MainPage import MainPage
from Page_Objects.CatalogPage import CatalogPage
from Page_Objects.ProductPage import ProductPage
from Page_Objects.AdminPage import AdminPage
from Page_Objects.RegisterPage import RegisterPage


def test_main_page_menu_availability_button_search(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.is_element_displayed_btn_search()


def test_catalog_desktops_title_page(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open(browser)
    catalog_page.get_text()


def test_page_item_title(browser):
    product_page = ProductPage(browser)
    product_page.open(browser)
    product_page.get_text()


def test_login_btn_is_displayed(browser):
    admin_page = AdminPage(browser)
    admin_page.open(browser)
    admin_page.is_element_displayed_check_btn()


def test_register_page_radio_is_selected(browser):
    register_page = RegisterPage(browser)
    register_page.open(browser)
    register_page.is_element_displayed_check_radio()


