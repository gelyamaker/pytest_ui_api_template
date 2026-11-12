from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://ru.yougile.com/team/"
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)

    def login_as(self, email: str, password: str):
        # дожидаемся, когда поле авторизации появится
        email_input = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[type="email"]')))
        email_input.send_keys(email)

        self.__driver.find_element(
                    By.CSS_SELECTOR, '[type="password"]').send_keys(password)
        self.__driver.find_element(
                            By.XPATH, '//div[text()="Войти"]').click()
