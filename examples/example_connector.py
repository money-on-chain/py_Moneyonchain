from decimal import Decimal
from web3 import Web3
from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoC


network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoC Main Contract")
moc_main = RDOCMoC(connection_manager)

addresses = moc_main.connector_addresses()
#addresses = moc_main.connector()
print(addresses)