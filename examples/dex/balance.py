
from web3 import Web3
from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import MoCDecentralizedExchange


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


print(Web3.fromWei(connection_manager.balance("0xF8C240521712488c50df208c9d66a7bcaB649bad"), 'ether'))
