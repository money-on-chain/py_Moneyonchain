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

from web3 import Web3
from web3.types import BlockIdentifier

from moneyonchain.contract import ContractBase
from moneyonchain.governance import ProxyAdmin

from moneyonchain.moc_base import MoCSettlementBase


class MoCSettlement(MoCSettlementBase):
    contract_name = 'MoCSettlement'

    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCSettlement.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCSettlement.bin'))

    precision = 10 ** 18
    mode = 'MoC'
    project = 'MoC'
