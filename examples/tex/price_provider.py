from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import MoCDecentralizedExchange


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCDecentralizedExchange")
dex = MoCDecentralizedExchange(connection_manager)

base_address = '0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0'
secondary_address = '0xA274d994F698Dd09256674960d86aBa22C086669'
print(dex.get_price_provider(base_address, secondary_address))
