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
feeders = [('0x461750b4824b14c3d9b7702bC6fBB82469082b23', '# MOC'),
           ('0xBEd51D83CC4676660e3fc3819dfAD8238549B975', '# RSK')]


oracle = RDOCMoCMedianizer(connection_manager,
                           contract_address=oracle_address)

print("Oracle price:")
print(oracle.peek())
print('')

for feed_c in feeders:
    feeder_cl = RDOCPriceFeed(connection_manager,
                              contract_address=feed_c[0],
                              contract_address_moc_medianizer=oracle_address)

    print("Price Feeder: {0}".format(feed_c[1]))
    print("===============")
    print('Address: {0}'.format(feed_c[0]))
    print('Price: {0}'.format(feeder_cl.peek()))
    if int(oracle.indexes(feed_c[0])) > 0:
        print('Enabled: True')
    else:
        print('Enabled: False')
    print('')
