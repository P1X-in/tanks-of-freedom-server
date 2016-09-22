"""Module for database operations on maps tables."""
import json
from tof_server import mysql


def find_code_by_hash(md5_hash):
    """Method for finding a map code by its hash."""
    cursor = mysql.connection.cursor()
    sql = "SELECT download_code FROM maps WHERE map_hash = %s"

    cursor.execute(sql, (md5_hash,))
    previous_code = cursor.fetchone()
    cursor.close()

    if previous_code:
        return previous_code[0]

    return None


def find_id_by_code(code):
    """Method for getting map id based on it's code."""
    cursor = mysql.connection.cursor()
    sql = "SELECT id FROM maps WHERE download_code = %s"

    cursor.execute(sql, (code,))
    previous_code = cursor.fetchone()
    cursor.close()

    if previous_code:
        return previous_code[0]

    return None


def persist_new_map(map_data, code, map_hash, author_id):
    """Method for persisting data for new map."""
    cursor = mysql.connection.cursor()
    serialized_map_data = json.dumps(map_data)

    map_sql = """INSERT INTO maps
                (download_code, map_hash, player_id)
                VALUES (%s, %s, %s)"""

    cursor.execute(map_sql, (code, map_hash, author_id))

    last_id_sql = "SELECT LAST_INSERT_ID()"
    cursor.execute(last_id_sql)

    last_id = cursor.fetchone()

    map_data_sql = "INSERT INTO maps_data (map_id, json) VALUES (%s, %s)"

    cursor.execute(map_data_sql, (last_id[0], serialized_map_data))

    mysql.connection.commit()
    cursor.close()


def find_data_by_code(code):
    """Method for getting map data by code."""
    map_id = find_id_by_code(code)
    if map_id is None:
        return None

    cursor = mysql.connection.cursor()
    map_data_sql = "SELECT json FROM maps_data WHERE map_id = %s"
    cursor.execute(map_data_sql, (map_id,))
    map_data = cursor.fetchone()
    cursor.close()

    if map_data:
        return map_data[0]

    return None
