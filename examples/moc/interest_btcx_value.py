from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoCInrate, MoCState


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_inrate = MoCInrate(connection_manager)
moc_state = MoCState(connection_manager)

print("BTCX Inrate")
print("===========")

# amount to mint
amount_value = 0.001

# get days to settlement from the contract
days_to_settlement = moc_state.days_to_settlement()

print("Interest of MINT {0} BTCX".format(amount_value))
interest_no_days = moc_inrate.btc2x_inrate_avg(amount_value, on_minting=True)

print("Current day to settlement: {0} Interest: {1}".format(days_to_settlement, interest_no_days * days_to_settlement))

print("Interest on minting...")
for day_to_sett in reversed(range(0, 30)):
    print("Days to settlement: {0} Interest: {1}".format(day_to_sett, interest_no_days * day_to_sett))

print("Interest on reedeeming...")
interest_no_days = moc_inrate.btc2x_inrate_avg(amount_value, on_minting=False)
for day_to_sett in reversed(range(0, 30)):
    print("Days to settlement: {0} Interest: {1}".format(day_to_sett, interest_no_days * day_to_sett))
