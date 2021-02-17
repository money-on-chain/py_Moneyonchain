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

"""

from web3 import Web3
from decimal import Decimal

from moneyonchain.networks import network_manager
from moneyonchain.moc_vendors import VENDORSMoCVendors, VENDORSMoCInrate

connection_network = 'rskTestnetPublic'
config_network = 'mocTestTyD'

# connection network is the brownie connection network
# config network is our enviroment we want to connect
network_manager.connect(connection_network=connection_network, config_network=config_network)

moc_vendors = VENDORSMoCVendors(network_manager).from_abi()

vendor_account = '0x9032f510a5b54a005f04e81b5c98b7f201c4dac1'
print("Vendor details: ", moc_vendors.get_vendor(Web3.toChecksumAddress(vendor_account)))

print("Connecting to MoCInrate")
moc_inrate = VENDORSMoCInrate(network_manager).from_abi()
vendor_address = Web3.toChecksumAddress(Web3.toChecksumAddress(vendor_account))
amount = 0.3
result = moc_inrate.calculate_vendor_markup(vendor_address, amount)
print("Vendor markup: ", result)

# finally disconnect from network
network_manager.disconnect()


"""

"""