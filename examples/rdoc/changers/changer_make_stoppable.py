from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import RDOCMocMakeStoppableChanger

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract = RDOCMocMakeStoppableChanger(connection_manager)
stoppable = True

if network in ['mocTestnetAlpha']:
    execute_change = True
else:
    execute_change = False

tx_hash, tx_receipt = contract.constructor(stoppable=stoppable, execute_change=execute_change)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")


"""
Connecting to rdocTestnetAlpha...
2020-12-08 14:22:54 root         INFO     Deploying new contract...
Connected: True
2020-12-08 14:23:50 root         INFO     Deployed contract done!
2020-12-08 14:23:50 root         INFO     0xad2a932bfc2b8d33a3e7b1b2cf7a3191ae7eddd5a52e97c978eb3de9658f52fe
2020-12-08 14:23:50 root         INFO     AttributeDict({'transactionHash': HexBytes('0xad2a932bfc2b8d33a3e7b1b2cf7a3191ae7eddd5a52e97c978eb3de9658f52fe'), 'transactionIndex': 8, 'blockHash': HexBytes('0xfba8091883f7c6b51d3fe0b2e054a18e5adc5813a7ff950383e8456baa852741'), 'blockNumber': 1427335, 'cumulativeGasUsed': 899865, 'gasUsed': 431679, 'contractAddress': '0x775bda7b6B2305dC9Be6472E8F8E28116aaD23A3', 'logs': [AttributeDict({'logIndex': 0, 'blockNumber': 1427335, 'blockHash': HexBytes('0xfba8091883f7c6b51d3fe0b2e054a18e5adc5813a7ff950383e8456baa852741'), 'transactionHash': HexBytes('0xad2a932bfc2b8d33a3e7b1b2cf7a3191ae7eddd5a52e97c978eb3de9658f52fe'), 'transactionIndex': 8, 'address': '0x775bda7b6B2305dC9Be6472E8F8E28116aaD23A3', 'data': '0x', 'topics': [HexBytes('0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0'), HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'), HexBytes('0x000000000000000000000000a8f94d08d3d9c045fe0b86a953df39b14206153c')]})], 'from': '0xa8F94d08d3d9C045fE0b86a953DF39b14206153c', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000800000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000020000000000000000000800000020000000000000000000000000400000004000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000020000000000040000008000000000000000000000000000000000000000000000000')})
2020-12-08 14:23:50 root         INFO     Changer Contract Address: 0x775bda7b6B2305dC9Be6472E8F8E28116aaD23A3
Changer Contract Address: 0x775bda7b6B2305dC9Be6472E8F8E28116aaD23A3

Connecting to rdocTestnet...
Connected: True
2020-12-08 15:18:49 root         INFO     Deploying new contract...
Changer Contract Address: 0x1058BDFa899D51609A349B98Bb9bF3bc32d92Ba6
2020-12-08 15:19:56 root         INFO     Deployed contract done!
2020-12-08 15:19:56 root         INFO     0x89ffce5f34e7b6ed824c66016781df15a2d22e2e48a0564507c0ad6aa09584af
2020-12-08 15:19:56 root         INFO     AttributeDict({'transactionHash': HexBytes('0x89ffce5f34e7b6ed824c66016781df15a2d22e2e48a0564507c0ad6aa09584af'), 'transactionIndex': 6, 'blockHash': HexBytes('0x753a699f108be11eb15a7351124cd552be7bbd939bd5162426da38b49d43cbf4'), 'blockNumber': 1427439, 'cumulativeGasUsed': 624399, 'gasUsed': 431679, 'contractAddress': '0x1058BDFa899D51609A349B98Bb9bF3bc32d92Ba6', 'logs': [AttributeDict({'logIndex': 0, 'blockNumber': 1427439, 'blockHash': HexBytes('0x753a699f108be11eb15a7351124cd552be7bbd939bd5162426da38b49d43cbf4'), 'transactionHash': HexBytes('0x89ffce5f34e7b6ed824c66016781df15a2d22e2e48a0564507c0ad6aa09584af'), 'transactionIndex': 6, 'address': '0x1058BDFa899D51609A349B98Bb9bF3bc32d92Ba6', 'data': '0x', 'topics': [HexBytes('0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0'), HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'), HexBytes('0x000000000000000000000000a8f94d08d3d9c045fe0b86a953df39b14206153c')]})], 'from': '0xa8F94d08d3d9C045fE0b86a953DF39b14206153c', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000101000010000000000000000000000000000000020000000000000000000800000000000000000000000000000000400000004000000000000000000080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000020000000000000000008000000000000000000000000000000000000000000000000')})
2020-12-08 15:19:56 root         INFO     Changer Contract Address: 0x1058BDFa899D51609A349B98Bb9bF3bc32d92Ba6


Connecting to rdocMainnet...
Connected: True
2020-12-14 14:47:22 root         INFO     Deploying new contract...
Changer Contract Address: 0x3deb347FA4D518023b9EfB8C076365dFfF8834bE
2020-12-14 14:48:28 root         INFO     Deployed contract done!
2020-12-14 14:48:28 root         INFO     0x3ceacacc2f559da0eae0ea43530672e37bd308ded8190ee1e8f939c0f9c32738
2020-12-14 14:48:28 root         INFO     AttributeDict({'transactionHash': HexBytes('0x3ceacacc2f559da0eae0ea43530672e37bd308ded8190ee1e8f939c0f9c32738'), 'transactionIndex': 0, 'blockHash': HexBytes('0x036017e24fa0dc91b54543bd646a5cf06299eaf4ea586a52762d5a97703e15f7'), 'blockNumber': 2942802, 'cumulativeGasUsed': 431679, 'gasUsed': 431679, 'contractAddress': '0x3deb347FA4D518023b9EfB8C076365dFfF8834bE', 'logs': [AttributeDict({'logIndex': 0, 'blockNumber': 2942802, 'blockHash': HexBytes('0x036017e24fa0dc91b54543bd646a5cf06299eaf4ea586a52762d5a97703e15f7'), 'transactionHash': HexBytes('0x3ceacacc2f559da0eae0ea43530672e37bd308ded8190ee1e8f939c0f9c32738'), 'transactionIndex': 0, 'address': '0x3deb347FA4D518023b9EfB8C076365dFfF8834bE', 'data': '0x', 'topics': [HexBytes('0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0'), HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'), HexBytes('0x000000000000000000000000ea14c08764c9e5f212c916e11a5c47eaf92571e4')]})], 'from': '0xEA14c08764c9e5F212c916E11a5c47Eaf92571e4', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000001000000000000000000000000000800000000000000000000000000000000000000000000000000000000000040000000000000000000000000008000000000000000000000001000000000000000000000000000000000000020000000000000000000800000000000000000000000000000000400000000000000000000000000000000000000000000010000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000400000000000000000000')})
2020-12-14 14:48:28 root         INFO     Changer Contract Address: 0x3deb347FA4D518023b9EfB8C076365dFfF8834bE

"""