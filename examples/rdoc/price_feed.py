from moneyonchain.manager import ConnectionManager
from moneyonchain.rdoc import RDOCPriceFeed

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()


network = 'rdocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
log.info("Connecting to %s..." % network)
log.info("Connected: {conectado}".format(conectado=connection_manager.is_connected))

#feeder_address = '0x652255254E79CD0954Bdd8B72ED00D9614Eba6A8'
#oracle_address = '0x2B54819531B7126bDEE2CeFDD9c5342d6c307595'

feeder_address = '0xe7295C7776Bf5f6a042bA009c41D9f900F8aE819'
oracle_address = '0x01a165cC33Ff8Bd0457377379962232886be3DE6'
feeder = RDOCPriceFeed(connection_manager,
                       contract_address=feeder_address,
                       contract_address_moc_medianizer=oracle_address)

# write price on price feeder
feeder.post(0.051 * 10 ** 18, block_expiration=300)
print(feeder.zzz())
print(feeder.peek())


"""
INFO:root:Connecting to rdocTestnetAlpha...
INFO:root:Connected: True
INFO:root:Successfully post price [6.5e+16] in Block [828984] Hash: [0x4d4146dbb58186cd5b5943e38b7228f6244bb21149f201774de203010a822e57] Gas used: [55949] From: [0xa8F94d08d3d9C045fE0b86a953DF39b14206153c]
"""