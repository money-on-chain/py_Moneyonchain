from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import PriceFeederWhitelistChanger


network = 'mocMainnet2'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


contract = PriceFeederWhitelistChanger(connection_manager)

contract_address_medianizer = '0x7B19bb8e6c5188eC483b784d6fB5d807a77b21bF'
contract_address_pricefeed = '0xE94007E81412eDfdB87680F768e331E8c691f0e1'
tx_hash, tx_receipt = contract.constructor(contract_address_pricefeed,
                                           contract_address_medianizer=contract_address_medianizer,
                                           execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""


"""