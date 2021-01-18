from moneyonchain.networks import NetworkManager
from moneyonchain.moc import MoC


connection_network='rskTesnetPublic'
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
l_info = moc_main.settlement_info()
for info in l_info:
    print("{0}:{1}".format(info[0], info[1]))

# finally disconnect from network
network_manager.disconnect()
