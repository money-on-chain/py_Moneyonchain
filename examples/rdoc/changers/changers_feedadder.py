from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import RDOCPriceFeederAdderChanger


network = 'rdocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


contract = RDOCPriceFeederAdderChanger(connection_manager)

price_feeder_owner = '0xC67D9eE30d2119A384E02de568BE80FE785074Ba'
tx_hash, tx_receipt = contract.constructor(price_feeder_owner, execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""

Connecting to rdocTestnet...
Connected: True
Changer Contract Address: 0xe127cB398f4f37E126Fa7F7af7a91b1D260eBd78

"""