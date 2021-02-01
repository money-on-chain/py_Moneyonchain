from moneyonchain.networks import NetworkManager
from moneyonchain.moc_vendors import VENDORSMoCState


connection_network='rskTesnetPublic'
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

moc_state = VENDORSMoCState(network_manager).from_abi()


print("MoC price:")
print(moc_state.moc_price())


# finally disconnect from network
network_manager.disconnect()
