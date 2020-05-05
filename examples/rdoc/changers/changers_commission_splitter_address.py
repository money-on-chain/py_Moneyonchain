from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import RDOCCommissionSplitterAddressChanger


network = 'rdocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract = RDOCCommissionSplitterAddressChanger(connection_manager)

destination_address = "0xf69287F5Ca3cC3C6d3981f2412109110cB8af076"

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
"""