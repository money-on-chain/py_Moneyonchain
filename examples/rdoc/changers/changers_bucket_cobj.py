from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import RDOCMoCBucketContainerChanger


network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


contract = RDOCMoCBucketContainerChanger(connection_manager)

cobj_C0 = int(5.5 * 10 ** 18)
cobj_X2 = int(2 * 10 ** 18)

tx_hash, tx_receipt = contract.constructor(cobj_C0, cobj_X2, execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""
Connecting to rdocTestnetAlpha...
Connected: True
Changer Contract Address: 0xF6C63ab812Aee15afe1Ce829249d6a9d08b5254F

Connecting to rdocTestnet...
Connected: True
Changer Contract Address: 0xC0Eea7C0F7eeCd71864FBE52736bB09F8710aC68

Connecting to rdocMainnet...
Connected: True
Changer Contract Address: 0x298dbC000ED82AaF5d94Fc8745148697779074Aa
"""