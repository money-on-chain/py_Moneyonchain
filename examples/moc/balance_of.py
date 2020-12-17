from moneyonchain.manager import ConnectionManager
from web3 import Web3


network = 'mocMainnet2'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

user_address = '0x5d2691B2F9f4F89e5d6a6759079dF629B36CCF51'

# Block Number
block_number = 2609806
balance = Web3.fromWei(connection_manager.balance_block_number(user_address, block_number=block_number), 'ether')

print("RBTC Balance of: {0} balance: {1} blockNumber: {2}".format(
    user_address,
    balance,
    block_number))


# Block Number
block_number = 2609807
balance = Web3.fromWei(connection_manager.balance_block_number(user_address, block_number=block_number), 'ether')

print("RBTC Balance of: {0} balance: {1} blockNumber: {2}".format(
    user_address,
    balance,
    block_number))
