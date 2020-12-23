"""
Changer to change the enable a token pair in the MoC Decentralized Exchange
"""

import os
import json

from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import DexTokenPairEnabler

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

contract = DexTokenPairEnabler(connection_manager)

# load settings from file
settings = options_from_settings(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.json'))


base_address = settings[network]['RDOC']
secondary_address = settings[network]['RIFP']

tx_hash, tx_receipt = contract.constructor(base_address,
                                           secondary_address,
                                           execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""
Connecting to dexMainnet...
2020-12-23 08:46:52 root         INFO     Deploying new contract...
Connected: True
2020-12-23 08:47:55 root         INFO     Deployed contract done!
2020-12-23 08:47:55 root         INFO     0xf74b58e5152360ceba04e56ab8249fe2ee53c9d1d3b30f8e0d6c0a2efca4028e
2020-12-23 08:47:55 root         INFO     AttributeDict({'transactionHash': HexBytes('0xf74b58e5152360ceba04e56ab8249fe2ee53c9d1d3b30f8e0d6c0a2efca4028e'), 'transactionIndex': 0, 'blockHash': HexBytes('0x6557a47d8d448ec9040b71412c546a97d694e1ff780737de5ec4e291aba462b3'), 'blockNumber': 2966013, 'cumulativeGasUsed': 229201, 'gasUsed': 229201, 'contractAddress': '0x653394D2B10BaA78d1192f9c570EB8B4C62c1d2c', 'logs': [], 'from': '0xEA14c08764c9e5F212c916E11a5c47Eaf92571e4', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')})
2020-12-23 08:47:55 root         INFO     Changer Contract Address: 0x653394D2B10BaA78d1192f9c570EB8B4C62c1d2c
Changer Contract Address: 0x653394D2B10BaA78d1192f9c570EB8B4C62c1d2c


Connecting to dexMainnet...
2020-12-23 10:41:53 root         INFO     Deploying new contract...
Connected: True
Changer Contract Address: 0xCa07256ECBfbA52d2782D8Dfd0d62f88D71Aa1f3
2020-12-23 10:42:29 root         INFO     Deployed contract done!
2020-12-23 10:42:29 root         INFO     0xdd4208dc1ad5e4de74ea3d2c2dfddd0304bf28ef722042bab34d39fd84f59bca
2020-12-23 10:42:29 root         INFO     AttributeDict({'transactionHash': HexBytes('0xdd4208dc1ad5e4de74ea3d2c2dfddd0304bf28ef722042bab34d39fd84f59bca'), 'transactionIndex': 3, 'blockHash': HexBytes('0x38f3f2a19afa54fb0c8c9980987bee5db2af93599906e1bf432d4ae097d029db'), 'blockNumber': 2966227, 'cumulativeGasUsed': 600741, 'gasUsed': 229201, 'contractAddress': '0xCa07256ECBfbA52d2782D8Dfd0d62f88D71Aa1f3', 'logs': [], 'from': '0xEA14c08764c9e5F212c916E11a5c47Eaf92571e4', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')})
2020-12-23 10:42:29 root         INFO     Changer Contract Address: 0xCa07256ECBfbA52d2782D8Dfd0d62f88D71Aa1f3
"""