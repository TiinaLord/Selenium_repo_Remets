from Page_Objects.AdminPage import AdminPage
from Page_Objects.AdminPage_Profile import AdminPage_Profile
from Page_Objects.RegisterPage import RegisterPage
from Page_Objects.MainPage import MainPage


def test_add_new_item_by_admin(browser):
    admin_page = AdminPage(browser)
    admin_page.open(browser)
    admin_page.input_creds()
    admin_page.click_log_in_button()

    admin_page_profile = AdminPage_Profile(browser)
    admin_page_profile.open_catalog()
    admin_page_profile.open_products()
    admin_page_profile.add_new_item()


def test_delete_item_by_admin(browser):
    admin_page = AdminPage(browser)
    admin_page.open(browser)
    admin_page.input_creds()
    admin_page.click_log_in_button()

    admin_page_profile = AdminPage_Profile(browser)
    admin_page_profile.open_catalog()
    admin_page_profile.open_products()
    admin_page_profile.click_checkbox()
    admin_page_profile.delete_item()
    admin_page_profile.check_alert_deleted_items()


def test_register_new_user(browser):
    register_page = RegisterPage(browser)
    register_page.open(browser)
    register_page.input_personal_data()
    register_page.agree_with_policy()
    register_page.press_continue_btn()
    register_page.check_success_create_acc()


def test_change_currency(browser):
    main_page = MainPage(browser)
    main_page.change_currency_main()
    main_page.check_euro_sign_in_header()
