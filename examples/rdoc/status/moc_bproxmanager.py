from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoCBProxManager

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

moc_bprox_manager = RDOCMoCBProxManager(connection_manager)

print("Available bucket: {0}".format(moc_bprox_manager.available_bucket()))
print("Active address count: {0}".format(moc_bprox_manager.active_address_count(block_identifier=2923911)))
