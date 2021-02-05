"""
"""

import datetime

from moneyonchain.networks import NetworkManager
from moneyonchain.networks import chain
from moneyonchain.moc import MoCExchangeRiskProMint, MoCExchangeRiskProRedeem, MoCExchangeRiskProxMint, \
    MoCExchangeRiskProxRedeem, MoCExchangeStableTokenMint, MoCExchangeStableTokenRedeem, \
    MoCExchangeFreeStableTokenRedeem
from moneyonchain.rdoc import RDOCMoCState


connection_network = 'rskMainnetPublic'
config_network = 'rdocMainnet'

# init network manager
# connection network is the brownie connection network
# config network is our enviroment we want to connect
network_manager = NetworkManager(
    connection_network=connection_network,
    config_network=config_network)

# Connect to network
network_manager.connect()

list_transactions = [
    '0x80253cd80bd7211e9fc2247aa612786d900ef89fb1b83752dce73212b1bfe5c2'
]

moc_state = RDOCMoCState(network_manager).from_abi()

l_actions = list()
for tx_id in list_transactions:
    tx_receipt = chain.get_transaction(tx_id)
    tx_receipt.info()

    d_event = dict()
    d_event['transactionHash'] = tx_receipt.txid
    d_event['blockNumber'] = tx_receipt.block_number
    d_event['timestamp'] = datetime.datetime.fromtimestamp(tx_receipt.timestamp)

    for tx_event in tx_receipt.events:
        if 'RiskProMint' in tx_event:
            event = MoCExchangeRiskProMint(tx_event['RiskProMint'])
            d_event['function'] = 'RiskProMint'
            d_event['account'] = event.formatted()['account']
            d_event['amount'] = event.formatted()['amount']
            d_event['reservePrice'] = event.formatted()['reservePrice']
        elif 'RiskProRedeem' in tx_event:
            event = MoCExchangeRiskProRedeem(tx_event['RiskProRedeem'])
            d_event['function'] = 'MoCExchangeRiskProRedeem'
            d_event['account'] = event.formatted()['account']
            d_event['amount'] = event.formatted()['amount']
            d_event['reservePrice'] = event.formatted()['reservePrice']
        elif 'RiskProxMint' in tx_event:
            event = MoCExchangeRiskProxMint(tx_event['RiskProxMint'])
            d_event['function'] = 'MoCExchangeRiskProxMint'
            d_event['account'] = event.formatted()['account']
            d_event['amount'] = event.formatted()['amount']
            d_event['reservePrice'] = event.formatted()['reservePrice']
        elif 'RiskProxRedeem' in tx_event:
            event = MoCExchangeRiskProxRedeem(tx_event['RiskProxRedeem'])
            d_event['function'] = 'RiskProxRedeem'
            d_event['account'] = event.formatted()['account']
            d_event['amount'] = event.formatted()['amount']
            d_event['reservePrice'] = event.formatted()['reservePrice']
        elif 'StableTokenMint' in tx_event:
            event = MoCExchangeStableTokenMint(tx_event['StableTokenMint'])
            d_event['function'] = 'StableTokenMint'
            d_event['account'] = event.formatted()['account']
            d_event['amount'] = event.formatted()['amount']
            d_event['reservePrice'] = event.formatted()['reservePrice']
        elif 'StableTokenRedeem' in tx_event:
            event = MoCExchangeStableTokenRedeem(tx_event['StableTokenRedeem'])
            d_event['function'] = 'StableTokenRedeem'
            d_event['account'] = event.formatted()['account']
            d_event['amount'] = event.formatted()['amount']
            d_event['reservePrice'] = event.formatted()['reservePrice']
        elif 'FreeStableTokenRedeem' in tx_event:
            event = MoCExchangeFreeStableTokenRedeem(tx_event['FreeStableTokenRedeem'])
            d_event['function'] = 'FreeStableTokenRedeem'
            d_event['account'] = event.formatted()['account']
            d_event['amount'] = event.formatted()['amount']
            d_event['reservePrice'] = event.formatted()['reservePrice']
        else:
            continue

    if 'function' not in d_event:
        continue

    d_event['reserves'] = moc_state.rbtc_in_system(block_identifier=tx_receipt.block_number)

    l_actions.append(d_event)




tx_hash = tx_receipt.txid
print(tx_hash)

print(tx_receipt.events)
print(tx_receipt.logs)
print(tx_receipt.sender)
print(tx_receipt.receiver)
print(tx_receipt.fn_name)
print(tx_receipt.contract_name)
print(tx_receipt.value)
print(tx_receipt.gas_price)
print(tx_receipt.confirmations)



# finally disconnect from network
network_manager.disconnect()
