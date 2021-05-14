"""
To run this script need private key, run this scripts with:

user> export ACCOUNT_PK_SECRET=PK
user> python ./mint_bpro.py

Where replace with your PK, and also you need to have funds in this account
"""


from decimal import Decimal
from moneyonchain.networks import NetworkManager
from moneyonchain.moc import MoC

connection_network = 'rskTestnetPublic'
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


moc_main = MoC(network_manager).from_abi()

amount_want_to_mint = Decimal(0.0001)

gas_estimated = moc_main.mint_bpro_gas_estimated(amount_want_to_mint)
print("To mint BPRO gas estimation: {0}".format(gas_estimated))

gas_estimated = moc_main.mint_doc_gas_estimated(amount_want_to_mint)
print("To mint DOC gas estimation: {0}".format(gas_estimated))

gas_estimated = moc_main.mint_bprox_gas_estimated(amount_want_to_mint)
print("To mint BTCX gas estimation: {0}".format(gas_estimated))

# finally disconnect from network
network_manager.disconnect()
