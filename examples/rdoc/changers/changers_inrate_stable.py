from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import RDOCMoCInrateStableChanger


network = 'rdocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


contract = RDOCMoCInrateStableChanger(connection_manager)

t_min = int(0.0001852564418 * 10 ** 18)
t_max = int(0.004 * 10 ** 18)
t_power = int(4)

tx_hash, tx_receipt = contract.constructor(t_min, t_max, t_power, execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""
Connecting to rdocTestnetAlpha...
Connected: True
Changer Contract Address: 0xccC0aF28935B7715c698E2E1A34e0BF294FC667d

Connecting to rdocTestnet...
Connected: True
Changer Contract Address: 0x7732dc9Fb3db490e2f145D8fCA2f5AC60F7cf313
"""