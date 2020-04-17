from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoCState, RDOCMoC

network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_state = RDOCMoCState(connection_manager)
print(moc_state.collateral_reserves())
