"""
Prices in enviroments
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoC

# Network types
#
# rdocTestnet: Testnet
# rdocMainnet: Production Mainnet


network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoC Main Contract")
moc_contract = RDOCMoC(connection_manager)

print("RIF Price in USD: {0}".format(moc_contract.sc_moc_state.bitcoin_price()))
print("RIF Moving Average in USD: {0}".format(moc_contract.sc_moc_state.bitcoin_moving_average()))
