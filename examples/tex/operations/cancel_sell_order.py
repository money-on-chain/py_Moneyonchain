"""

cancels the sell _orderId order.
the contract must not be paused; the caller should be the order owner
_baseToken Base Token involved in the canceled Order pair
_secondaryToken Secondary Token involved in the canceled Order pair
_orderId Order id to cancel
_previousOrderIdHint previous order in the orderbook, used as on optimization to search for.

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


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

# load settings from file
settings = options_from_settings(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.json'))

# instantiate DEX Contract
dex = MoCDecentralizedExchange(connection_manager)

base_token = settings[network]['DOC']
secondary_token = settings[network]['WRBTC']
order_id = 107
previous_order_id = 0

print("Order cancel. Please wait to the transaction be mined!...")
tx_hash, tx_receipt, tx_logs, tx_logs_formatted = dex.cancel_sell_order(
    base_token,
    secondary_token,
    order_id,
    previous_order_id)
print("Tx hash: [{0}]".format(Web3.toHex(tx_hash)))
if tx_logs:
    print(tx_logs_formatted['OrderCancelled'].print_row())


"""

Tx hash: [0xf5962de6b7f36425943be54522f804c358b171bd6414084dfc979655278952ee]
Block Nº	Timestamp	id	sender	returnedAmount	commission	returnedCommission	isBuy
1408435	2020-12-01 09:49:19	107	0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3	0.000969604920060969	0.000000000000000000	0.000030395079939031	False
None

"""