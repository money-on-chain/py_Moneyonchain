from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import PriceFeederAdderChanger


network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


contract = PriceFeederAdderChanger(connection_manager)

price_feeder_owner = '0x64dcc3bcbeae8ce586cabdef79104986beafcad6'
tx_hash, tx_receipt = contract.constructor(price_feeder_owner, execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""


"""