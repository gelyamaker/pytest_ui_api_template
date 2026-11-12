from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    def get_current_url(self) -> str:
        return self.__driver.current_url

    def open_menu(self):
        self.__driver.find_element(
            By.CSS_SELECTOR, '[data-testid="profile-avatar-item"]').click()

    def get_account_info(self) -> list[str]:
        element = self.__driver.find_element(
            By.CSS_SELECTOR, '[placeholder="Отображаемое имя…"]')
        name = element.get_attribute("value")

        self.__driver.find_element(
            By.CSS_SELECTOR, '[data-testid="change-email"]').click()
        div = self.__driver.find_element(
            By.CSS_SELECTOR, '[data-testid="current-email"]')
        divs = div.find_elements(By.CSS_SELECTOR, 'div')
        email = divs[1].text

        self.__driver.find_element(
            By.CSS_SELECTOR, '[data-icon="IconCustomClose"]').click()

        return [name, email]
