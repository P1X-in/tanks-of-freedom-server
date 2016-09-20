"""Module for operations on matches."""
from tof_server.repository import map as map_repository
from tof_server.repository import match as match_repository


def get_player_matches(player_id):
    """Method for getting list of player matches with details."""
    return []


def create_new_match(host_id, host_side, map_code):
    """Create new match."""
    map_id = map_repository.find_id_by_code(map_code)

    match_repository.create_new_match(map_id, 'code')
