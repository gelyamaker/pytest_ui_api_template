import allure
from api.board_api import BoardApi


def test_create_board(api_client: BoardApi, delete_board: dict,
                      test_data: dict):
    proj_id = test_data.get("proj_id")
    board_list_before = api_client.get_all_boards_by_proj_id(proj_id)

    resp = api_client.create_board("New board to be deleted", proj_id)
    delete_board["board_id"] = resp.get("id")

    board_list_after = api_client.get_all_boards_by_proj_id(proj_id)

    with allure.step("Проверить, что количество досок стало больше на 1"):
        assert len(board_list_after) - len(board_list_before) == 1


def test_delete_board(api_client: BoardApi, dummy_board_id: str,
                      test_data: dict):
    proj_id = test_data.get("proj_id")
    board_list_before = api_client.get_all_boards_by_proj_id(proj_id)

    api_client.delete_board_by_id(dummy_board_id)

    board_list_after = api_client.get_all_boards_by_proj_id(proj_id)

    with allure.step("Проверить, что количество досок стало меньше на 1"):
        assert len(board_list_before) - len(board_list_after) == 1
