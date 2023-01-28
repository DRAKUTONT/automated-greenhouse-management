from greenhouse_management.network.transporter import Transporter


class AbstractDevice:
    def __init__(self, url: str):
        self.is_work = False

        self.url = url
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