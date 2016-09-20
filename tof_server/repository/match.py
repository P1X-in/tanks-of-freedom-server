"""Module for database operations on matches tables."""
from tof_server import mysql


MATCH_STATE_NEW = 0
MATCH_STATE_STARTED = 1
MATCH_STATE_ENDED = 2
MATCH_STATE_FORFEIT = 3

MATCH_SIDE_BLUE = 0
MATCH_SIDE_RED = 1

MATCH_PLAYER_STATE_ACTIVE = 0
MATCH_PLAYER_STATE_INACTIVE = 1
MATCH_PLAYER_STATE_WIN = 2
MATCH_PLAYER_STATE_LOSS = 3
MATCH_PLAYER_STATE_DISMISSED = 4

MATCH_CODE_ERASED = 'nope'


def get_player_visible_matches(player_id):
    """Method for getting non-dismissed matches."""
    cursor = mysql.connection.cursor()
    sql = "SELECT match_id, side, status FROM match_players WHERE player_id = %s"

    cursor.execute(sql, (player_id,))
    matches = cursor.fetchall()
    cursor.close()

    return matches


def create_new_match(map_id, match_code):
    """Method for creating new match."""
