from moneyonchain.manager import ConnectionManager
from moneyonchain.governance import RDOCGoverned

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


contact_address = connection_manager.options['networks'][network]['addresses']['CommissionSplitter']
contract = RDOCGoverned(connection_manager, contract_address=contact_address)
print(contract.governor())

governor_address = connection_manager.options['networks'][network]['addresses']['governor']
tx_hash, tx_receipt = contract.initialize(governor_address)
if tx_receipt:
    print("Sucessfully initialized")
else:
    print("Error initialized")


"""
Connecting to rdocMainnet...
Connected: True
0xC61F0392d5170214b5D93C0BC4c4354163aBC1f7
2020-05-05 17:37:00 root         INFO     Successfully initialized in Block [2329974] Hash: [0xeea7be5c47cdc21b5064fde98fa6e572be8625ebf49af8bc2441541fff77fdb4] Gas used: [55451] From: [0x27a3074Db95Ec5f6a0E73DC41a4859F48990e841]
Sucessfully initialized
"""