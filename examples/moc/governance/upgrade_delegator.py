from moneyonchain.networks import network_manager
from moneyonchain.governance import UpgradeDelegator

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')

# Connect to network
network_manager.connect(connection_network='rskTestnetPublic', config_network='mocTestnetAlpha')


upgrade_delegator = UpgradeDelegator(network_manager).from_abi()
proxy_admin_address = upgrade_delegator.get_proxy_admin('0xF3d40B15DCe0b6257a6A8F62c707621E1e464c1e')

log.info("Upgrade delegator: {0}".format(upgrade_delegator.address()))
log.info("Admin: {0}".format(proxy_admin_address))
log.info("Governor: {0}".format(upgrade_delegator.governor()))

# finally disconnect from network
network_manager.disconnect()
