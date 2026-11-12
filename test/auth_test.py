import allure
import config
from pages.auth_page import AuthPage
from pages.main_page import MainPage


def auth_test(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(config.EMAIL, config.PASSWORD)

    main_page = MainPage(browser)

    current_url = main_page.get_current_url()
    with allure.step("Проверить, что URL " + current_url + "заканчивается на "
                     "team/"):
        assert current_url.endswith("team/")

    main_page.open_menu()
    info = main_page.get_account_info()

    current_url = main_page.get_current_url()
    with allure.step("Проверить, что URL " + current_url + "заканчивается на "
                     "team/settings-account"):
        assert current_url.endswith("team/settings-account")

    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть " + config.USERNAME):
            assert info[0] == config.USERNAME
        with allure.step("Почта пользователя должна быть " + config.EMAIL):
            assert info[1] == config.EMAIL
