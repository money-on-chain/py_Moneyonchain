from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import PriceFeederRemoverChanger


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


contract = PriceFeederRemoverChanger(connection_manager)

contract_address_medianizer = '0x78c892Dc5b7139d0Ec1eF513C9E28eDfAA44f2d4'
contract_address_pricefeed = '0x5d111d1b49Aa39d0172712266B0DE2F1eB9957F4'
tx_hash, tx_receipt = contract.constructor(contract_address_pricefeed,
                                           contract_address_medianizer=contract_address_medianizer,
                                           execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""


"""