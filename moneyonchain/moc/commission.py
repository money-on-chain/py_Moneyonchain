"""
        GNU AFFERO GENERAL PUBLIC LICENSE
           Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 THIS IS A PART OF MONEY ON CHAIN
 @2020
 by Martin Mulone (martin.mulone@moneyonchain.com)

"""

import os

from moneyonchain.contract import ContractBase
from moneyonchain.moc_base import CommissionSplitterBase


class CommissionSplitter(CommissionSplitterBase):
    contract_name = 'CommissionSplitter'
    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/CommissionSplitter.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/CommissionSplitter.bin'))

    mode = 'MoC'
    precision = 10 ** 18
