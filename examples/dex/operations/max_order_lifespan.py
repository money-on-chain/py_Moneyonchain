"""

MaxOrderLifespan is the maximum lifespan in ticks for an order

"""

import json
import os
from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import MoCDecentralizedExchange


def options_from_settings(filename='settings.json'):
    """ Options from file settings.json """

    with open(filename) as f:
        config_options = json.load(f)

    return config_options


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

# load settings from file
settings = options_from_settings(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.json'))

dex = MoCDecentralizedExchange(connection_manager)


print("Max Order Life Span: {0}".format(dex.max_order_lifespan()))

