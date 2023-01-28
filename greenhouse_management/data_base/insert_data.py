from greenhouse_management.data_base.connect_to_db import connect_to_database


def add_temperature(data: dict[str, float]):
    values = ', '.join([f'{value}' for value in data.values()])
    query = f'''INSERT INTO temperature VALUES ({values})'''

    connect_to_database(query, mode='w')


def add_humidity(data: dict[str, float]):
    values = ', '.join([f'{value}' for value in data.values()])
    query = f'''INSERT INTO humidity VALUES ({values})'''

    connect_to_database(query, mode='w')


def add_soil_humidity(data: dict[str, float]):
    values = ', '.join([f'{value}' for value in data.values()])
    query = f'''INSERT INTO soil_humidity VALUES ({values})'''

    connect_to_database(query, mode='w')