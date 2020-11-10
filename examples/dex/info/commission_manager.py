from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import CommissionManager


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCDecentralizedExchange")
dex_commission = CommissionManager(connection_manager)

print("beneficiary_address: {0}".format(dex_commission.beneficiary_address()))
print("commision_rate: {0}".format(dex_commission.commision_rate()))
print("cancelation_penalty_rate: {0}".format(dex_commission.cancelation_penalty_rate()))
print("expiration_penalty_rate: {0}".format(dex_commission.expiration_penalty_rate()))
print("minimum_commission: {0}".format(dex_commission.minimum_commission()))

inital_fee = dex_commission.calculate_initial_fee(0.001, 10000)
print("Initial fee... amount: {0} fee: {1:f}".format(1.0, inital_fee))

print("exchange_commissions DOC: {0}".format(dex_commission.exchange_commissions('0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0')))
print("exchange_commissions WRBTC: {0}".format(dex_commission.exchange_commissions('0x09b6ca5E4496238A1F176aEa6Bb607DB96c2286E')))

