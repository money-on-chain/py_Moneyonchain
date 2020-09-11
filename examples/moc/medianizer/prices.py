"""
Prices in enviroments
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoC

# Network types
#
# mocTestnet: Testnet
# mocMainnet2: Production Mainnet


network = 'mocMainnet2'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoC Main Contract")
moc_contract = MoC(connection_manager)

print("Bitcoin Price in USD: {0}".format(moc_contract.sc_moc_state.bitcoin_price()))
print("Bitcoin Moving Average in USD: {0}".format(moc_contract.sc_moc_state.bitcoin_moving_average()))
