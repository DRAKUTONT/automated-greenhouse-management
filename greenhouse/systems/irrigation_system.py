from typing import List
from greenhouse.sensors.soil_humidity_sensor import SoilHumiditySensor
from greenhouse.devices.sprinkler import Sprinkler


class IrrigationSystem:
    def __init__(self, sensors: List[SoilHumiditySensor], sprinklers: List[Sprinkler],
                 min_soil_humidity: int):
        self.sensors = sensors
        self.sprinklers = sprinklers
        self.min_soil_humidity = min_soil_humidity

        self.emergency_mode = False

    def set_min_soil_humidity(self, min_soil_humidity: int):
        self.min_soil_humidity = min_soil_humidity

    def get_min_soil_humidity(self):
        return self.min_soil_humidity

    def get_current_soil_humidity(self) -> dict:
        data = {}
        for sensor in self.sensors:
            data[sensor.number] = int(sensor.get_data()['soil_humidity'])

        return data

    def calculate_average_soil_humidity(self) -> float:
        average_temp = sum(self.get_current_soil_humidity().values()) / len(self.get_current_soil_humidity().values())
        return average_temp

    def enable_device(self, number):
        if self.calculate_average_soil_humidity() < self.min_soil_humidity or self.emergency_mode:
            self.sprinklers[number].enable()

    def disable_device(self, number):
        self.sprinklers[number].disable()

    def enable_emergency_mode(self):
        self.emergency_mode = True

    def disable_emergency_mode(self):
        self.emergency_mode = False
