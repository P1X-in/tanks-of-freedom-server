"""Module for operations on players."""
from tof_server.utils import randcoder
from tof_server.repository import player

def create_new_player():
    """Method for creating new player account."""
    new_pin = randcoder.get_random_code(8)

    new_player_id = player.create_new_player(new_pin)

    return {
        'id': new_player_id,
        'pin': new_pin
    }