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

print("Bitpro rate: {0}".format(moc_inrate.bitpro_rate()))
print("Bitpro interest blockspan: {0}".format(moc_inrate.bitpro_interest_blockspan()))
print("Commission rate: {0}".format(moc_inrate.commision_rate()))
print("last_bitpro_interest_block: {0}".format(moc_inrate.last_bitpro_interest_block()))
print("daily_enabled: {0}".format(moc_inrate.daily_enabled()))
print("daily_inrate: {0}".format(moc_inrate.daily_inrate()))
print("spot_inrate: {0}".format(moc_inrate.spot_inrate()))
print("commission_address: {0}".format(moc_inrate.commission_address()))
print("last_daily_pay: {0}".format(moc_inrate.last_daily_pay()))
print("bitpro_interest_address: {0}".format(moc_inrate.bitpro_interest_address()))
print("is_bitpro_interest_enabled: {0}".format(moc_inrate.is_bitpro_interest_enabled()))

