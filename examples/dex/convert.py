from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import MoCDecentralizedExchange


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCDecentralizedExchange")
dex = MoCDecentralizedExchange(connection_manager)

token_address = '0x23A1aA7b11e68beBE560a36beC04D1f79357f28d'
amount = int(1 * 10 ** 18)
base_address = '0xC3De9F38581f83e281f260d0DdbaAc0e102ff9F8'

print(dex.convert_token_to_common_base(token_address, amount, base_address))

print(dex.token_pairs_status(base_address, token_address))
