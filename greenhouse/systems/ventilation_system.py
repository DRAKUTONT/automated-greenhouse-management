from typing import List
from greenhouse.sensors.humidity_and_temperature_sensor import HumidityAndTemperatureSensor
from greenhouse.devices.windows import Window


class VentilationSystem:
    def __init__(self, sensors: List[HumidityAndTemperatureSensor], window: Window, max_temperature: int):
        self.sensors = sensors
        self.window = window
        self.max_temperature = max_temperature

        self.emergency_mode = False

    def set_max_temperature(self, max_temperature: int):
        self.max_temperature = max_temperature

    def get_max_temperature(self):
        return self.max_temperature

    def get_current_temperatures(self) -> dict:
        data = {}
        for sensor in self.sensors:
            data[sensor.number] = int(sensor.get_data()['temperature'])

        return data

    def calculate_average_temperature(self) -> float:
        average_temp = sum(self.get_current_temperatures().values()) / len(self.get_current_temperatures().values())
        return average_temp

    def open_windows(self):
        if self.calculate_average_temperature() > self.max_temperature or self.emergency_mode:
            self.window.open()

    def close_windows(self):
        self.window.close()

    def enable_emergency_mode(self):
        self.emergency_mode = True

    def disable_emergency_mode(self):
        self.emergency_mode = False