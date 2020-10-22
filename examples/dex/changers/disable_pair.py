"""
DISABLE PAIRS

[ [ '0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0',
    '0x4dA7997A819bb46B6758B9102234c289dD2Ad3bf',
    '1000000000000000000',
    '1000000000000000000' ],
  [ '0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0',
    '0x840871cbb73dC94dcb11b2CEA963553Db71a95b7',
    '1000000000000000000',
    '1000000000000000000' ],
  [ '0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0',
    '0xA274d994F698Dd09256674960d86aBa22C086669',
    '1000000000000000000',
    '1000000000000000000' ],
  [ '0xA274d994F698Dd09256674960d86aBa22C086669',
    '0x4dA7997A819bb46B6758B9102234c289dD2Ad3bf',
    '1000000000000000000',
    '1000000000000000000' ],
  [ '0xA274d994F698Dd09256674960d86aBa22C086669',
    '0x840871cbb73dC94dcb11b2CEA963553Db71a95b7',
    '1000000000000000000',
    '1000000000000000000' ] ]



"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import DexTokenPairDisabler

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract = DexTokenPairDisabler(connection_manager)

base_address = '0xC3De9F38581f83e281f260d0DdbaAc0e102ff9F8'
secondary_address = '0x23A1aA7b11e68beBE560a36beC04D1f79357f28d'

tx_hash, tx_receipt = contract.constructor(base_address,
                                           secondary_address,
                                           execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""

"""