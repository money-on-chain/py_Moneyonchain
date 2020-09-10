import json
import logging
import logging.config
from web3 import Web3

from moneyonchain.manager import ConnectionManager
from moneyonchain.commission import CommissionSplitter

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


def options_from_settings(filename='settings.json'):
    """ Options from file settings.json """

    with open(filename) as f:
        config_options = json.load(f)

    return config_options


network = 'mocMainnet2'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

# load settings from file
settings = options_from_settings()

contact_address = settings[network]['CommissionSplitter']

splitter = CommissionSplitter(connection_manager, contract_address=contact_address)

info_dict = dict()
info_dict['before'] = dict()
info_dict['after'] = dict()
info_dict['proportion'] = dict()

info_dict['proportion']['moc'] = Web3.fromWei(splitter.moc_proportion(), 'ether')
info_dict['proportion']['multisig'] = 1 - info_dict['proportion']['moc']

print("Splitter address: [{0}]".format(contact_address))
print("Multisig address: [{0}]".format(splitter.commission_address()))
print("MoC address: [{0}]".format(splitter.moc_address()))
print("Proportion MOC: [{0}]".format(info_dict['proportion']['moc']))
print("Proportion Multisig: [{0}]".format(info_dict['proportion']['multisig']))

print("BEFORE SPLIT:")
print("=============")


info_dict['before']['splitter'] = splitter.balance()
print("Splitter balance: [{0}]".format(info_dict['before']['splitter']))

# balances commision
balance = Web3.fromWei(connection_manager.balance(splitter.commission_address()), 'ether')
info_dict['before']['commission'] = balance
print("Multisig balance (proportion: {0}): [{1}]".format(info_dict['proportion']['multisig'],
                                                         info_dict['before']['commission']))

# balances moc
balance = Web3.fromWei(connection_manager.balance(splitter.moc_address()), 'ether')
info_dict['before']['moc'] = balance
print("MoC balance (proportion: {0}): [{1}]".format(info_dict['proportion']['moc'],
                                                    info_dict['before']['moc']))


tx_hash, tx_receipt = splitter.split()
if tx_receipt:
    print("Sucessfully splited!")
else:
    print("Error splited!!!")


print("AFTER SPLIT:")
print("=============")

info_dict['after']['splitter'] = splitter.balance()
dif = info_dict['after']['splitter'] - info_dict['before']['splitter']
print("Splitter balance: [{0}] Difference: [{1}]".format(info_dict['after']['splitter'], dif))

# balances commision
balance = Web3.fromWei(connection_manager.balance(splitter.commission_address()), 'ether')
info_dict['after']['commission'] = balance
dif = info_dict['after']['commission'] - info_dict['before']['commission']
print("Multisig balance (proportion: {0}): [{1}] Difference: [{2}]".format(
    info_dict['proportion']['multisig'],
    info_dict['after']['commission'],
    dif))

# balances moc
balance = Web3.fromWei(connection_manager.balance(splitter.moc_address()), 'ether')
info_dict['after']['moc'] = balance
dif = info_dict['after']['moc'] - info_dict['before']['moc']
print("MoC balance (proportion: {0}): [{1}] Difference: [{2}]".format(
    info_dict['proportion']['moc'],
    info_dict['after']['moc'],
    dif))


"""

"""