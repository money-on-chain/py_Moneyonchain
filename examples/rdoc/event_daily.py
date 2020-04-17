import datetime
from web3 import Web3
from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoCInrate, RDOCMoC

network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_inrate = RDOCMoCInrate(connection_manager)

events_functions = ['InrateDailyPay']
hours_delta = 0
from_block = 2270000  # from block start
to_block = 2280720  # block end or 0 to last block
l_events = moc_inrate.logs_from(events_functions, from_block, to_block, block_steps=2880)

l_info = list()
if 'InrateDailyPay' in l_events:
    if l_events['InrateDailyPay']:
        count = 0
        for e_event_block in l_events['InrateDailyPay']:
            for e_event in e_event_block:

                count += 1
                ts = connection_manager.block_timestamp(e_event['blockNumber'])
                dt = ts - datetime.timedelta(hours=hours_delta)
                d_timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")

                d_info = dict()
                d_info['blockNumber'] = e_event['blockNumber']
                d_info['timestamp'] = d_timestamp
                d_info['amount'] = Web3.fromWei(e_event['args']['amount'], 'ether')
                d_info['daysToSettlement'] = e_event['args']['daysToSettlement']
                d_info['nReserveBucketC0'] = Web3.fromWei(e_event['args']['nReserveBucketC0'], 'ether')

                l_info.append(d_info)

print(l_info)
"""
[
{'blockNumber': 2272797, 'timestamp': '2020-04-14 12:44:43', 'amount': Decimal('1.478432015673136349'), 'daysToSettlement': 16, 'nReserveBucketC0': Decimal('19422.062734555368925119')}, 
{'blockNumber': 2275680, 'timestamp': '2020-04-15 13:39:32', 'amount': Decimal('1.478432015673136349'), 'daysToSettlement': 15, 'nReserveBucketC0': Decimal('39520.756960735107326976')}, 
{'blockNumber': 2280716, 'timestamp': '2020-04-17 09:38:37', 'amount': Decimal('5.58735204719715373'), 'daysToSettlement': 14, 'nReserveBucketC0': Decimal('64050.044705172883757847')}]


"""