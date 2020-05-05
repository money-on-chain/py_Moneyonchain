from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoCInrate, RDOCMoC

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()


network = 'rdocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
log.info("Connecting to %s..." % network)
log.info("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_inrate = RDOCMoCInrate(connection_manager)

print("RDOC Freestable reedeem")
print("=======================")
info = moc_inrate.stable_inrate()
print(info)

print("Interest of reedeeming 0.01 DOC")
interest_no_days = moc_inrate.doc_inrate_avg(0.1)

for day_to_sett in reversed(range(0, 30)):
    print("Days to settlement: {0} Interest: {1}".format(day_to_sett, interest_no_days * day_to_sett))

print("RIFX Inrate")
print("===========")
info = moc_inrate.riskprox_inrate()
print(info)

print("Interest of MINT 1.0 RIFX")
interest_no_days = moc_inrate.btc2x_inrate_avg(2.0, on_minting=True)

for day_to_sett in reversed(range(0, 30)):
    print("Days to settlement: {0} Interest: {1}".format(day_to_sett, interest_no_days * day_to_sett))

print("Interest of REEDEEM 1.0 RIFX")
interest_no_days = moc_inrate.btc2x_inrate_avg(2.0, on_minting=False)

for day_to_sett in reversed(range(0, 30)):
    print("Days to settlement: {0} Interest: {1}".format(day_to_sett, interest_no_days * day_to_sett))

info = moc_inrate.calc_mint_interest_value(1.0)
print(info)
