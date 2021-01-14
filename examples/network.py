from brownie import network

from moneyonchain.networks import NetworkManager, BitPROToken
from moneyonchain.tokens.bpro import BProToken

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()

network_manager = NetworkManager(
    connection_network='rskTesnetPublic',
    config_network='mocTestnet')
#nm.install()
network_manager.connect()
log.info(network_manager.is_connected())

bit = BProToken(network_manager).from_abi()
print(bit.name())
print(bit.symbol())
print(bit.total_supply())
print(network_manager.show_active())
print(network_manager.gas_price())

network_manager.disconnect()
