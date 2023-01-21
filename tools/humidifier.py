from network.transporter import Transporter


class Humidifier:
    def __init__(self):
        self.is_work = False

        self.url = f"https://dt.miet.ru/ppo_it/api/total_hum"
        self.transporter = Transporter(self.url)

    def enable(self):
        self.is_work = True

        params = {
            "state": 1
        }
        self.transporter.set_state(params)

    def disable(self):
        self.is_work = False

        params = {
            "state": 0
        }
        self.transporter.set_state(params)

    def get_state(self):
        return self.is_work