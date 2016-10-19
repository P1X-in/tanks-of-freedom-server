"""Module for validating match requests."""
import json
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
    return side in [match_repository.MATCH_SIDE_BLUE, match_repository.MATCH_SIDE_RED]


def is_in_match(player_id, match_code):
    """Method for verifying if player is in a match."""
    match_details = match_repository.get_match_info_by_code(match_code)
    if not match_details:
        return False

    player_details = match_repository.get_player_in_match(player_id, match_details[0])
    if not player_details:
        return False

    return True


def is_match_joinable(match_code):
    """Method for checking if match can be joined."""
    match_details = match_repository.get_match_info_by_code(match_code)
    if not match_details:
        return False

    if match_details[1] != match_repository.MATCH_STATE_NEW:
        return False

    players = match_repository.get_players_for_match(match_details[0])
    if len(players) != 1:
        return False

    return True


def verify_turn_data(last_turn_data, new_turn_data):
    """Method for checking if new turn data does not cheat too much."""
    if 'final_state' not in last_turn_data:
        return True

    end_of_last_turn = last_turn_data['final_state']
    start_of_new_turn = new_turn_data['initial_state']

    end_data = json.dumps(end_of_last_turn)
    start_data = json.dumps(start_of_new_turn)

    if end_data != start_data:
        return False

    return True
