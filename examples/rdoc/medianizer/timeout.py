from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCPriceFeed, RDOCMoCMedianizer

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

oracle_address = '0x01a165cC33Ff8Bd0457377379962232886be3DE6'

oracle = RDOCMoCMedianizer(connection_manager,
                           contract_address=oracle_address)

print("Peek:")
print(oracle.peek())
print("Compute:")
print(oracle.compute())

if not oracle.compute()[1] and oracle.peek()[1]:
    print("Recalculating oracle status...")
    oracle.poke()
    print("Oracle status updated!")
else:
    print("Not time to recalculate status!")
