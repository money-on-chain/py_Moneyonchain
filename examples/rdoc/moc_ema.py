from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoCState


network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCState")
moc_state = RDOCMoCState(connection_manager)

print("Bitcoin Price in USD: {0}".format(moc_state.bitcoin_price()))
print("Bitcoin Moving Average in USD: {0}".format(moc_state.bitcoin_moving_average()))
print("Smoothing Factor: {0}".format(moc_state.smoothing_factor()))

"""
"""

