from data_base.connect_to_db import connect_to_data_base


def clear_data_base():  # this method will be implemented later
    ...


def set_temperatures(data: dict[str, float]):
    need_values = ', '.join([f'{key} = {value}' for key, value in data.items()])
    query = f'''UPDATE temperatures SET {need_values}'''

    connect_to_data_base(query, mode='w')


def set_humidity(data: dict[str, float]):
    need_values = ', '.join([f'{key} = {value}' for key, value in data.items()])
    query = f'''UPDATE humidity SET {need_values}'''

    connect_to_data_base(query, mode='w')


def set_soil_humidity(data: dict[str, float]):
    need_values = ', '.join([f'{key} = {value}' for key, value in data.items()])
    query = f'''UPDATE soil_humidity SET {need_values}'''

    connect_to_data_base(query, mode='w')

# TODO: в переспективе стоит переделать

