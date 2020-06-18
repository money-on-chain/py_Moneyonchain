from moneyonchain.manager import ConnectionManager
from moneyonchain.commission import RDOCCommissionSplitter

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


Connecting to rdocMainnet...
Connected: True
Sucessfully splited
2020-05-06 14:09:41 root         INFO     Successfully split executed in Block [2332266] Hash: [0x6351a94fc53560c5f9b34f014d03aa023264d257ee1856fd05b4d29912c2b470] Gas used: [113893] From: [0x27a3074Db95Ec5f6a0E73DC41a4859F48990e841]


Connecting to rdocMainnet...
Connected: True
Sucessfully splited
2020-06-10 17:52:31 root         INFO     Successfully split executed in Block [2432125] Hash: [0xcd7bcf8bc4402f146967754748fa205335f89bdc24f9eef1faaf72bfbc799770] Gas used: [113893] From: [0x27a3074Db95Ec5f6a0E73DC41a4859F48990e841]


"""