"""
Proxy implementation
"""

from web3 import Web3
from moneyonchain.manager import ConnectionManager
from moneyonchain.admin import ProxyAdmin


network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract_admin = ProxyAdmin(connection_manager)
contract_address = Web3.toChecksumAddress(connection_manager.options['networks'][network]['addresses']['MoC'])
print(contract_admin.implementation(contract_address))
