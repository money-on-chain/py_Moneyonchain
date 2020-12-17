from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoCState


network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_state = RDOCMoCState(connection_manager)

print("Bucket NBTC: {0}".format(moc_state.bucket_nbtc(str.encode('C0'), formatted=False)))
print("Bucket NDOC: {0}".format(moc_state.bucket_ndoc(str.encode('C0'), formatted=False)))
