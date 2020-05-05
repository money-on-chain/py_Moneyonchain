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
import logging

from web3.types import BlockIdentifier
from web3 import Web3
from moneyonchain.contract import Contract


class CommissionSplitter(Contract):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/CommissionSplitter.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/CommissionSplitter.bin'))

    mode = 'MoC'
    precision = 10 ** 18

    def __init__(self, connection_manager,
                 contract_address=None,
                 contract_abi=None,
                 contract_bin=None):

        network = connection_manager.network
        if not contract_address:
            # load from connection manager

            contract_address = connection_manager.options['networks'][network]['addresses']['CommissionSplitter']

        super().__init__(connection_manager,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

        # finally load the contract
        self.load_contract()

    def commission_address(self, block_identifier: BlockIdentifier = 'latest'):
        """Contract address output"""

        result = self.sc.functions.commissionsAddress().call(
            block_identifier=block_identifier)

        return result

    def moc_address(self, block_identifier: BlockIdentifier = 'latest'):
        """The MOC contract address"""

        result = self.sc.functions.moc().call(
            block_identifier=block_identifier)

        return result

    def reserve_address(self, block_identifier: BlockIdentifier = 'latest'):
        """The reserve contract address"""

        result = self.sc.functions.reserveToken().call(
            block_identifier=block_identifier)

        return result


class RDOCCommissionSplitter(CommissionSplitter):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/CommissionSplitter.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/CommissionSplitter.bin'))

    mode = 'RDoC'
    precision = 10 ** 18
