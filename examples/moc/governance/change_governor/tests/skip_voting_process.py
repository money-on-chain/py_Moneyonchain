from moneyonchain.networks import network_manager
from moneyonchain.governance import SkipVotingProcessChange


import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='logs/skip_voting_process.log',
                    filemode='a')

# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# set a format which is simpler for console use
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
console.setFormatter(formatter)

log = logging.getLogger()
log.addHandler(console)


connection_network = 'rskTestnetPublic'
config_network = 'mocTestnetAlpha3'


# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)

contract = SkipVotingProcessChange(network_manager)

voting_machine_address = '0x7D124cC0f59aDA5793AD8edA9eD1836cB7e797a3'
governor_address = '0x7b716178771057195bB511f0B1F7198EEE62Bc22'
changer_address = '0x4E1E9fc492A3AE59F7344665828e76F293Eb1f6D'

tx_receipt = contract.constructor(voting_machine_address, governor_address, changer_address, execute_change=False)
if tx_receipt:
    log.info("Changer Contract Address: {address}".format(address=tx_receipt.contract_address))
else:
    log.info("Error deploying changer")

# finally disconnect from network
network_manager.disconnect()
