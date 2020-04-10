from moneyonchain.manager import ConnectionManager
from moneyonchain.token import BProToken


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to BProToken")
bpro_token = BProToken(connection_manager)
print("Token Name: {0}".format(bpro_token.name()))
print("Token Symbol: {0}".format(bpro_token.symbol()))
print("Total Supply: {0}".format(bpro_token.total_supply()))
