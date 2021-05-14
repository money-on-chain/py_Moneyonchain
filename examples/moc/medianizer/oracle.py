from moneyonchain.networks import network_manager
from moneyonchain.medianizer import MoCMedianizer

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()


connection_network = 'rskTestnetPublic'
config_network = 'mocTestnetAlpha'


# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)


#oracle_address = '0x2B54819531B7126bDEE2CeFDD9c5342d6c307595'
#oracle_address = '0x01a165cC33Ff8Bd0457377379962232886be3DE6'
#oracle_address = '0x9d4b2c05818A0086e641437fcb64ab6098c7BbEc'
#oracle_address = '0x2d39Cc54dc44FF27aD23A91a9B5fd750dae4B218'
#oracle_address = '0x667bd3d048FaEBb85bAa0E9f9D87cF4c8CDFE849'
#oracle_address = '0x2d39Cc54dc44FF27aD23A91a9B5fd750dae4B218'
oracle_address = '0x26a00aF444928d689DDEC7b4D17c0E4a8c9D407d'

#oracle_address = '0xb856Ca7c722cfb202D81c55DC7925e02ed3f0A2F'

oracle = MoCMedianizer(network_manager, contract_address=oracle_address).from_abi()
#print(oracle.price())
#oracle = MoCMedianizer(connection_manager)
print(oracle.peek())


# finally disconnect from network
network_manager.disconnect()
