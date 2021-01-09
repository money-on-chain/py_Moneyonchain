"""
Oracle price get current oracle from MOC
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoC
from moneyonchain.moc import MoCMedianizer

# Network types
#
# mocTestnet: Testnet
# mocMainnet2: Production Mainnet


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoC Main Contract")
moc_contract = MoC(connection_manager)

oracle_provider = moc_contract.sc_moc_state.price_provider()
print("Oracle address: {0}".format(oracle_provider))

oracle = MoCMedianizer(connection_manager, contract_address=oracle_provider)

print("Bitcoin Price in USD: {0}".format(oracle.price()))
