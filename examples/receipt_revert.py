"""
"""

from web3 import Web3

from moneyonchain.networks import network_manager, web3
from moneyonchain.transaction import TransactionReceipt

connection_network = 'rskMainnetLocal'
config_network = 'dexMainnet'

# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)


tx_id = '0xa0b5bda0b594ad7b272bcc072f9621c20ae5935aaa57c727eec1ac14a9738cf4'
tx_receipt = TransactionReceipt(tx_id, trace_enabled=True)
print(tx_receipt.status)
#tx_receipt.info()
print(tx_receipt.revert_msg)

# finally disconnect from network
network_manager.disconnect()
