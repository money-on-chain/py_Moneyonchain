from web3 import Web3
from moneyonchain.networks import network_manager
from moneyonchain.multicall import Multicall2
from moneyonchain.moc import MoCState

connection_network = 'rskTestnetPublic'
config_network = 'mocTestnet'

# Connect to network
network_manager.connect(
    connection_network=connection_network,
    config_network=config_network)

print("Connecting to Multicall2")
multicall = Multicall2(network_manager, contract_address='0x9E469E1FC7Fb4c5d17897b68eaF1aFC9df39f103').from_abi()
moc_state = MoCState(network_manager).from_abi()

moc_state_address = moc_state.address()

list_aggregate = list()
list_aggregate.append((moc_state_address, moc_state.sc.getBitcoinPrice, [], lambda x: Web3.fromWei(x, 'ether')))
list_aggregate.append((moc_state_address, moc_state.sc.bproUsdPrice, [], lambda x: Web3.fromWei(x, 'ether')))

results = multicall.aggregate_multiple(list_aggregate)
print(results)

# finally disconnect from network
network_manager.disconnect()
