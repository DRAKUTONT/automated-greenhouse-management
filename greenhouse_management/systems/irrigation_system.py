from typing import List
from greenhouse_management.sensors.soil_humidity_sensor import SoilHumiditySensor
from greenhouse_management.systems.abstract_system import AbstractSystem
from greenhouse_management.devices.sprinkler import Sprinkler


class IrrigationSystem(AbstractSystem):
    def __init__(self, sensors: List[SoilHumiditySensor], devices: List[Sprinkler],
                 parameter: int):
        super(IrrigationSystem, self).__init__(sensors=sensors, device=devices, parameter=parameter)

    def get_data(self):
        return self.get_current_sensors_values(need_average_value=True)

    def get_current_sensors_values(self, need_average_value=False) -> dict:
        data = {}
        for sensor in self.sensors:
            data[f'soil_hum_{sensor.number}'] = float(sensor.get_data()['humidity'])

        if need_average_value:
            data['average_soil_hum'] = self.calculate_average_sensors_value(data)

        return data

    def enable_device(self, device_id: int):
        if self.calculate_average_sensors_value(self.get_current_sensors_values()) < self.parameter or self.emergency_mode:
            self.device[device_id].enable()

    def disable_device(self, device_id: int):
        self.device[device_id].disable()

    def get_device_state(self, device_id: int):
        return self.device[device_id].get_state()


