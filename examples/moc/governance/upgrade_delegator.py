from moneyonchain.networks import network_manager
from moneyonchain.governance import UpgradeDelegator

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')

# Connect to network
network_manager.connect(connection_network='rskMainnetPublic', config_network='rdocMainnet')


upgrade_delegator = UpgradeDelegator(network_manager, contract_address='0x5cE577f6Ec969CE9a282838D350206C52A6F338C').from_abi()
proxy_admin_address = upgrade_delegator.get_proxy_admin('0xaC7dE98a426F6FF51e1Bd6588b41544C8Addb2D1')

log.info("Upgrade delegator: {0}".format(upgrade_delegator.address()))
log.info("Admin: {0}".format(proxy_admin_address))
log.info("Governor: {0}".format(upgrade_delegator.governor()))

# finally disconnect from network
network_manager.disconnect()
