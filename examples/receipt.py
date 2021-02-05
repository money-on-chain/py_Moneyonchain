"""
"""

from web3 import Web3

from moneyonchain.networks import NetworkManager
from moneyonchain.transaction import TransactionReceipt

from brownie import web3

connection_network = 'rskMainnetPublic'
config_network = 'rdocMainnet'

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

tx_id = '0x80253cd80bd7211e9fc2247aa612786d900ef89fb1b83752dce73212b1bfe5c2'
tx_receipt = web3.eth.getTransactionReceipt(tx_id)
print(tx_receipt)

tx_receipt = TransactionReceipt(tx_id)
tx_receipt.info()

# tx_id = '0x73a0ce47ab64a31e542670578c73dbfb8f21c1c59a176bd462918db63566f42a'
# tx_receipt = TransactionReceiptBase(tx_id, trace_enabled=True)
# print(tx_receipt.status)
# #tx_receipt.info()
# print(tx_receipt.revert_msg)


tx_hash = tx_receipt.txid
print(tx_hash)

print(tx_receipt.events)
print(tx_receipt.logs)
print(tx_receipt.sender)
print(tx_receipt.receiver)
print(tx_receipt.fn_name)
print(tx_receipt.contract_name)
print(tx_receipt.value)
print(tx_receipt.gas_price)
print(tx_receipt.confirmations)



# finally disconnect from network
network_manager.disconnect()
