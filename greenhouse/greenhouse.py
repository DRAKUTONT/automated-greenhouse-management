from greenhouse.sensors.soil_humidity_sensor import SoilHumiditySensor
from greenhouse.sensors.humidity_and_temperature_sensor import HumidityAndTemperatureSensor

from greenhouse.systems.irrigation_system import IrrigationSystem
from greenhouse.systems.ventilation_system import VentilationSystem
from greenhouse.systems.humidification_system import HumidificationSystem

from greenhouse.devices.windows import Window
from greenhouse.devices.sprinkler import Sprinkler
from greenhouse.devices.humidifier import Humidifier


class Greenhouse:
    temp_sensors_count = 4
    hum_sensors_count = 4
    soil_hum_sensors_count = 6
    sprinklers_count = 6

    def __init__(self, max_temperature: int, min_humidity: int, min_soil_humidity: int):
        self.max_temperature = max_temperature
        self.min_humidity = min_humidity
        self.min_soil_humidity = min_soil_humidity

        self.ventilation_system = self.create_ventilation_system()
        self.humidification_system = self.create_humidification_system()
        self.irrigation_system = self.create_irrigation_system()

    def create_ventilation_system(self) -> VentilationSystem:
        return VentilationSystem(sensors=[HumidityAndTemperatureSensor(i) for i in range(self.temp_sensors_count)],
                                 window=Window(), max_temperature=self.max_temperature)

    def create_humidification_system(self) -> HumidificationSystem:
        return HumidificationSystem(sensors=[HumidityAndTemperatureSensor(i) for i in range(self.hum_sensors_count)],
                                    humidifier=Humidifier(), min_humidity=self.min_humidity)

    def create_irrigation_system(self) -> IrrigationSystem:
        return IrrigationSystem(sensors=[SoilHumiditySensor(i) for i in range(self.soil_hum_sensors_count)],
                                sprinklers=[Sprinkler(i) for i in range(self.sprinklers_count)],
                                min_soil_humidity=self.min_soil_humidity)
