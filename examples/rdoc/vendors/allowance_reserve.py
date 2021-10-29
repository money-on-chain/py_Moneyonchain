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
user> python ./allowance.py

Where replace with your PK, and also you need to have funds in this account
"""

from web3 import Web3
from decimal import Decimal
from moneyonchain.networks import network_manager
from moneyonchain.tokens import RIF

connection_network = 'rskTestnetPublic'
config_network = 'rdocTestnetAlpha'

# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)

moc_address = network_manager.options['networks'][config_network]['addresses']['MoC']

account_address = '0xCD8a1C9aCC980Ae031456573e34Dc05CD7dAE6e3'
amount_allow = 0

rif_token = RIF(network_manager).from_abi()

print("RIF Token address: {0}".format(rif_token.address()))
print("Account: {0}".format(account_address))
print("Balance: {0} {1}".format(rif_token.balance_of(account_address), rif_token.symbol()))
print("Allowance: {0} {1}".format(rif_token.allowance(account_address, moc_address), rif_token.symbol()))

#if amount_allow > 0:
print("Allowing ... {0} MOC".format(amount_allow))
rif_token.approve(moc_address, amount_allow)

# finally disconnect from network
network_manager.disconnect()
