from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoCVendors, MoCInrate
from web3 import Web3
from decimal import Decimal

network = 'mocTestTyD'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCVendors")
moc_vendors = MoCVendors(connection_manager)

vendor_account = '0x9032f510a5b54a005f04e81b5c98b7f201c4dac1'
print("Vendor details: ", moc_vendors.get_vendor(Web3.toChecksumAddress(vendor_account)))

print("Connecting to MoCInrate")
moc_inrate = MoCInrate(connection_manager)
vendor_address = Web3.toChecksumAddress(Web3.toChecksumAddress(vendor_account))
amount = 0.3
result = moc_inrate.calculate_vendor_markup(vendor_address, amount)
print("Vendor markup: ", result)

"""
Connecting to mocTestTyD...
Connected: True
Connecting to MoCVendors
Vendor details:  {'isActive': True, 'markup': Decimal('0.01'), 'totalPaidInMoC': Decimal('0.001639168286129008'), 'staking': Decimal('10'), 'paidMoC': Decimal('0.001548733503520314'), 'paidRBTC': Decimal('0.000104')}
Connecting to MoCInrate
Vendor markup:  0.003
"""