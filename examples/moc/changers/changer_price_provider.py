from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import MoCPriceProviderChanger

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


contract = MoCPriceProviderChanger(connection_manager)
# BTC: 0x667bd3d048FaEBb85bAa0E9f9D87cF4c8CDFE849
# RIF: 0x9315AFD6aEc0bb1C1FB3fdcdC2E43797B0A61853
#price_provider = '0x2d39Cc54dc44FF27aD23A91a9B5fd750dae4B218'
price_provider = '0x26a00aF444928d689DDEC7b4D17c0E4a8c9D407d'
tx_hash, tx_receipt = contract.constructor(price_provider, execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""

"""