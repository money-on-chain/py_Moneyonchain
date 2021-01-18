import json
import os
from moneyonchain.manager import ConnectionManager
from moneyonchain.token import DoCToken, WRBTC, BProToken, RIFDoC, RIF, RIFPro


def options_from_settings(filename='settings.json'):
    """ Options from file settings.json """

    with open(filename) as f:
        config_options = json.load(f)

    return config_options


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

# load settings from file
settings = options_from_settings(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.json'))

#account = '0xB5E2Bed9235b6366Fa0254c2e6754E167e0a2383'
account = '0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3'
#account = '0x0e424e9a8598a55918e12de47172f3180c4b4e13'
token = 'RDOC'
amount_allow = 0  # 0 if you dont want to allow anything

dex_address = connection_manager.options['networks'][network]['addresses']['dex']

if token in ['DOC']:
    token_sc = DoCToken(connection_manager, contract_address=settings[network]['DOC'])
elif token in ['BPRO']:
    token_sc = BProToken(connection_manager, contract_address=settings[network]['BPRO'])
elif token in ['WRBTC']:
    token_sc = WRBTC(connection_manager, contract_address=settings[network]['WRBTC'])
elif token in ['RDOC']:
    token_sc = RIFDoC(connection_manager, contract_address=settings[network]['RDOC'])
elif token in ['RIF']:
    token_sc = RIF(connection_manager, contract_address=settings[network]['RIF'])
elif token in ['RIFP']:
    token_sc = RIFPro(connection_manager, contract_address=settings[network]['RIFP'])
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
