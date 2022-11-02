import os
from HueClient import Light
from dotenv import load_dotenv


# Load environment variables from .env file (must be in ~)
load_dotenv(f'{os.environ["HOME"]}/.env')

# Hue client
hue_user = os.environ['HUE_USER']
hue_ip = os.environ['HUE_IP']

comedor = Light(hue_user, hue_ip, 1)
sala_de_estar = Light(hue_user, hue_ip, 4)
dormitorio = Light(hue_user, hue_ip, 3)

comedor.turn_off()
sala_de_estar.turn_off()
dormitorio.turn_off()
