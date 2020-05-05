from moneyonchain.manager import ConnectionManager
from moneyonchain.commission import RDOCCommissionSplitter

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

splitter = RDOCCommissionSplitter(connection_manager)

print("Contract address:")
print(splitter.commission_address())

print("MoC Address")
print(splitter.moc_address())

print("Reserve Address")
print(splitter.reserve_address())
