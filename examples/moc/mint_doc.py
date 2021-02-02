"""
To run this script need private key, run this scripts with:

user> export ACCOUNT_PK_SECRET=fdas46f4dsafds7f89ds7f8dafd4fdsaf3dsA4ds5a
user> python ./example_moc_mint_doc.py

Where replace with your PK, and also you need to have funds in this account
"""


from decimal import Decimal
from web3 import Web3
from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoC


network = 'mocTestTyD'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoC Main Contract")
moc_main = MoC(connection_manager)

vendor_account = Web3.toChecksumAddress('0x9032f510a5b54a005f04e81b5c98b7f201c4dac1')
amount_want_to_mint = Decimal(0.001)

total_amount, commission_value, markup_value = moc_main.amount_mint_doc(
    amount=amount_want_to_mint,
    vendor_account=vendor_account)

print("To mint {0} RBTC in DOC need {1} RBTC. Commission {2}. Markup {3}".format(format(amount_want_to_mint, '.18f'),
                                                               format(total_amount, '.18f'),
                                                               format(commission_value, '.18f'),
                                                               format(markup_value, '.18f')))
# Mint DOC
# This transaction is not async, you have to wait to the transaction is mined
print("Please wait to the transaction be mined!...")
tx_hash, tx_receipt, tx_logs, tx_logs_formatted = moc_main.mint_doc(
    amount=amount_want_to_mint,
    vendor_account=vendor_account)
print("Tx hash: [{0}]".format(Web3.toHex(tx_hash)))
print("Transaction done!")
if tx_logs:
    amount = Decimal(Web3.fromWei(tx_logs['StableTokenMint'][0]['args']['amount'], 'ether'))
    print("You mint {0} DOC".format(format(amount, '.18f')))
    print(tx_logs_formatted['StableTokenMint'].print_row())

"""
Connecting to mocTestnet...
Connected: True
Connecting to MoC Main Contract
To mint 0.001000000000000000 RBTC in DOC need 0.001013000000000000 RBTC. Commission 0.000003000000000000. Markup 0.000010000000000000
Please wait to the transaction be mined!...
Transaction done!
You mint 10.000000000000000000 DOC
"""