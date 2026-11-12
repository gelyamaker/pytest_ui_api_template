import requests


class BoardApi:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def get_all_boards_by_proj_id(self, proj_id: str) -> list:
        path = ("{yougile}/boards?projectId={id}".
                format(yougile=self.base_url, id=proj_id))
        resp = requests.get(path, headers=self.headers)

        return resp.json().get("content")

    def create_board(self, title: str, proj_id: str) -> dict:
        path = "{yougile}/boards".format(yougile=self.base_url)
        body = {
            "title": title,
            "projectId": proj_id
            }
        resp = requests.post(path, json=body, headers=self.headers)

        return resp.json()

    def delete_board_by_id(self, board_id: str):
        path = ("{yougile}/boards/{id}"
                .format(yougile=self.base_url, id=board_id))
        body = {
            "deleted": True
                    }
        resp = requests.put(path, json=body, headers=self.headers)

        return resp.json()
