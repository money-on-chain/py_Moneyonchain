from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoC

network = 'rdocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_main = RDOCMoC(connection_manager)
l_info = moc_main.settlement_info()
for info in l_info:
    print("{0}:{1}".format(info[0], info[1]))