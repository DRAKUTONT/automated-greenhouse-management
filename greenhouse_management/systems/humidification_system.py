from typing import List
from greenhouse_management.sensors.humidity_and_temperature_sensor import HumidityAndTemperatureSensor
from greenhouse_management.devices.humidifier import Humidifier
from greenhouse_management.systems.abstract_system import AbstractSystem
from greenhouse_management.exceptions.humidity_exception import HumidityParameterException


class HumidificationSystem(AbstractSystem):
    def __init__(self, sensors: List[HumidityAndTemperatureSensor], device: Humidifier, parameter: int):
        super(HumidificationSystem, self).__init__(sensors=sensors, device=device, parameter=parameter)

    def get_data(self):
        return self.get_current_sensors_values(need_average_value=True)

    def get_current_sensors_values(self, need_average_value=False) -> dict:
        data = {}
        for sensor in self.sensors:
            data[f'hum_{sensor.number}'] = float(sensor.get_data()['humidity'])

        if need_average_value:
            data['average_hum'] = self.calculate_average_sensors_value(data)

        return data

    def enable_device(self):
        if self.calculate_average_sensors_value(
                self.get_current_sensors_values()) > self.parameter or self.emergency_mode:
            self.device.enable()
        else:
            raise HumidityParameterException

    def disable_device(self):
        self.device.disable()
