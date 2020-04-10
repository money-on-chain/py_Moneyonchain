from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoCInrate


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCInrate")
moc_inrate = MoCInrate(connection_manager)
print("Commission rate: {0}".format(moc_inrate.commision_rate()))
print("Bitpro rate: {0}".format(moc_inrate.bitpro_rate()))
print("Daily inrate: {0}".format(moc_inrate.daily_inrate()))
print("Calc commission value: {0}".format(moc_inrate.calc_commission_value(10.0)))

