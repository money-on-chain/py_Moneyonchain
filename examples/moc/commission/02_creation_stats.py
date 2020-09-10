import json
import logging
import logging.config
from web3 import Web3

from moneyonchain.manager import ConnectionManager
from moneyonchain.governance import Governed
from moneyonchain.commission import CommissionSplitter
from moneyonchain.moc import MoCInrate


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


def options_from_settings(filename='settings.json'):
    """ Options from file settings.json """

    with open(filename) as f:
        config_options = json.load(f)

    return config_options


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


# load settings from file
settings = options_from_settings()

contact_address = settings[network]['CommissionSplitter']

governed = Governed(connection_manager, contract_address=contact_address)
splitter = CommissionSplitter(connection_manager, contract_address=contact_address)
moc_inrate = MoCInrate(connection_manager)

info_dict = dict()
info_dict['proportion'] = dict()
info_dict['balance'] = dict()

print("Splitter Address: [{0}]".format(contact_address))
print("Governor: [{0}]".format(governed.governor()))
print("Multisig address: [{0}]".format(splitter.commission_address()))
print("MoC Address: [{0}]".format(splitter.moc_address()))
print("MoCInrate Target commission: [{0}] (have to be the splitter)".format(moc_inrate.commission_address()))

info_dict['proportion']['moc'] = Web3.fromWei(splitter.moc_proportion(), 'ether')
info_dict['proportion']['multisig'] = 1 - info_dict['proportion']['moc']

print("Proportion MOC: [{0}]".format(info_dict['proportion']['moc']))
print("Proportion Multisig: [{0}]".format(info_dict['proportion']['multisig']))

info_dict['balance']['splitter'] = splitter.balance()
print("Splitter balance: [{0}]".format(info_dict['balance']['splitter']))

# balances commision
balance = Web3.fromWei(connection_manager.balance(splitter.commission_address()), 'ether')
info_dict['balance']['commission'] = balance
print("Multisig balance (proportion: {0}): [{1}]".format(info_dict['proportion']['multisig'],
                                                         info_dict['balance']['commission']))

# balances moc
balance = Web3.fromWei(connection_manager.balance(splitter.moc_address()), 'ether')
info_dict['balance']['moc'] = balance
print("MoC balance (proportion: {0}): [{1}]".format(info_dict['proportion']['moc'],
                                                    info_dict['balance']['moc']))
