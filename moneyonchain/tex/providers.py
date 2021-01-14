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
from decimal import Decimal
from web3 import Web3
from web3.types import BlockIdentifier

from moneyonchain.contract import ContractBase
from moneyonchain.admin import ProxyAdmin


class BaseConstructor(Contract):
    log = logging.getLogger()

    contract_abi = None
    contract_bin = None

    mode = 'DEX'

    def __init__(self, connection_manager, contract_address=None, contract_abi=None, contract_bin=None):

        super().__init__(connection_manager,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

    def fnx_constructor(self, *tx_parameters, wait_receipt=True):
        """ Constructor deploy """

        sc, content_abi, content_bin = self.connection_manager.load_bytecode_contract(self.contract_abi,
                                                                                      self.contract_bin)
        tx_hash = self.connection_manager.fnx_constructor(sc, *tx_parameters)

        tx_receipt = None
        if wait_receipt:
            tx_receipt = self.connection_manager.wait_for_transaction_receipt(tx_hash)

        return tx_hash, tx_receipt


class TokenPriceProviderLastClosingPrice(BaseConstructor):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/TokenPriceProviderLastClosingPrice.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/TokenPriceProviderLastClosingPrice.bin'))

    mode = 'DEX'

    def constructor(self, base_token, secondary_token):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['dex']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(Web3.toChecksumAddress(contract_address),
                                                   Web3.toChecksumAddress(base_token),
                                                   Web3.toChecksumAddress(secondary_token)
                                                   )

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Contract Address: {address}".format(address=tx_receipt.contractAddress))

        return tx_hash, tx_receipt


class MocBproBtcPriceProviderFallback(BaseConstructor):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MocBproBtcPriceProviderFallback.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MocBproBtcPriceProviderFallback.bin'))

    mode = 'DEX'

    def constructor(self, moc_state, base_token, secondary_token):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['dex']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(Web3.toChecksumAddress(moc_state),
                                                   Web3.toChecksumAddress(contract_address),
                                                   Web3.toChecksumAddress(base_token),
                                                   Web3.toChecksumAddress(secondary_token)
                                                   )

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Contract Address: {address}".format(address=tx_receipt.contractAddress))

        return tx_hash, tx_receipt


class MocBproUsdPriceProviderFallback(BaseConstructor):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MocBproUsdPriceProviderFallback.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MocBproUsdPriceProviderFallback.bin'))

    mode = 'DEX'

    def constructor(self, moc_state, base_token, secondary_token):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['dex']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(Web3.toChecksumAddress(moc_state),
                                                   Web3.toChecksumAddress(contract_address),
                                                   Web3.toChecksumAddress(base_token),
                                                   Web3.toChecksumAddress(secondary_token)
                                                   )

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Contract Address: {address}".format(address=tx_receipt.contractAddress))

        return tx_hash, tx_receipt


class UnityPriceProvider(BaseConstructor):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/UnityPriceProvider.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/UnityPriceProvider.bin'))

    mode = 'DEX'

    def constructor(self):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['dex']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor()

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Contract Address: {address}".format(address=tx_receipt.contractAddress))

        return tx_hash, tx_receipt


class ExternalOraclePriceProviderFallback(BaseConstructor):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/ExternalOraclePriceProviderFallback.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/ExternalOraclePriceProviderFallback.bin'))

    mode = 'DEX'

    def constructor(self, external_price_provider, base_token, secondary_token):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['dex']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(Web3.toChecksumAddress(external_price_provider),
                                                   Web3.toChecksumAddress(contract_address),
                                                   Web3.toChecksumAddress(base_token),
                                                   Web3.toChecksumAddress(secondary_token)
                                                   )

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Contract Address: {address}".format(address=tx_receipt.contractAddress))

        return tx_hash, tx_receipt


class MocRiskProReservePriceProviderFallback(BaseConstructor):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MocRiskProReservePriceProviderFallback.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MocRiskProReservePriceProviderFallback.bin'))

    mode = 'DEX'

    def constructor(self, moc_state, base_token, secondary_token):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['dex']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(Web3.toChecksumAddress(moc_state),
                                                   Web3.toChecksumAddress(contract_address),
                                                   Web3.toChecksumAddress(base_token),
                                                   Web3.toChecksumAddress(secondary_token)
                                                   )

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Contract Address: {address}".format(address=tx_receipt.contractAddress))

        return tx_hash, tx_receipt


class MocRiskProUsdPriceProviderFallback(BaseConstructor):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MocRiskProUsdPriceProviderFallback.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/MocRiskProUsdPriceProviderFallback.bin'))

    mode = 'DEX'

    def constructor(self, moc_state, base_token, secondary_token):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['dex']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(Web3.toChecksumAddress(moc_state),
                                                   Web3.toChecksumAddress(contract_address),
                                                   Web3.toChecksumAddress(base_token),
                                                   Web3.toChecksumAddress(secondary_token)
                                                   )

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Contract Address: {address}".format(address=tx_receipt.contractAddress))

        return tx_hash, tx_receipt
