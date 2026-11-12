import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step("Открыть 'Мой профиль'")
    def open_menu(self):
        self.__driver.find_element(
            By.CSS_SELECTOR, '[data-testid="profile-avatar-item"]').click()

    @allure.step("Получить информацию о пользователе")
    def get_account_info(self) -> list[str]:
        with allure.step("Получить имя пользователя"):
            element = self.__driver.find_element(
                By.CSS_SELECTOR, '[placeholder="Отображаемое имя…"]')
            name = element.get_attribute("value")

        with allure.step("Получить email пользователя"):
            with allure.step("Нажать кнопку 'Сменить e-mail'"):
                self.__driver.find_element(
                    By.CSS_SELECTOR, '[data-testid="change-email"]').click()

            with allure.step("Найти e-mail пользователя"):
                div = self.__driver.find_element(
                    By.CSS_SELECTOR, '[data-testid="current-email"]')
                divs = div.find_elements(By.CSS_SELECTOR, 'div')
                email = divs[1].text

            with allure.step("Закрыть модальное окно"):
                self.__driver.find_element(
                    By.CSS_SELECTOR, '[data-icon="IconCustomClose"]').click()

        return [name, email]
