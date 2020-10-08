"""

This pause MOC Contract

"""

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

contract_to_pause = contract_moc.address()
tx_hash, tx_receipt = contract_stopper.pause(contract_to_pause)
if tx_receipt:
    print("Stop Contract Address: {address} successfully!".format(address=contract_to_pause))
else:
    print("Error Stopping contract")


"""
Connecting to mocTestnetAlpha...
Connected: True
Stop Contract Address: 0x01AD6f8E884ed4DDC089fA3efC075E9ba45C9039 successfully!
2020-10-08 10:02:39 root         INFO     Successfully paused contract 0x01AD6f8E884ed4DDC089fA3efC075E9ba45C9039 in Block [1240607] Hash: [0x159193398e0981a3f91f383cfd272d372d0fffd80c0de2fa2b4cbb1bf8f29f60] Gas used: [24926] From: [0xB7d4B3c37d17D66B88da41e8A87561323A6DBDA0]
"""