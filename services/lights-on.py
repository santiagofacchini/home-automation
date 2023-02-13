import os
from HueClient import Light


# Hue client
hue_user = os.environ['HUE_USER']
hue_ip = os.environ['HUE_IP']

comedor = Light(hue_user, hue_ip, 1)
sala_de_estar = Light(hue_user, hue_ip, 5)
# dormitorio = Light(hue_user, hue_ip, 3)

comedor.turn_on()
sala_de_estar.turn_on()
# dormitorio.turn_on()
