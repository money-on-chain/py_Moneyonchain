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

token_address = '0x09b6ca5E4496238A1F176aEa6Bb607DB96c2286E'
amount = int(1 * 10 ** 18)
base_address = '0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0'

print(dex.convert_token_to_common_base(token_address, amount, base_address))

print(dex.token_pairs_status(base_address, token_address))

# finally disconnect from network
network_manager.disconnect()
