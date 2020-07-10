from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoCMedianizer

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()


network = 'rdocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
log.info("Connecting to %s..." % network)
log.info("Connected: {conectado}".format(conectado=connection_manager.is_connected))

#oracle_address = '0x2B54819531B7126bDEE2CeFDD9c5342d6c307595'
#oracle_address = '0x01a165cC33Ff8Bd0457377379962232886be3DE6'
#oracle_address = '0x9d4b2c05818A0086e641437fcb64ab6098c7BbEc'
#oracle_address = '0x9315AFD6aEc0bb1C1FB3fdcdC2E43797B0A61853'
oracle_address = '0xb856Ca7c722cfb202D81c55DC7925e02ed3f0A2F'
oracle = RDOCMoCMedianizer(connection_manager, contract_address=oracle_address) #contract_address=oracle_address
#print(oracle.price())
print(oracle.peek())
