"""
To run this script need private key, run this scripts with:
user> export ACCOUNT_PK_SECRET=fdas46f4dsafds7f89ds7f8dafd4fdsaf3dsA4ds5a
user> python ./example_moc_mint_btc2x.py
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

moc_main = MoC(connection_manager)

amount_want_to_mint = Decimal(0.001)
# Set MoC balance and MoC allowance if commissions should be paid in MoC instead of RBTC
moc_balance = 0
moc_allowance = 0

total_amount, commission_value, interest_value = moc_main.amount_mint_btc2x(amount_want_to_mint, moc_balance, moc_allowance)
print("To mint {0} BTC2X need {1} RBTC. Commision: {2} Interest: {3}".format(format(amount_want_to_mint, '.18f'),
                                                                             format(total_amount, '.18f'),
                                                                             format(commission_value, '.18f'),
                                                                             format(interest_value, '.18f')))

# Mint BTC2X
# This transaction is not async, you have to wait to the transaction is mined
print("Please wait to the transaction be mined!...")
tx_hash, tx_receipt, tx_logs = moc_main.mint_btc2x(amount_want_to_mint)
print("Tx hash: [{0}]".format(Web3.toHex(tx_hash)))
print("Transaction done!")
if tx_logs:
    amount = Decimal(Web3.fromWei(tx_logs[0]['args']['amount'], 'ether'))
    amount_usd = moc_main.btc2x_amount_in_usd(amount)
    print("You mint {0} BTC2X equivalent to {1} USD".format(format(amount, '.18f'), format(amount_usd, '.3f')))

print(tx_receipt)
print(tx_logs)

"""
Connected: True
Connecting to MoC Main Contract
To mint 0.001000000000000000 BTC2X need 0.001003472177478192 RBTC. Commision: 0.000001000000000000 Interest: 0.000002472177478192
Please wait to the transaction be mined!...
Transaction done!
You mint 0.001008039846725211 BTC2X equivalent to 0.001 USD
"""