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
from moneyonchain.contract import ContractBase
from moneyonchain.changers import BaseChanger
from moneyonchain.governance import Governor


class MoCStateMoCPriceProviderChanger(BaseChanger):
    contract_name = 'MoCStateMoCPriceProviderChanger'

    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCStateMoCPriceProviderChanger.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCStateMoCPriceProviderChanger.bin'))

    mode = 'MoC'

    def constructor(self, price_provider, execute_change=False, **tx_arguments):

        config_network = self.network_manager.config_network
        contract_address = self.network_manager.options['networks'][config_network]['addresses']['MoCState']

        self.log.info("Deploying new contract...")

        tx_receipt = self.deploy(contract_address, Web3.toChecksumAddress(price_provider), **tx_arguments)

        tx_receipt.info()
        tx_receipt.info_to_log()

        self.log.info("Deployed contract done!")
        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contract_address))

        if execute_change:
            self.log.info("Executing change....")
            governor = Governor(self.network_manager).from_abi()
            tx_receipt = governor.execute_change(tx_receipt.contract_address, **tx_arguments)
            self.log.info("Change successfull!")

        return tx_receipt


class MoCStateLiquidationEnabledChanger(BaseChanger):
    contract_name = 'MoCStateLiquidationEnabledChanger'

    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCStateLiquidationEnabledChanger.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCStateLiquidationEnabledChanger.bin'))

    mode = 'MoC'

    def constructor(self, is_enabled, execute_change=False, **tx_arguments):

        config_network = self.network_manager.config_network
        contract_address = self.network_manager.options['networks'][config_network]['addresses']['MoCState']

        self.log.info("Deploying new contract...")

        tx_receipt = self.deploy(contract_address, is_enabled, **tx_arguments)

        tx_receipt.info()
        tx_receipt.info_to_log()

        self.log.info("Deployed contract done!")
        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contract_address))

        if execute_change:
            self.log.info("Executing change....")
            governor = Governor(self.network_manager).from_abi()
            tx_receipt = governor.execute_change(tx_receipt.contract_address, **tx_arguments)
            self.log.info("Change successfull!")

        return tx_receipt


class MoCVendorsChanger(BaseChanger):
    contract_name = 'MoCVendorsChanger'

    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCVendorsChanger.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCVendorsChanger.bin'))

    mode = 'MoC'

    def constructor(self, vendor_guardian_address, execute_change=False, **tx_arguments):

        config_network = self.network_manager.config_network
        contract_address = self.network_manager.options['networks'][config_network]['addresses']['MoCVendors']

        self.log.info("Deploying new contract...")

        tx_receipt = self.deploy(contract_address, Web3.toChecksumAddress(vendor_guardian_address), **tx_arguments)

        tx_receipt.info()
        tx_receipt.info_to_log()

        self.log.info("Deployed contract done!")
        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contract_address))

        if execute_change:
            self.log.info("Executing change....")
            governor = Governor(self.network_manager).from_abi()
            tx_receipt = governor.execute_change(tx_receipt.contract_address, **tx_arguments)
            self.log.info("Change successfull!")

        return tx_receipt
