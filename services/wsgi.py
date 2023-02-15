import os
import shelve
from flask import Flask, render_template
from HueClient import Light
from SonoffClient import Switch
from WeatherClient import Weather
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

# API
class Devices(Resource):
    def get(self):
        db = shelve.open('devices')

        devices = []
        for device in db:
            devices.append(device)

        db.close()

        return {"devices": devices}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('device_type', required=True)
        parser.add_argument('controller_gateway', required=True)
        parser.add_argument('controller_port')
        parser.add_argument('hue_user')
        args = parser.parse_args()

        db = shelve.open('devices')
        db[args['identifier']] = args
        db.close()

        return {'message': 'Device registered', 'data': args}, 201

class Device(Resource):
    def get(self, identifier):
        db = shelve.open('devices')
        device = db[identifier]
        db.close()

        return {"data": device}, 200

    def delete(self, identifier):
        db = shelve.open('devices')

        if not (identifier in db):
            return {'message': 'Device not found', 'data': {}}, 404

        del db[identifier]

        return '', 204

api.add_resource(Devices, '/devices')
api.add_resource(Device, '/device/<string:identifier>')

# Weather API
today = Weather(
    api_key=os.environ['WEATHER_API_KEY'],
    latitude=os.environ['LATITUDE'],
    longitude=os.environ['LONGITUDE'],
)

# Devices
comedor = Light(os.environ['HUE_USER'], os.environ['HUE_IP'], 1)
sala_de_estar = Light(os.environ['HUE_USER'], os.environ['HUE_IP'], 5)
dormitorio = Light(os.environ['HUE_USER'], os.environ['HUE_IP'], 3)
sprinklers = Switch(os.environ['SPRINKLERS_IP'], os.environ['SPRINKLERS_PORT'])

# Main template rendering
def render_main():
    return render_template('main.html')

@app.route('/')
def main():
    return render_main()

@app.route("/lights/all-on")
def all_on():
    comedor.turn_on()
    sala_de_estar.turn_on()
    dormitorio.turn_on()
    return render_main()

@app.route("/lights/all-off")
def all_off():
    comedor.turn_off()
    sala_de_estar.turn_off()
    dormitorio.turn_off()
    return render_main()

@app.route("/lights/comedor")
def comedor_lights():
    return comedor.flip_state()

@app.route("/lights/sala-de-estar")
def sala_de_estar_lights():
    return sala_de_estar.flip_state()

@app.route("/lights/dormitorio")
def dormitorio_lights():
    return dormitorio.flip_state()

@app.route("/sprinklers")
def sprinklers_switch():
    return sprinklers.flip_state()

# For scheduled execution only
@app.route("/sprinklers/off")
def sprinklers_off():
    return sprinklers.turn_off()

# For scheduled execution only
@app.route("/sprinklers/automatic")
def sprinklers_automatic():
    days = 1
    if today.rain_forecast(days):
        return sprinklers.turn_on()
