from greenhouse.devices.abstract_device import AbstractDevice


class Humidifier(AbstractDevice):
    def __init__(self):
        super(Humidifier, self).__init__(url="https://dt.miet.ru/ppo_it/api/total_hum")