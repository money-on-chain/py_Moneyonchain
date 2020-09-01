from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoC


network = 'rdocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_moc = RDOCMoC(connection_manager, contracts_discovery=False)
print("Connector: {0}".format(moc_moc.connector()))

print("Addresses: {0}".format(moc_moc.connector_addresses()))
