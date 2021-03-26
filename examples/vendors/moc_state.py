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

from moneyonchain.networks import network_manager
from moneyonchain.moc_vendors import VENDORSMoCState


connection_network='rskTestnetPublic'
config_network = 'mocTestnetAlpha3'

# connection network is the brownie connection network
# config network is our enviroment we want to connect
network_manager.connect(connection_network=connection_network, config_network=config_network)

moc_state = VENDORSMoCState(network_manager).from_abi()


print("Bitcoin Price in USD: {0}".format(moc_state.bitcoin_price()))
print("Bitcoin Moving Average in USD: {0}".format(moc_state.bitcoin_moving_average()))
print("Days to settlement: {0}".format(moc_state.days_to_settlement()))
print("Global Coverage: {0}".format(moc_state.global_coverage()))
print("Bitpro Total Supply: {0}".format(moc_state.bitpro_total_supply()))
print("DOC Total Supply: {0}".format(moc_state.doc_total_supply()))
print("Implementation: {0}".format(moc_state.implementation()))
print("BPro Discount: {0}".format(moc_state.bpro_discount_rate()))
print("BPro Tec Price: {0}".format(moc_state.bpro_tec_price()))

print("Vendors STATS:")
print("==============")
print("MoC Price: {0}".format(moc_state.moc_price()))
print("MoC Price Provider: {0}".format(moc_state.moc_price_provider()))
print("MoC Token: {0}".format(moc_state.moc_token()))
print("MoC Vendors: {0}".format(moc_state.moc_vendors()))
print("Protected: {0}".format(moc_state.protected()))
print("Liquidation enabled: {0}".format(moc_state.liquidation_enabled()))


# finally disconnect from network
network_manager.disconnect()
