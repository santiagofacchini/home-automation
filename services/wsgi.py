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

@app.route("/lights/all/off")
def all_off():
    comedor = Light(hue_user, hue_ip, 1)
    sala_de_estar = Light(hue_user, hue_ip, 4)
    dormitorio = Light(hue_user, hue_ip, 3)
    comedor.turn_off()
    sala_de_estar.turn_off()
    dormitorio.turn_off()
    return render_template('main.html')

@app.route("/lights/comedor/on")
def comedor_on():
    comedor = Light(hue_user, hue_ip, 1)
    comedor.turn_on()
    return render_template('main.html')

@app.route("/lights/comedor/off")
def comedor_off():
    comedor = Light(hue_user, hue_ip, 1)
    comedor.turn_off()
    return render_template('main.html')

@app.route("/lights/sala-de-estar/on")
def sala_de_estar_on():
    sala_de_estar = Light(hue_user, hue_ip, 4)
    sala_de_estar.turn_on()
    return render_template('main.html')

@app.route("/lights/sala-de-estar/off")
def sala_de_estar_off():
    sala_de_estar = Light(hue_user, hue_ip, 4)
    sala_de_estar.turn_off()
    return render_template('main.html')

@app.route("/lights/dormitorio/on")
def dormitorio_on():
    dormitorio = Light(hue_user, hue_ip, 3)
    dormitorio.turn_on()
    return render_template('main.html')

@app.route("/lights/dormitorio/off")
def dormitorio_off():
    dormitorio = Light(hue_user, hue_ip, 3)
    dormitorio.turn_off()
    return render_template('main.html')

@app.route("/sprinklers/on")
def sprinklers_on():
    sprinklers = Switch(sprinklers_ip, sprinklers_port)
    sprinklers.turn_on()
    return render_template('main.html')

@app.route("/sprinklers/off")
def sprinklers_off():
    sprinklers = Switch(sprinklers_ip, sprinklers_port)
    sprinklers.turn_off()
    return render_template('main.html')
