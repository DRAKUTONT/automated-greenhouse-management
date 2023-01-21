from network.transporter import Transporter


class SoilHumiditySensor:
    def __init__(self, number: int):
        self.number = number
        self.url = f"https://dt.miet.ru/ppo_it/api/hum/{number}"

        self.transporter = Transporter(self.url)

    def get_data(self):
        return self.transporter.get_state()