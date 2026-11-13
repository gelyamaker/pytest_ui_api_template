import pytest
import allure
import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from api.board_api import BoardApi
from configuration.config_provider import ConfigProvider


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):

        timeout = ConfigProvider().getint("ui", "timeout")

        browser_name = ConfigProvider().get("ui", "browser_name")

        if browser_name == 'chrome':
            browser = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()))
        else:
            service = FirefoxService(GeckoDriverManager().install())
            browser = webdriver.Firefox(service=service)

        browser.implicitly_wait(timeout)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def api_client() -> BoardApi:
    base_url = ConfigProvider().get("api", "base_url")
    return BoardApi(base_url, config.TOKEN)


@pytest.fixture
def api_client_no_auth() -> BoardApi:
    base_url = ConfigProvider().get("api", "base_url")
    return BoardApi(base_url, "")


@pytest.fixture
def dummy_board_id() -> str:
    base_url = ConfigProvider().get("api", "base_url")
    api = BoardApi(base_url, config.TOKEN)
    with allure.step("Предварительно создать доску"):
        resp = (api.create_board("Board to be deleted", config.PROJ_ID)
                .get("id"))
    return resp


@pytest.fixture
def delete_board():
    dictionary = {"board_id": ""}
    yield dictionary

    with allure.step("Удалит доску, после теста"):
        base_url = ConfigProvider().get("api", "base_url")
        api = BoardApi(base_url, config.TOKEN)
        api.delete_board_by_id(dictionary.get("board_id"))
