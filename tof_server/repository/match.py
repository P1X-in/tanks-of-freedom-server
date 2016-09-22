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


def create_new_match(map_id, join_code):
    """Method for creating new match."""
    cursor = mysql.connection.cursor()
    sql = """INSERT INTO matches
            (join_code, map_id, status)
            VALUES (%s, %s, %s)"""

    cursor.execute(sql, (join_code, map_id, MATCH_STATE_NEW))

    last_id_sql = "SELECT LAST_INSERT_ID()"
    cursor.execute(last_id_sql)

    last_id = cursor.fetchone()

    mysql.connection.commit()
    cursor.close()

    return last_id[0]


def join_player_to_match(match_id, player_id, side):
    """Method for joining a player to a match."""
    cursor = mysql.connection.cursor()
    sql = """INSERT INTO match_players
            (match_id, player_id, side, status)
            VALUES (%s, %s, %s, %s)"""
    cursor.execute(sql, (match_id, player_id, side, side))

    mysql.connection.commit()
    cursor.close()


def get_match_info(match_id):
    """Method for getting match details for listing."""
    cursor = mysql.connection.cursor()
    sql = "SELECT join_code, status, map_id FROM matches WHERE id = %s"

    cursor.execute(sql, (match_id,))
    match_data = cursor.fetchone()
    cursor.close()

    return match_data


def get_match_info_by_code(join_code):
    """Method for getting match details for join query."""
    cursor = mysql.connection.cursor()
    sql = "SELECT id, status, map_id FROM matches WHERE join_code = %s"

    cursor.execute(sql, (join_code,))
    match_data = cursor.fetchone()
    cursor.close()

    return match_data


def get_players_for_match(match_id):
    """Method for getting list of players in a match."""
    cursor = mysql.connection.cursor()
    sql = "SELECT player_id, side, status FROM match_players WHERE match_id = %s"

    cursor.execute(sql, (match_id,))
    players = cursor.fetchall()
    cursor.close()

    return players


def get_player_in_match(player_id, match_id):
    """Get information about player in a match."""
    cursor = mysql.connection.cursor()
    sql = "SELECT side, status FROM match_players WHERE match_id = %s AND player_id = %s"

    cursor.execute(sql, (match_id, player_id))
    player = cursor.fetchone()
    cursor.close()

    return player
