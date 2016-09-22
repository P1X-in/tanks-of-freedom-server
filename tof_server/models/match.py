"""Module for operations on matches."""
from tof_server.repository import map as map_repository
from tof_server.repository import match as match_repository
from tof_server.utils import randcoder

MAP_CODE_LENGTH = 5


def get_player_matches(player_id):
    """Method for getting list of player matches with details."""
    return []


def create_new_match(host_id, host_side, map_code):
    """Create new match."""
    map_id = map_repository.find_id_by_code(map_code)

    new_match_code = randcoder.get_random_code(MAP_CODE_LENGTH)

    new_match_id = match_repository.create_new_match(map_id, new_match_code)
    match_repository.join_player_to_match(new_match_id, host_id, host_side)

    return new_match_id
