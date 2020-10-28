"""
This script list all of the proxy and implementation addresses of the contracts
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoC, MoCConverter, MoCSettlement, MoCExchange, MoCInrate, MoCBurnout, MoCBProxManager, \
    MoCState, MoCConnector, MoCMedianizer
from moneyonchain.token import DoCToken, BProToken, MoCToken


network = 'mocMainnet2'
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

# MoCToken
contract = MoCState(connection_manager).moc_token
count += 1
line = '| {0} | {1}  | {2}  | {3} |'.format(count, 'MoCToken', '',
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

"""
Connecting to mocMainnet2...
Connected: True

| Nº     | Contract                      | Address Proxy                  | Address Implementation           |
| :---:  | :---------------------------- | ----------------------------   | -------------------------------- |

| 1 | MOC  | 0xf773B590aF754D597770937Fa8ea7AbDf2668370  | 0xba5F92D00b932c3b57457AbCa7D2DAa625906054 |
| 2 | MoCConnector  | 0xcE2A128cC73e5d98355aAfb2595647F2D3171Faa  | 0x437221B50b0066186e58412B0BA940441A7B7df5 |
| 3 | MoCState  | 0xb9C42EFc8ec54490a37cA91c423F7285Fa01e257  | 0x08817f585A9F2601fB7bFFfE913Dac305Aaf2dDd |
| 4 | MoCConverter  | 0x0B7507032f140f5Ae5C0f1dA2251a0cd82c82296  | 0x0CFc08501780bc02Ca4c16324D22F32511B309a9 |
| 5 | MoCSettlement  | 0x609dF03D8a85eAffE376189CA7834D4C35e32F22  | 0xe3abCE2B0eE0D7eA48a5bcD0442D5505aE5B6334 |
| 6 | MoCExchange  | 0x6aCb83bB0281FB847b43cf7dd5e2766BFDF49038  | 0x785814724324C63ec52e6675C899508E74850046 |
| 7 | MoCInrate  | 0xc0f9B54c41E3d0587Ce0F7540738d8d649b0A3F3  | 0x56e327FA971572828f846BE9E37FB850e5852822 |
| 8 | MoCBurnout  | 0xE69fB8C8fE9dCa08350AF5C47508f3E688D0CDd1  | 0x1d1BeE3A56C01Cae266BfB62dD6FeF53e3f5E508 |
| 9 | MoCBProxManager  | 0xC4fBFa2270Be87FEe5BC38f7a1Bb6A9415103b6c  | 0xee35b51EdF623533A83D3aEf8f1518ff67da4e89 |
| 10 | DoCToken  |   | 0xe700691dA7b9851F2F35f8b8182c69c53CcaD9Db |
| 11 | BProToken  |   | 0x440CD83C160De5C96Ddb20246815eA44C7aBBCa8 |
| 12 | MoCMedianizer  |   | 0x7B19bb8e6c5188eC483b784d6fB5d807a77b21bF |
"""