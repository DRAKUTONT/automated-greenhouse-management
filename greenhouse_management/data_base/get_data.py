from typing import List

from greenhouse_management.data_base.connect_to_db import connect_to_database


def get_temperatures() -> List[dict]:
    query = '''SELECT * FROM temperature'''
    result = connect_to_database(query)

    data = []
    for record in result:
        params = {}
        for i, item in enumerate(record[:-2]):
            params[f'temp_{i + 1}'] = item

        params['average_temp'] = record[-2]
        data.append(params)

    return data


def get_humidity() -> List[dict]:
    query = '''SELECT * FROM humidity'''
    result = connect_to_database(query)

    data = []
    for record in result:
        params = {}
        for i, item in enumerate(record[:-2]):
            params[f'hum_{i + 1}'] = item

        params['average_hum'] = record[-2]
        data.append(params)

    return data


def get_soil_humidity() -> List[dict]:
    query = '''SELECT * FROM soil_humidity'''
    result = connect_to_database(query)

    data = []
    for record in result:
        params = {}
        for i, item in enumerate(record[:-2]):
            params[f'soil_hum_{i + 1}'] = item

        params['average_soil_hum'] = record[-2]
        data.append(params)

    return data