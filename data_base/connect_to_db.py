import sqlite3


def connect_to_data_base(query: str, mode: str = 'r'):
    connection = sqlite3.connect('greenhouse_db.db')
    cursor = connection.cursor()

    cursor.execute(query)

    if mode == 'r':
        return cursor.fetchall()