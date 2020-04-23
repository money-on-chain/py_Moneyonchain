from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import MoCDecentralizedExchange


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCDecentralizedExchange")
dex = MoCDecentralizedExchange(connection_manager)
print(dex.token_pairs())
