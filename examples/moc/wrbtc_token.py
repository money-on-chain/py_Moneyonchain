from moneyonchain.manager import ConnectionManager
from moneyonchain.token import WRBTC


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

account = '0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3'

print("Connecting to WRBTC")
wrbtc_token = WRBTC(connection_manager)
print("Token Name: {0}".format(wrbtc_token.name()))
print("Token Symbol: {0}".format(wrbtc_token.symbol()))
print("Total Supply: {0}".format(wrbtc_token.total_supply()))
print("Account: {0} Balance DOC: {1}".format(account, wrbtc_token.balance_of(account)))

"""

"""