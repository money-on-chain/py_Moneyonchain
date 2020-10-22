from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import MoCDecentralizedExchange


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCDecentralizedExchange")
#0xB08A63aE65E55b56790EfE3FBc39EaB20FC62939
dex = MoCDecentralizedExchange(connection_manager)
print(dex.token_pairs())

#pair = ['0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0', '0x840871cbb73dC94dcb11b2CEA963553Db71a95b7']
#print(dex.token_pairs_status(pair[0], pair[1]))

"""

[
['0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0', '0x09B6Ca5E4496238a1F176aEA6bB607db96C2286E'], 
['0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0', '0xC3De9F38581f83e281f260d0DdbaAc0e102ff9F8'], 
['0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0', '0x4dA7997A819bb46B6758B9102234c289dD2Ad3bf'], 
['0x09B6Ca5E4496238a1F176aEA6bB607db96C2286E', '0x4dA7997A819bb46B6758B9102234c289dD2Ad3bf'], 
['0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0', '0x19F64674D8A5B4E652319F5e239eFd3bc969A1fE'], 
['0xC3De9F38581f83e281f260d0DdbaAc0e102ff9F8', '0x23A1aA7b11e68beBE560a36beC04D1f79357f28d'], 
['0x19F64674D8A5B4E652319F5e239eFd3bc969A1fE', '0x23A1aA7b11e68beBE560a36beC04D1f79357f28d']
]




"""