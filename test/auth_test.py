from pages.auth_page import AuthPage
from pages.main_page import MainPage
import config


def auth_test(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(config.EMAIL, config.PASSWORD)

    main_page = MainPage(browser)
    assert main_page.get_current_url().endswith("team/")
    main_page.open_menu()
    info = main_page.get_account_info()

    assert main_page.get_current_url().endswith("team/settings-account")
    assert info[0] == config.USERNAME
    assert info[1] == config.EMAIL
