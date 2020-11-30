"""

Multiply factor:
    Minimum range avalaible price to be paid
    Maximum range avalaible price to be paid

(100 + priceDifference) / 100 = Multiply Factor

Examples:

     1% Multiply Factor:
       (100 + 1) / 100 = 1.01
    -1% Multiply Factor:
       (100 - 1 ) / 100 = 0.99

     10% Multiply Factor:
       (100 + 10) / 100 = 1.1
    -10% Multiply Factor:
       (100 - 10 ) / 100 = 0.9



Range:

  Min Multiply Factor: 0.01
  Max Multiply Factor: 1.99

  0.01 < Multiply Factor < 1.99

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

print("Min Multiply Factor: {0}".format(dex.min_multiply_factor()))
print("Max Multiply Factor: {0}".format(dex.max_multiply_factor()))

