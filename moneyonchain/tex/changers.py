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
import sys

from web3 import Web3
from moneyonchain.contract import ContractBase
from moneyonchain.changers import BaseChanger
from moneyonchain.governance import DEXGovernor


class DexAddTokenPairChanger(BaseChanger):

    contract_name = 'DexAddTokenPairChanger'
    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/AddTokenPairChanger.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/AddTokenPairChanger.bin'))

    contract_governor_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.abi'))
    contract_governor_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.bin'))

    mode = 'DEX'

    def constructor(self,
                    base_token,
                    secondary_address,
                    price_provider,
                    price_precision,
                    init_price,
                    execute_change=False,
                    **tx_arguments):

        config_network = self.network_manager.config_network
        contract_address = Web3.toChecksumAddress(
            self.network_manager.options['networks'][config_network]['addresses']['dex'])

        self.log.info("Deploying new contract...")

        tx_receipt = self.deploy(
            contract_address,
            [Web3.toChecksumAddress(base_token)],
            [Web3.toChecksumAddress(secondary_address)],
            [Web3.toChecksumAddress(price_provider)],
            [price_precision],
            [init_price],
            **tx_arguments
            )

        self.log.info("Deployed contract done!")
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contract_address))

        if execute_change:
            self.log.info("Executing change....")
            governor = DEXGovernor(self.network_manager).from_abi()
            tx_receipt = governor.executeChange(tx_receipt.contract_address)
            self.log.info("Change successfull!")

        return tx_receipt


class DexMaxOrderLifespanChanger(BaseChanger):

    contract_name = 'DexMaxOrderLifespanChanger'
    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MaxOrderLifespanChanger.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MaxOrderLifespanChanger.bin'))

    contract_governor_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.abi'))
    contract_governor_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.bin'))

    mode = 'DEX'

    def constructor(self,
                    order_lifespan,
                    execute_change=False,
                    **tx_arguments):
        config_network = self.network_manager.config_network
        contract_address = Web3.toChecksumAddress(
            self.network_manager.options['networks'][config_network]['addresses']['dex'])

        self.log.info("Deploying new contract...")

        tx_receipt = self.deploy(
            contract_address,
            order_lifespan,
            **tx_arguments)

        tx_receipt.info()
        tx_receipt.info_to_log()

        self.log.info("Deployed contract done!")
        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contract_address))

        if execute_change:
            self.log.info("Executing change....")
            governor = DEXGovernor(self.network_manager).from_abi()
            tx_receipt = governor.executeChange(tx_receipt.contract_address)
            self.log.info("Change successfull!")

        return tx_receipt

