from rich.console import Console
from rich.table import Table

from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import MoCDecentralizedExchange, CommissionManager

console = Console()

network = 'dexMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

dex = MoCDecentralizedExchange(connection_manager)
dex_commission = CommissionManager(connection_manager)

table = Table(show_header=True, header_style="bold magenta", title="Contracts network: {0}".format(network))
table.add_column("Contract")
table.add_column("Proxy")
table.add_column("Implementation")

lib_address = connection_manager.options['networks'][network]['addresses']['MoCExchangeLib']
rows = list()
rows.append(('MoCDecentralizedExchange', dex.address(), dex.implementation()))
rows.append(('CommissionManager', dex_commission.address(), dex_commission.implementation()))
rows.append(('MoCExchangeLib', lib_address, lib_address))

for row in rows:
    table.add_row(
        row[0], row[1], row[2]
    )

console.print(table)


if network in 'dexMainnet':
    link_explorer = 'https://explorer.rsk.co/address/{0}'
elif network in 'dexTestnet':
    link_explorer = 'https://explorer.testnet.rsk.co/address/{0}'
else:
    link_explorer = 'https://explorer.rsk.co/address/{0}'

md_header = '''
| Contract                      | Proxy                           | Implementation                 |
| :---------------------------- | -----------------------------   | ------------------------------ |'''

md_lines = list()
for row in rows:
    line = '| {0} | [{1}]({2}) | [{3}]({4}) | '.format(row[0],
                                                       row[1], link_explorer.format(row[1]),
                                                       row[2], link_explorer.format(row[2]))
    md_lines.append(line)

print(md_header)
print('\n'.join(md_lines))
