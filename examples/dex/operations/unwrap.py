import json
import os
from decimal import Decimal

from moneyonchain.manager import ConnectionManager
from moneyonchain.token import WRBTC


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

dex_address = connection_manager.options['networks'][network]['addresses']['dex']
token_sc = WRBTC(connection_manager, contract_address=settings[network]['WRBTC'])

amount = Decimal(0.001)
token_sc.deposit(amount)
