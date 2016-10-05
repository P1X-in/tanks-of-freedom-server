"""Module for database operations on matches tables."""
from tof_server import mysql


MATCH_STATE_NEW = 0
MATCH_STATE_IN_PROGRESS = 1
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
    sql = "SELECT match_id, side, status FROM match_players WHERE player_id = %s AND status <> %s"

    cursor.execute(sql, (player_id, MATCH_PLAYER_STATE_DISMISSED))
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


def create_empty_match_state(match_id):
    """Method for creating empty match state."""
    cursor = mysql.connection.cursor()
    sql = """INSERT INTO match_states
            (match_id, json)
            VALUES (%s, %s)"""

    initial_json = "{}"

    cursor.execute(sql, (match_id, initial_json))

    mysql.connection.commit()
    cursor.close()


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


def get_match_state(match_id):
    """Get state of a match."""
    cursor = mysql.connection.cursor()
    sql = "SELECT json FROM match_states WHERE match_id = %s"

    cursor.execute(sql, (match_id, ))
    state = cursor.fetchone()
    cursor.close()

    if not state:
        return "{}"

    return state[0]


def update_match_state(match_id, json_data):
    """Method for updating match state."""
    cursor = mysql.connection.cursor()
    sql = "UPDATE match_states SET json = %s WHERE match_id = %s"
    cursor.execute(sql, (json_data, match_id))
    mysql.connection.commit()
    cursor.close()


def update_match_status(match_id, status):
    """Method for updating match status."""
    cursor = mysql.connection.cursor()
    sql = "UPDATE matches SET status = %s WHERE id = %s"
    cursor.execute(sql, (status, match_id))
    mysql.connection.commit()
    cursor.close()


def update_player_status(match_id, player_id, status):
    """Method for updating player status."""
    cursor = mysql.connection.cursor()
    sql = "UPDATE match_players SET status = %s WHERE match_id = %s AND player_id = %s"
    cursor.execute(sql, (status, match_id, player_id))
    mysql.connection.commit()
    cursor.close()


def update_other_players_status(match_id, player_id, status):
    """Method for updating player status."""
    cursor = mysql.connection.cursor()
    sql = "UPDATE match_players SET status = %s WHERE match_id = %s AND player_id <> %s"
    cursor.execute(sql, (status, match_id, player_id))
    mysql.connection.commit()
    cursor.close()
