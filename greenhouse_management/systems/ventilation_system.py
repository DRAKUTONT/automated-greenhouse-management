from typing import List
from greenhouse_management.sensors.humidity_and_temperature_sensor import HumidityAndTemperatureSensor
from greenhouse_management.systems.abstract_system import AbstractSystem
from greenhouse_management.devices.windows import Window
from greenhouse_management.exceptions.temperature_exception import TemperatureParameterException


class VentilationSystem(AbstractSystem):
    def __init__(self, sensors: List[HumidityAndTemperatureSensor], device: Window, parameter: int):
        super(VentilationSystem, self).__init__(sensors=sensors, device=device, parameter=parameter)

    def get_data(self):
        return self.get_current_sensors_values(need_average_value=True)

    def get_current_sensors_values(self, need_average_value=False) -> dict:
        data = {}
        for sensor in self.sensors:
            data[f'temp_{sensor.number}'] = float(sensor.get_data()['temperature'])

        if need_average_value:
            data['average_temp'] = self.calculate_average_sensors_value(data)

        return data

    def enable_device(self):
        if self.calculate_average_sensors_value(self.get_current_sensors_values()) > self.parameter or self.emergency_mode:
            self.device.enable()
        else:
            raise TemperatureParameterException

    def disable_device(self):
        self.device.disable()