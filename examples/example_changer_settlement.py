import os
from web3 import Web3
from moneyonchain.manager import ConnectionManager


network = 'mocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

path_abi = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi')
moc_settlement_address = Web3.toChecksumAddress('0xa0dA80B5E5bdf96F9e99630Fa333821fB741A308')
moc_settlement = connection_manager.load_abi_contract_file(os.path.join(path_abi, "MoCSettlement.abi"),
                                                           contract_address=moc_settlement_address)

governor_address = Web3.toChecksumAddress('0x9258531274B945eB628656F4b30e8216938A619C')
moc_governor = connection_manager.load_abi_contract_file(os.path.join(path_abi, "Governor.abi"),
                                                         contract_address=governor_address)

init_settings = dict()
init_settings['blockSpan'] = 65#2648 * 30

print("Initializing settlemnt")
print("Wait...")

abi_file = os.path.join(path_abi, "MoCSettlementChanger.abi")
bin_file = os.path.join(path_abi, "MoCSettlementChanger.bin")
sc, content_abi, content_bin = connection_manager.load_bytecode_contract_file(abi_file, bin_file)
tx_hash = connection_manager.fnx_constructor(sc,
                                             moc_settlement_address,
                                             init_settings['blockSpan']
                                             )
tx_receipt = connection_manager.wait_transaction_receipt(tx_hash)
print(tx_receipt)

# Create the contract instance with the newly-deployed address
moc_changer = connection_manager.web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=content_abi,
)

print("Contract Address: {address}".format(address=tx_receipt.contractAddress))

# Change governor
tx_hash = connection_manager.fnx_transaction(moc_governor, 'executeChange', moc_changer.address)
tx_receipt = connection_manager.wait_transaction_receipt(tx_hash)
print(tx_receipt)

print("Governor changes done!")
