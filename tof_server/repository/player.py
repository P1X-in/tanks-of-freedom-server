"""Module for database operations on players table."""
from tof_server import mysql


def create_new_player(pin):
    """Method for creating new player entry."""
    cursor = mysql.connection.cursor()

    insert_sql = "INSERT INTO players (auto_pin) VALUES (%s)"
    id_sql = "SELECT LAST_INSERT_ID()"

    cursor.execute(insert_sql, (pin,))
    cursor.execute(id_sql)

    insert_data = cursor.fetchone()

    mysql.connection.commit()
    cursor.close()

    return insert_data[0]
