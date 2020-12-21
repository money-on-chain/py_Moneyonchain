from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoCState

network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_state = RDOCMoCState(connection_manager)

print("Max Mint RiskPro setted: {0}".format(moc_state.max_mint_bpro()))
print("Max mint RiskPro available: {0}".format(moc_state.max_mint_bpro_available()))
