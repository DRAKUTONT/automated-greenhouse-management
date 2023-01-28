from greenhouse_management.data_base.connect_to_db import connect_to_database


def clear_data_base():
    query = '''DROP TABLE temperature, humidity, soil_humidity'''
    connect_to_database(query, mode='w')


def update_temperatures(data: dict[str, float]):
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