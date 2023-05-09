"""
Price feeder verification. Test if pricefeeder is working and sending prices.
"""
import datetime
from tabulate import tabulate
from decimal import Decimal

from moneyonchain.networks import network_manager
from moneyonchain.medianizer import RDOCMoCMedianizer, \
    RDOCPriceFeed

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()


connection_network = 'rskMainnetPublic'
config_network = 'rdocMainnet'

# connection network is the brownie connection network
# config network is our enviroment we want to connect
network_manager.connect(connection_network=connection_network, config_network=config_network)


oracle_address = '0x504EfCadFB020d6bBaeC8a5c5BB21453719d0E00'
feeders = [('0x461750b4824b14c3d9b7702bC6fBB82469082b23', '# MOC'),
           ('0xBEd51D83CC4676660e3fc3819dfAD8238549B975', '# ROC')]

oracle = RDOCMoCMedianizer(network_manager,
                           contract_address=oracle_address).from_abi()

feeder_moc = RDOCPriceFeed(network_manager,
                           contract_address=feeders[0][0],
                           contract_address_moc_medianizer=oracle_address).from_abi()

feeder_roc = RDOCPriceFeed(network_manager,
                           contract_address=feeders[1][0],
                           contract_address_moc_medianizer=oracle_address).from_abi()

range_blocks = [5285307, 5285901]
block_skip = 1

display_table = []
titles = ['blockNumber', 'Price Oracle', 'Price Feeder MOC', 'Price Feeder ROC', 'Timestamp']

ora_prev = None
moc_prev = None
roc_prev = None

for block_n in range(range_blocks[0], range_blocks[1], block_skip):

    print("Indexing Block {0} / {1}".format(block_n, range_blocks[1]))

    ts = network_manager.block_timestamp(block_n)
    dt = ts - datetime.timedelta(hours=0)
    d_timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")

    ora = oracle.peek(block_identifier=block_n)[0]
    moc = feeder_moc.peek(block_identifier=block_n)[0]
    roc = feeder_roc.peek(block_identifier=block_n)[0]

    if ora_prev != ora:
        ora_prev = ora
    else:
        ora = None

    if moc_prev != moc:
        moc_prev = moc
    else:
        moc = None

    if roc_prev != roc:
        roc_prev = roc
    else:
        roc = None

    display_table.append([
        block_n,
        ora,
        moc,
        roc,
        d_timestamp])

print(tabulate(display_table, headers=titles, tablefmt="pipe"))
with open('out.txt', 'w') as f:
    print(tabulate(display_table, headers=titles, tablefmt="presto"), file=f)

# finally disconnect from network
network_manager.disconnect()
