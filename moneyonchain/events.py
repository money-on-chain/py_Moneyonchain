"""
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 THIS IS A PART OF MONEY ON CHAIN PACKAGE
 by Martin Mulone (martin.mulone@moneyonchain.com)

"""

from rich.console import Console
from rich.table import Table


class BaseEvent(object):
    name = "BaseEvent"
    hours_delta = 0

    @staticmethod
    def columns():
        columns = []
        return columns

    def print_row(self):
        print('\t'.join(self.columns()))
        print('\t'.join(str(v) for v in self.row()))

    def print_table(self, info_table=None):

        console = Console()

        d_info_table = dict(
            title='Event: {0}'.format(self.name),
            header_style='bold magenta',
            show_header=True
        )
        if info_table:
            d_info_table = info_table

        table = Table(show_header=d_info_table['show_header'],
                      header_style=d_info_table['header_style'],
                      title=d_info_table['title'])

        for col in self.columns():
            table.add_column(col, no_wrap=True)

        rows = [str(v) for v in self.row()]

        table.add_row(*rows)

        console.print(table)

