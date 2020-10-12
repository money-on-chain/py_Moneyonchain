from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoCInrate


network = 'mocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCInrate")
moc_inrate = MoCInrate(connection_manager)

"""
Commissions
"""
print("Commission rate: {0}".format(moc_inrate.commision_rate()))


"""
0.25% Annual
"""

print("Bitpro rate: {0}".format(moc_inrate.bitpro_rate()))
print("Bitpro holders interest: {0}".format(moc_inrate.calc_bitpro_holders_interest()))
print("Bitpro interest address: {0}".format(moc_inrate.bitpro_interest_address()))
print("Bitpro interest block span: {0}".format(moc_inrate.bitpro_interest_blockspan()))
print("Bitpro interest last payed block: {0}".format(moc_inrate.last_bitpro_interest_block()))

print("Daily inrate: {0}".format(moc_inrate.daily_inrate()))
print("Calc commission value: {0}".format(moc_inrate.calc_commission_value(10.0)))

