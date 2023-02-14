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
# sprinklers = Switch(os.environ['SPRINKLERS_IP'], os.environ['SPRINKLERS_PORT'])

# Get states
comedor_state = comedor.get_state()
sala_de_estar_state = sala_de_estar.get_state()
dormitorio_state = dormitorio.get_state()
# sprinklers_state = sprinklers.get_info()

# Main template rendering
def render_main():
    return render_template(
        'main.html',
        comedor_state=comedor_state,
        sala_de_estar_state=sala_de_estar_state,
        dormitorio_state=dormitorio_state,
        # sprinklers_state=sprinklers_state
    )

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
    comedor.flip_state()
    return render_main()

@app.route("/lights/sala-de-estar")
def sala_de_estar_lights():
    sala_de_estar.flip_state()
    return render_main()

@app.route("/lights/dormitorio")
def dormitorio_lights():
    dormitorio.flip_state()
    return render_main()

# @app.route("/sprinklers")
# def sprinklers_switch():
#     sprinklers.flip_state()
#     return render_main()

# # For scheduled execution only
# @app.route("/sprinklers/off")
# def sprinklers_off():
#     sprinklers.turn_off()

# # For scheduled execution only
# @app.route("/sprinklers/automatic")
# def sprinklers_automatic():
#     days = 1
#     if today.rain_forecast(days):
#         sprinklers.turn_on()
