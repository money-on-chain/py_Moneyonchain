"""
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 THIS IS A PART OF MONEY ON CHAIN PACKAGE
 by Martin Mulone (martin.mulone@moneyonchain.com)

"""

import json
import logging
from typing import Any, Dict, List, Optional, Tuple, Union

from brownie import Contract
from brownie.convert import EthAddress, Wei, to_address
from brownie.network.account import Account


class AccountBase(Account):

    log = logging.getLogger()

    def __init__(self,
                 network_manager,
                 default_account=None
                 ):

        self.network_manager = network_manager

        try:
            tx_account = self.network_manager.accounts[self.network_manager.default_account]
            if default_account:
                tx_account = self.network_manager.accounts[default_account]
        except ValueError:
            raise Exception("You need an account to deploy a contract!")

        self.tx_account = tx_account
        super().__init__(tx_account.address)

    def deploy(self,
               *args: Tuple,
               amount: int = 0,
               gas_limit: Optional[int] = None,
               gas_buffer: Optional[float] = None,
               gas_price: Optional[int] = None,
               nonce: Optional[int] = None,
               required_confs: int = 1,
               allow_revert: bool = None,
               silent: bool = None):
        """ Deploy contract """

        if gas_limit and gas_buffer:
            raise ValueError("Cannot set gas_limit and gas_buffer together")

        gas_price, gas_strategy, gas_iter = self._gas_price(gas_price)
        gas_limit = Wei(gas_limit) or self._gas_limit(
            None, amount, gas_price, gas_buffer
        )

        self.log.info("DEBUGG")
        self.log.info(gas_price)


class ContractBase(object):

    log = logging.getLogger()
    contract_name = 'Contract Name'
    contract_address = None
    contract_abi = None
    contract_bin = None
    sc = None
    precision = 10 ** 18

    def __init__(self,
                 network_manager,
                 contract_name=None,
                 contract_address=None,
                 contract_abi=None,
                 contract_bin=None):

        self.network_manager = network_manager

        # Contract Name
        if contract_name:
            self.contract_name = contract_name

        # Contract address
        if contract_address:
            self.contract_address = contract_address

        # Contract abi
        if contract_abi:
            self.contract_abi = contract_abi

        # Contract bin
        if contract_bin:
            self.contract_bin = contract_bin

    def from_abi(self):
        self.sc = Contract.from_abi(self.contract_name, self.contract_address, self.contract_abi)
        return self

    def address(self):
        return self.sc.address

    def tx_arguments(self,
                     gas_limit=None,
                     gas_buffer=None,
                     gas_price=None,
                     amount=None,
                     nonce=None,
                     required_confs=1,
                     allow_revert=True,
                     default_account=None):

        tx_account = self.network_manager.accounts[self.network_manager.default_account]
        if default_account:
            tx_account = self.network_manager.accounts[default_account]

        d_tx = {
            "gas_limit": gas_limit,
            "gas_buffer": gas_buffer,
            "gas_price": gas_price,
            "amount": amount,
            "nonce": nonce,
            "required_confs": required_confs,
            "allow_revert": allow_revert,
            "from": tx_account
        }

        return d_tx

    def deploy(self,
               *args,
               default_account=None,
               **tx_arguments):
        """ Deploy contract """

        account_base = AccountBase(self.network_manager,
                                   default_account=default_account)
        account_base.deploy(*args, **tx_arguments)

    @staticmethod
    def content_abi_file(abi_file):

        with open(abi_file) as f:
            abi = json.load(f)

        return abi

    @staticmethod
    def content_bin_file(bin_file):

        with open(bin_file) as f:
            content_bin = f.read()

        return content_bin

    def load_abi_file(self, abi_file):

        self.contract_abi = self.content_abi_file(abi_file)

    def load_bin_file(self, bin_file):

        self.contract_bin = self.content_bin_file(bin_file)
