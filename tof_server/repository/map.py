"""Module for database operations on maps tables."""
import json
from tof_server import mysql

MAPS_PER_PAGE = 20


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
    map_id = cursor.fetchone()
    cursor.close()

    if map_id:
        return map_id[0]

    return None


def find_code_by_id(map_id):
    """Method for getting map code based on it's id."""
    cursor = mysql.connection.cursor()
    sql = "SELECT download_code FROM maps WHERE id = %s"

    cursor.execute(sql, (map_id,))
    code = cursor.fetchone()
    cursor.close()

    if code:
        return code[0]

    return None


def find_player_by_code(code):
    """Method for finding player_id by map code."""
    cursor = mysql.connection.cursor()
    sql = "SELECT player_id FROM maps WHERE download_code = %s"

    cursor.execute(sql, (code,))
    player_id = cursor.fetchone()
    cursor.close()

    if player_id:
        return player_id[0]

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


def find_data_by_ids(ids):
    """Method for getting map data by list of ids."""
    ids = ", ".join(str(x) for x in ids)

    cursor = mysql.connection.cursor()
    map_data_sql = "SELECT map_id, json FROM maps_data WHERE map_id IN (" + ids + ")"
    cursor.execute(map_data_sql)
    maps_data = cursor.fetchall()
    cursor.close()

    result = {}

    for map_data in maps_data:
        result[map_data[0]] = map_data[1]

    return result


def find_metadata_by_code(code):
    """Method for getting map metadata by code."""
    cursor = mysql.connection.cursor()
    sql = "SELECT id, creation_time, player_id FROM maps WHERE download_code = %s"

    cursor.execute(sql, (code,))
    map_id = cursor.fetchone()
    cursor.close()

    if map_id:
        return {
            'id': map_id[0],
            'created': map_id[1],
            'author': map_id[2],
            'code': code
        }

    return None


def find_latest_maps_metadata(offset_id):
    """Method for getting latest maps metadata."""
    cursor = mysql.connection.cursor()

    if offset_id > -1:
        sql = "SELECT id, download_code, creation_time, player_id FROM maps WHERE id < %s ORDER BY id DESC LIMIT %s"
        cursor.execute(sql, (offset_id, MAPS_PER_PAGE))
    else:
        sql = "SELECT id, download_code, creation_time, player_id FROM maps ORDER BY id DESC LIMIT %s"
        cursor.execute(sql, (MAPS_PER_PAGE,))

    maps_metadata = cursor.fetchall()
    cursor.close()

    result = []

    for map_metadata in maps_metadata:
        result.append({
            'id': map_metadata[0],
            'code': map_metadata[1],
            'created': map_metadata[2],
            'author': map_metadata[3],
        })

    return result


def get_all_codes():
    """Method for getting all map codes."""
    cursor = mysql.connection.cursor()

    sql = "SELECT download_code FROM maps"
    cursor.execute(sql)

    map_codes = cursor.fetchall()
    cursor.close()

    return map_codes


def mark_map_download(map_id):
    """Method for marking map download for stats."""
    cursor = mysql.connection.cursor()

    download_sql = "INSERT INTO maps_downloads (map_id) VALUES (%s)"

    cursor.execute(download_sql, (map_id, ))

    mysql.connection.commit()
    cursor.close()


def find_download_by_ids(ids):
    """Method for getting map data by list of ids."""
    ids = ", ".join(str(x) for x in ids)

    cursor = mysql.connection.cursor()
    map_downloads_sql = "SELECT map_id, count(map_id) FROM maps_downloads WHERE map_id IN (" + ids + ") GROUP BY map_id"
    cursor.execute(map_downloads_sql)
    maps_data = cursor.fetchall()
    cursor.close()

    result = {}

    for map_data in maps_data:
        result[map_data[0]] = map_data[1]

    return result


def find_maps_metadata_by_player(player_id):
    """Method for getting player maps metadata."""
    cursor = mysql.connection.cursor()

    sql = "SELECT id, download_code, creation_time, player_id FROM maps WHERE player_id = %s ORDER BY id DESC"
    cursor.execute(sql, (player_id, ))

    maps_metadata = cursor.fetchall()
    cursor.close()

    result = []

    for map_metadata in maps_metadata:
        result.append({
            'id': map_metadata[0],
            'code': map_metadata[1],
            'created': map_metadata[2],
            'author': map_metadata[3],
        })

    return result
