import requests


class Transporter:
    def __init__(self, url):
        self.url = url

    def set_state(self, params: dict):
        a = requests.patch(url=self.url, params=params)
        print(a.url)
        print(a)

    def get_state(self) -> dict:
        response = requests.get(url=self.url)
        if response.status_code:
            return response.json()

        else:
            print(f'Transporter: status_code: {response.status_code}')
