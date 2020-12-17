"""


"""

import time
import csv

from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoCExchange, RDOCMoC
from moneyonchain.events import MoCExchangeStableTokenRedeem

network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Starting to import events from contract...")
start_time = time.time()

moc_Exchange_contract = RDOCMoCExchange(connection_manager)

events_functions = ['StableTokenRedeem']
hours_delta = 0
from_block = 2923912  # from block start
to_block = 2929266  # block end or 0 to last block
l_events = moc_Exchange_contract.logs_from(events_functions, from_block, to_block, block_steps=2880)


l_historic_data = list()
if 'StableTokenRedeem' in l_events:
    if l_events['StableTokenRedeem']:
        count = 0
        for e_event_block in l_events['StableTokenRedeem']:
            for e_event in e_event_block:
                tx_event = MoCExchangeStableTokenRedeem(connection_manager, e_event)
                l_historic_data.append(tx_event.row())

# Write list to CSV File

if l_historic_data:
    columns = MoCExchangeStableTokenRedeem.columns()
    path_file = '{0}_stable_redeem_{1}_{2}.csv'.format(network, from_block, to_block)
    with open(path_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(columns)

        count = 0
        for historic_data in l_historic_data:
            count += 1
            writer.writerow(historic_data)

duration = time.time() - start_time
print("Getting events from MOC done! Succesfull!! Done in {0} seconds".format(duration))
