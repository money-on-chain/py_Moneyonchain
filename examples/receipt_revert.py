"""
"""

from web3 import Web3

from moneyonchain.networks import network_manager, web3
from moneyonchain.transaction import TransactionReceipt

connection_network = 'rskTestnetLocal'
config_network = 'mocTestnetAlpha'

# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)


tx_id = '0x14b487543f60dc534a83204965466d3665cebe5745ee5c5cebb00b65a9b49ee4'
tx_receipt = TransactionReceipt(tx_id, trace_enabled=True)
print(tx_receipt.status)
#tx_receipt.info()
print(tx_receipt.revert_msg)

# finally disconnect from network
network_manager.disconnect()
