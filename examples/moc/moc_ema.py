from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoCState


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCState")
moc_state = MoCState(connection_manager)

print("Bitcoin Price in USD: {0}".format(moc_state.bitcoin_price()))
print("Bitcoin Moving Average in USD: {0}".format(moc_state.bitcoin_moving_average()))
print("Smoothing Factor: {0}".format(moc_state.smoothing_factor()))

"""
Connecting to mocMainnet2...
Connected: True
Connecting to MoCState
Bitcoin Price in USD: 9206.600000000000509579
Bitcoin Moving Average in USD: 8691.773665743441728397
Smoothing Factor: 0.009950249

Connecting to mocTestnet...
Connected: True
Connecting to MoCState
Bitcoin Price in USD: 9205.31
Bitcoin Moving Average in USD: 8881.279549746037722543
Smoothing Factor: 0.016528926

"""

