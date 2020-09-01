from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoC


network = 'mocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_moc = MoC(connection_manager, contracts_discovery=True)
print("Connector: {0}".format(moc_moc.connector()))

print("Addresses: {0}".format(moc_moc.connector_addresses()))
