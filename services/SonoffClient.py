import requests
import datetime


class Switch:
    '''Used to interact with Sonoff DIY Basic API.
    Model: BASICR3
    Documentation: https://sonoff.tech/sonoff-diy-developer-documentation-basicr3-rfr3-mini-http-api/
    '''

    def __init__(self, sonoff_ip:str, sonoff_port:int):
        self.sonoff_ip = sonoff_ip
        self.sonoff_port = sonoff_port

    def get_info(self):
        try:
            response = requests.post(
                url=f'http://{self.sonoff_ip}:{self.sonoff_port}/zeroconf/info',
                json={
                    "data": {}
                },
            )
            return response.json()
        except:
            print(f'http://{self.sonoff_ip}:{self.sonoff_port} unreachable')
            return None


    def turn_on(self):
        try:
            response = requests.post(
                url=f'http://{self.sonoff_ip}:{self.sonoff_port}/zeroconf/switch',
                json={
                    "data": {
                        "switch": "on"
                    }
                },
            )
            print(f'{datetime.datetime.now()} => Turning switch at '
                f'{self.sonoff_ip} on. {response}')
            return response.json()
        except:
            print(f'http://{self.sonoff_ip}:{self.sonoff_port} unreachable')
            return None

    def turn_off(self):
        try:
            response = requests.post(
                url=f'http://{self.sonoff_ip}:{self.sonoff_port}/zeroconf/switch',
                json={
                    "data": {
                        "switch": "off"
                    }
                },
            )
            print(f'{datetime.datetime.now()} => Turning switch at '
                f'{self.sonoff_ip} off. {response}')
            return response.json()
        except:
            print(f'http://{self.sonoff_ip}:{self.sonoff_port} unreachable')
            return None

    def inching_on(self, time:int):
        miliseconds = time*60000
        try:
            response = requests.post(
                url=f'http://{self.sonoff_ip}:{self.sonoff_port}/zeroconf/pulse',
                json={
                    "data": {
                        "pulse": "on",
                        "pulseWidth": miliseconds,
                    }
                },
            )
            print(f'{datetime.datetime.now()} => Inching set to '
                f'{miliseconds}. {response}')
            return response.json()
        except:
            print(f'http://{self.sonoff_ip}:{self.sonoff_port} unreachable')
            return None

    def inching_off(self):
        try:
            response = requests.post(
                url=f'http://{self.sonoff_ip}:{self.sonoff_port}/zeroconf/pulse',
                json={
                    "data": {
                        "pulse": "off",
                    }
                },
            )
            print(f'{datetime.datetime.now()} => Inching off. {response}')
            return response.json()
        except:
            print(f'http://{self.sonoff_ip}:{self.sonoff_port} unreachable')
            return None

    def switch_state(self):
        try:
            sprinklers_state = self.get_info()
            if sprinklers_state['data']['switch'] == 'off':
                self.turn_on()
            else:
                self.turn_off()
            return self.get_info()
        except:
            print(f'http://{self.sonoff_ip}:{self.sonoff_port} unreachable')
            return None

