"""

Dex Events

"""

import time
import csv
import os

from moneyonchain.networks import NetworkManager
from moneyonchain.tex import MoCDecentralizedExchange
#from moneyonchain.events import DEXBuyerMatch, DEXSellerMatch, DEXExpiredOrderProcessed

connection_network='rskTesnetPublic'
config_network = 'dexTestnet'

# init network manager
# connection network is the brownie connection network
# config network is our enviroment we want to connect
network_manager = NetworkManager(
    connection_network=connection_network,
    config_network=config_network)

# run install() if is the first time and you want to install
# networks connection from brownie
# network_manager.install()

# Connect to network
network_manager.connect()

print("Starting to import events from contract...")
start_time = time.time()

# MoCDecentralizedExchange.sol
dex = MoCDecentralizedExchange(network_manager).from_abi()

events_functions = ['BuyerMatch']
hours_delta = 0
from_block = 1333853  # from block start
to_block = 1333953  # block end or 0 to last block
l_events = dex.logs_from(events_functions, from_block, to_block, block_steps=2880)

print(l_events)

# BuyerMatch

# l_historic_data = list()
# if 'BuyerMatch' in l_events:
#     if l_events['BuyerMatch']:
#         count = 0
#         for e_event_block in l_events['BuyerMatch']:
#             for e_event in e_event_block:
#                 tx_event = DEXBuyerMatch(connection_manager, e_event)
#                 l_historic_data.append(tx_event.row())
#
# # Write list to CSV File
#
# if l_historic_data:
#     columns = DEXBuyerMatch.columns()
#     path_file = '{0}_buyer_match_{1}_{2}.csv'.format(network, from_block, to_block)
#     with open(os.path.join('csv', path_file), 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         writer.writerow(columns)
#
#         count = 0
#         for historic_data in l_historic_data:
#             count += 1
#             writer.writerow(historic_data)

# finally disconnect from network
network_manager.disconnect()
