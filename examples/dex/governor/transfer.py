"""
Transfer ownership governor control
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.governance import DEXGovernor

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')

network = 'dexMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract = DEXGovernor(connection_manager)

# New owner
new_owner = '0xC61820bFB8F87391d62Cd3976dDc1d35e0cf7128'

tx_hash, tx_receipt = contract.transfer_ownership(new_owner)

if tx_receipt:
    print("Successfully transfer ownership to : {new_owner}".format(new_owner=new_owner))
else:
    print("Error changing governance")

"""
Connecting to dexMainnet...
Connected: True
Successfully transfer ownership to : 0xC61820bFB8F87391d62Cd3976dDc1d35e0cf7128
2020-11-24 09:07:03 root         INFO     Successfully transfer ownership to: 0xC61820bFB8F87391d62Cd3976dDc1d35e0cf7128 in Block [2888710] Hash: [0x6dde90fa93bcd4d1753b4457b0f085a499310474cb25de0c22918f7b4485afec] Gas used: [32475] From: [0xB1ef062C364750DeECdCaCBf7190ed591B7a0Bfe]

"""