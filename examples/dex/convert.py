from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import MoCDecentralizedExchange


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCDecentralizedExchange")
dex = MoCDecentralizedExchange(connection_manager)

token_address = '0x09b6ca5E4496238A1F176aEa6Bb607DB96c2286E'
amount = int(1 * 10 ** 18)
base_address = '0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0'

print(dex.convert_token_to_common_base(token_address, amount, base_address))

print(dex.token_pairs_status(base_address, token_address))
