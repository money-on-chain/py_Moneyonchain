from moneyonchain.manager import ConnectionManager
from moneyonchain.governance import MoCStopper
from moneyonchain.moc import MoC

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


network = 'mocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract_moc = MoC(connection_manager)
contract_stopper = MoCStopper(connection_manager)

print("Paused: {0}".format(contract_moc.paused()))
print("Stoppable: {0}".format(contract_moc.stoppable()))
print("Stopper: {0}".format(contract_moc.stopper()))