import logging
import logging.config

from moneyonchain.networks import network_manager
from moneyonchain.rdoc import RDOCMoCInrate, RDOCCommissionSplitterAddressChanger


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='logs/changer_commission_address.log',
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
config_network = 'rdocMainnet'

log.info('Connecting enviroment {0}...'.format(config_network))

# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)

moc_inrate = RDOCMoCInrate(network_manager).from_abi()

# get splitter from commission address
contract_splitter = moc_inrate.commission_address()

log.info("Current commission address (splitter): {0}".format(contract_splitter))

contract = RDOCCommissionSplitterAddressChanger(network_manager)

beneficiary_address = '0x728967DD751F5f21bF390eeE66527dBC17bD7E25'
tx_receipt = contract.constructor(beneficiary_address,
                                  commission_splitter=contract_splitter,
                                  execute_change=False)
if tx_receipt:
    log.info("Changer Contract Address: {address}".format(address=tx_receipt.contract_address))
else:
    log.info("Error deploying changer")

# finally disconnect from network
network_manager.disconnect()
