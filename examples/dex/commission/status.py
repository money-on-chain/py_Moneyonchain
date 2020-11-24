"""
Commission Manager
"""

import json
import os
from rich.console import Console
from rich.table import Table

from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import CommissionManager


def options_from_settings(filename='settings.json'):
    """ Options from file settings.json """

    with open(filename) as f:
        config_options = json.load(f)

    return config_options


console = Console()

network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


# load settings from file
settings = options_from_settings(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.json'))


dex_commission = CommissionManager(connection_manager)

table = Table(show_header=True, header_style="bold magenta", title="Commission Manager: {0}".format(network))
table.add_column("Storage")
table.add_column("Value")

table.add_row(
    "Beneficiary", dex_commission.beneficiary_address()
)

table.add_row(
    "Commission Rate", str(dex_commission.commision_rate())
)

table.add_row(
    "Cancelation Rate", str(dex_commission.cancelation_penalty_rate())
)

table.add_row(
    "Expiration Rate", str(dex_commission.expiration_penalty_rate())
)

table.add_row(
    "Minimum Fix Commision", str(dex_commission.minimum_commission())
)

table.add_row(
    "Fee 0.001 WRBTC", str(dex_commission.calculate_initial_fee(0.001, 10000))
)

table.add_row(
    "Fee 10 DOC", str(dex_commission.calculate_initial_fee(10, 10000))
)

console.print(table)
print("")
print("")

block_identifier = connection_manager.block_number

table = Table(show_header=True, header_style="bold magenta", title="Commission Balances: {0}".format(network))
table.add_column("Token")
table.add_column("Balance")
table.add_column("Address")
table.add_column("Block N")

token_name = 'WRBTC'
token = settings[network][token_name]

table.add_row(
    token_name, str(dex_commission.exchange_commissions(token, block_identifier=block_identifier)), token, str(block_identifier)
)

token_name = 'DOC'
token = settings[network][token_name]

table.add_row(
    token_name, str(dex_commission.exchange_commissions(token, block_identifier=block_identifier)), token, str(block_identifier)
)

token_name = 'BPRO'
token = settings[network][token_name]

table.add_row(
    token_name, str(dex_commission.exchange_commissions(token, block_identifier=block_identifier)), token, str(block_identifier)
)

token_name = 'RDOC'
token = settings[network][token_name]

table.add_row(
    token_name, str(dex_commission.exchange_commissions(token, block_identifier=block_identifier)), token, str(block_identifier)
)

token_name = 'RIF'
token = settings[network][token_name]

table.add_row(
    token_name, str(dex_commission.exchange_commissions(token, block_identifier=block_identifier)), token, str(block_identifier)
)

token_name = 'RIFP'
token = settings[network][token_name]

table.add_row(
    token_name, str(dex_commission.exchange_commissions(token, block_identifier=block_identifier)), token, str(block_identifier)
)

console.print(table)
