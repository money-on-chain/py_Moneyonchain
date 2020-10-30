
from web3 import Web3
from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import MoCDecentralizedExchange


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


print(Web3.fromWei(connection_manager.balance("0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3"), 'ether'))
"""
0.369947978838833479

0.369931379918578111

**1.6598920255350702e-05

0.0001

"""