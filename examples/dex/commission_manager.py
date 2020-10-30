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

