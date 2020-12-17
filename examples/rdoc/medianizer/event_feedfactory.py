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
from_block = 568216  # from block start
to_block = 1446334  # block end or 0 to last block
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
'blockNumber': 2335154, 
'timestamp': '2020-05-07 15:51:43', 
'sender': '0xFaFdfc8aa79114bF45cC5db630B92318878cAac6', 
'feed': '0xBEd51D83CC4676660e3fc3819dfAD8238549B975'
}
]


[{'blockNumber': 2112308, 'timestamp': '2020-02-13 15:35:56', 'sender': '0x27a3074Db95Ec5f6a0E73DC41a4859F48990e841', 
        'feed': '0x4B6a4151D59b30a09C3565c17d83176cfAea6474'}, 
{'blockNumber': 2122562, 'timestamp': '2020-02-17 13:47:07', 'sender': '0xE24b5147a003A57414E8757Ddbf7D7A1c53e9e32', 
         'feed': '0x461750b4824b14c3d9b7702bC6fBB82469082b23'}, 
{'blockNumber': 2235020, 'timestamp': '2020-03-31 12:09:20', 'sender': '0xaa0E3753aDA1fB85016c8C611C0573452c587208', 
         'feed': '0x94446fA55c7740Df3494804424734721B3Ea0354'}, 
{'blockNumber': 2335154, 'timestamp': '2020-05-07 15:51:43', 'sender': '0xFaFdfc8aa79114bF45cC5db630B92318878cAac6', 
         'feed': '0xBEd51D83CC4676660e3fc3819dfAD8238549B975'}]



[{'blockNumber': 568222, 'timestamp': '2020-01-28 14:08:57', 'sender': '0xC67D9EE30d2119A384E02de568BE80fe785074Ba', 
     'feed': '0x462D7082F3671a3BE160638Be3f8C23Ca354F48A'}, 
 {'blockNumber': 700193, 'timestamp': '2020-03-19 08:19:39', 'sender': '0x41054126325E8181b8A3F7504cE68305dF51E875', 
     'feed': '0xE0A3dce741b7EaD940204820B78E7990a136EAC1'}, 
 {'blockNumber': 825873, 'timestamp': '2020-05-05 10:22:30', 'sender': '0xe127cB398f4f37E126Fa7F7af7a91b1D260eBd78', 
     'feed': '0xFFF8e36C9e9660a88CD16A215338190AaDbB4F50'}]

"""