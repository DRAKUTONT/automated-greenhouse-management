from greenhouse.network import Transporter


class HumidityAndTemperatureSensor:
    def __init__(self, number: int):
        self.number = number
        self.url = f"https://dt.miet.ru/ppo_it/api/temp_hum/{number}"

        self.transporter = Transporter(self.url)

    def get_data(self) -> dict:
        return self.transporter.get_state()