import os
from SonoffClient import Switch


# Sprinklers
sprinklers_ip = os.environ['SPRINKLERS_IP']
sprinklers_port = os.environ['SPRINKLERS_PORT']

sprinklers = Switch(
    sonoff_ip=sprinklers_ip,
    sonoff_port=sprinklers_port,
)

sprinklers.turn_off()