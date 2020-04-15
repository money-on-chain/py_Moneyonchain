from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoC

network = 'rdocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_main = RDOCMoC(connection_manager)
moc_main.settlement_remaining()
