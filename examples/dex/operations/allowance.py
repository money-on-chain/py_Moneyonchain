from moneyonchain.manager import ConnectionManager
from moneyonchain.token import DoCToken, WRBTC, BProToken


network = 'dexDevelopment'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

account = '0x0e424e9a8598a55918e12de47172f3180c4b4e13'
token = 'BPRO'
amount_allow = 0  # 0 if you dont want to allow anything

dex_address = connection_manager.options['networks'][network]['addresses']['dex']

if token in ['DOC']:
    token_sc = DoCToken(connection_manager)
elif token in ['BPRO']:
    token_sc = BProToken(connection_manager)
elif token in ['WRBTC']:
    token_sc = WRBTC(connection_manager)
else:
    raise Exception("Token not recognize")

print("TOKEN INFO")
print("==========")
print("")
print("Token Name: {0}".format(token_sc.name()))
print("Token Symbol: {0}".format(token_sc.symbol()))
print("Total Supply: {0}".format(token_sc.total_supply()))
print("")
print("BALANCES")
print("==========")
print("")
print("Balance: {0} {1}".format(token_sc.balance_of(account), token))
print("Allowance: {0} {1}".format(token_sc.allowance(account, dex_address), token))

if amount_allow > 0:
    print("Allowing ... {0} {1}".format(amount_allow, token))
    token_sc.approve(dex_address, amount_allow)
