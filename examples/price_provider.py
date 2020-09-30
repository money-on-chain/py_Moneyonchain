from moneyonchain.manager import ConnectionManager
from moneyonchain.price_provider import PriceProvider

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()

# Connect to MoC enviroment network
network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
log.info("Connecting to %s..." % network)
log.info("Connected: {conectado}".format(conectado=connection_manager.is_connected))

price_provider = PriceProvider(connection_manager)

log.info("Last price: {0}".format(price_provider.price()))
