"""

This pause MOC Contract

"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.governance import RDOCStopper
from moneyonchain.rdoc import RDOCMoC

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


contract_moc = RDOCMoC(connection_manager)
contract_stopper = RDOCStopper(connection_manager)

contract_to_pause = contract_moc.address()
tx_hash, tx_receipt = contract_stopper.pause(contract_to_pause)
if tx_receipt:
    print("Stop Contract Address: {address} successfully!".format(address=contract_to_pause))
else:
    print("Error Stopping contract")


"""
"""