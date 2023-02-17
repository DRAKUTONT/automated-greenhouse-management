from greenhouse_management.devices.abstract_device import AbstractDevice


class Sprinkler(AbstractDevice):
    def __init__(self, device_id):
        self.device_id = device_id
        super(Sprinkler, self).__init__(url="https://dt.miet.ru/ppo_it/api/watering")

    def enable(self):
        self.is_work = True

        params = {
            "id": self.device_id,
            "state": 1
        }
        self.transporter.set_state(params)

    def disable(self):
        self.is_work = False

        params = {
            "id": self.device_id,
            "state": 0
        }
        self.transporter.set_state(params)