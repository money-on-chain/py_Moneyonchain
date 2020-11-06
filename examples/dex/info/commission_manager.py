from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import CommissionManager


network = 'dexDevelopment'
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

inital_fee = dex_commission.calculate_initial_fee(1.0, 1.0)
print("Initial fee... amount: {0} fee: {1:f}".format(1.0, inital_fee))

#print("exchange_commissions: {0}".format(dex_commission.exchange_commissions('0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0')))

