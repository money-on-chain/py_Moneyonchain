from moneyonchain.manager import ConnectionManager
from moneyonchain.token import DoCToken


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

account = '0xCD8a1C9aCC980Ae031456573e34Dc05CD7dAE6e3'

print("Connecting to MoCToken")
moc_token = MoCState(connection_manager).moc_token
print("Token Name: {0}".format(moc_token.name()))
print("Token Symbol: {0}".format(moc_token.symbol()))
print("Total Supply: {0}".format(moc_token.total_supply()))
print("Account: {0} Balance DOC: {1}".format(account, moc_token.balance_of(account)))
