"""
This script list all of the proxy and implementation addresses of the contracts
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoC, MoCConverter, MoCSettlement, MoCExchange, MoCInrate, MoCBurnout, MoCBProxManager, \
    MoCState, MoCConnector, MoCMedianizer
from moneyonchain.token import DoCToken, BProToken


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_main = MoC(connection_manager)
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
contract = MoCConnector(connection_manager)
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCConnector', contract.address(),
                                            contract.implementation())
lines.append(line)


# MoCState
count += 1
contract = MoCState(connection_manager)
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCState', addresses['MoCState'],
                                            contract.implementation())
lines.append(line)

# MoCConverter
contract = MoCConverter(connection_manager)
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCConverter', addresses['MoCConverter'],
                                            contract.implementation())
lines.append(line)

# MoCSettlement
contract = MoCSettlement(connection_manager)
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCSettlement', addresses['MoCSettlement'],
                                            contract.implementation())
lines.append(line)

# MoCExchange
contract = MoCExchange(connection_manager)
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCExchange', addresses['MoCExchange'],
                                            contract.implementation())
lines.append(line)

# MoCInrate
contract = MoCInrate(connection_manager)
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCInrate', addresses['MoCInrate'],
                                            contract.implementation())
lines.append(line)


# MoCBurnout
contract = MoCBurnout(connection_manager)
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCBurnout', addresses['MoCBurnout'],
                                            contract.implementation())
lines.append(line)

# MoCBProxManager
contract = MoCBProxManager(connection_manager)
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCBProxManager', addresses['MoCBProxManager'],
                                            contract.implementation())
lines.append(line)

# DoCToken
contract = DoCToken(connection_manager)
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'DoCToken', '',
                                            contract.address())
lines.append(line)


# BProToken
contract = BProToken(connection_manager)
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'BProToken', '',
                                            contract.address())
lines.append(line)


# Oracle
contract = MoCMedianizer(connection_manager)
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCMedianizer', '',
                                            contract.address())
lines.append(line)


# finally print
print(md_header)
print('\n'.join(lines))
