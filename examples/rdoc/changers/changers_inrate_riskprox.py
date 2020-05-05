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
Connecting to rdocTestnetAlpha...
Connected: True
Changer Contract Address: 0x00Bf297D5ea6Dd557f0ac8327bdf142F853826F1

Connecting to rdocTestnet...
Connected: True
Changer Contract Address: 0x6ffce946361C311ab2cdce9b33E1339ccBfb589a

Connecting to rdocMainnet...
Connected: True
Changer Contract Address: 0x4BC02E34B8436EAc4C16eB71D90cD31BfCA3F21B
"""