from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import MoCPriceProviderChanger

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


network = 'mocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


contract = MoCPriceProviderChanger(connection_manager)

price_provider = '0x2d39Cc54dc44FF27aD23A91a9B5fd750dae4B218'
tx_hash, tx_receipt = contract.constructor(price_provider, execute_change=True)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""

Connecting to mocTestnet...
2020-06-11 14:55:27 root         INFO     Deploying new contract...
Connected: True
2020-06-11 14:56:19 root         INFO     Deployed contract done!
2020-06-11 14:56:19 root         INFO     0x34bd9ddecfca4cf85c2979dcc53e3960dbc298ae6294f483b7adc34cb546258d
2020-06-11 14:56:19 root         INFO     AttributeDict({'transactionHash': HexBytes('0x34bd9ddecfca4cf85c2979dcc53e3960dbc298ae6294f483b7adc34cb546258d'), 'transactionIndex': 28, 'blockHash': HexBytes('0x84080e9e26b740f0edba09ec13d488283a1c0ef8548125beb989518dd4376dfe'), 'blockNumber': 924419, 'cumulativeGasUsed': 2098982, 'gasUsed': 420315, 'contractAddress': '0xCa867a7DCb47246d8a874E9A1c2712ab966e368b', 'logs': [AttributeDict({'logIndex': 0, 'blockNumber': 924419, 'blockHash': HexBytes('0x84080e9e26b740f0edba09ec13d488283a1c0ef8548125beb989518dd4376dfe'), 'transactionHash': HexBytes('0x34bd9ddecfca4cf85c2979dcc53e3960dbc298ae6294f483b7adc34cb546258d'), 'transactionIndex': 28, 'address': '0xCa867a7DCb47246d8a874E9A1c2712ab966e368b', 'data': '0x', 'topics': [HexBytes('0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0'), HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'), HexBytes('0x000000000000000000000000ab242e50e95c2f539242763a4ed5db1aee5ce461')]})], 'from': '0xaB242E50E95C2F539242763A4ed5DB1AEe5CE461', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000001000000000000000000000000000000000000020000000000000000000800000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000800000000000000000080004000000000000000000000000000000000000000000000000000000000000000000000000004000000000004000000000000000020000000000000000000000000000000000000000000000000000000000000000000')})
2020-06-11 14:56:19 root         INFO     Changer Contract Address: 0xCa867a7DCb47246d8a874E9A1c2712ab966e368b
Changer Contract Address: 0xCa867a7DCb47246d8a874E9A1c2712ab966e368b

"""