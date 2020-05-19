from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import RDOCPriceFeederAdderChanger


network = 'rdocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


contract = RDOCPriceFeederAdderChanger(connection_manager)

price_feeder_owner = '0xA8f94D08D3D9C045fe0B86A953dF39B14206153c'
contract_address_medianizer = '0x01a165cC33Ff8Bd0457377379962232886be3DE6'
contract_address_feedfactory = '0xbB26D11bd2a9F2274cD1a8E571e5A352816acaEA'
tx_hash, tx_receipt = contract.constructor(price_feeder_owner,
                                           contract_address_medianizer=contract_address_medianizer,
                                           contract_address_feedfactory=contract_address_feedfactory,
                                           execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""

Connecting to rdocTestnet...
Connected: True
Changer Contract Address: 0xe127cB398f4f37E126Fa7F7af7a91b1D260eBd78

Connecting to rdocMainnet...
Connected: True
Changer Contract Address: 0xFaFdfc8aa79114bF45cC5db630B92318878cAac6


Connecting to rdocTestnetAlpha...
Connected: True
Changer Contract Address: 0x950C18fa33D079B01Ff7b4Fc18Ec830643CBf9eC

"""