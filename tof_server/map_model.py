"""Model for handling operations on map data"""
import json

def persist_map(map_data, metadata, cursor, player_id):
    """Method for persisting map data"""
    serialized_map_data = json.dumps(map_data)

    map_sql = """INSERT INTO maps
                (download_code, map_hash, player_id)
                VALUES (%s, %s, %s)"""

    cursor.execute(map_sql, (metadata['code'], metadata['hash'], player_id))

    last_id_sql = "SELECT LAST_INSERT_ID()"
    cursor.execute(last_id_sql)

    last_id = cursor.fetchone()

    map_data_sql = "INSERT INTO maps_data (map_id, json) VALUES (%s, %s)"

    cursor.execute(map_data_sql, (last_id[0], serialized_map_data))

def find_map(map_code, cursor):
    """Method for retrieving map data"""
    map_code_sql = "SELECT id FROM maps WHERE download_code = %s"
    cursor.execute(map_code_sql, (map_code,))
    map_id = cursor.fetchone()

    if not map_id:
        return None

    map_data_sql = "SELECT json FROM maps_data WHERE map_id = %s"
    cursor.execute(map_data_sql, (map_id[0],))
    map_data = cursor.fetchone()

    return json.loads(map_data[0])
