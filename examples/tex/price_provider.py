from moneyonchain.networks import NetworkManager
from moneyonchain.tex import MoCDecentralizedExchange


connection_network='rskMainnetPublic'
config_network = 'dexMainnet'

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

base_address = '0xe700691dA7b9851F2F35f8b8182c69c53CcaD9Db'
secondary_address = '0x9AC7fE28967B30E3A4e6e03286d715b42B453D10'
print(dex.get_price_provider(base_address, secondary_address))

# finally disconnect from network
network_manager.disconnect()
