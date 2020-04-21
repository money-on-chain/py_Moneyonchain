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


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoC Main Contract")
moc_main = MoC(connection_manager)

amount_want_to_mint = Decimal(0.001)

total_amount, commission_value = moc_main.amount_mint_doc(amount_want_to_mint)
print("To mint {0} RBTC in DOC need {1} RBTC. Commision {2}".format(format(amount_want_to_mint, '.18f'),
                                                                    format(total_amount, '.18f'),
                                                                    format(commission_value, '.18f')))

# Mint DOC
# This transaction is not async, you have to wait to the transaction is mined
print("Please wait to the transaction be mined!...")
tx_hash, tx_receipt, tx_logs = moc_main.mint_doc(amount_want_to_mint)
print("Tx hash: [{0}]".format(Web3.toHex(tx_hash)))
print("Transaction done!")
if tx_logs:
    amount = Decimal(Web3.fromWei(tx_logs[0]['args']['amount'], 'ether'))
    print("You mint {0} DOC".format(format(amount, '.18f')))

"""
Connecting to mocTestnet...
Connected: True
Connecting to MoC Main Contract
To mint 0.001000000000000000 RBTC in DOC need 0.001001000000000000 RBTC. Commision 0.000001000000000000
Please wait to the transaction be mined!...
Transaction done!
You mint 6.833970000000000254 DOC
"""