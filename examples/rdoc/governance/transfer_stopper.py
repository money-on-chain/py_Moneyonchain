"""
Transfer ownership stopper control
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.governance import RDOCStopper

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')

network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract = RDOCStopper(connection_manager)

# New owner
if network in ['rdocTestnetAlpha', 'rdocTestnet']:
    new_owner = '0xf69287F5Ca3cC3C6d3981f2412109110cB8af076'
else:
    new_owner = '0xC61820bFB8F87391d62Cd3976dDc1d35e0cf7128'


new_owner = '0xC61820bFB8F87391d62Cd3976dDc1d35e0cf7128'
tx_hash, tx_receipt = contract.transfer_ownership(new_owner)

if tx_receipt:
    print("Successfully transfer ownership to : {new_owner}".format(new_owner=new_owner))
else:
    print("Error changing governance")

"""

"""