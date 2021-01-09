from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import MocMakeStoppableChanger

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


network = 'mocMainnet2'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract = MocMakeStoppableChanger(connection_manager)
stoppable = True

if network in ['mocTestnetAlpha']:
    execute_change = True
else:
    execute_change = False

tx_hash, tx_receipt = contract.constructor(stoppable=stoppable, execute_change=execute_change)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")


"""

"""