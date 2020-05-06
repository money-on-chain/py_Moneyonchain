from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import RDOCCommissionSplitterAddressChanger


network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract = RDOCCommissionSplitterAddressChanger(connection_manager)

destination_address = "0xC61820bFB8F87391d62Cd3976dDc1d35e0cf7128"

tx_hash, tx_receipt = contract.constructor(destination_address, execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")


"""
Connecting to rdocTestnetAlpha...
Connected: True
Changer Contract Address: 0x4Dc2101E6Dc32Bed5d804cfF372f0C60558de09C

Connecting to rdocTestnetAlpha...
Connected: True
Changer Contract Address: 0xf932543D193112Dd7ace08937c755FFE03DE5738

Connecting to rdocTestnet...
Connected: True
Changer Contract Address: 0x3A54cc66455f95C983887d7ae5Cb885602c454B3

Connecting to rdocMainnet...
Connected: True
Changer Contract Address: 0x2FC8261E5653306f9BCD187960cFF4Bcf19aB133
"""