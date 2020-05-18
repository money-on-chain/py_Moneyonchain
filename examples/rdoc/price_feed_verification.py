"""
Price feeder verification. Test if pricefeeder is working and sending prices.
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoCMedianizer, \
    RDOCPriceFeed

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


oracle_address = '0x504EfCadFB020d6bBaeC8a5c5BB21453719d0E00'
feeder_address = '0xBEd51D83CC4676660e3fc3819dfAD8238549B975'

oracle = RDOCMoCMedianizer(connection_manager,
                           contract_address=oracle_address)

feeder = RDOCPriceFeed(connection_manager,
                       contract_address=feeder_address,
                       contract_address_moc_medianizer=oracle_address)

print("Oracle price:")
print(oracle.peek())

print("Price feeder price and have value (if have value if false, no price setted) :")
print(feeder.peek())

print("Index > 0 is active price feeder")
print(oracle.indexes(feeder_address))
