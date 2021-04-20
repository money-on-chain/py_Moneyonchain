"""
Deploy Price Provider WRBTC/MoC
"""

from moneyonchain.networks import network_manager
from moneyonchain.tex import TexMocBtcPriceProviderFallback

connection_network = 'rskTestnetPublic'
config_network = 'dexTestnet'

# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)

base_token = '0x09b6ca5E4496238A1F176aEa6Bb607DB96c2286E'  # WRBTC
secondary_token = '0x0399c7F7B37E21cB9dAE04Fb57E24c68ed0B4635'  # AMOC
moc_state = '0x0adb40132cB0ffcEf6ED81c26A1881e214100555'
base_token_doc_moc = '0x489049c48151924c07F86aa1DC6Cc3Fea91ed963'  # DOC
secondary_token_doc_moc = '0x0399c7F7B37E21cB9dAE04Fb57E24c68ed0B4635'  # AMOC


price_provider = TexMocBtcPriceProviderFallback(network_manager)
tx_receipt = price_provider.constructor(
    moc_state,
    base_token,
    secondary_token,
    base_token_doc_moc,
    secondary_token_doc_moc)

if tx_receipt:
    print("Price provider deployed Contract Address: {address}".format(address=tx_receipt.contract_address))
else:
    print("Error deploying price provider")

