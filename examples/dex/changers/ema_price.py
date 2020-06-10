"""
Ema Price Changer
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import DexEMAPriceChanger

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

contract = DexEMAPriceChanger(connection_manager)

"""
RDOC: 0xC3De9F38581f83e281f260d0DdbaAc0e102ff9F8
DOC: 0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0
ERBTC: 0xA274d994F698Dd09256674960d86aBa22C086669
BPRO: 0x4dA7997A819bb46B6758B9102234c289dD2Ad3bf


RDOC / ERBTC

"""

base_token = '0xA274d994F698Dd09256674960d86aBa22C086669'
secondary_token = '0x4dA7997A819bb46B6758B9102234c289dD2Ad3bf'
ema_price = int(1.04420 * 10 ** 18)

tx_hash, tx_receipt = contract.constructor(base_token,
                                           secondary_token,
                                           ema_price,
                                           execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""


Connecting to dexTestnet...
Connected: True
2020-06-10 10:59:51 root         INFO     Deploying new contract...
Changer Contract Address: 0x6417FcB26b9514720e60E45Ebf54467142a6D71B
2020-06-10 11:00:30 root         INFO     Deployed contract done!
2020-06-10 11:00:30 root         INFO     0x407d85017b93f8140a91d7cae01297ff1b103329947f7b9b7760e1f9bc1dd497
2020-06-10 11:00:30 root         INFO     AttributeDict({'transactionHash': HexBytes('0x407d85017b93f8140a91d7cae01297ff1b103329947f7b9b7760e1f9bc1dd497'), 'transactionIndex': 26, 'blockHash': HexBytes('0x237c7854c4393281ba51157e7e0d7dd0fe26a52c86a37105b3ddb67f64be0ace'), 'blockNumber': 921253, 'cumulativeGasUsed': 1176642, 'gasUsed': 264641, 'contractAddress': '0x6417FcB26b9514720e60E45Ebf54467142a6D71B', 'logs': [], 'from': '0xA8342cC05241E0d940E1c74043faCd931562f19a', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')})
2020-06-10 11:00:30 root         INFO     Changer Contract Address: 0x6417FcB26b9514720e60E45Ebf54467142a6D71B


RDOC / ERBTC

base_token = '0xC3De9F38581f83e281f260d0DdbaAc0e102ff9F8'
secondary_token = '0xA274d994F698Dd09256674960d86aBa22C086669'
ema_price = int(9770 * 10 ** 18)

Connecting to dexTestnet...
Connected: True
2020-06-10 14:04:02 root         INFO     Deploying new contract...
2020-06-10 14:04:44 root         INFO     Deployed contract done!
2020-06-10 14:04:44 root         INFO     0x123b007c203a1a3b0e2ac72d334bba1a82304acfa7f3d59a914e3b0f905ef482
2020-06-10 14:04:44 root         INFO     AttributeDict({'transactionHash': HexBytes('0x123b007c203a1a3b0e2ac72d334bba1a82304acfa7f3d59a914e3b0f905ef482'), 'transactionIndex': 5, 'blockHash': HexBytes('0xe2dcf6eb59116ad760c2fc51aeeef8962fc75f7b6671b2658287ed5aee576a91'), 'blockNumber': 921593, 'cumulativeGasUsed': 468103, 'gasUsed': 264833, 'contractAddress': '0x09920bbc693CB862ffe996e085bC101909C9e2a5', 'logs': [], 'from': '0xA8342cC05241E0d940E1c74043faCd931562f19a', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')})
2020-06-10 14:04:44 root         INFO     Changer Contract Address: 0x09920bbc693CB862ffe996e085bC101909C9e2a5
Changer Contract Address: 0x09920bbc693CB862ffe996e085bC101909C9e2a5



DOC->BPRO  = 10182
DOC->ERBTC = 9770
ERBTC->BPRO = 1.044200595

"""