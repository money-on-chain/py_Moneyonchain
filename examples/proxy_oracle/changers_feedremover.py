from moneyonchain.networks import network_manager
from moneyonchain.medianizer import ETHPriceFeederRemoverChanger


import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='logs/changers_feedremover.log',
                    filemode='a')

# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# set a format which is simpler for console use
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
console.setFormatter(formatter)

log = logging.getLogger()
log.addHandler(console)


connection_network = 'rskMainnetPublic'
config_network = 'ethMainnet'


# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)


contract = ETHPriceFeederRemoverChanger(network_manager)
contract_address_pricefeed = '0x85c6cD0BCce63fdF9D3fA4C0661aEEd0976C9B97'
tx_receipt = contract.constructor(contract_address_pricefeed,
                                  execute_change=False)
if tx_receipt:
    log.info("Changer Contract Address: {address}".format(address=tx_receipt.contract_address))
else:
    log.info("Error deploying changer")

# finally disconnect from network
network_manager.disconnect()

