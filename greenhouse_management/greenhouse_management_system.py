from telegram_bot.utils.draw_graphic import draw_graph_average_values, draw_sensors_graphics
from greenhouse_management.greenhouse import Greenhouse
from greenhouse_management.data_base.get_data import get_max_id, get_humidity, get_temperatures, get_soil_humidity
from greenhouse_management.data_base.insert_data import add_temperature, add_humidity, add_soil_humidity
from greenhouse_management.data_base.update_data import update_temperature, update_humidity, update_soil_humidity, \
    clear_database
from telegram_bot.utils.formatting import formatting_data_for_graphic, formatting_data_for_tables
from telegram_bot.utils.create_table import create_table
from greenhouse_management.constants import MAX_VALUES_IN_DB


class GreenhouseManagementSystem:
    def __init__(self, max_temperature: int, min_humidity: int, min_soil_humidity: int):
        self.greenhouse = Greenhouse(max_temperature, min_humidity, min_soil_humidity)

        self.unique_id = get_max_id() + 1

    def fill_database(self):
        for _ in range(MAX_VALUES_IN_DB):
            data = self.greenhouse.get_systems_data()
            add_temperature({**data['ventilation_system'], 'id': self.unique_id})
            add_humidity({**data['humidification_system'], 'id': self.unique_id})
            add_soil_humidity({**data['irrigation_system'], 'id': self.unique_id})

            self.unique_id += 1

    def update_data(self):
        data = self.greenhouse.get_systems_data()
        update_temperature({**data['ventilation_system'], 'id': self.unique_id})
        update_humidity({**data['humidification_system'], 'id': self.unique_id})
        update_soil_humidity({**data['irrigation_system'], 'id': self.unique_id})

        self.unique_id += 1


    def get_data(self):
        return self.greenhouse.get_systems_data()

    def get_parameters(self) -> dict:
        return self.greenhouse.get_parameters()

    def set_parameters(self, parameters: dict):
        self.greenhouse.set_parameters(parameters)

    def is_window_work(self) -> bool:
        return self.greenhouse.is_window_worked()

    def set_window_state(self, state: bool):
        self.greenhouse.set_window_state(state=state)

    def is_humidifier_work(self) -> bool:
        return self.greenhouse.is_humidifier_worked()

    def set_humidifier_state(self, state: bool):
        self.greenhouse.set_humidifier_state(state=state)

    def get_sprinklers_state(self) -> dict:
        return self.greenhouse.get_sprinklers_state()

    def is_sprinkler_work(self, device_id: int) -> bool:
        return self.greenhouse.is_sprinkler_worked(device_id=device_id)

    def set_sprinkler_state(self, state: bool, device_id: int):
        self.greenhouse.set_sprinkler_state(state=state, device_id=device_id)

    def get_emergency_mode_status(self):
        return self.greenhouse.get_emergency_mode_status()

    def enable_emergency_mode(self):
        self.greenhouse.enable_emergency_mode()

    def disable_emergency_mode(self):
        self.greenhouse.disable_emergency_mode()

    def clear_database(self):
        clear_database()
        self.unique_id = 1

    @staticmethod
    def create_average_value_table():
        temp_data = get_temperatures()
        hum_data = get_humidity()
        temp_and_hum_data = [{**temp, **hum} for temp, hum in zip(temp_data, hum_data)]
        data = formatting_data_for_tables(need_keys=['average_temp', 'average_hum'],
                                          data=temp_and_hum_data,
                                          new_keys=['Средняя температура', 'Средняя влажность'])
        create_table(data=data, filename='average_values.csv')

    @staticmethod
    def create_sensors_table(sensor_type: str):
        if sensor_type == 'temp_and_hum':
            temp_data = get_temperatures()
            hum_data = get_humidity()
            temp_and_hum_data = [{**temp, **hum} for temp, hum in zip(temp_data, hum_data)]
            need_keys = [f'temp_{i}' for i in range(1, 5)] + [f'hum_{i}' for i in range(1, 5)]
            new_keys = [f'Датчик температуры №{i}' for i in range(1, 5)] + [f'Датчик влажности №{i}' for i in
                                                                            range(1, 5)]
            data = formatting_data_for_tables(need_keys=need_keys, data=temp_and_hum_data, new_keys=new_keys)
            create_table(data=data, filename='temp_and_hum.csv')

        elif sensor_type == 'soil_hum':
            soil_hum_data = get_soil_humidity()
            need_keys = [f'soil_hum_{i}' for i in range(1, 7)]
            new_keys = [f'Датчик влажности почвы №{i}' for i in range(1, 7)]
            data = formatting_data_for_tables(need_keys=need_keys, data=soil_hum_data, new_keys=new_keys)
            create_table(data=data, filename='soil_hum.csv')

    @staticmethod
    def draw_average_value_graphic():
        temp_data = get_temperatures()
        av_temp = [i['average_temp'] for i in temp_data]

        hum_data = get_humidity()
        av_hum = [i['average_hum'] for i in hum_data]

        draw_graph_average_values(av_temp, av_hum, 'average_values.png', 20, 20)

    @staticmethod
    def draw_sensors_graphic(sensor_type: str):
        if sensor_type == 'temp_and_hum':
            temp_data = get_temperatures()
            hum_data = get_humidity()

            temp_values, hum_values = formatting_data_for_graphic(type_of_graphic='temp_and_hum', temperature=temp_data,
                                                                  humidity=hum_data)
            draw_sensors_graphics(temp_values, 'temp_graphic.png', 20, 20)
            draw_sensors_graphics(hum_values, 'hum_graphic.png', 20, 20)

        elif sensor_type == 'soil_hum':
            soil_hum_data = get_soil_humidity()
            soil_hum_values = formatting_data_for_graphic(type_of_graphic='soil_hum', soil_humidity=soil_hum_data)
            draw_sensors_graphics(soil_hum_values, 'soil_hum_graphic.png', 20, 20)
