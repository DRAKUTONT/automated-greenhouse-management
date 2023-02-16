from greenhouse_management.sensors.soil_humidity_sensor import SoilHumiditySensor
from greenhouse_management.sensors.humidity_and_temperature_sensor import HumidityAndTemperatureSensor

from greenhouse_management.systems.irrigation_system import IrrigationSystem
from greenhouse_management.systems.ventilation_system import VentilationSystem
from greenhouse_management.systems.humidification_system import HumidificationSystem

from greenhouse_management.devices.windows import Window
from greenhouse_management.devices.sprinkler import Sprinkler
from greenhouse_management.devices.humidifier import Humidifier

from greenhouse_management.constants import *


class Greenhouse:
    def __init__(self, max_temperature: int, min_humidity: int, min_soil_humidity: int):
        self.max_temperature = max_temperature
        self.min_humidity = min_humidity
        self.min_soil_humidity = min_soil_humidity
        self.emergency_mode = False

        self.ventilation_system = VentilationSystem(
            sensors=[HumidityAndTemperatureSensor(i + 1) for i in range(TEMP_SENSORS_COUNT)],
            device=Window(), parameter=self.max_temperature)

        self.humidification_system = HumidificationSystem(
            sensors=[HumidityAndTemperatureSensor(i + 1) for i in range(HUM_SENSORS_COUNT)],
            device=Humidifier(), parameter=self.min_humidity)

        self.irrigation_system = IrrigationSystem(
            sensors=[SoilHumiditySensor(i + 1) for i in range(SOIL_HUM_SENSORS_COUNT)],
            devices=[Sprinkler(i + 1) for i in range(SPRINKLERS_COUNT)], parameter=self.min_soil_humidity)

        self.systems = [self.ventilation_system, self.humidification_system, self.irrigation_system]

    def set_parameters(self, params: dict):
        self.max_temperature = params.get('max_temp', self.max_temperature)
        self.min_humidity = params.get('min_hum', self.min_humidity)
        self.min_soil_humidity = params.get('min_soil_hum', self.min_soil_humidity)

        self.ventilation_system.set_parameter(self.max_temperature)
        self.humidification_system.set_parameter(self.min_humidity)
        self.irrigation_system.set_parameter(self.min_soil_humidity)

    def get_parameters(self) -> dict:
        data = {
            'max_temp': self.max_temperature,
            'min_hum': self.min_humidity,
            'min_soil_hum': self.min_soil_humidity
        }

        return data

    def get_systems_data(self):
        data = {
            'ventilation_system': self.ventilation_system.get_data(),
            'humidification_system': self.humidification_system.get_data(),
            'irrigation_system': self.irrigation_system.get_data()
        }

        return data

    def is_window_worked(self) -> bool:
        return self.ventilation_system.get_device_state()

    def set_window_state(self, state: bool):
        if state:
            self.ventilation_system.enable_device()
        else:
            self.ventilation_system.disable_device()

    def is_humidifier_worked(self) -> bool:
        return self.ventilation_system.get_device_state()

    def set_humidifier_state(self, state: bool):
        if state:
            self.humidification_system.enable_device()
        else:
            self.humidification_system.disable_device()

    def is_sprinkler_worked(self, device_id: int) -> bool:
        return self.irrigation_system.get_device_state(device_id)

    def set_sprinkler_state(self, state: bool, device_id: int):
        if state:
            self.irrigation_system.enable_device(device_id)
        else:
            self.irrigation_system.disable_device(device_id)

    def get_emergency_mode_status(self):
        return self.emergency_mode

    def enable_emergency_mode(self):
        self.emergency_mode = True
        for system in self.systems:
            system.enable_emergency_mode()

    def disable_emergency_mode(self):
        self.emergency_mode = False
        for system in self.systems:
            system.disable_emergency_mode()
