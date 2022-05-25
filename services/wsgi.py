import os
from flask import Flask
from flask import render_template
from HueClient import Light
from SonoffClient import Switch
from dotenv import load_dotenv


# Load environment variables from .env file (must be in ~)
load_dotenv(f'{os.environ["HOME"]}/.env')

# Hue client
hue_user = os.environ['HUE_USER']
hue_ip = os.environ['HUE_IP']

# Sprinklers
sprinklers_ip = os.environ['SPRINKLERS_IP']
sprinklers_port = os.environ['SPRINKLERS_PORT'] 

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route("/lights/all/on")
def all_on():
    comedor = Light(hue_user, hue_ip, 1)
    sala_de_estar = Light(hue_user, hue_ip, 4)
    dormitorio = Light(hue_user, hue_ip, 3)
    comedor.turn_on()
    sala_de_estar.turn_on()
    dormitorio.turn_on()
    return render_template('main.html')

@app.route("/lights/all")
def flip_all():
    comedor = Light(hue_user, hue_ip, 1)
    sala_de_estar = Light(hue_user, hue_ip, 4)
    dormitorio = Light(hue_user, hue_ip, 3)
    comedor.flip_state()
    sala_de_estar.flip_state()
    dormitorio.flip_state()
    return render_template('main.html')

@app.route("/lights/comedor")
def comedor():
    comedor = Light(hue_user, hue_ip, 1)
    comedor.flip_state()
    return render_template('main.html')

@app.route("/lights/sala-de-estar")
def sala_de_estar():
    sala_de_estar = Light(hue_user, hue_ip, 4)
    sala_de_estar.flip_state()
    return render_template('main.html')

@app.route("/lights/dormitorio")
def dormitorio():
    dormitorio = Light(hue_user, hue_ip, 3)
    dormitorio.flip_state()
    return render_template('main.html')

@app.route("/sprinklers")
def sprinklers():
    sprinklers = Switch(sprinklers_ip, sprinklers_port)
    sprinklers.switch_state()
    return render_template('main.html')
