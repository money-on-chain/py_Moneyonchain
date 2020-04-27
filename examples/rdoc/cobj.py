from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCMoCState

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()


network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
log.info("Connecting to %s..." % network)
log.info("Connected: {conectado}".format(conectado=connection_manager.is_connected))

moc_state = RDOCMoCState(connection_manager)

info = moc_state.cobj()
log.info("CObj: {0}".format(info))

info = moc_state.cobj_X2()
log.info("CObj X2: {0}".format(info))

