"""
"""

from moneyonchain.networks import NetworkManager
from moneyonchain.transaction import TransactionReceiptBase

from brownie import web3

connection_network = 'rskTesnetLocal'
config_network = 'mocTestnetAlpha'

# init network manager
# connection network is the brownie connection network
# config network is our enviroment we want to connect
network_manager = NetworkManager(
    connection_network=connection_network,
    config_network=config_network)

# run install() if is the first time and you want to install
# networks connection from brownie
# network_manager.install()

# Connect to network
network_manager.connect()

tx_id = '0xaa84039451ee87e08dff15374d7068b836908e75d38530b66cb36e607fdc3232'
tx_receipt = web3.eth.getTransactionReceipt(tx_id)
print(tx_receipt)

tx_receipt = TransactionReceiptBase(tx_id)
tx_receipt.info()

tx_id = '0x73a0ce47ab64a31e542670578c73dbfb8f21c1c59a176bd462918db63566f42a'
tx_receipt = TransactionReceiptBase(tx_id, trace_enabled=True)
print(tx_receipt.status)
#tx_receipt.info()
print(tx_receipt.revert_msg)

# finally disconnect from network
network_manager.disconnect()
