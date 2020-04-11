from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoC

"""
To run this script need private key, run this scripts with:

user> export ACCOUNT_PK_SECRET=fdas46f4dsafds7f89ds7f8dafd4fdsaf3dsA4ds5a
user> python ./example_moc_mint_bpro.py

Where replace with your PK, and also you need to have funds in this account 
"""


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoC Main Contract")
moc_main = MoC(connection_manager)

amount_want_to_mint = 0.005

total_amount, commission_value = moc_main.amount_mint_bpro(amount_want_to_mint)
print("To mint {0} bitpro need {1} RBTC. Commision {2}".format(amount_want_to_mint,
                                                               total_amount,
                                                               commission_value))

# Mint BPro
# This transaction is not async, you have to wait to the transaction is mined
#receipt = moc_main.mint_bpro(amount_want_to_mint)
#print(receipt)
#print("Transaction done!")
