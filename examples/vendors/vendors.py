from web3 import Web3
from decimal import Decimal

from moneyonchain.networks import NetworkManager
from moneyonchain.moc_vendors import VENDORSMoCVendors, VENDORSMoCInrate

connection_network = 'rskTesnetPublic'
config_network = 'mocTestTyD'

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

moc_vendors = VENDORSMoCVendors(network_manager).from_abi()

vendor_account = '0x9032f510a5b54a005f04e81b5c98b7f201c4dac1'
print("Vendor details: ", moc_vendors.get_vendor(Web3.toChecksumAddress(vendor_account)))

print("Connecting to MoCInrate")
moc_inrate = VENDORSMoCInrate(network_manager).from_abi()
vendor_address = Web3.toChecksumAddress(Web3.toChecksumAddress(vendor_account))
amount = 0.3
result = moc_inrate.calculate_vendor_markup(vendor_address, amount)
print("Vendor markup: ", result)

# finally disconnect from network
network_manager.disconnect()


"""

"""