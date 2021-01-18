from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import MoCDecentralizedExchange


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCDecentralizedExchange")
dex = MoCDecentralizedExchange(connection_manager)
print(dex.token_pairs())

pair = ['0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0', '0x4dA7997A819bb46B6758B9102234c289dD2Ad3bf']
tx_hash, tx_receipt = dex.run_tick_for_pair(pair)

print("Done!")