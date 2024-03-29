# Money On Chain

Python API to Money On Chain projects. We want to provide easy to use access to our contracts. 

**Note**: Use version 2.0.39 for RIF Project on production.

### Requirements

* Python 3.6+ support
* Brownie

### Brownie

[Brownie](https://github.com/eth-brownie/brownie) is a Python-based development and testing framework for smart contracts.
Brownie is easy so we integrated it with Money on Chain.


### Installation

```
pip install moneyonchain
```

or with specific version

```
pip install moneyonchain==2.1.0
```

**Also we need brownie installed**

`pip install eth-brownie==1.14.6`



#### Network connection 

First we need to install custom networks (RSK Nodes) in brownie:

```
console> brownie networks add RskNetwork rskTestnetPublic host=https://public-node.testnet.rsk.co chainid=31 explorer=https://blockscout.com/rsk/mainnet/api
console> brownie networks add RskNetwork rskTestnetLocal host=http://localhost:4444 chainid=31 explorer=https://blockscout.com/rsk/mainnet/api
console> brownie networks add RskNetwork rskMainnetPublic host=https://public-node.rsk.co chainid=30 explorer=https://blockscout.com/rsk/mainnet/api
console> brownie networks add RskNetwork rskMainnetLocal host=http://localhost:4444 chainid=30 explorer=https://blockscout.com/rsk/mainnet/api
 brownie networks add BSCNetwork bscTestnet host=https://data-seed-prebsc-1-s1.binance.org:8545/ chainid=97 explorer=https://blockscout.com/rsk/mainnet/api
```


#### Connection table

| Network Name      | Network node          | Host                               | Chain    |
|-------------------|-----------------------|------------------------------------|----------|
| rskTestnetPublic   | RSK Testnet Public    | https://public-node.testnet.rsk.co | 31       |    
| rskTestnetLocal    | RSK Testnet Local     | http://localhost:4444              | 31       |
| rskMainnetPublic  | RSK Mainnet Public    | https://public-node.rsk.co         | 30       |
| rskMainnetLocal   | RSK Mainnet Local     | http://localhost:4444              | 30       |


Example 1. Connect by default to RSK Testnet public node and to mocTestnet enviroment and print is connected

```
from moneyonchain.networks import network_manager

# this is our connection node, in this case RSK Public node
connection_network='rskTestnetPublic'

# this is our enviroment we want to use.
config_network = 'mocTestnet'

# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)

print(network_manager.is_connected())

# finally disconnect from network
network_manager.disconnect()

```

#### Enviroment table

Enviroment is our already deployed contracts. For example **mocMainnet2** is our MOC current production enviroment.

| Network Name      | Project | Enviroment                       | Network    |
|-------------------|---------|----------------------------------|------------|
| mocTestnetAlpha   | MOC     |                                  | Testnet    |
| mocTestnet        | MOC     | moc-testnet.moneyonchain.com     | Testnet    |
| mocMainnet2       | MOC     | alpha.moneyonchain.com           | Mainnet    |
| rdocTestnetAlpha  | RIF     |                                  | Testnet    |
| rdocTestnet       | RIF     | rif-testnet.moneyonchain.com     | Testnet    |
| rdocMainnet       | RIF     | rif.moneyonchain.com             | Mainnet    |
| dexTestnet        | TEX     | tex-testnet.moneyonchain.com     | Testnet    |
| dexMainnet        | TEX     | tex.moneyonchain.com             | Mainnet    |

#### Price provider

Get the last price from MOC or RDOC contract.

See example in source/example/price_provider.py


```
from moneyonchain.networks import network_manager
from moneyonchain.oracle import PriceProvider

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()

# this is our connection node, in this case RSK Public node
connection_network='rskTestnetPublic'

# this is our enviroment we want to use.
config_network = 'mocTestnet'

# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)

price_provider = PriceProvider(network_manager)

log.info("Last price: {0}".format(price_provider.price()))

# finally disconnect from network
network_manager.disconnect()

```

result:

```
INFO:root:Connecting to mocTestnet...
INFO:root:Connected: True
INFO:root:Last price: 10725.4
```

RDOC Contract:

```
from moneyonchain.networks import network_manager
from moneyonchain.oracle import PriceProvider

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()

connection_network='rskTestnetPublic'

# connect to RDOC Enviroment
config_network = 'rdocTestnet'

# Connect to network
network_manager.connect(connection_network=connection_network,  config_network=config_network)

price_provider = PriceProvider(network_manager)

log.info("Last price: {0}".format(price_provider.price()))

# finally disconnect from network
network_manager.disconnect()

```

Result:

```
INFO:root:Connecting to rdocTestnet...
INFO:root:Connected: True
INFO:root:Last price: 0.092123288999999996
```


#### Mint BPro example

To run this script need private key, where replace with your PK in **PRIVATE_KEY**, and also you need to have funds in this account

```
martin@martin-desktop:~$ export ACCOUNT_PK_SECRET=PRIVATE_KEY
martin@martin-desktop:~$ python ./mint_bpro.py
```

Example code

```
from decimal import Decimal
from moneyonchain.networks import NetworkManager
from moneyonchain.moc import MoC

connection_network = 'rskTestnetPublic'
config_network = 'mocTestnet'

# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)


moc_main = MoC(network_manager).from_abi()

amount_want_to_mint = Decimal(0.001)

total_amount, commission_value = moc_main.amount_mint_bpro(amount_want_to_mint)
print("To mint {0} bitpro need {1} RBTC. Commision {2}".format(format(amount_want_to_mint, '.18f'),
                                                               format(total_amount, '.18f'),
                                                               format(commission_value, '.18f')))

print("Please wait to the transaction be mined!...")
tx_receipt = moc_main.mint_bpro(amount_want_to_mint)

# finally disconnect from network
network_manager.disconnect()

```

this print

```
Connecting to mocTestnet...
Connected: True
Connecting to MoC Main Contract
To mint 0.001000000000000000 bitpro need 0.001001000000000000 RBTC. Commision 0.000001000000000000
Please wait to the transaction be mined!...
Transaction done!
You mint 0.000965723337947316 BPro equivalent to 7.107 USD
```

More examples in folder 'examples/'