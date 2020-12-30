from moneyonchain.manager import ConnectionManager
from moneyonchain.token import BProToken


network = 'mocMainnet2'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

account = '0x4ebd075534d9E24cE134f8BC962311c913730a84'

print("Connecting to BProToken")
bpro_token = BProToken(connection_manager)
print("Token Name: {0}".format(bpro_token.name()))
print("Token Symbol: {0}".format(bpro_token.symbol()))
print("Total Supply: {0}".format(bpro_token.total_supply()))
print("Account: {0} Balance BPro: {1}".format(account, bpro_token.balance_of(account)))
print(bpro_token.address())
