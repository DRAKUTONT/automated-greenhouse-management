from greenhouse_management.draw_graphics.draw_graphic import draw_graph_average_values, draw_sensors_graphics
from greenhouse_management.greenhouse import Greenhouse
from greenhouse_management.data_base.get_data import get_max_id, get_humidity, get_temperatures, get_soil_humidity
from greenhouse_management.data_base.insert_data import add_temperature, add_humidity, add_soil_humidity
from greenhouse_management.data_base.update_data import update_temperature, update_humidity, update_soil_humidity, \
    clear_database
from greenhouse_management.constants import MAX_VALUES_IN_DB


class GreenhouseManagementSystem:
    def __init__(self, max_temperature: int, min_humidity: int, min_soil_humidity: int):
        self.max_temperature = max_temperature
        self.min_humidity = min_humidity
        self.min_soil_humidity = min_soil_humidity

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

    def is_sprinkler_work(self, device_id: int) -> bool:
        return self.greenhouse.is_sprinkler_worked(device_id=device_id)

    def set_sprinkler_state(self, state: bool, device_id: int):
        self.greenhouse.set_sprinkler_state(state=state, device_id=device_id)

    def get_emergency_mode_status(self):
        return

    def enable_emergency_mode(self):
        self.greenhouse.enable_emergency_mode()

    def disable_emergency_mode(self):
        self.greenhouse.disable_emergency_mode()

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
            temp_values = [[i['temp_1'] for i in temp_data],
                           [i['temp_2'] for i in temp_data],
                           [i['temp_3'] for i in temp_data],
                           [i['temp_4'] for i in temp_data]]
            draw_sensors_graphics(temp_values, 'temp_graphic.png', 20, 20)

            hum_data = get_humidity()
            hum_values = [[i['hum_1'] for i in hum_data],
                          [i['hum_2'] for i in hum_data],
                          [i['hum_3'] for i in hum_data],
                          [i['hum_4'] for i in hum_data]]
            draw_sensors_graphics(hum_values, 'hum_graphic.png', 20, 20)

        elif sensor_type == 'soil_hum':
            soil_hum_data = get_soil_humidity()
            hum_values = [[i['soil_hum_1'] for i in soil_hum_data],
                          [i['soil_hum_2'] for i in soil_hum_data],
                          [i['soil_hum_3'] for i in soil_hum_data],
                          [i['soil_hum_4'] for i in soil_hum_data],
                          [i['soil_hum_5'] for i in soil_hum_data],
                          [i['soil_hum_6'] for i in soil_hum_data]]
            draw_sensors_graphics(hum_values, 'soil_hum_graphic.png', 20, 20)

    @staticmethod
    def clear_database():
        clear_database()
