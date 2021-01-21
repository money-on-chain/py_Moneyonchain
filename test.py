from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoCState, MoCVendors, MoCInrate, MoCExchange, MoC
from web3 import Web3
from decimal import Decimal

network = 'mocTestTyD'
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

# print("Vendors: ", moc_vendors.get_vendors())
# #print("Vendors: ", moc_vendors.get_vendor(Web3.toChecksumAddress('0x9032f510a5b54a005f04e81b5c98b7f201c4dac1')))


moc_inrate = MoCInrate(connection_manager)
vendor_address = Web3.toChecksumAddress('0x9032f510a5b54a005f04e81b5c98b7f201c4dac1')
amount = 0.3
result = moc_inrate.calculate_vendor_markup(vendor_address, amount)
print("Vendor markup: ", result)
print("Is expected: ", result == 0.003)



moc_exchange = MoCExchange(connection_manager)
balance = moc_exchange.get_moc_token_balance(vendor_address, moc_vendors_address)
print("Balance and allowance: ", balance)

tx_type_mint_bpro_fees_rbtc = moc_inrate.tx_type_mint_bpro_fees_rbtc()
tx_type_mint_bpro_fees_moc = moc_inrate.tx_type_mint_bpro_fees_moc()
commissions = moc_exchange.calculate_commissions_with_prices(
    amount, tx_type_mint_bpro_fees_moc, tx_type_mint_bpro_fees_rbtc, vendor_address)
print("Commissions: ", commissions)


moc_main = MoC(connection_manager)
amount_want_to_mint = Decimal(0.0001)
# Mint BPro
print("Please wait to the transaction be mined!...")
tx_hash, tx_receipt, tx_logs, tx_logs_formatted = moc_main.mint_bpro(amount=amount_want_to_mint, vendor_account=vendor_address)
print("Tx hash: [{0}]".format(Web3.toHex(tx_hash)))
print("Transaction done!")
if tx_logs:
    amount = Decimal(Web3.fromWei(tx_logs['RiskProMint'][0]['args']['amount'], 'ether'))
    amount_usd = moc_main.bpro_amount_in_usd(amount)
    print("You mint {0} BPro equivalent to {1} USD".format(format(amount, '.18f'), format(amount_usd, '.3f')))
    print(tx_logs_formatted['RiskProMint'].print_row())

"""
user> export ACCOUNT_PK_SECRET=<secret>
user> python test.py
"""