"""
"""

from web3 import Web3

from moneyonchain.networks import network_manager, web3
from moneyonchain.transaction import TransactionReceipt

connection_network = 'rskTesnetLocal'
config_network = 'dexTestnet'

# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)


tx_id = '0xe570b02b60cbcc5decf0c10624797fd92a25cb07b303e91ee9e9146b69c94796'
tx_receipt = TransactionReceipt(tx_id, trace_enabled=True)
print(tx_receipt.status)
#tx_receipt.info()
print(tx_receipt.revert_msg)

# finally disconnect from network
network_manager.disconnect()
