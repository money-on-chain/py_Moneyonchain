from moneyonchain.networks import NetworkManager
from moneyonchain.tex import MoCDecentralizedExchange


connection_network='rskTesnetPublic'
config_network = 'dexTestnet'

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


print("Connecting to MoCDecentralizedExchange")
dex = MoCDecentralizedExchange(network_manager).from_abi()

base_address = '0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0'
secondary_address = '0xA274d994F698Dd09256674960d86aBa22C086669'
print(dex.get_price_provider(base_address, secondary_address))

# finally disconnect from network
network_manager.disconnect()
