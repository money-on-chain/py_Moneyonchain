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
from moneyonchain.governance import GovernedInterface, ProxyAdminInterface


BUCKET_X2 = '0x5832000000000000000000000000000000000000000000000000000000000000'
BUCKET_C0 = '0x4330000000000000000000000000000000000000000000000000000000000000'


class MoCInrateBase(GovernedInterface, ProxyAdminInterface):
    contract_name = 'MoCInrate'

    contract_abi = ContractBase.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCInrate.abi'))
    contract_bin = ContractBase.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCInrate.bin'))

    precision = 10 ** 18
    mode = 'MoC'
    project = 'MoC'

    def __init__(self,
                 network_manager,
                 contract_name=None,
                 contract_address=None,
                 contract_abi=None,
                 contract_bin=None):

        if not contract_address:
            config_network = network_manager.config_network
            contract_address = network_manager.options['networks'][config_network]['addresses']['MoCInrate']

        super().__init__(network_manager,
                         contract_name=contract_name,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

    def commision_rate(self, formatted: bool = True,
                       block_identifier: BlockIdentifier = 'latest'):
        """Gets commision rate"""

        raise Exception('DEPRECATED')

    def bitpro_rate(self, formatted: bool = True,
                    block_identifier: BlockIdentifier = 'latest'):
        """Gets the rate for BitPro/RiskProHolder Holders"""

        if self.mode == 'MoC':
            result = self.sc.getBitProRate(block_identifier=block_identifier)
        else:
            result = self.sc.getRiskProRate(block_identifier=block_identifier)

        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    # alias
    riskpro_rate = bitpro_rate

    def bitpro_interest_blockspan(self,
                                  block_identifier: BlockIdentifier = 'latest'):
        """Gets the blockspan of BPRO that represents the frecuency of BitPro holders intereset payment"""

        if self.mode == 'MoC':
            result = self.sc.getBitProInterestBlockSpan(block_identifier=block_identifier)
        else:
            result = self.sc.getRiskProInterestBlockSpan(block_identifier=block_identifier)

        return result

    # alias
    riskpro_interest_blockspan = bitpro_interest_blockspan

    def last_bitpro_interest_block(self,
                                   block_identifier: BlockIdentifier = 'latest'):
        """ Last block when an BitPro holders instereste was calculated"""

        if self.mode == 'MoC':
            result = self.sc.lastBitProInterestBlock(block_identifier=block_identifier)
        else:
            result = self.sc.lastRiskProInterestBlock(block_identifier=block_identifier)

        return result

    # alias
    last_riskpro_interest_block = last_bitpro_interest_block

    def daily_enabled(self,
                      formatted: bool = True,
                      block_identifier: BlockIdentifier = 'latest'):
        """"""

        result = self.sc.isDailyEnabled(block_identifier=block_identifier)

        return result

    def daily_inrate(self, formatted: bool = True,
                     block_identifier: BlockIdentifier = 'latest'):
        """returns the amount of BTC to pay in concept of interest"""

        result = self.sc.dailyInrate(block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def spot_inrate(self, formatted: bool = True,
                    block_identifier: BlockIdentifier = 'latest'):
        """"""

        result = self.sc.spotInrate(block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def commission_rate(self,
                        formatted: bool = True,
                        block_identifier: BlockIdentifier = 'latest'):
        """"""

        result = self.sc.getCommissionRate(block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def commission_address(self, block_identifier: BlockIdentifier = 'latest'):
        """Returns the address of the target receiver of commissions"""

        result = self.sc.commissionsAddress(block_identifier=block_identifier)

        return result

    def last_daily_pay(self,
                       formatted: bool = True,
                       block_identifier: BlockIdentifier = 'latest'):
        """returns the amount of BTC to pay in concept of interest"""

        result = self.sc.lastDailyPayBlock(block_identifier=block_identifier)

        return result

    def commission_rate_by_transaction_type(
            self,
            tx_type,
            formatted: bool = True,
            block_identifier: BlockIdentifier = 'latest'):
        """Gets commision rate by transaction type from mapping"""

        result = self.sc.commissionRatesByTxType(tx_type, block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def calc_commission_value(
            self,
            amount,
            tx_type,
            formatted: bool = True):
        """ Calc commission value amount in ether float"""

        if self.mode == 'MoC':
            result = self.sc.calcCommissionValue(int(amount * self.precision), tx_type)
        else:
            result = self.sc.calcCommissionValue(int(amount * self.precision))

        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def calc_mint_interest_value(self, amount,
                                 formatted: bool = True,
                                 precision: bool = True,
                                 block_identifier: BlockIdentifier = 'latest'):
        """ Calc interest value amount in ether float"""

        bucket = BUCKET_X2

        if precision:
            amount = int(amount * self.precision)
        result = self.sc.calcMintInterestValues(bucket, int(amount),
                                                block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def calc_bitpro_holders_interest(self, formatted: bool = True,
                                     block_identifier: BlockIdentifier = 'latest'):
        """ Calc bitpro holders interest"""

        if self.mode == 'MoC':
            result = self.sc.calculateBitProHoldersInterest(block_identifier=block_identifier)
        else:
            result = self.sc.calculateRiskProHoldersInterest(block_identifier=block_identifier)

        if formatted:
            result = [Web3.fromWei(result[0], 'ether'), Web3.fromWei(result[1], 'ether')]

        return result

    # alias
    calc_riskpro_holders_interest = calc_bitpro_holders_interest

    def bitpro_interest_address(self, formatted: bool = True,
                                block_identifier: BlockIdentifier = 'latest'):
        """ Calc bitpro holders interest"""

        if self.mode == 'MoC':
            result = self.sc.getBitProInterestAddress(block_identifier=block_identifier)
        else:
            result = self.sc.getRiskProInterestAddress(block_identifier=block_identifier)

        return result

    # alias
    riskpro_interest_address = bitpro_interest_address

    def is_bitpro_interest_enabled(self, formatted: bool = True,
                                   block_identifier: BlockIdentifier = 'latest'):
        """ Calc bitpro holders interest"""

        if self.mode == 'MoC':
            result = self.sc.isBitProInterestEnabled(block_identifier=block_identifier)
        else:
            result = self.sc.isRiskProInterestEnabled(block_identifier=block_identifier)

        return result

    # alias
    is_riskpro_interest_enabled = is_bitpro_interest_enabled

    def doc_inrate_avg(self,
                       amount,
                       formatted: bool = True,
                       block_identifier: BlockIdentifier = 'latest'):
        """ Calculates an average interest rate between after and before free doc Redemption"""

        if self.mode == 'MoC':
            result = self.sc.docInrateAvg(int(amount * self.precision), block_identifier=block_identifier)
        else:
            result = self.sc.stableTokenInrateAvg(int(amount * self.precision),
                                                  block_identifier=block_identifier)

        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    # alias
    stable_inrate_avg = doc_inrate_avg

    def btc2x_inrate_avg(self, amount, on_minting=False, formatted: bool = True,
                         block_identifier: BlockIdentifier = 'latest'):
        """ Calculates an average interest rate between after and before mint/redeem """

        bucket = BUCKET_X2

        if self.mode == 'MoC':
            result = self.sc.btcxInrateAvg(bucket, int(amount * self.precision), on_minting,
                                           block_identifier=block_identifier)
        else:
            result = self.sc.riskProxInrateAvg(bucket, int(amount * self.precision), on_minting,
                                               block_identifier=block_identifier)

        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    # alias
    riskprox_inrate_avg = btc2x_inrate_avg

    def doc_inrate(self,
                   formatted: bool = True,
                   block_identifier: BlockIdentifier = 'latest'):
        """Parameters inrate Doc"""

        info = dict()

        result = self.sc.getDoCTmax(block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')
        info['DoCTmax'] = result

        result = self.sc.getDoCPower(block_identifier=block_identifier)
        info['DoCPower'] = result

        result = self.sc.getDoCTmin(block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')
        info['DoCTmin'] = result

        return info

    # alias
    stable_inrate = doc_inrate

    def btcx_inrate(self,
                    formatted: bool = True,
                    block_identifier: BlockIdentifier = 'latest'):
        """Parameters inrate btcx"""

        info = dict()

        result = self.sc.getBtcxTmax(block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')
        info['BtcxTmax'] = result

        result = self.sc.getBtcxPower(block_identifier=block_identifier)
        info['BtcxPower'] = result

        result = self.sc.getBtcxTmin(block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')
        info['BtcxTmin'] = result

        return info

    # alias
    riskprox_inrate = btcx_inrate

    def calc_final_redeem_interest(self, amount,
                                   formatted: bool = True,
                                   precision: bool = True,
                                   block_identifier: BlockIdentifier = 'latest'):
        """ Calc interest value amount in ether float"""

        bucket = BUCKET_X2

        if precision:
            amount = int(amount * self.precision)
        result = self.sc.calcFinalRedeemInterestValue(bucket, int(amount),
                                                      block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def tx_type_mint_bpro_fees_rbtc(
            self,
            block_identifier: BlockIdentifier = 'latest'):

        if self.mode == 'MoC':
            result = self.sc.MINT_BPRO_FEES_RBTC(block_identifier=block_identifier)
        else:
            result = self.sc.MINT_RISKPRO_FEES_RESERVE(block_identifier=block_identifier)

        return result

    # alias
    tx_type_mint_riskpro_fees_rbtc = tx_type_mint_bpro_fees_rbtc

    def tx_type_redeem_bpro_fees_rbtc(
            self,
            block_identifier: BlockIdentifier = 'latest'):

        if self.mode == 'MoC':
            result = self.sc.REDEEM_BPRO_FEES_RBTC(block_identifier=block_identifier)
        else:
            result = self.sc.REDEEM_RISKPRO_FEES_RESERVE(block_identifier=block_identifier)

        return result

    # alias
    tx_type_redeem_riskpro_fees_rbtc = tx_type_redeem_bpro_fees_rbtc

    def tx_type_mint_doc_fees_rbtc(
            self,
            block_identifier: BlockIdentifier = 'latest'):

        if self.mode == 'MoC':
            result = self.sc.MINT_DOC_FEES_RBTC(block_identifier=block_identifier)
        else:
            result = self.sc.MINT_STABLETOKEN_FEES_RESERVE(block_identifier=block_identifier)

        return result

    # alias
    tx_type_mint_stabletoken_fees_rbtc = tx_type_mint_doc_fees_rbtc

    def tx_type_redeem_doc_fees_rbtc(
            self,
            block_identifier: BlockIdentifier = 'latest'):

        if self.mode == 'MoC':
            result = self.sc.REDEEM_DOC_FEES_RBTC(block_identifier=block_identifier)
        else:
            result = self.sc.REDEEM_STABLETOKEN_FEES_RESERVE(block_identifier=block_identifier)

        return result

    # alias
    tx_type_redeem_stabletoken_fees_rbtc = tx_type_redeem_doc_fees_rbtc

    def tx_type_mint_btcx_fees_rbtc(
            self,
            block_identifier: BlockIdentifier = 'latest'):

        if self.mode == 'MoC':
            result = self.sc.MINT_BTCX_FEES_RBTC(block_identifier=block_identifier)
        else:
            result = self.sc.MINT_RISKPROX_FEES_RESERVE(block_identifier=block_identifier)

        return result

    # alias
    tx_type_mint_riskprox_fees_rbtc = tx_type_mint_btcx_fees_rbtc

    def tx_type_redeem_btcx_fees_rbtc(
            self,
            block_identifier: BlockIdentifier = 'latest'):

        if self.mode == 'MoC':
            result = self.sc.REDEEM_BTCX_FEES_RBTC(block_identifier=block_identifier)
        else:
            result = self.sc.REDEEM_RISKPROX_FEES_RESERVE(block_identifier=block_identifier)

        return result

    # alias
    tx_type_redeem_riskprox_fees_rbtc = tx_type_redeem_btcx_fees_rbtc

    def tx_type_mint_bpro_fees_moc(
            self,
            block_identifier: BlockIdentifier = 'latest'):

        if self.mode == 'MoC':
            result = self.sc.MINT_BPRO_FEES_MOC(block_identifier=block_identifier)
        else:
            result = self.sc.MINT_RISKPRO_FEES_MOC(block_identifier=block_identifier)

        return result

    # alias
    tx_type_mint_riskpro_fees_moc = tx_type_mint_bpro_fees_moc

    def tx_type_redeem_bpro_fees_moc(
            self,
            block_identifier: BlockIdentifier = 'latest'):

        if self.mode == 'MoC':
            result = self.sc.REDEEM_BPRO_FEES_MOC(block_identifier=block_identifier)
        else:
            result = self.sc.REDEEM_RISKPRO_FEES_MOC(block_identifier=block_identifier)

        return result

    # alias
    tx_type_redeem_riskpro_fees_moc = tx_type_redeem_bpro_fees_moc

    def tx_type_mint_doc_fees_moc(
            self,
            block_identifier: BlockIdentifier = 'latest'):

        if self.mode == 'MoC':
            result = self.sc.MINT_DOC_FEES_MOC(block_identifier=block_identifier)
        else:
            result = self.sc.MINT_STABLETOKEN_FEES_MOC(block_identifier=block_identifier)

        return result

    # alias
    tx_type_mint_stabletoken_fees_moc = tx_type_mint_doc_fees_moc

    def tx_type_redeem_doc_fees_moc(
            self,
            block_identifier: BlockIdentifier = 'latest'):

        if self.mode == 'MoC':
            result = self.sc.REDEEM_DOC_FEES_MOC(block_identifier=block_identifier)
        else:
            result = self.sc.REDEEM_STABLETOKEN_FEES_MOC(block_identifier=block_identifier)

        return result

    # alias
    tx_type_redeem_stabletoken_fees_moc = tx_type_redeem_doc_fees_moc

    def tx_type_mint_btcx_fees_moc(
            self,
            block_identifier: BlockIdentifier = 'latest'):

        if self.mode == 'MoC':
            result = self.sc.MINT_BTCX_FEES_MOC(block_identifier=block_identifier)
        else:
            result = self.sc.MINT_RISKPROX_FEES_MOC(block_identifier=block_identifier)

        return result

    # alias
    tx_type_mint_riskprox_fees_moc = tx_type_mint_btcx_fees_moc

    def tx_type_redeem_btcx_fees_moc(
            self,
            block_identifier: BlockIdentifier = 'latest'):

        if self.mode == 'MoC':
            result = self.sc.REDEEM_BTCX_FEES_MOC(block_identifier=block_identifier)
        else:
            result = self.sc.REDEEM_RISKPROX_FEES_MOC(block_identifier=block_identifier)

        return result

    # alias
    tx_type_redeem_riskprox_fees_moc = tx_type_redeem_btcx_fees_moc

    def calculate_vendor_markup(
            self,
            vendor_account,
            amount,
            formatted: bool = True):
        """ Calc vendor markup in ether float"""

        if self.mode == 'MoC':
            result = self.sc.calculateVendorMarkup(vendor_account, int(amount * self.precision))
        else:
            raise NotImplementedError('Only supported in MoC mode')

        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result



