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
