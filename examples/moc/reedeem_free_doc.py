"""
To run this script need private key, run this scripts with:

user> export ACCOUNT_PK_SECRET=fdas46f4dsafds7f89ds7f8dafd4fdsaf3dsA4ds5a
user> python ./example_moc_mint_bpro.py

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

moc_main = MoC(connection_manager)

vendor_account = Web3.toChecksumAddress('0x9032f510a5b54a005f04e81b5c98b7f201c4dac1')
amount = Decimal(10.0)
print("Reedem Free Doc: {0}".format(amount))

# This transaction is not async, you have to wait to the transaction is mined
print("Please wait to the transaction be mined!...")
tx_hash, tx_receipt, tx_logs, tx_logs_formatted = moc_main.reedeem_free_doc(
    amount_token=amount,
    vendor_account=vendor_account)
print("Tx hash: [{0}]".format(Web3.toHex(tx_hash)))
print("Transaction done!")
if tx_logs:
    amount_doc = Decimal(Web3.fromWei(tx_logs[0]['args']['amount'], 'ether'))
    amount_btc = Decimal(Web3.fromWei(tx_logs[0]['args']['reserveTotal'], 'ether'))
    amount_commision = Decimal(Web3.fromWei(tx_logs[0]['args']['commission'], 'ether'))
    amount_markup = Decimal(Web3.fromWei(tx_logs[0]['args']['btcMarkup'], 'ether'))
    amount_interest = Decimal(Web3.fromWei(tx_logs[0]['args']['interests'], 'ether'))

    print("You reedeem {0} DOC equivalent to {1} RBTC".format(format(amount_doc, '.4f'), format(amount_btc, '.18f')))
    print("Commission {0} RBTC. Markup {1} RBTC. Interest {2} RBTC".format(format(amount_commision, '.18f'), format(amount_markup, '.18f'), format(amount_interest, '.18f')))

print(tx_receipt)
print(tx_logs)
