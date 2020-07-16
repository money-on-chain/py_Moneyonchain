from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import MoCSettlementChanger


network = 'mocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


contract = MoCSettlementChanger(connection_manager)

tx_hash, tx_receipt = contract.constructor(6000, execute_change=True)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""

"""