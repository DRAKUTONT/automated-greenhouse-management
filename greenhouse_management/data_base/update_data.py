from greenhouse_management.data_base.connect_to_db import connect_to_database


def clear_database():
    query_1 = '''DELETE FROM temperature'''
    query_2 = '''DELETE FROM humidity'''
    query_3 = '''DELETE FROM soil_humidity'''

    connect_to_database(query_1, mode='w')
    connect_to_database(query_2, mode='w')
    connect_to_database(query_3, mode='w')


def update_temperature(data: dict[str, float]):
    need_values = ', '.join([f'{key} = {value}' for key, value in data.items()])
    query = f'''UPDATE temperature SET {need_values} WHERE id = (SELECT min(id) from temperature)'''

    connect_to_database(query, mode='w')


def update_humidity(data: dict[str, float]):
    need_values = ', '.join([f'{key} = {value}' for key, value in data.items()])
    query = f'''UPDATE humidity SET {need_values} WHERE id = (SELECT min(id) from humidity)'''

    connect_to_database(query, mode='w')


def update_soil_humidity(data: dict[str, float]):
    need_values = ', '.join([f'{key} = {value}' for key, value in data.items()])
    query = f'''UPDATE soil_humidity SET {need_values} WHERE id = (SELECT min(id) from soil_humidity)'''

    connect_to_database(query, mode='w')