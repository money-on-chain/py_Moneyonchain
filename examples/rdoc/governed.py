from moneyonchain.manager import ConnectionManager
from moneyonchain.governance import RDOCGoverned

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


network = 'rdocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


contact_address = connection_manager.options['networks'][network]['addresses']['CommissionSplitter']
contract = RDOCGoverned(connection_manager, contract_address=contact_address)
print(contract.governor())

governor_address = connection_manager.options['networks'][network]['addresses']['governor']
tx_hash, tx_receipt = contract.initialize(governor_address)
if tx_receipt:
    print("Sucessfully initialized")
else:
    print("Error initialized")
