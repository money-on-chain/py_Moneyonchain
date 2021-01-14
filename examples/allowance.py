from moneyonchain.networks import NetworkManager
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
bit = BProToken(network_manager).from_abi()
print(bit.name())
print(bit.symbol())
print(bit.total_supply())
print(network_manager.show_active())
print(network_manager.gas_price())

account = '0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3'
dex_address = '0xA066d6e20e122deB1139FA3Ae3e96d04578c67B5'
amount_allow = 0.0001

print(bit.allowance(account, dex_address))

#tx_receipt = bit.approve(dex_address, amount_allow)
#print(tx_receipt)

network_manager.disconnect()
