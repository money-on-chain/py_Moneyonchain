import os
from web3 import Web3
from collections import OrderedDict
from moneyonchain.manager import ConnectionManager
from moneyonchain.token import DoCToken


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to DoCToken")
doc_token = DoCToken(connection_manager)
print("Token Name: {0}".format(doc_token.name()))
