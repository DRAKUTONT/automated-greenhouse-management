from typing import List
from greenhouse.sensors.humidity_and_temperature_sensor import HumidityAndTemperatureSensor
from greenhouse.devices.humidifier import Humidifier


class HumidificationSystem:
    def __init__(self, sensors: List[HumidityAndTemperatureSensor], humidifier: Humidifier,
                 min_humidity: int):
        self.sensors = sensors
        self.humidifier = humidifier
        self.min_humidity = min_humidity

        self.emergency_mode = False

    def set_min_humidity(self, min_humidity: int):
        self.min_humidity = min_humidity

    def get_min_humidity(self):
        return self.min_humidity

    def get_current_humidity(self) -> dict:
        data = {}
        for sensor in self.sensors:
            data[sensor.number] = int(sensor.get_data()['humidity'])

        return data

    def calculate_average_humidity(self) -> float:
        average_temp = sum(self.get_current_humidity().values()) / len(self.get_current_humidity().values())
        return average_temp

    def enable_humidifier(self):
        if self.calculate_average_humidity() < self.min_humidity or self.emergency_mode:
            self.humidifier.enable()

    def disable_humidifier(self):
        self.humidifier.disable()

    def enable_emergency_mode(self):
        self.emergency_mode = True

    def disable_emergency_mode(self):
        self.emergency_mode = False
