from typing import List
from sensors.soil_humidity_sensor import SoilHumiditySensor
from tools.sprinkler import Sprinkler


class IrrigationSystem:
    def __init__(self, sensors: List[SoilHumiditySensor], sprinklers: List[Sprinkler],
                 min_soil_humidity: int):
        self.sensors = sensors
        self.sprinklers = sprinklers
        self.min_soil_humidity = min_soil_humidity

        self.emergency_mode = False

    def get_current_humidity(self) -> dict:
        data = {}
        for sensor in self.sensors:
            data[sensor.number] = int(sensor.get_data()['humidity'])

        return data

    def calculate_average_soil_humidity(self) -> float:
        average_temp = sum(self.get_current_humidity().values()) / len(self.get_current_humidity().values())
        return average_temp

    def enable_sprinkler(self, number):
        if self.calculate_average_soil_humidity() < self.min_soil_humidity or self.emergency_mode:
            self.sprinklers[number].enable()

    def disable_sprinkler(self, number):
        self.sprinklers[number].disable()

    def enable_emergency_mode(self):
        self.emergency_mode = True

    def disable_emergency_mode(self):
        self.emergency_mode = False
