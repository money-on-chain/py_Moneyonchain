import json
import logging
import logging.config

from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import MoCInrateCommissionsAddressChanger


def options_from_settings(filename='settings.json'):
    """ Options from file settings.json """

    with open(filename) as f:
        config_options = json.load(f)

    return config_options


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


network = 'mocMainnet2'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

# load settings from file, take a look on settings.json
settings = options_from_settings()

contract_splitter = settings[network]['CommissionSplitter']
contract = MoCInrateCommissionsAddressChanger(connection_manager)

if network in ['mocTestnetAlpha']:
    execute_change = True
else:
    execute_change = False

tx_hash, tx_receipt = contract.constructor(contract_splitter,
                                           execute_change=execute_change)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""
Connecting to mocMainnet2...
2020-09-10 16:33:25 root         INFO     Deploying new contract...
Connected: True
Changer Contract Address: 0xF03C1229B74ef57195e700A163b35AF6d70E32B0
2020-09-10 16:34:26 root         INFO     Deployed contract done!
2020-09-10 16:34:26 root         INFO     0x93eccea11209eba18a26171a6951d923a34c91d67103d3cf83e3651a154879ee
2020-09-10 16:34:26 root         INFO     AttributeDict({'transactionHash': HexBytes('0x93eccea11209eba18a26171a6951d923a34c91d67103d3cf83e3651a154879ee'), 'transactionIndex': 2, 'blockHash': HexBytes('0x11fbdf799177490ad41d48d46307f06e3b7cdca5087134c7fde689b993086b69'), 'blockNumber': 2689404, 'cumulativeGasUsed': 313834, 'gasUsed': 182637, 'contractAddress': '0xF03C1229B74ef57195e700A163b35AF6d70E32B0', 'logs': [], 'from': '0xEA14c08764c9e5F212c916E11a5c47Eaf92571e4', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')})
2020-09-10 16:34:26 root         INFO     Changer Contract Address: 0xF03C1229B74ef57195e700A163b35AF6d70E32B0
"""