from moneyonchain.manager import ConnectionManager
from moneyonchain.commission import RDOCCommissionSplitter

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

splitter = RDOCCommissionSplitter(connection_manager)

tx_hash, tx_receipt = splitter.split()
if tx_receipt:
    print("Sucessfully splited")
else:
    print("Error splited")


"""
Connecting to rdocTestnetAlpha...
Connected: True
2020-05-05 17:06:30 root         INFO     Successfully split executed in Block [826604] Hash: [0x5b519c9f03fc1efef27bedb2c4565761773d46c599ddfd0f7f2a32726520e90c] Gas used: [108615] From: [0xa8F94d08d3d9C045fE0b86a953DF39b14206153c]
Sucessfully initialized

Connecting to rdocTestnet...
Connected: True
2020-05-05 17:23:43 root         INFO     Successfully split executed in Block [826635] Hash: [0xd5fb6ee6a9d3a3161f9c566f97d17f71c676c0df121279198dc16bcd4256fca5] Gas used: [123615] From: [0xa8F94d08d3d9C045fE0b86a953DF39b14206153c]
Sucessfully initialized

"""