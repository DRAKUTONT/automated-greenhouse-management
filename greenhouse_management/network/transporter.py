import requests
from greenhouse_management.constants import TOKEN


class Transporter:
    def __init__(self, url):
        self.url = url

    def set_state(self, params: dict):
        requests.patch(url=self.url, params=params, headers={'X-Auth-Token': TOKEN})

    def get_state(self) -> dict:
        response = requests.get(url=self.url)
        if response.status_code:
            return response.json()

        else:
            print(f'Transporter: status_code: {response.status_code}')
