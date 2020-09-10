import json
import logging
import logging.config

from moneyonchain.manager import ConnectionManager
from moneyonchain.commission import CommissionSplitter


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


def options_from_settings(filename='settings.json'):
    """ Options from file settings.json """

    with open(filename) as f:
        config_options = json.load(f)

    return config_options


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

# load settings from file
settings = options_from_settings()

splitter = CommissionSplitter(connection_manager, contract_address=settings[network]['CommissionSplitter'])

governor_address = connection_manager.options['networks'][network]['addresses']['governor']
moc_address = connection_manager.options['networks'][network]['addresses']['MoC']
comission_address = settings[network]['CommissionAddress']
moc_proportion = settings[network]['MocProportion']

print("Initializing contract with this parameters:")
print("Network: {0}".format(network))
print("MoC Address: {0}".format(moc_address))
print("Commission Address: {0}".format(comission_address))
print("Moc Proportion: {0}".format(moc_proportion))
print("Governor Address: {0}".format(governor_address))

tx_hash, tx_receipt = splitter.initialize(moc_address, comission_address, moc_proportion, governor_address)
if tx_receipt:
    print("Sucessfully initialized")
else:
    print("Error initialized")

"""
Connecting to mocTestnetAlpha...
Connected: True
Sucessfully initialized
2020-09-09 14:39:28 root         INFO     Successfully initialized executed in Block [1164144] Hash: [0x6636d65fe55879a7a5ed8f103f5f2fc9cb13df7144eefca7300a61e09e022b12] Gas used: [29540] From: [0xaB242E50E95C2F539242763A4ed5DB1AEe5CE461]

Connecting to mocTestnet...
Connected: True
Initializing contract with this parameters:
Network: mocTestnet
MoC Address: 0x2820f6d4D199B8D8838A4B26F9917754B86a0c1F
Commission Address: 0xf69287F5Ca3cC3C6d3981f2412109110cB8af076
Moc Proportion: 200000000000000000
Governor Address: 0x4eAC4518e81B3A5198aADAb998D2610B46aAA609
Sucessfully initialized
2020-09-10 15:01:13 root         INFO     Successfully initialized executed in Block [1166941] Hash: [0x26a63e41f351d2261fb0b69fcb7a46a88fdbce0abd666f38fc7623b15caf67c4] Gas used: [136674] From: [0xaB242E50E95C2F539242763A4ed5DB1AEe5CE461]


"""