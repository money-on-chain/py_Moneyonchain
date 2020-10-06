from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import MoCInrateRiskProRateChangerChanger

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


network = 'mocMainnet2'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract = MoCInrateRiskProRateChangerChanger(connection_manager)
new_riskpro_rate = int(0.0000478537 * 10 ** 18)

if network in ['mocTestnetAlpha']:
    execute_change = True
else:
    execute_change = False

tx_hash, tx_receipt = contract.constructor(new_riskpro_rate, execute_change=execute_change)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")


"""
Connecting to mocTestnetAlpha...
Connected: True
Connecting to MoCInrate
Bitpro rate: 0.000047945
Bitpro rate: 0.0000478537
Bitpro rate: 0.0000478537


Connecting to mocMainnet2...
Connected: True
2020-09-16 10:35:48 root         INFO     Deploying new contract...
Changer Contract Address: 0x4E4dC0d568D719cdE662b37E1AB3c15C28c424Dd
2020-09-16 10:36:53 root         INFO     Deployed contract done!
2020-09-16 10:36:53 root         INFO     0xa4d676d911c81f7769adbb8aed2dc61b152372e95a4d31bbcd050b31af7eabec
2020-09-16 10:36:53 root         INFO     AttributeDict({'transactionHash': HexBytes('0xa4d676d911c81f7769adbb8aed2dc61b152372e95a4d31bbcd050b31af7eabec'), 'transactionIndex': 1, 'blockHash': HexBytes('0x6526a3f603d34cb68eddf09402bc03560a0a1c249c01e0ece46d9118c5b4925a'), 'blockNumber': 2705289, 'cumulativeGasUsed': 471858, 'gasUsed': 401490, 'contractAddress': '0x4E4dC0d568D719cdE662b37E1AB3c15C28c424Dd', 'logs': [AttributeDict({'logIndex': 0, 'blockNumber': 2705289, 'blockHash': HexBytes('0x6526a3f603d34cb68eddf09402bc03560a0a1c249c01e0ece46d9118c5b4925a'), 'transactionHash': HexBytes('0xa4d676d911c81f7769adbb8aed2dc61b152372e95a4d31bbcd050b31af7eabec'), 'transactionIndex': 1, 'address': '0x4E4dC0d568D719cdE662b37E1AB3c15C28c424Dd', 'data': '0x', 'topics': [HexBytes('0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0'), HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'), HexBytes('0x000000000000000000000000ea14c08764c9e5f212c916e11a5c47eaf92571e4')]})], 'from': '0xEA14c08764c9e5F212c916E11a5c47Eaf92571e4', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000001000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000001000000000000000000000000000000000000020000000000000000000800000000000000000000000000000000400000000000000000001000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000400000000000000000000')})
2020-09-16 10:36:53 root         INFO     Changer Contract Address: 0x4E4dC0d568D719cdE662b37E1AB3c15C28c424Dd
"""