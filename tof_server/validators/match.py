"""Module for validating match requests."""
from tof_server.repository import match as match_repository
from tof_server.repository import map as map_repository

MATCH_LIMIT = 4


def are_slots_available(player_id):
    """Method for checking if player has available match slots."""
    current_matches = match_repository.get_player_visible_matches(player_id)

    if len(current_matches) > MATCH_LIMIT:
        return False

    return True


def is_map_available(map_code):
    """Method for checking if map code is correct."""
    map_id = map_repository.find_id_by_code(map_code)

    if map_id is None:
        return False

    return True


def is_side_valid(side):
    """Method for checkign if side value is valid."""
    return side in [map_repository.MATCH_SIDE_BLUE, map_repository.MATCH_SIDE_RED]
