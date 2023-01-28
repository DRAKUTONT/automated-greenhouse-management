from typing import Union, List
from greenhouse_management.devices.abstract_device import AbstractDevice


class AbstractSystem:
    def __init__(self, sensors: List, device: Union[AbstractDevice, List[AbstractDevice]], parameter: int):
        self.sensors = sensors
        self.device = device
        self.parameter = parameter

        self.emergency_mode = False

    def set_parameter(self, parameter: int):
        self.parameter = parameter

    def get_parameter(self):
        return self.parameter

    def get_data(self):  # this method will be implemented by the heirs
        pass

    def get_current_sensors_values(self) -> dict:  # this method will be implemented by the heirs
        pass

    def calculate_average_sensors_value(self, data) -> float:
        average_value = sum(data.values()) / len(data.values())
        return average_value

    def enable_emergency_mode(self):
        self.emergency_mode = True

    def disable_emergency_mode(self):
        self.emergency_mode = False

    def get_device_state(self, *args, **kwargs):
        return self.device.get_state()