from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import RDOCMoCInrateRiskproxChanger


network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


contract = RDOCMoCInrateRiskproxChanger(connection_manager)

t_min = int(0.0001852564418 * 10 ** 18)
t_max = int(0.004 * 10 ** 18)
t_power = int(4)

tx_hash, tx_receipt = contract.constructor(t_min, t_max, t_power, execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""

"""