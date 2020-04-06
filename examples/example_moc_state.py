import os
from web3 import Web3
from collections import OrderedDict
from moneyonchain.manager import ConnectionManager


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

path_abi = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi')
moc_state_address = Web3.toChecksumAddress('0x0adb40132cB0ffcEf6ED81c26A1881e214100555')
moc_state = connection_manager.load_abi_contract(os.path.join(path_abi, "MoCState.abi"),
                                                 contract_address=moc_state_address)

print("Starting to call contract...")

info = OrderedDict()
description = OrderedDict()

# Get bitcoin price from moc state
info['BTCprice'] = Web3.fromWei(moc_state.functions.getBitcoinPrice().call(), 'ether')
description['BTCprice'] = 'Bitcoin price USD'

print("{0}: {1}".format(description['BTCprice'], info['BTCprice']))
