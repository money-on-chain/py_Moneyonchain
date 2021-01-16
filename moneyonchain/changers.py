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

import logging

from moneyonchain.contract import ContractBase


class BaseChanger(ContractBase):
    log = logging.getLogger()
    contract_name = 'BaseChanger'

    contract_abi = None
    contract_bin = None

    contract_governor_abi = None
    contract_governor_bin = None

    mode = 'MoC'

    def __init__(self,
                 network_manager,
                 **tx_args):

        super().__init__(network_manager, **tx_args)


"""

class MoCSettlementChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCSettlementChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCSettlementChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.bin'))

    mode = 'RDoC'

    def constructor(self, input_block_span, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCSettlement']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address, input_block_span)

        self.log.info("Deployed contract done!")
        self.log.info(tx_hash)
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(tx_hash)
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class RDOCMoCSettlementChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCSettlementChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCSettlementChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.bin'))

    mode = 'RDoC'

    def constructor(self, input_block_span, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCSettlement']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address, input_block_span)

        self.log.info("Deployed contract done!")
        self.log.info(tx_hash)
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(tx_hash)
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class RDOCMoCInrateStableChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MocInrateStableChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MocInrateStableChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.bin'))

    mode = 'RDoC'

    def constructor(self, t_min, t_max, t_power, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCInrate']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address, t_min, t_max, t_power)

        self.log.info("Deployed contract done!")
        self.log.info(tx_hash)
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(tx_hash)
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class RDOCMoCInrateRiskproxChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCInrateRiskproxChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCInrateRiskproxChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.bin'))

    mode = 'RDoC'

    def constructor(self, t_min, t_max, t_power, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCInrate']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address, t_min, t_max, t_power)

        self.log.info("Deployed contract done!")
        self.log.info(tx_hash)
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(tx_hash)
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class RDOCMoCBucketContainerChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCBucketContainerChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCBucketContainerChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.bin'))

    mode = 'RDoC'

    def constructor(self, cobj_c0, cobj_x2, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCBProxManager']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address, cobj_c0, cobj_x2)

        self.log.info("Deployed contract done!")
        self.log.info(tx_hash)
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(tx_hash)
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class RDOCCommissionSplitterAddressChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/SetCommissionFinalAddressChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/SetCommissionFinalAddressChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.bin'))

    mode = 'RDoC'

    def constructor(self, commission_address, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['CommissionSplitter']
        commission_address = Web3.toChecksumAddress(commission_address)

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address, commission_address)

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


class RDOCPriceFeederAdderChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/PriceFeederAdder.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/PriceFeederAdder.bin'))

    contract_medianizer_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCMedianizer.abi'))
    contract_medianizer_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCMedianizer.bin'))

    contract_feedfactory_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/FeedFactory.abi'))
    contract_feedfactory_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/FeedFactory.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.bin'))

    mode = 'RDoC'

    def constructor(self, account_owner,
                    contract_address_medianizer=None,
                    contract_address_feedfactory=None,
                    execute_change=False):

        network = self.connection_manager.network
        if not contract_address_medianizer:
            contract_address_medianizer = self.connection_manager.options['networks'][network]['addresses']['oracle']
        if not contract_address_feedfactory:
            contract_address_feedfactory = self.connection_manager.options['networks'][network]['addresses']['FeedFactory']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(Web3.toChecksumAddress(contract_address_feedfactory),
                                                   Web3.toChecksumAddress(contract_address_medianizer),
                                                   Web3.toChecksumAddress(account_owner))

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


class RDOCPriceFeederRemoverChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/PriceFeederRemover.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/PriceFeederRemover.bin'))

    contract_medianizer_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCMedianizer.abi'))
    contract_medianizer_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCMedianizer.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.bin'))

    mode = 'RDoC'

    def constructor(self, contract_address_price_feed,
                    contract_address_medianizer=None,
                    execute_change=False):

        network = self.connection_manager.network
        if not contract_address_medianizer:
            contract_address_medianizer = self.connection_manager.options['networks'][network]['addresses']['oracle']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(Web3.toChecksumAddress(contract_address_medianizer),
                                                   Web3.toChecksumAddress(contract_address_price_feed))

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


class MoCPriceProviderChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/PriceProviderChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/PriceProviderChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.bin'))

    mode = 'MoC'

    def constructor(self, price_provider, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCState']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address, Web3.toChecksumAddress(price_provider))

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


class MoCSetCommissionMocProportionChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/SetCommissionMocProportionChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/SetCommissionMocProportionChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.bin'))

    mode = 'MoC'

    def constructor(self, moc_proportion, commission_splitter=None, execute_change=False):

        network = self.connection_manager.network
        if not commission_splitter:
            commission_splitter = self.connection_manager.options['networks'][network]['addresses']['CommissionSplitter']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(Web3.toChecksumAddress(commission_splitter), moc_proportion)

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


class MoCSetCommissionFinalAddressChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/SetCommissionFinalAddressChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/SetCommissionFinalAddressChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.bin'))

    mode = 'MoC'

    def constructor(self, commission_address, commission_splitter=None, execute_change=False):

        network = self.connection_manager.network
        if not commission_splitter:
            commission_splitter = self.connection_manager.options['networks'][network]['addresses']['CommissionSplitter']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(Web3.toChecksumAddress(commission_splitter),
                                                   Web3.toChecksumAddress(commission_address))

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


class MoCInrateCommissionsAddressChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/CommissionsAddressChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/CommissionsAddressChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.bin'))

    mode = 'MoC'

    def constructor(self, commission_address, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCInrate']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(Web3.toChecksumAddress(contract_address),
                                                   Web3.toChecksumAddress(commission_address))

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


class MoCInrateRiskProRateChangerChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCInrateRiskProRateChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCInrateRiskProRateChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.bin'))

    mode = 'MoC'

    def constructor(self, bitpro_rate, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCInrate']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(Web3.toChecksumAddress(contract_address),
                                                   bitpro_rate)

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


class MocInrateBitProInterestChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MocInrateBitProInterestChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MocInrateBitProInterestChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.bin'))

    mode = 'MoC'

    def constructor(self, bitpro_blockspan, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCInrate']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(Web3.toChecksumAddress(contract_address),
                                                   bitpro_blockspan)

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


class MocStateMaxMintBProChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MocStateMaxMintBProChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MocStateMaxMintBProChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.bin'))

    mode = 'MoC'

    def constructor(self, max_mint_bpro, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCState']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address, max_mint_bpro)

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


class RDOCMoCStateMaxMintRiskProChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCStateMaxMintRiskProChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCStateMaxMintRiskProChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.bin'))

    mode = 'MoC'

    def constructor(self, max_mint_riskpro, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCState']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address, max_mint_riskpro)

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


class MocMakeStoppableChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MocMakeStoppableChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MocMakeStoppableChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.bin'))

    mode = 'MoC'

    def constructor(self, stoppable=True, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoC']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address, stoppable)

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


class RDOCPriceProviderChanger(MoCPriceProviderChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/PriceProviderChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/PriceProviderChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.bin'))

    mode = 'RDoC'




class RDOCMocMakeStoppableChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MocMakeStoppableChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MocMakeStoppableChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.bin'))

    mode = 'RDOC'

    def constructor(self, stoppable=True, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoC']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address, stoppable)

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