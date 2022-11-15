import os
from flask import Flask
from flask import render_template
from HueClient import Light
from SonoffClient import Switch
from WeatherClient import Weather


# Hue client
hue_user = os.environ['HUE_USER']
hue_ip = os.environ['HUE_IP']

# Sprinklers
sprinklers_ip = os.environ['SPRINKLERS_IP']
sprinklers_port = os.environ['SPRINKLERS_PORT']

# Weather API
today = Weather(
    api_key=os.environ['WEATHER_API_KEY'],
    latitude=os.environ['LATITUDE'],
    longitude=os.environ['LONGITUDE'],
)

app = Flask(__name__)

@app.route('/')
def main():
    comedor = Light(hue_user, hue_ip, 1)
    sala_de_estar = Light(hue_user, hue_ip, 4)
    dormitorio = Light(hue_user, hue_ip, 3)
    comedor_state = comedor.get_state()
    sala_de_estar_state = sala_de_estar.get_state()
    dormitorio_state = dormitorio.get_state()
    sprinklers = Switch(sprinklers_ip, sprinklers_port)
    sprinklers_state = sprinklers.get_info()
    return render_template('main.html', comedor_state=comedor_state, sala_de_estar_state=sala_de_estar_state, dormitorio_state=dormitorio_state, sprinklers_state=sprinklers_state)

@app.route("/lights/all-on")
def all_on():
    comedor = Light(hue_user, hue_ip, 1)
    sala_de_estar = Light(hue_user, hue_ip, 4)
    dormitorio = Light(hue_user, hue_ip, 3)
    comedor.turn_on()
    sala_de_estar.turn_on()
    dormitorio.turn_on()
    comedor_state = comedor.get_state()
    sala_de_estar_state = sala_de_estar.get_state()
    dormitorio_state = dormitorio.get_state()
    sprinklers = Switch(sprinklers_ip, sprinklers_port)
    sprinklers_state = sprinklers.get_info()
    return render_template('main.html', comedor_state=comedor_state, sala_de_estar_state=sala_de_estar_state, dormitorio_state=dormitorio_state, sprinklers_state=sprinklers_state)

@app.route("/lights/all-off")
def all_off():
    comedor = Light(hue_user, hue_ip, 1)
    sala_de_estar = Light(hue_user, hue_ip, 4)
    dormitorio = Light(hue_user, hue_ip, 3)
    comedor.turn_off()
    sala_de_estar.turn_off()
    dormitorio.turn_off()
    comedor_state = comedor.get_state()
    sala_de_estar_state = sala_de_estar.get_state()
    dormitorio_state = dormitorio.get_state()
    sprinklers = Switch(sprinklers_ip, sprinklers_port)
    sprinklers_state = sprinklers.get_info()
    return render_template('main.html', comedor_state=comedor_state, sala_de_estar_state=sala_de_estar_state, dormitorio_state=dormitorio_state, sprinklers_state=sprinklers_state)

@app.route("/lights/comedor")
def comedor():
    comedor = Light(hue_user, hue_ip, 1)
    sala_de_estar = Light(hue_user, hue_ip, 4)
    dormitorio = Light(hue_user, hue_ip, 3)
    comedor.flip_state()
    comedor_state = comedor.get_state()
    sala_de_estar_state = sala_de_estar.get_state()
    dormitorio_state = dormitorio.get_state()
    sprinklers = Switch(sprinklers_ip, sprinklers_port)
    sprinklers_state = sprinklers.get_info()
    return render_template('main.html', comedor_state=comedor_state, sala_de_estar_state=sala_de_estar_state, dormitorio_state=dormitorio_state, sprinklers_state=sprinklers_state)

@app.route("/lights/sala-de-estar")
def sala_de_estar():
    comedor = Light(hue_user, hue_ip, 1)
    sala_de_estar = Light(hue_user, hue_ip, 4)
    dormitorio = Light(hue_user, hue_ip, 3)
    sala_de_estar.flip_state()
    comedor_state = comedor.get_state()
    sala_de_estar_state = sala_de_estar.get_state()
    dormitorio_state = dormitorio.get_state()
    sprinklers = Switch(sprinklers_ip, sprinklers_port)
    sprinklers_state = sprinklers.get_info()
    return render_template('main.html', comedor_state=comedor_state, sala_de_estar_state=sala_de_estar_state, dormitorio_state=dormitorio_state, sprinklers_state=sprinklers_state)

@app.route("/lights/dormitorio")
def dormitorio():
    comedor = Light(hue_user, hue_ip, 1)
    sala_de_estar = Light(hue_user, hue_ip, 4)
    dormitorio = Light(hue_user, hue_ip, 3)
    dormitorio.flip_state()
    comedor_state = comedor.get_state()
    sala_de_estar_state = sala_de_estar.get_state()
    dormitorio_state = dormitorio.get_state()
    sprinklers = Switch(sprinklers_ip, sprinklers_port)
    sprinklers_state = sprinklers.get_info()
    return render_template('main.html', comedor_state=comedor_state, sala_de_estar_state=sala_de_estar_state, dormitorio_state=dormitorio_state, sprinklers_state=sprinklers_state)

@app.route("/sprinklers/on")
def sprinklers_on():
    sprinklers = Switch(sprinklers_ip, sprinklers_port)
    sprinklers.turn_on()
    sprinklers_state = sprinklers.get_info()
    comedor = Light(hue_user, hue_ip, 1)
    sala_de_estar = Light(hue_user, hue_ip, 4)
    dormitorio = Light(hue_user, hue_ip, 3)
    comedor_state = comedor.get_state()
    sala_de_estar_state = sala_de_estar.get_state()
    dormitorio_state = dormitorio.get_state()
    return render_template('main.html', comedor_state=comedor_state, sala_de_estar_state=sala_de_estar_state, dormitorio_state=dormitorio_state, sprinklers_state=sprinklers_state)

@app.route("/sprinklers/off")
def sprinklers_off():
    sprinklers = Switch(sprinklers_ip, sprinklers_port)
    sprinklers.turn_off()
    sprinklers_state = sprinklers.get_info()
    comedor = Light(hue_user, hue_ip, 1)
    sala_de_estar = Light(hue_user, hue_ip, 4)
    dormitorio = Light(hue_user, hue_ip, 3)
    comedor_state = comedor.get_state()
    sala_de_estar_state = sala_de_estar.get_state()
    dormitorio_state = dormitorio.get_state()
    return render_template('main.html', comedor_state=comedor_state, sala_de_estar_state=sala_de_estar_state, dormitorio_state=dormitorio_state, sprinklers_state=sprinklers_state)

@app.route("/sprinklers/automatic")
def sprinklers_automatic():
    sprinklers = Switch(sprinklers_ip, sprinklers_port)
    days = 1
    if today.rain_forecast(days):
        sprinklers.turn_on()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)