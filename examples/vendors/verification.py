"""
This script list all of the proxy and implementation addresses of the contracts
"""

from moneyonchain.networks import NetworkManager
from moneyonchain.moc import MoCBProxManager
from moneyonchain.moc_vendors import VENDORSMoC, VENDORSMoCConverter, VENDORSMoCSettlement, VENDORSMoCExchange, \
    VENDORSMoCInrate, VENDORSMoCState, VENDORSMoCConnector
from moneyonchain.medianizer import MoCMedianizer
from moneyonchain.tokens import DoCToken, BProToken


connection_network = 'rskTesnetPublic'
config_network = 'mocTestTyD'

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


moc_main = VENDORSMoC(network_manager).from_abi()
addresses = moc_main.connector_addresses()

count = 0
lines = list()

md_header = '''
| Nº     | Contract                      | Address Proxy                  | Address Implementation           |
| :---:  | :---------------------------- | ----------------------------   | -------------------------------- |
'''

# MOC
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MOC', addresses['MoC'], moc_main.implementation())
lines.append(line)

# MoCConnector
count += 1
contract = VENDORSMoCConnector(network_manager).from_abi()
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCConnector', contract.address(),
                                            contract.implementation())
lines.append(line)


# MoCState
count += 1
contract = VENDORSMoCState(network_manager).from_abi()
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCState', addresses['MoCState'],
                                            contract.implementation())
lines.append(line)

# MoCConverter
contract = VENDORSMoCConverter(network_manager).from_abi()
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCConverter', addresses['MoCConverter'],
                                            contract.implementation())
lines.append(line)

# MoCSettlement
contract = VENDORSMoCSettlement(network_manager).from_abi()
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCSettlement', addresses['MoCSettlement'],
                                            contract.implementation())
lines.append(line)

# MoCExchange
contract = VENDORSMoCExchange(network_manager).from_abi()
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCExchange', addresses['MoCExchange'],
                                            contract.implementation())
lines.append(line)

# MoCInrate
contract = VENDORSMoCInrate(network_manager).from_abi()
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCInrate', addresses['MoCInrate'],
                                            contract.implementation())
lines.append(line)


# MoCBProxManager
contract = MoCBProxManager(network_manager).from_abi()
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCBProxManager', addresses['MoCBProxManager'],
                                            contract.implementation())
lines.append(line)

# DoCToken
contract = DoCToken(network_manager).from_abi()
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'DoCToken', '',
                                            contract.address())
lines.append(line)


# BProToken
contract = BProToken(network_manager).from_abi()
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'BProToken', '',
                                            contract.address())
lines.append(line)


# Oracle
contract = MoCMedianizer(network_manager).from_abi()
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCMedianizer', '',
                                            contract.address())
lines.append(line)


# finally print
print(md_header)
print('\n'.join(lines))

"""

"""