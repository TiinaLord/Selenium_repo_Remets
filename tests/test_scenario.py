from Page_Objects.AdminPage import AdminPage
from Page_Objects.AdminPage_Profile import AdminPage_Profile
from Page_Objects.MainPage import MainPage
from Page_Objects.CatalogPage import CatalogPage


def test_log_in_out_admin(browser):
    admin_page = AdminPage(browser)
    admin_page.open(browser)
    admin_page.input_creds()
    admin_page.click_log_in_button()

    admin_page_profile = AdminPage_Profile(browser)
    admin_page_profile.is_element_displayed_on_page()
    admin_page_profile.click_sign_out()

    admin_page.is_element_displayed_check_btn()


def test_add_item_from_main_page(browser):
    main_page = MainPage(browser)
    main_page.scroll_to_item()
    main_page.click_btn_add_to_cart()
    main_page.click_btn_open_cart()
    main_page.compare_text_page_and_cart()


def test_change_currency_check_prices_main_page(browser):
    main_page = MainPage(browser)
    main_page.compare_currency_price_main()


def test_change_currency_check_prices_catalog(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open(browser)
    catalog_page.compare_currency_price_product()
