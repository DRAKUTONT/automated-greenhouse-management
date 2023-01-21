from network.transporter import Transporter


class Sprinkler:
    def __init__(self, number):
        self.is_work = False

        self.url = 'https://dt.miet.ru/ppo_it/api/watering'
        self.number = number
        self.transporter = Transporter(self.url)

    def enable(self):
        self.is_work = True

        params = {
                "id": self.number,
                "state": 1
                }
        self.transporter.set_state(params)

    def disable(self):
        params = {
            "id": self.number,
            "state": 0
        }
        self.transporter.set_state(params)

    def get_state(self):
        return self.is_work