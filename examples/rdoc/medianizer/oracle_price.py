"""
Oracle price get current oracle from MOC
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoC
from moneyonchain.rdoc import RDOCMoCMedianizer

# Network types
#
# rdocTestnet: Testnet
# rdocMainnet: Production Mainnet


network = 'rdocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to RDOC Main Contract")
moc_contract = RDOCMoC(connection_manager)

#oracle_provider = moc_contract.sc_moc_state.price_provider()
#print("Oracle address: {0}".format(oracle_provider))

oracle_provider = '0x987ccC60c378a61d167B6DD1EEF7613c6f63938f'

oracle = RDOCMoCMedianizer(connection_manager, contract_address=oracle_provider)

print("RIF Price in USD: {0}".format(oracle.price()))
