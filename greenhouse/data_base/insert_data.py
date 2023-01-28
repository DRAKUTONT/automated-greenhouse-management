from greenhouse.data_base.connect_to_db import connect_to_data_base


def add_temperature(data: dict[str, float]):
    values = ', '.join([f'{value}' for value in data.values()])
    query = f'''INSERT INTO temperature VALUES ({values})'''

    connect_to_data_base(query, mode='w')


def add_humidity(data: dict[str, float]):
    values = ', '.join([f'{value}' for value in data.values()])
    query = f'''INSERT INTO temperature VALUES ({values})'''

    connect_to_data_base(query, mode='w')


def add_soil_humidity(data: dict[str, float]):
    values = ', '.join([f'{value}' for value in data.values()])
    query = f'''INSERT INTO temperature VALUES ({values})'''

    connect_to_data_base(query, mode='w')