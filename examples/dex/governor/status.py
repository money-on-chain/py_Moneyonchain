from moneyonchain.manager import ConnectionManager
from moneyonchain.governance import DEXGovernor


network = 'dexMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to DEX Governor")
gov = DEXGovernor(connection_manager)
print("Owner: {0}".format(gov.owner()))
