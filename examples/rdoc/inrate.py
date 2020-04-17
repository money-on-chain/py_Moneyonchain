from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoCInrate, RDOCMoC

network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_inrate = RDOCMoCInrate(connection_manager)

info = moc_inrate.daily_enabled()
print(info)

info = moc_inrate.daily_inrate()
print(info)

info = moc_inrate.last_daily_pay()
print(info)


