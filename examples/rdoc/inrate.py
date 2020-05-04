from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoCInrate, RDOCMoC

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()


network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
log.info("Connecting to %s..." % network)
log.info("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_inrate = RDOCMoCInrate(connection_manager)

info = moc_inrate.stable_inrate()
print(info)

print("Interest of reedeeming 1.0 DOC")
interest_no_days = moc_inrate.doc_inrate_avg(1.0)

for day_to_sett in reversed(range(0, 30)):
    print("Days to settlement: {0} Interest: {1}".format(day_to_sett, interest_no_days * day_to_sett))