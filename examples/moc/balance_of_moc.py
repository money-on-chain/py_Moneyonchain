from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoC


network = 'mocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoC Contract ...")
moc_contract = MoC(connection_manager)
moc_address = moc_contract.address()

if moc_contract.mode != 'MoC':
    raise Exception("Note: This script is only for MOC mode contract ...")

print("RBTC Balance of contract: {0} balance: {1}".format(
    moc_address,
    moc_contract.rbtc_balance_of(moc_address)))
