from moneyonchain.networks import network_manager
from moneyonchain.medianizer import ETHPriceFeederAdderChanger


import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='logs/changers_feedadder.log',
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
config_network = 'tetherTestnet'


# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)


contract = ETHPriceFeederAdderChanger(network_manager)

price_feeder_owner = '0xe317349c7279ffF242cc8ADCb575EbA0153760BA'
tx_receipt = contract.constructor(price_feeder_owner, execute_change=False)
if tx_receipt:
    log.info("Changer Contract Address: {address}".format(address=tx_receipt.contract_address))
else:
    log.info("Error deploying changer")


# finally disconnect from network
network_manager.disconnect()
