import datetime
from web3 import Web3
from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCFeedFactory

network = 'rdocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract_address_feedfactory = '0xbB26D11bd2a9F2274cD1a8E571e5A352816acaEA'
moc_feedfactory = RDOCFeedFactory(connection_manager, contract_address=contract_address_feedfactory)

events_functions = ['Created']
hours_delta = 0
from_block = 863000  # from block start
to_block = 863851  # block end or 0 to last block
l_events = moc_feedfactory.logs_from(events_functions, from_block, to_block, block_steps=2880)

l_info = list()
if 'Created' in l_events:
    if l_events['Created']:
        count = 0
        for e_event_block in l_events['Created']:
            for e_event in e_event_block:

                count += 1
                ts = connection_manager.block_timestamp(e_event['blockNumber'])
                dt = ts - datetime.timedelta(hours=hours_delta)
                d_timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")

                d_info = dict()
                d_info['blockNumber'] = e_event['blockNumber']
                d_info['timestamp'] = d_timestamp
                d_info['sender'] = e_event['args']['sender']
                d_info['feed'] = e_event['args']['feed']

                l_info.append(d_info)

print(l_info)
"""
[
    {
        'blockNumber': 863840, 
        'timestamp': '2020-05-19 09:33:37', 
        'sender': '0x950C18fa33D079B01Ff7b4Fc18Ec830643CBf9eC', 
        'feed': '0x0c8F4e12820CA09a9Fba5E3a05e695e8E4C2bf0C'
    }
]

"""