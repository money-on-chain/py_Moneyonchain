from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import RDOCPriceProviderChanger

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


contract = RDOCPriceProviderChanger(connection_manager)

#price_provider = '0x2B54819531B7126bDEE2CeFDD9c5342d6c307595'
#price_provider = '0x01a165cC33Ff8Bd0457377379962232886be3DE6'
#price_provider = '0x9d4b2c05818A0086e641437fcb64ab6098c7BbEc'
#price_provider = '0x9315AFD6aEc0bb1C1FB3fdcdC2E43797B0A61853'
##price_provider = '0xb856Ca7c722cfb202D81c55DC7925e02ed3f0A2F'
#price_provider = '0x9d4b2c05818A0086e641437fcb64ab6098c7BbEc'
price_provider = '0x987ccC60c378a61d167B6DD1EEF7613c6f63938f'
tx_hash, tx_receipt = contract.constructor(price_provider, execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""

"""