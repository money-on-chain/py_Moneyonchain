import json
import logging
import logging.config

from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import MoCSetCommissionMocProportionChanger


def options_from_settings(filename='settings.json'):
    """ Options from file settings.json """

    with open(filename) as f:
        config_options = json.load(f)

    return config_options


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

# load settings from file, take a look on settings.json
settings = options_from_settings()

contract_splitter = settings[network]['CommissionSplitter']
contract = MoCSetCommissionMocProportionChanger(connection_manager)

if network in ['mocTestnetAlpha']:
    execute_change = True
else:
    execute_change = False

proportion = 200000000000000000
tx_hash, tx_receipt = contract.constructor(proportion,
                                           commission_splitter=contract_splitter,
                                           execute_change=execute_change)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")
