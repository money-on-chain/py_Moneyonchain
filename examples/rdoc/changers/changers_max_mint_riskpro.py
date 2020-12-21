from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import RDOCMoCStateMaxMintRiskProChanger


network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract = RDOCMoCStateMaxMintRiskProChanger(connection_manager)

max_mint_riskpro = int(20000000 * 10 ** 18)
tx_hash, tx_receipt = contract.constructor(max_mint_riskpro, execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

