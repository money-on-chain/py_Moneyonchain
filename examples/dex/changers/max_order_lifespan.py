"""
Changer Max Order lifespan
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import DexMaxOrderLifespanChanger

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')

network = 'dexMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract = DexMaxOrderLifespanChanger(connection_manager)

max_order_life_span = 5000

tx_hash, tx_receipt = contract.constructor(max_order_life_span,
                                           execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""
Connecting to dexMainnet...
2020-11-24 09:17:34 root         INFO     Deploying new contract...
Connected: True
Changer Contract Address: 0x85Bd06C85e1A9435619F6d9f71918a9e64c796ee
2020-11-24 09:18:16 root         INFO     Deployed contract done!
2020-11-24 09:18:16 root         INFO     0xa22e7b13a3f00ca56d10b523536be4bd9ea238197b648dc670cf6f3af19bb48d
2020-11-24 09:18:16 root         INFO     AttributeDict({'transactionHash': HexBytes('0xa22e7b13a3f00ca56d10b523536be4bd9ea238197b648dc670cf6f3af19bb48d'), 'transactionIndex': 0, 'blockHash': HexBytes('0xe82bf28b9fc4367f1ecbbc3d0d11193c325caa81665c4f13ba6380c2f8d34a55'), 'blockNumber': 2888733, 'cumulativeGasUsed': 203883, 'gasUsed': 203883, 'contractAddress': '0x85Bd06C85e1A9435619F6d9f71918a9e64c796ee', 'logs': [], 'from': '0xB1ef062C364750DeECdCaCBf7190ed591B7a0Bfe', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')})
2020-11-24 09:18:16 root         INFO     Changer Contract Address: 0x85Bd06C85e1A9435619F6d9f71918a9e64c796ee


"""