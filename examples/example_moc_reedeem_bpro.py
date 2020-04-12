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


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoC Main Contract")
moc_main = MoC(connection_manager)

amount = Decimal(0.001)
print("Reedem BPro: {0}".format(amount))

# Reedeem BPro
# This transaction is not async, you have to wait to the transaction is mined
print("Please wait to the transaction be mined!...")
tx_hash, tx_receipt, tx_logs = moc_main.reedeem_bpro(amount)
if tx_logs:
    print("Transaction done!")
    amount = Decimal(Web3.fromWei(tx_logs[0]['args']['amount'], 'ether'))
    amount_usd = moc_main.bpro_amount_in_usd(amount)
    print("You reedeem {0} BPro equivalent to {1} USD".format(format(amount, '.18f'), format(amount_usd, '.2f')))
else:
    print("Transaction Failed")
