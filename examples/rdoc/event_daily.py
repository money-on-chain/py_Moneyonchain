import datetime
from web3 import Web3
from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoCInrate, RDOCMoC

network = 'rdocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_inrate = RDOCMoCInrate(connection_manager)

events_functions = ['InrateDailyPay']
hours_delta = 0
from_block = 830859  # from block start
to_block = 844859  # block end or 0 to last block
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
{'blockNumber': 833242, 'timestamp': '2020-05-08 05:43:34', 'amount': Decimal('0.062581989356276525'), 'daysToSettlement': 17, 'nReserveBucketC0': Decimal('2367.478205379475749698')}, 
{'blockNumber': 836128, 'timestamp': '2020-05-09 08:18:04', 'amount': Decimal('0.062581989356276525'), 'daysToSettlement': 16, 'nReserveBucketC0': Decimal('2367.427494777035258405')}, 
{'blockNumber': 839013, 'timestamp': '2020-05-10 10:39:04', 'amount': Decimal('0.062581989356276525'), 'daysToSettlement': 15, 'nReserveBucketC0': Decimal('2367.376786601284723118')}, 
{'blockNumber': 841897, 'timestamp': '2020-05-11 11:57:42', 'amount': Decimal('0.062581989356276525'), 'daysToSettlement': 14, 'nReserveBucketC0': Decimal('2370.472025514650366083')}, 
{'blockNumber': 844803, 'timestamp': '2020-05-12 09:49:14', 'amount': Decimal('0.062581989356276525'), 'daysToSettlement': 13, 'nReserveBucketC0': Decimal('2370.421171646839272184')}]


"""