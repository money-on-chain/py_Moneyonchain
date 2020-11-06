"""
Inserts an order in the sell orderbook of a given pair without a hint
the pair should not be disabled; the contract should not be paused. Takes the funds
with a transferFrom
"""
from decimal import Decimal
from web3 import Web3
import json
import os

from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import MoCDecentralizedExchange

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


def options_from_settings(filename='settings.json'):
    """ Options from file settings.json """

    with open(filename) as f:
        config_options = json.load(f)

    return config_options


network = 'dexDevelopment'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

# load settings from file
settings = options_from_settings(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.json'))

# instantiate DEX Contract
dex = MoCDecentralizedExchange(connection_manager)

base_token = settings[network]['DOC']
secondary_token = settings[network]['BPRO']
amount = 1
price = 1
lifespan = 5

print("Insert sell limit order. Please wait to the transaction be mined!...")
tx_hash, tx_receipt, tx_logs, tx_logs_formatted = dex.insert_sell_limit_order(
    base_token,
    secondary_token,
    amount,
    price,
    lifespan)
print("Tx hash: [{0}]".format(Web3.toHex(tx_hash)))
if tx_logs:
    print(tx_logs_formatted['NewOrderInserted'].print_row())
