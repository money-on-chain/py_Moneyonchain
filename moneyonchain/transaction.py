"""
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 THIS IS A PART OF MONEY ON CHAIN PACKAGE
 by Martin Mulone (martin.mulone@moneyonchain.com)

"""

import logging

from brownie.network.transaction import TransactionReceipt


def color(select_color):
    return ''


class TransactionReceiptBase(TransactionReceipt):

    log = logging.getLogger()

    def __init__(self,
                 *args,
                 logger=None,
                 **parameters):

        if logger:
            self.log = logger

        super().__init__(*args, **parameters)

    def info_to_log(self) -> None:
        """Displays verbose information about the transaction, including decoded event logs."""
        status = ""
        if not self.status:
            status = f"({color('bright red')}{self.revert_msg or 'reverted'}{color})"

        result = (
            f"Transaction was Mined {status}\n---------------------\n"
            f"Tx Hash: {color('bright blue')}{self.txid}\n"
            f"From: {color('bright blue')}{self.sender}\n"
        )

        if self.contract_address and self.status:
            result += (
                f"New {self.contract_name} address: {color('bright blue')}{self.contract_address}\n"
            )
        else:
            result += (
                f"To: {color('bright blue')}{self.receiver}{color}\n"
                f"Value: {color('bright blue')}{self.value}\n"
            )
            if self.input != "0x" and int(self.input, 16):
                result += f"Function: {color('bright blue')}{self._full_name()}\n"

        result += (
            f"Block: {color('bright blue')}{self.block_number}{color}\nGas Used: "
            f"{color('bright blue')}{self.gas_used}{color} / {color('bright blue')}{self.gas_limit}"
            f"{color} ({color('bright blue')}{self.gas_used / self.gas_limit:.1%}{color})\n"
        )

        if self.events:
            result += "\n   Events In This Transaction\n   --------------------------"
            for event in self.events:  # type: ignore
                result += f"\n   {color('bright yellow')}{event.name}{color}"  # type: ignore
                for key, value in event.items():  # type: ignore
                    result += f"\n      {key}: {color('bright blue')}{value}{color}"

        self.log.info(result)
