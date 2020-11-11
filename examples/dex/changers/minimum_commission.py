"""
Minimum Commission changer
"""

from decimal import Decimal

from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import DexMinimumCommissionChanger

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')

network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract = DexMinimumCommissionChanger(connection_manager)

# New minimum commission to be set in USD.
minimum_commission = int(0.5 * 10 ** 18)

tx_hash, tx_receipt = contract.constructor(minimum_commission,
                                           execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""


"""