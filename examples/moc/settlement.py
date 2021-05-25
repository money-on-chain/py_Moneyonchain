from moneyonchain.networks import network_manager
from moneyonchain.moc import MoC


connection_network = 'rskMainnetPublic'
config_network = 'mocMainnet2'

# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)

moc_main = MoC(network_manager).from_abi()
l_info = moc_main.settlement_info()
for info in l_info:
    print("{0}:{1}".format(info[0], info[1]))

# finally disconnect from network
network_manager.disconnect()
