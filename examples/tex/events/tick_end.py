"""

Dex Events

"""

import time
import csv
import os

from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import MoCDecentralizedExchange
from moneyonchain.events import DEXTickEnd

network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Starting to import events from contract...")
start_time = time.time()

# MoCDecentralizedExchange.sol
dex = MoCDecentralizedExchange(connection_manager)

events_functions = ['TickEnd']
hours_delta = 0
from_block = 1332673  # from block start
to_block = 1332700  # block end or 0 to last block
l_events = dex.logs_from(events_functions, from_block, to_block, block_steps=2880)

# TickStart

l_historic_data = list()
if 'TickEnd' in l_events:
    if l_events['TickEnd']:
        count = 0
        for e_event_block in l_events['TickEnd']:
            for e_event in e_event_block:
                tx_event = DEXTickEnd(connection_manager, e_event)
                l_historic_data.append(tx_event.row())

# Write list to CSV File

if l_historic_data:
    columns = DEXTickEnd.columns()
    path_file = '{0}_tick_end_{1}_{2}.csv'.format(network, from_block, to_block)
    with open(os.path.join('csv', path_file), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(columns)

        count = 0
        for historic_data in l_historic_data:
            count += 1
            writer.writerow(historic_data)


duration = time.time() - start_time
print("Getting events from DEX done! Succesfull!! Done in {0} seconds".format(duration))
