#!/usr/bin/python3

import requests
import json
import datetime


class Weather:
    '''Weather API.
    Docs available at https://docs.stormglass.io/#/
    '''

    def __init__(self, api_key:str, latitude:int, longitude:int):
        self.api_key = api_key
        self.latitude = latitude
        self.longitude = longitude

    def rain_forecast(self):
        day = datetime.date.today()
        response = requests.get(
            url='https://api.stormglass.io/v2/weather/point',
            headers={
                'Authorization': self.api_key,
            },
            params={
                'lat': self.latitude,
                'lng': self.longitude,
                'params': 'precipitation',
                'start': f'{day}T00:00:00+00:00',
                'end': f'{day}T23:00:00+00:00',
            },
        )
        data_dict = json.loads(response.content)
        total_rain = 0
        desired_rain = 25
        try:
            for mmh in data_dict['hours']:
                total_rain += mmh['precipitation']['noaa']
            total_rain_round = round(total_rain)
            activate_sprinklers = total_rain_round < desired_rain
            if activate_sprinklers:
                print(f'{datetime.datetime.now()} => Desired rain set to {desired_rain} mm. Estimated precipitation (00:00-23:00) is {total_rain_round} mm. Activate sprinklers: {activate_sprinklers}')
            else:
                print(f'{datetime.datetime.now()} => Desired rain set to {desired_rain} mm. Estimated precipitation (00:00-23:00) is {total_rain_round} mm. Activate sprinklers: {activate_sprinklers}')
        except:
            print(f'{datetime.datetime.now()} => Failed to get data from https://api.stormglass.io/v2/weather/point. {response} - {data_dict["errors"]["key"]}')
            activate_sprinklers = False
        return activate_sprinklers
