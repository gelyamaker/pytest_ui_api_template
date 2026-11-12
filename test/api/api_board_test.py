import config
from api.board_api import BoardApi


def test_create_board(api_client: BoardApi, delete_board: dict):
    board_list_before = api_client.get_all_boards_by_proj_id(config.PROJ_ID)

    resp = api_client.create_board("New board to be deleted", config.PROJ_ID)
    delete_board["board_id"] = resp.get("id")

    board_list_after = api_client.get_all_boards_by_proj_id(config.PROJ_ID)

    assert len(board_list_after) - len(board_list_before) == 1


def test_delete_board(api_client: BoardApi, dummy_board_id: str):
    board_list_before = api_client.get_all_boards_by_proj_id(config.PROJ_ID)

    api_client.delete_board_by_id(dummy_board_id)

    board_list_after = api_client.get_all_boards_by_proj_id(config.PROJ_ID)

    assert len(board_list_before) - len(board_list_after) == 1
