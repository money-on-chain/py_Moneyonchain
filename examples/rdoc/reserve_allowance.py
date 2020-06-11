from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoC

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()


network = 'rdocTestnet'
connection_manager = ConnectionManager(network=network)
log.info("Connecting to %s..." % network)
log.info("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_sc = RDOCMoC(connection_manager)

account = '0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3'
info = moc_sc.reserve_allowance(account)
log.info("Reserve Allowance: {0}".format(info))
