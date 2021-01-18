"""
Changer to change the commission rate in the MoC Decentralized Exchange
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import DexCommissionRateChanger

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

contract = DexCommissionRateChanger(connection_manager)

commission_rate = int(0.001 * 10 ** 18)

tx_hash, tx_receipt = contract.constructor(commission_rate,
                                           execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""


"""