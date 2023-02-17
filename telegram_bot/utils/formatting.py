from typing import Union


def formatting_sensor_data_for_user(data: dict, sensor_name: str, name_of_average_value: str = None) -> dict:
    formatted_data = {}
    for index, (key, value) in enumerate(data.items()):
        if key.startswith('average_'):
            formatted_data[name_of_average_value] = value
        else:
            formatted_data[f'{sensor_name} №{index + 1}'] = value

    return formatted_data


def formatting_device_data_for_user(data: dict, device_name: str, enable_name: str, disable_name: str) -> dict:
    formatted_data = {}
    for index, (key, value) in enumerate(data.items()):
        formatted_data[f'{device_name} №{index + 1}'] = enable_name if value else disable_name

    return formatted_data


def formatting_data_for_graphic(type_of_graphic: str, **data) -> Union[tuple, list]:
    if type_of_graphic == 'temp_and_hum':
        temp_data = data['temperature']
        temp_values = [[i['temp_1'] for i in temp_data],
                       [i['temp_2'] for i in temp_data],
                       [i['temp_3'] for i in temp_data],
                       [i['temp_4'] for i in temp_data]]

        hum_data = data['humidity']
        hum_values = [[i['hum_1'] for i in hum_data],
                      [i['hum_2'] for i in hum_data],
                      [i['hum_3'] for i in hum_data],
                      [i['hum_4'] for i in hum_data]]

        return temp_values, hum_values

    elif type_of_graphic == 'soil_hum':
        soil_hum_data = data['soil_humidity']
        soil_hum_values = [[i['soil_hum_1'] for i in soil_hum_data],
                           [i['soil_hum_2'] for i in soil_hum_data],
                           [i['soil_hum_3'] for i in soil_hum_data],
                           [i['soil_hum_4'] for i in soil_hum_data],
                           [i['soil_hum_5'] for i in soil_hum_data],
                           [i['soil_hum_6'] for i in soil_hum_data]]

        return soil_hum_values
