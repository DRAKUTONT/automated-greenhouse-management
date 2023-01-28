from typing import List
from greenhouse_management.sensors.humidity_and_temperature_sensor import HumidityAndTemperatureSensor
from greenhouse_management.devices.humidifier import Humidifier
from greenhouse_management.systems.abstract_system import AbstractSystem


class HumidificationSystem(AbstractSystem):
    def __init__(self, sensors: List[HumidityAndTemperatureSensor], device: Humidifier, parameter: int):
        super(HumidificationSystem, self).__init__(sensors=sensors, device=device, parameter=parameter)

    def get_data(self):
        data = {**self.get_current_temperatures(), 'average_temp': self.calculate_average_sensors_value()}
        return data

    def get_current_temperatures(self) -> dict:
        data = {}
        for sensor in self.sensors:
            data[f'temp_{sensor.number}'] = float(sensor.get_data()['temperature'])

        return data

    def enable_device(self):
        if self.calculate_average_sensors_value() > self.parameter or self.emergency_mode:
            self.device.enable()

    def disable_device(self):
        self.device.disable()
