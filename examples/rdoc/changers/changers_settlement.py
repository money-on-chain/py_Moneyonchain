from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import RDOCMoCSettlementChanger


network = 'rdocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


contract = RDOCMoCSettlementChanger(connection_manager)

tx_hash, tx_receipt = contract.constructor(5000, execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""
Connecting to rdocTestnetAlpha...
Connected: True
Changer Contract Address: 0x2875792db3152F172Afcb6B2a4DD926f17eF0d5B
"""