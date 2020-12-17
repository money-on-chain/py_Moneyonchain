from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import RDOCPriceFeederRemoverChanger


network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


contract = RDOCPriceFeederRemoverChanger(connection_manager)

contract_address_medianizer = '0x504EfCadFB020d6bBaeC8a5c5BB21453719d0E00'
contract_address_pricefeed = '0x94446fA55c7740Df3494804424734721B3Ea0354'
tx_hash, tx_receipt = contract.constructor(contract_address_pricefeed,
                                           contract_address_medianizer=contract_address_medianizer,
                                           execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""


"""