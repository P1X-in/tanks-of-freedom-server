"""Module for database operations on maps tables."""
from tof_server import mysql


def find_code_by_hash(md5_hash):
    """Method for finding a map code by its hash."""
    cursor = mysql.connection.cursor()
    sql = "SELECT download_code FROM maps WHERE map_hash = %s"

    cursor.execute(sql, (md5_hash,))
    previous_code = cursor.fetchone()

    if previous_code:
        return previous_code[0]

    return None
