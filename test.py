from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoCState, MoCVendors
from web3 import Web3

network = 'mocTestnetAlpha'
connection_manager = ConnectionManager(network=network)

moc_state = MoCState(connection_manager=connection_manager)

# oracle_address = '0xE19Df38aC824E2189aC3b67bE1AefbA9eE27D002'
# moc_oracle_address = '0xEeae0B52Ac1F0D7D139898997b8367Dd67E3527c'

# oracle = MoCMedianizer(connection_manager,
#                        contract_address=oracle_address)

# moc_oracle = MoCMedianizer(connection_manager,
#                        contract_address=moc_oracle_address)


# print("Bitcoin price:")
# print(moc_state.bitcoin_price())

# print("MoC price:")
# print(moc_state.moc_price())

# print("Oracles (if have value if false, no price setted) :")
# print(oracle.peek())
# print(moc_oracle.peek())

moc_vendors_address = '0x748C0ccbDFeb85DF79fE978e9BADe1c4aaE8c757'

moc_vendors = MoCVendors(connection_manager, moc_vendors_address)

print("Vendors: ", moc_vendors.get_vendors())
#print("Vendors: ", moc_vendors.get_vendor(Web3.toChecksumAddress('0x9032f510a5b54a005f04e81b5c98b7f201c4dac1')))