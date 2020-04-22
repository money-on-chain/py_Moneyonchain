"""
Coin pair price
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.oracle import CoinPairPrice


network = 'mocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract = CoinPairPrice(connection_manager)
print(contract.price())
