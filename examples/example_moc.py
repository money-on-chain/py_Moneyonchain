from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoC


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoC Main Contract")
moc_main = MoC(connection_manager)
print("The contract is paused?: {0}".format(moc_main.paused()))

total_amount, commission_value = moc_main.amount_mint_bitpro(10.0)
print("To mint 10 bitpro need {0} RBTC. Commision {1}".format(total_amount, commission_value))



