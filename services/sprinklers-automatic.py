import os
from WeatherClient import Weather
from SonoffClient import Switch


# Weather API
api_key = os.environ['WEATHER_API_KEY']
latitude = os.environ['LATITUDE']
longitude = os.environ['LONGITUDE']

today = Weather(
    api_key=api_key,
    latitude=latitude,
    longitude=longitude,
)

# Sprinklers
sprinklers_ip = os.environ['SPRINKLERS_IP']
sprinklers_port = os.environ['SPRINKLERS_PORT']

sprinklers = Switch(
    sonoff_ip=sprinklers_ip,
    sonoff_port=sprinklers_port,
)

days = 1
if today.rain_forecast(days):
    sprinklers.turn_on()
