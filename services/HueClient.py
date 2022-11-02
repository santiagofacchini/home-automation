import requests
import datetime


class Light:
    '''Used to interact with Philips Hue bridge API.
    '''

    def __init__(self, hue_user: str, hue_ip: str, light: int) -> None:
        self.hue_user = hue_user
        self.hue_ip = hue_ip
        self.light = light

    def get_state(self):
        response = requests.get(
            url=f'http://{self.hue_ip}/api/{self.hue_user}/lights/{self.light}'
        )
        return response.json()['state']['on']

    def turn_on(self):
        response = requests.put(
            url=f'http://{self.hue_ip}/api/{self.hue_user}/lights/{self.light}/state',
            json={
                "on": True,
                "bri": 254,
            },
        )
        print(f'{datetime.datetime.now()} => Turning light {self.light} on. '
        f'{response}')
        return response.content

    def turn_off(self):
        response = requests.put(
            url=f'http://{self.hue_ip}/api/{self.hue_user}/lights/{self.light}/state',
            json={
                "on": False,
            },
        )
        print(f'{datetime.datetime.now()} => Turning light {self.light} '
            f'off. {response}')
        return response.content

    def flip_state(self):
        response = requests.get(
            url=f'http://{self.hue_ip}/api/{self.hue_user}/lights/{self.light}'
        )
        if response.json()['state']['on'] == False:
            new_state = True
        else:
            new_state = False
        response = requests.put(
            url=f'http://{self.hue_ip}/api/{self.hue_user}/lights/{self.light}/state',
            json={
                "on": new_state,
            },
        )
        print(f'{datetime.datetime.now()} => Flipping light {self.light} '
            f'state. Light on: {new_state}. {response}')
        return response.content
