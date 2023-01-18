"""Module for database operations on maps_v2 tables."""
from tof_server import mysql

MAPS_PER_PAGE = 20


def find_id_by_code(code):
    """Method for getting map id based on it's code."""
    cursor = mysql.connection.cursor()
    sql = "SELECT id FROM maps_v2 WHERE download_code = %s"

    cursor.execute(sql, (code,))
    map_id = cursor.fetchone()
    cursor.close()

    if map_id:
        return map_id[0]

    return None


def is_base_code_used(base_code):
    """Method for checking if base code is in use."""
    cursor = mysql.connection.cursor()
    sql = "SELECT id FROM maps_v2 WHERE base_code = %s"

    cursor.execute(sql, (base_code,))
    map_id = cursor.fetchone()
    cursor.close()

    if map_id:
        return True

    return False


def find_highest_iteration_for_base_code(base_code):
    """Method for finding highest iteration for a base code."""
    cursor = mysql.connection.cursor()
    sql = "SELECT max(iteration) FROM maps_v2 WHERE base_code = %s"

    cursor.execute(sql, (base_code,))
    iteration = cursor.fetchone()
    cursor.close()

    return iteration


def find_code_by_id(map_id):
    """Method for getting map code based on it's id."""
    cursor = mysql.connection.cursor()
    sql = "SELECT download_code FROM maps_v2 WHERE id = %s"

    cursor.execute(sql, (map_id,))
    code = cursor.fetchone()
    cursor.close()

    if code:
        return code[0]

    return None


def find_player_by_code(code):
    """Method for finding player_id by map code."""
    cursor = mysql.connection.cursor()
    sql = "SELECT player_id FROM maps_v2 WHERE download_code = %s"

    cursor.execute(sql, (code,))
    player_id = cursor.fetchone()
    cursor.close()

    if player_id:
        return player_id[0]

    return None


def persist_new_map(code, base_code, iteration, author_id):
    """Method for persisting data for new map."""
    cursor = mysql.connection.cursor()

    map_sql = """INSERT INTO maps_v2
                (download_code, base_code, iteration, player_id)
                VALUES (%s, %s, %s, %s)"""

    cursor.execute(map_sql, (code, base_code, iteration, author_id))

    mysql.connection.commit()
    cursor.close()


def find_metadata_by_code(code):
    """Method for getting map metadata by code."""
    cursor = mysql.connection.cursor()
    sql = "SELECT id, base_code, iteration, creation_time, player_id FROM maps_v2 WHERE download_code = %s"

    cursor.execute(sql, (code,))
    map_id = cursor.fetchone()
    cursor.close()

    if map_id:
        return {
            'id': map_id[0],
            'created': map_id[3],
            'author': map_id[4],
            'base_code': map_id[1],
            'iteration': map_id[2],
            'code': code
        }

    return None


def find_latest_maps_metadata(offset_id):
    """Method for getting latest maps metadata."""
    cursor = mysql.connection.cursor()

    if offset_id > -1:
        sql = "SELECT id, download_code, base_code, iteration, creation_time, player_id \
            FROM maps_v2 WHERE id < %s ORDER BY id DESC LIMIT %s"
        cursor.execute(sql, (offset_id, MAPS_PER_PAGE))
    else:
        sql = "SELECT id, download_code, base_code, iteration, creation_time, player_id \
            FROM maps_v2 ORDER BY id DESC LIMIT %s"
        cursor.execute(sql, (MAPS_PER_PAGE,))

    maps_metadata = cursor.fetchall()
    cursor.close()

    result = []

    for map_metadata in maps_metadata:
        result.append({
            'id': map_metadata[0],
            'code': map_metadata[1],
            'base_code': map_metadata[2],
            'iteration': map_metadata[3],
            'created': map_metadata[4],
            'author': map_metadata[5],
        })

    return result


def get_all_codes():
    """Method for getting all map codes."""
    cursor = mysql.connection.cursor()

    sql = "SELECT download_code FROM maps_v2"
    cursor.execute(sql)

    map_codes = cursor.fetchall()
    cursor.close()

    return map_codes


def mark_map_download(map_id):
    """Method for marking map download for stats."""
    cursor = mysql.connection.cursor()

    download_sql = "INSERT INTO maps_downloads_v2 (map_id) VALUES (%s)"

    cursor.execute(download_sql, (map_id, ))

    mysql.connection.commit()
    cursor.close()


def find_download_by_ids(ids):
    """Method for getting map data by list of ids."""
    ids = ", ".join(str(x) for x in ids)

    cursor = mysql.connection.cursor()
    map_downloads_sql = "SELECT map_id, count(map_id) FROM maps_downloads_v2 WHERE map_id \
        IN (" + ids + ") GROUP BY map_id"
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

    sql = "SELECT id, download_code, base_code, iteration, creation_time, player_id \
        FROM maps_v2 WHERE player_id = %s ORDER BY id DESC"
    cursor.execute(sql, (player_id, ))

    maps_metadata = cursor.fetchall()
    cursor.close()

    result = []

    for map_metadata in maps_metadata:
        result.append({
            'id': map_metadata[0],
            'code': map_metadata[1],
            'base_code': map_metadata[2],
            'iteration': map_metadata[3],
            'created': map_metadata[4],
            'author': map_metadata[5],
        })

    return result


def find_maps_metadata_by_top_downloads(limit):
    """Method for getting top downloaded maps metadata."""
    cursor = mysql.connection.cursor()

    sql = "SELECT \
        maps_v2.id, \
        maps_v2.download_code, \
        maps_v2.base_code, \
        maps_v2.iteration, \
        maps_v2.creation_time, \
        maps_v2.player_id, \
        count(maps_v2.id) AS downloads \
        FROM maps_downloads_v2 \
        JOIN maps_v2 ON maps_downloads_v2.map_id = maps_v2.id \
        GROUP BY maps_v2.id ORDER BY \
        downloads DESC, \
        id ASC \
        LIMIT %s;"

    cursor.execute(sql, (limit,))
    maps_metadata = cursor.fetchall()
    cursor.close()

    result = []

    for map_metadata in maps_metadata:
        result.append({
            'id': map_metadata[0],
            'code': map_metadata[1],
            'base_code': map_metadata[2],
            'iteration': map_metadata[3],
            'created': map_metadata[4],
            'author': map_metadata[5],
            'downloads': map_metadata[6]
        })

    return result
