"""
Oracle price get current oracle from MOC
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoCMedianizer

# Network types
#
# rdocTestnet: Testnet
# rdocMainnet: Production Mainnet


network = 'rdocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


oracle_provider = '0xDC3551f16FfDeBAa3Cb8D3b6C16d2A5bB9646dA4'
oracle = RDOCMoCMedianizer(connection_manager, contract_address=oracle_provider)

print("Before")
print("Min: {0}".format(oracle.min()))
oracle.set_min(2)
print("After")
print("Min: {0}".format(oracle.min()))
