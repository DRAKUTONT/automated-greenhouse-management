from data_base.connect_to_db import connect_to_data_base


def get_temperatures() -> dict[str, float]:
    query = '''SELECT * FROM temperature'''
    result = connect_to_data_base(query)

    data = {}
    for i, item in enumerate(result[:-1]):
        data[f'temp_{i + 1}'] = item

    data['average_temp'] = result[-1]

    return data


def get_humidity() -> dict[str, float]:
    query = '''SELECT * FROM humidity'''
    result = connect_to_data_base(query)

    data = {}
    for i, item in enumerate(result[:-1]):
        data[f'hum_{i + 1}'] = item

    data['average_hum'] = result[-1]

    return data


def get_soil_humidity() -> dict[str, float]:
    query = '''SELECT * FROM humidity'''
    result = connect_to_data_base(query)

    data = {}
    for i, item in enumerate(result[:-1]):
        data[f'soil_hum_{i + 1}'] = item

    data['average_soil_hum'] = result[-1]

    return data

