from moneyonchain.manager import ConnectionManager
from moneyonchain.token import WRBTC


network = 'dexMainnet'
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
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 0.202216582228348149
Insert:
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 0.202216582228348149
Match:
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 0.203215582228348149


1.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 0.203215582228348149
2.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 0.203215582228348149
3.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 0.204214582228348149

1.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 0.204214582228348149
2.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 0.203214582228348149
3.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 0.203214582228348149


1.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 0.203214582228348149
2.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 0.202214582228348149
3.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 0.203214332228348149


1.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 0.203214332228348149
2.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 0.203214332228348149
3.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 0.204213332228348149

"""