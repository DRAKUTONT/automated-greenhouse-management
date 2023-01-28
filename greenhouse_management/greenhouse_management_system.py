from greenhouse_management.greenhouse import Greenhouse
from greenhouse_management.data_base.insert_data import add_temperature, add_humidity, add_soil_humidity
from greenhouse_management.data_base.update_data import update_temperature, update_humidity, update_soil_humidity
from greenhouse_management.constants import MAX_VALUES_IN_DB


class GreenhouseManagementSystem:
    def __init__(self, max_temperature: int, min_humidity: int, min_soil_humidity: int):
        self.max_temperature = max_temperature
        self.min_humidity = min_humidity
        self.min_soil_humidity = min_soil_humidity

        self.greenhouse = Greenhouse(max_temperature, min_humidity, min_soil_humidity)

        self.unique_id = 0

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

    def get_parameters(self) -> dict:
        return self.greenhouse.get_parameters()

    def set_parameters(self, parameters: dict):
        self.greenhouse.set_parameters(parameters)

    def enable_emergency_mode(self):
        self.greenhouse.enable_emergency_mode()

    def disable_emergency_mode(self):
        self.greenhouse.disable_emergency_mode()
