from moneyonchain.manager import ConnectionManager
from moneyonchain.commission import RDOCCommissionSplitter

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


network = 'rdocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

splitter = RDOCCommissionSplitter(connection_manager)

tx_hash, tx_receipt = splitter.split()
if tx_receipt:
    print("Sucessfully initialized")
else:
    print("Error initialized")


"""
Connecting to rdocTestnetAlpha...
Connected: True
2020-05-05 17:06:30 root         INFO     Successfully split executed in Block [826604] Hash: [0x5b519c9f03fc1efef27bedb2c4565761773d46c599ddfd0f7f2a32726520e90c] Gas used: [108615] From: [0xa8F94d08d3d9C045fE0b86a953DF39b14206153c]
Sucessfully initialized
"""