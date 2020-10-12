from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoCState

network = 'mocMainnet2'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCState...")
moc_state = MoCState(connection_manager)

print("Max Mint BPRO setted: {0}".format(moc_state.max_mint_bpro()))
print("Max mint BPRO avalaible: {0}".format(moc_state.max_mint_bpro_available()))
