from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import MocStateMaxMintBProChanger

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

contract = MocStateMaxMintBProChanger(connection_manager)
max_mint_bpro = int(200 * 10 ** 18)

if network in ['mocTestnetAlpha']:
    execute_change = True
else:
    execute_change = False

tx_hash, tx_receipt = contract.constructor(max_mint_bpro, execute_change=execute_change)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")


"""

Connecting to mocMainnet2...
2020-10-07 09:18:29 root         INFO     Deploying new contract...
Connected: True
Changer Contract Address: 0xa5cB60AD6f4F4eD815185e67B322Fc036605795b
2020-10-07 09:18:54 root         INFO     Deployed contract done!
2020-10-07 09:18:54 root         INFO     0xcbd180140dea3300e47c0f0f90beb29debd817c0fb90f7c0c3356b0a9542c61a
2020-10-07 09:18:54 root         INFO     AttributeDict({'transactionHash': HexBytes('0xcbd180140dea3300e47c0f0f90beb29debd817c0fb90f7c0c3356b0a9542c61a'), 'transactionIndex': 0, 'blockHash': HexBytes('0xc4e68b9118c537f1beb4bd9a6e60d79554dfdf91ed1df46d260babf0c90cb151'), 'blockNumber': 2760683, 'cumulativeGasUsed': 410672, 'gasUsed': 410672, 'contractAddress': '0xa5cB60AD6f4F4eD815185e67B322Fc036605795b', 'logs': [AttributeDict({'logIndex': 0, 'blockNumber': 2760683, 'blockHash': HexBytes('0xc4e68b9118c537f1beb4bd9a6e60d79554dfdf91ed1df46d260babf0c90cb151'), 'transactionHash': HexBytes('0xcbd180140dea3300e47c0f0f90beb29debd817c0fb90f7c0c3356b0a9542c61a'), 'transactionIndex': 0, 'address': '0xa5cB60AD6f4F4eD815185e67B322Fc036605795b', 'data': '0x', 'topics': [HexBytes('0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0'), HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'), HexBytes('0x000000000000000000000000ea14c08764c9e5f212c916e11a5c47eaf92571e4')]})], 'from': '0xEA14c08764c9e5F212c916E11a5c47Eaf92571e4', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000001000000000000000000000000000800000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000080020000000000000000000800000000000000000000000000000000400000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000800000000000000000400000000000000000000')})
2020-10-07 09:18:54 root         INFO     Changer Contract Address: 0xa5cB60AD6f4F4eD815185e67B322Fc036605795b

"""