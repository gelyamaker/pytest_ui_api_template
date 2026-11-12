import pytest
import allure
import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from api.board_api import BoardApi


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def api_client() -> BoardApi:
    return BoardApi(config.BASE_URL_API, config.TOKEN)


@pytest.fixture
def api_client_no_auth() -> BoardApi:
    return BoardApi(config.BASE_URL_API, "")


@pytest.fixture
def dummy_board_id() -> str:
    api = BoardApi(config.BASE_URL_API, config.TOKEN)
    with allure.step("Предварительно создать доску"):
        resp = (api.create_board("Board to be deleted", config.PROJ_ID)
                .get("id"))
    return resp


@pytest.fixture
def delete_board():
    dictionary = {"board_id": ""}
    yield dictionary

    with allure.step("Удалит доску, после теста"):
        api = BoardApi(config.BASE_URL_API, config.TOKEN)
        api.delete_board_by_id(dictionary.get("board_id"))
