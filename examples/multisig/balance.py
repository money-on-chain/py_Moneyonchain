from web3 import Web3
from moneyonchain.manager import ConnectionManager
from moneyonchain.token import RIF

network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

rif_token = RIF(connection_manager)

account_address = '0xc61820BFb8F87391d62cD3976DDC1D35E0cF7128'

block_number = 2405000

balance_on_block = Web3.fromWei(
    connection_manager.balance_block_number(account_address, block_number), 'ether')
print("Balance: [{0}] on block: [{1}] Balance: [{2}] RBTC".format(
    account_address,
    block_number,
    balance_on_block))

balance_on_block = rif_token.balance_of(account_address, block_identifier=block_number)
print("Balance: [{0}] on block: [{1}] Balance: [{2}] RIF".format(
    account_address,
    block_number,
    balance_on_block))


block_number = 2467288

balance_on_block = Web3.fromWei(
    connection_manager.balance_block_number(account_address, block_number), 'ether')
print("Balance: [{0}] on block: [{1}] Balance: [{2}] RBTC".format(
    account_address,
    block_number,
    balance_on_block))

balance_on_block = rif_token.balance_of(account_address, block_identifier=block_number)
print("Balance: [{0}] on block: [{1}] Balance: [{2}] RIF".format(
    account_address,
    block_number,
    balance_on_block))
