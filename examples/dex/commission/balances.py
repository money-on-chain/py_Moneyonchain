import json
import os

from rich.console import Console
from rich.table import Table

from moneyonchain.manager import ConnectionManager
from moneyonchain.token import DoCToken, WRBTC, BProToken, RIFDoC, RIF, RIFPro


def options_from_settings(filename='settings.json'):
    """ Options from file settings.json """

    with open(filename) as f:
        config_options = json.load(f)

    return config_options


console = Console()

network = 'dexMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

# load settings from file
settings = options_from_settings(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.json'))

account = '0xC61820bFB8F87391d62Cd3976dDc1d35e0cf7128'
#'0xf69287F5Ca3cC3C6d3981f2412109110cB8af076'
#'0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3'
block_identifier = connection_manager.block_number

table = Table(show_header=True, header_style="bold magenta", title="Account Balances: {0}".format(account))
table.add_column("Token")
table.add_column("Balance")
table.add_column("Token Address")
table.add_column("Block N")

token_name = 'WRBTC'
token = settings[network][token_name]
token_sc = WRBTC(connection_manager, contract_address=token)

table.add_row(
    token_name, str(token_sc.balance_of(account)), token, str(block_identifier)
)

token_name = 'DOC'
token = settings[network][token_name]
token_sc = DoCToken(connection_manager, contract_address=token)

table.add_row(
    token_name, str(token_sc.balance_of(account)), token, str(block_identifier)
)

token_name = 'BPRO'
token = settings[network][token_name]
token_sc = BProToken(connection_manager, contract_address=token)

table.add_row(
    token_name, str(token_sc.balance_of(account)), token, str(block_identifier)
)

token_name = 'RDOC'
token = settings[network][token_name]
token_sc = RIFDoC(connection_manager, contract_address=token)

table.add_row(
    token_name, str(token_sc.balance_of(account)), token, str(block_identifier)
)

token_name = 'RIF'
token = settings[network][token_name]
token_sc = RIF(connection_manager, contract_address=token)

table.add_row(
    token_name, str(token_sc.balance_of(account)), token, str(block_identifier)
)

token_name = 'RIFP'
token = settings[network][token_name]
token_sc = RIFPro(connection_manager, contract_address=token)

table.add_row(
    token_name, str(token_sc.balance_of(account)), token, str(block_identifier)
)


console.print(table)
