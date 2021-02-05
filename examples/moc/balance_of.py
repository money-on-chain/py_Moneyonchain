from moneyonchain.networks import network_manager
from web3 import Web3


connection_network = 'rskMainnetPublic'
config_network = 'mocMainnet2'

# connection network is the brownie connection network
# config network is our enviroment we want to connect
network_manager.connect(connection_network=connection_network, config_network=config_network)


user_address = '0x5d2691B2F9f4F89e5d6a6759079dF629B36CCF51'

# Block Number
block_number = 2609806
balance = Web3.fromWei(network_manager.balance_block_number(user_address, block_number=block_number), 'ether')

print("RBTC Balance of: {0} balance: {1} blockNumber: {2}".format(
    user_address,
    balance,
    block_number))


# Block Number
block_number = 2609807
balance = Web3.fromWei(network_manager.network_balance(user_address, block_number=block_number), 'ether')

print("RBTC Balance of: {0} balance: {1} blockNumber: {2}".format(
    user_address,
    balance,
    block_number))

# finally disconnect from network
network_manager.disconnect()
