"""
Price feeder verification. Test if pricefeeder is working and sending prices.
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoCMedianizer, \
    PriceFeed

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()


network = 'mocMainnet2'
connection_manager = ConnectionManager(network=network)
log.info("Connecting to %s..." % network)
log.info("Connected: {conectado}".format(conectado=connection_manager.is_connected))


oracle_address = '0x7B19bb8e6c5188eC483b784d6fB5d807a77b21bF'
feeder_address_1 = '0xfE05Ee3d651670F807Db7dD56e1E0FCBa29B234a'
feeder_address_2 = '0xE94007E81412eDfdB87680F768e331E8c691f0e1'

oracle = MoCMedianizer(connection_manager,
                       contract_address=oracle_address)

feeder_1 = PriceFeed(connection_manager,
                     contract_address=feeder_address_1,
                     contract_address_moc_medianizer=oracle_address)

print("Oracle price:")
print(oracle.peek())

print("Price Feeder 1")
print("===============")

print("Price feeder price and have value (if have value if false, no price setted) :")
print(feeder_1.peek())

print("Index > 0 is active price feeder")
print(oracle.indexes(feeder_address_1))

feeder_2 = PriceFeed(connection_manager,
                     contract_address=feeder_address_2,
                     contract_address_moc_medianizer=oracle_address)


print("Price Feeder 2")
print("===============")

print("Price feeder price and have value (if have value if false, no price setted) :")
print(feeder_2.peek())

print("Index > 0 is active price feeder")
print(oracle.indexes(feeder_address_2))
