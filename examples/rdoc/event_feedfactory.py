import datetime
from web3 import Web3
from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCFeedFactory

network = 'rdocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_feedfactory = RDOCFeedFactory(connection_manager)

events_functions = ['Created']
hours_delta = 0
from_block = 820888  # from block start
to_block = 825888  # block end or 0 to last block
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
        'blockNumber': 825873, 
        'timestamp': '2020-05-05 10:22:30', 
        'sender': '0xe127cB398f4f37E126Fa7F7af7a91b1D260eBd78', 
        'feed': '0xFFF8e36C9e9660a88CD16A215338190AaDbB4F50'
    }
]

"""