"""
Changer to change the cancelation penalty rate used in the MoC Decentralized Exchange
cancelationPenaltyRate wad from 0 to 1 that represents the rate of the commission to charge as cancelation penalty, 1 represents the full commission
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import DexCancelationPenaltyRateChanger

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

contract = DexCancelationPenaltyRateChanger(connection_manager)

# New cancelation penalty rate to be set. Must be between 0 and 1(RATE_PRECISION)
cancelation_penalty_rate = int(0 * 10 ** 18)

tx_hash, tx_receipt = contract.constructor(cancelation_penalty_rate,
                                           execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""


"""