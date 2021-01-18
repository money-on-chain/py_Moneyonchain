
from web3 import Web3
from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import MoCDecentralizedExchange


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


print(Web3.fromWei(connection_manager.balance("0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3"), 'ether'))
"""
0.094381071809110578
Insertada
0.094364468728599714
Match:
0.094364468728599714
"""