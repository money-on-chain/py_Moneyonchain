from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoCState


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCState")
moc_state = MoCState(connection_manager)
print("Bitcoin Price in USD: {0}".format(moc_state.bitcoin_price()))

