from moneyonchain.networks import NetworkManager

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()

nm = NetworkManager()
nm.install()
