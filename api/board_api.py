import requests
import allure


class BoardApi:
    @allure.step("URL: {base_url}, токен авторизации {token}")
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    @allure.step("Запросить список всех досок для проекта {proj_id}")
    def get_all_boards_by_proj_id(self, proj_id: str) -> list:
        path = ("{yougile}/boards?projectId={id}".
                format(yougile=self.base_url, id=proj_id))
        resp = requests.get(path, headers=self.headers)

        return resp.json().get("content")

    @allure.step("Создать доску {title}")
    def create_board(self, title: str, proj_id: str) -> dict:
        path = "{yougile}/boards".format(yougile=self.base_url)
        body = {
            "title": title,
            "projectId": proj_id
            }
        resp = requests.post(path, json=body, headers=self.headers)

        return resp.json()

    @allure.step("Удалить доску {board_id}")
    def delete_board_by_id(self, board_id: str):
        path = ("{yougile}/boards/{id}"
                .format(yougile=self.base_url, id=board_id))
        body = {
            "deleted": True
                    }
        resp = requests.put(path, json=body, headers=self.headers)

        return resp.json()
