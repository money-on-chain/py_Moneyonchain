"""
Inserts an order in the sell orderbook of a given pair without a hint
the pair should not be disabled; the contract should not be paused. Takes the funds
with a transferFrom
"""

from decimal import Decimal
from web3 import Web3
import json
import os

from moneyonchain.networks import NetworkManager
from moneyonchain.tokens.bpro import BProToken

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


connection_network='rskTesnetPublic'
config_network = 'mocTestnet'

# init network manager
# connection network is the brownie connection network
# config network is our enviroment we want to connect
network_manager = NetworkManager(
    connection_network=connection_network,
    config_network=config_network)

# run install() if is the first time and you want to install
# networks connection from brownie
# network_manager.install()

# Connect to network
network_manager.connect()

# instantiate DEX Contract
bit = BProToken(network_manager)

bit.deploy()

# finally disconnect from network
network_manager.disconnect()
