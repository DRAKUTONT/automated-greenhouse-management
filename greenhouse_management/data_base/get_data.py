from typing import List

from greenhouse_management.data_base.connect_to_db import connect_to_database


def get_max_id() -> int:
    query = '''SELECT max(id) FROM temperature'''
    result = connect_to_database(query)[0][0]
    if result:
        return int(result)

    return 0


def get_temperatures() -> List[dict]:
    query = '''SELECT temp_1, temp_2, temp_3, temp_4, average_temp FROM temperature'''
    result = connect_to_database(query)

    data = []
    for record in result:
        params = {}
        for i, item in enumerate(record[:-1]):
            params[f'temp_{i + 1}'] = item

        params['average_temp'] = record[-1]
        data.append(params)

    return data


def get_humidity() -> List[dict]:
    query = '''SELECT hum_1, hum_2, hum_3, hum_4, average_hum FROM humidity'''
    result = connect_to_database(query)

    data = []
    for record in result:
        params = {}
        for i, item in enumerate(record[:-1]):
            params[f'hum_{i + 1}'] = item

        params['average_hum'] = record[-1]
        data.append(params)

    return data


def get_soil_humidity() -> List[dict]:
    query = '''SELECT soil_hum_1, soil_hum_2, soil_hum_3, soil_hum_4, soil_hum_5, soil_hum_6, average_soil_hum FROM soil_humidity'''
    result = connect_to_database(query)

    data = []
    for record in result:
        params = {}
        for i, item in enumerate(record[:-1]):
            params[f'soil_hum_{i + 1}'] = item

        params['average_soil_hum'] = record[-1]
        data.append(params)

    return data