"""
class DexTokenPairDisabler(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/TokenPairDisabler.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/TokenPairDisabler.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.bin'))

    mode = 'DEX'

    def constructor(self,
                    base_address,
                    secondary_address,
                    execute_change=False):

        network = self.connection_manager.network
        contract_address = Web3.toChecksumAddress(self.connection_manager.options['networks'][network]['addresses']['dex'])

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address,
                                                   Web3.toChecksumAddress(base_address),
                                                   Web3.toChecksumAddress(secondary_address))

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(Web3.toHex(tx_hash))
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class DexTokenPairEnabler(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/TokenPairEnabler.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/TokenPairEnabler.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.bin'))

    mode = 'DEX'

    def constructor(self,
                    base_address,
                    secondary_address,
                    execute_change=False):

        network = self.connection_manager.network
        contract_address = Web3.toChecksumAddress(self.connection_manager.options['networks'][network]['addresses']['dex'])

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address,
                                                   Web3.toChecksumAddress(base_address),
                                                   Web3.toChecksumAddress(secondary_address))

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(Web3.toHex(tx_hash))
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class DexEMAPriceChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/EMAPriceChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/EMAPriceChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.bin'))

    mode = 'DEX'

    def constructor(self,
                    base_token,
                    secondary_token,
                    ema_price,
                    execute_change=False):

        network = self.connection_manager.network
        contract_address = Web3.toChecksumAddress(self.connection_manager.options['networks'][network]['addresses']['dex'])

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address,
                                                   Web3.toChecksumAddress(base_token),
                                                   Web3.toChecksumAddress(secondary_token),
                                                   ema_price)

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(Web3.toHex(tx_hash))
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt



class DexPriceProviderChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/PriceProviderChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/PriceProviderChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.bin'))

    mode = 'DEX'

    def constructor(self,
                    base_token,
                    secondary_token,
                    price_provider,
                    execute_change=False):

        network = self.connection_manager.network
        contract_address = Web3.toChecksumAddress(self.connection_manager.options['networks'][network]['addresses']['dex'])

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address,
                                                   Web3.toChecksumAddress(base_token),
                                                   Web3.toChecksumAddress(secondary_token),
                                                   Web3.toChecksumAddress(price_provider))

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(Web3.toHex(tx_hash))
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class DexMaxBlocksForTickChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MaxBlocksForTickChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MaxBlocksForTickChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.bin'))

    mode = 'DEX'

    def constructor(self,
                    max_blocks_for_ticks,
                    execute_change=False):

        network = self.connection_manager.network
        contract_address = Web3.toChecksumAddress(self.connection_manager.options['networks'][network]['addresses']['dex'])

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address,
                                                   max_blocks_for_ticks)

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(Web3.toHex(tx_hash))
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class DexMinBlocksForTickChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MinBlocksForTickChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MinBlocksForTickChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.bin'))

    mode = 'DEX'

    def constructor(self,
                    min_blocks_for_ticks,
                    execute_change=False):

        network = self.connection_manager.network
        contract_address = Web3.toChecksumAddress(self.connection_manager.options['networks'][network]['addresses']['dex'])

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address,
                                                   min_blocks_for_ticks)

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(Web3.toHex(tx_hash))
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class DexCommissionRateChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/CommissionRateChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/CommissionRateChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.bin'))

    mode = 'DEX'

    def constructor(self,
                    commission_rate,
                    execute_change=False):

        network = self.connection_manager.network
        contract_address = Web3.toChecksumAddress(
            self.connection_manager.options['networks'][network]['addresses']['commissionManager'])

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address,
                                                   commission_rate)

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(Web3.toHex(tx_hash))
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class DexMinOrderAmountChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MinOrderAmountChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MinOrderAmountChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.bin'))

    mode = 'DEX'

    def constructor(self,
                    min_order_amount,
                    execute_change=False):

        network = self.connection_manager.network
        contract_address = Web3.toChecksumAddress(
            self.connection_manager.options['networks'][network]['addresses']['dex'])

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address,
                                                   min_order_amount)

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(Web3.toHex(tx_hash))
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class DexCancelationPenaltyRateChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/CancelationPenaltyRateChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/CancelationPenaltyRateChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.bin'))

    mode = 'DEX'

    def constructor(self,
                    cancelation_penalty_rate,
                    execute_change=False):

        network = self.connection_manager.network
        contract_address = Web3.toChecksumAddress(
            self.connection_manager.options['networks'][network]['addresses']['commissionManager'])

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address,
                                                   cancelation_penalty_rate)

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(Web3.toHex(tx_hash))
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class DexExpirationPenaltyRateChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/ExpirationPenaltyRateChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/ExpirationPenaltyRateChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.bin'))

    mode = 'DEX'

    def constructor(self,
                    expiration_penalty_rate,
                    execute_change=False):

        network = self.connection_manager.network
        contract_address = Web3.toChecksumAddress(
            self.connection_manager.options['networks'][network]['addresses']['commissionManager'])

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address,
                                                   expiration_penalty_rate)

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(Web3.toHex(tx_hash))
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class DexMinimumCommissionChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MinimumCommissionChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MinimumCommissionChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.bin'))

    mode = 'DEX'

    def constructor(self,
                    minimum_commission,
                    execute_change=False):

        network = self.connection_manager.network
        contract_address = Web3.toChecksumAddress(
            self.connection_manager.options['networks'][network]['addresses']['commissionManager'])

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address,
                                                   minimum_commission)

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(Web3.toHex(tx_hash))
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt
"""