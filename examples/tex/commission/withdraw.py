"""
Withdraws all the already charged(because of a matching, a cancellation or an expiration)
commissions of a given token
token Address of the token to withdraw the commissions from
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


network = 'dexMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

# load settings from file
settings = options_from_settings(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.json'))

# instantiate DEX Contract
dex = MoCDecentralizedExchange(connection_manager)

token_name = 'DOC'
token = settings[network][token_name]

print("Withdraw commission from token: {0}. Please wait to the transaction be mined!...".format(
    token_name
))
tx_hash, tx_receipt, tx_logs, tx_logs_formatted = dex.withdraw_commissions(
    token)
print("Tx hash: [{0}]".format(Web3.toHex(tx_hash)))
if tx_logs:
    print(tx_logs_formatted['CommissionWithdrawn'].print_row())
