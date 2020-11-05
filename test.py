from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoCState, MoCMedianizer

network = 'mocTestnetAlpha'
connection_manager = ConnectionManager(network=network)

moc_state = MoCState(connection_manager=connection_manager)

oracle_address = '0xE19Df38aC824E2189aC3b67bE1AefbA9eE27D002'
moc_oracle_address = '0xEeae0B52Ac1F0D7D139898997b8367Dd67E3527c'

oracle = MoCMedianizer(connection_manager,
                       contract_address=oracle_address)

moc_oracle = MoCMedianizer(connection_manager,
                       contract_address=moc_oracle_address)


print("Bitcoin price:")
print(moc_state.bitcoin_price())

print("MoC price:")
print(moc_state.moc_price())

print("Oracles (if have value if false, no price setted) :")
print(oracle.peek())
print(moc_oracle.peek())