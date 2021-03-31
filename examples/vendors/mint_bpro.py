"""
If is the first time to py_Moneyonchain we need brownie framework installed

`pip install eth-brownie==1.12.2`

and to install connection nodes required to connect, also run :

```
console> brownie networks add RskNetwork rskTestnetPublic host=https://public-node.testnet.rsk.co chainid=31 explorer=https://blockscout.com/rsk/mainnet/api
console> brownie networks add RskNetwork rskTestnetLocal host=http://localhost:4444 chainid=31 explorer=https://blockscout.com/rsk/mainnet/api
console> brownie networks add RskNetwork rskMainnetPublic host=https://public-node.rsk.co chainid=30 explorer=https://blockscout.com/rsk/mainnet/api
console> brownie networks add RskNetwork rskMainnetLocal host=http://localhost:4444 chainid=30 explorer=https://blockscout.com/rsk/mainnet/api
```

To run this script need private key, run this scripts with:

user> export ACCOUNT_PK_SECRET=PK
user> python ./mint_bpro.py

Where replace with your PK, and also you need to have funds in this account
"""

from web3 import Web3
from decimal import Decimal
from moneyonchain.networks import network_manager
from moneyonchain.moc_vendors import VENDORSMoC

connection_network = 'rskTestnetPublic'
config_network = 'mocTestnetAlpha3'

# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)

moc_main = VENDORSMoC(network_manager).from_abi()

amount_want_to_mint = Decimal(0.001)

vendor_account = Web3.toChecksumAddress('0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3')

total_amount, commission_value, markup_value = moc_main.amount_mint_bpro(
    amount=amount_want_to_mint,
    vendor_account=vendor_account)

print("To mint {0} bitpro need {1} RBTC. Commission {2}. Markup {3}".format(
    format(amount_want_to_mint, '.18f'),
    format(total_amount, '.18f'),
    format(commission_value, '.18f'),
    format(markup_value, '.18f')))

print("Please wait to the transaction be mined!...")
tx_receipt = moc_main.mint_bpro(amount_want_to_mint, vendor_account)

# finally disconnect from network
network_manager.disconnect()
