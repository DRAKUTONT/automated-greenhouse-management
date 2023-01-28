from greenhouse_management.devices.abstract_device import AbstractDevice


class Window(AbstractDevice):
    def __init__(self):
        super(Window, self).__init__(url="https://dt.miet.ru/ppo_it/api/fork_drive/")
