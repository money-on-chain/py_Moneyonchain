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

import logging
import logging.config


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')

network = 'mocMainnet2'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_main = MoC(connection_manager)

amount_want_to_mint = Decimal(0.00001)

total_amount, commission_value, interest_value = moc_main.amount_mint_btc2x(amount_want_to_mint)
print("To mint {0} BTC2X need {1} RBTC. Commision: {2} Interest: {3}".format(format(amount_want_to_mint, '.18f'),
                                                                             format(total_amount, '.18f'),
                                                                             format(commission_value, '.18f'),
                                                                             format(interest_value, '.18f')))

# Mint BTC2X
# This transaction is not async, you have to wait to the transaction is mined
print("Please wait to the transaction be mined!...")
tx_hash, tx_receipt, tx_logs, tx_logs_formatted = moc_main.mint_btc2x(amount_want_to_mint)
print("Tx hash: [{0}]".format(Web3.toHex(tx_hash)))
print("Transaction done!")
if tx_logs:
    print(tx_logs_formatted['RiskProxMint'].print_row())


"""

"""