from brownie import network

from moneyonchain.networks import NetworkManager, BitPROToken

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()

#nm = NetworkManager()
#nm.install()

network.connect('rskTesnetPublic')
log.info(network.is_connected())

bit = BitPROToken(contract_address='0x4dA7997A819bb46B6758B9102234c289dD2Ad3bf')
print(bit.name())
print(bit.symbol())
print(bit.total_supply())
print(network.show_active())
print(network.gas_price())

network.disconnect()
