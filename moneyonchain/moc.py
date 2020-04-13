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
import datetime
from decimal import Decimal
from web3 import Web3
from web3.types import BlockIdentifier

from moneyonchain.contract import Contract


class MoCState(Contract):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCState.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCState.bin'))

    def __init__(self, connection_manager, contract_address=None, contract_abi=None, contract_bin=None):

        if not contract_address:
            # load from connection manager
            network = connection_manager.network
            contract_address = connection_manager.options['networks'][network]['addresses']['MoCState']

        super().__init__(connection_manager,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

        # finally load the contract
        self.load_contract()

    def blocks_to_settlement(self, formatted: bool = True,
                             block_identifier: BlockIdentifier = 'latest'):
        """Blocks to settlement"""

        result = self.sc.functions.blocksToSettlement().call(
            block_identifier=block_identifier)

        return result

    def bitcoin_price(self, formatted: bool = True,
                      block_identifier: BlockIdentifier = 'latest'):
        """Bitcoin price in USD"""

        result = self.sc.functions.getBitcoinPrice().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def bpro_price(self, formatted: bool = True,
                   block_identifier: BlockIdentifier = 'latest'):
        """BPro price in USD"""

        result = self.sc.functions.bproUsdPrice().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def bpro_tec_price(self, formatted: bool = True,
                       block_identifier: BlockIdentifier = 'latest'):
        """BPro Technical price in RBTC"""

        result = self.sc.functions.bproTecPrice().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def btc2x_tec_price(self, formatted: bool = True,
                        block_identifier: BlockIdentifier = 'latest'):
        """BTC2X Technical price in RBTC"""

        result = self.sc.functions.bucketBProTecPrice(str.encode('X2')).call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def bitcoin_moving_average(self, formatted: bool = True,
                               block_identifier: BlockIdentifier = 'latest'):
        """Bitcoin Moving Average price in USD"""

        result = self.sc.functions.getBitcoinMovingAverage().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def days_to_settlement(self, formatted: bool = True,
                           block_identifier: BlockIdentifier = 'latest'):
        """Days to settlement"""

        result = int(self.sc.functions.daysToSettlement().call(
            block_identifier=block_identifier))

        return result

    def global_coverage(self, formatted: bool = True,
                        block_identifier: BlockIdentifier = 'latest'):
        """Global coverage"""

        result = self.sc.functions.globalCoverage().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def bitpro_total_supply(self, formatted: bool = True,
                            block_identifier: BlockIdentifier = 'latest'):
        """Bitpro total supply"""

        result = self.sc.functions.bproTotalSupply().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def doc_total_supply(self, formatted: bool = True,
                         block_identifier: BlockIdentifier = 'latest'):
        """DOC total supply"""

        result = self.sc.functions.docTotalSupply().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result


class MoCInrate(Contract):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCInrate.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCInrate.bin'))

    precision = 10 ** 18

    def __init__(self, connection_manager, contract_address=None, contract_abi=None, contract_bin=None):

        if not contract_address:
            # load from connection manager
            network = connection_manager.network
            contract_address = connection_manager.options['networks'][network]['addresses']['MoCInrate']

        super().__init__(connection_manager,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

        # finally load the contract
        self.load_contract()

    def commision_rate(self, formatted: bool = True,
                       block_identifier: BlockIdentifier = 'latest'):
        """Gets commision rate"""

        result = self.sc.functions.getCommissionRate().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def bitpro_rate(self, formatted: bool = True,
                    block_identifier: BlockIdentifier = 'latest'):
        """Gets the rate for BitPro Holders"""

        result = self.sc.functions.getBitProRate().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def daily_inrate(self, formatted: bool = True,
                     block_identifier: BlockIdentifier = 'latest'):
        """returns the amount of BTC to pay in concept of interest"""

        result = self.sc.functions.dailyInrate().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def calc_commission_value(self, amount, formatted: bool = True):
        """ Calc commission value amount in ether float"""

        result = self.sc.functions.calcCommissionValue(int(amount * self.precision)).call()
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def calc_mint_interest_value(self, amount, formatted: bool = True):
        """ Calc interest value amount in ether float"""

        bucket = str.encode('X2')

        result = self.sc.functions.calcMintInterestValues(bucket, int(amount * self.precision)).call()
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result


class MoCExchange(Contract):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCExchange.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCExchange.bin'))

    def __init__(self, connection_manager, contract_address=None, contract_abi=None, contract_bin=None):

        if not contract_address:
            # load from connection manager
            network = connection_manager.network
            contract_address = connection_manager.options['networks'][network]['addresses']['MoCExchange']

        super().__init__(connection_manager,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

        # finally load the contract
        self.load_contract()


class MoCSettlement(Contract):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCSettlement.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCSettlement.bin'))

    def __init__(self, connection_manager, contract_address=None, contract_abi=None, contract_bin=None):

        if not contract_address:
            # load from connection manager
            network = connection_manager.network
            contract_address = connection_manager.options['networks'][network]['addresses']['MoCSettlement']

        super().__init__(connection_manager,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

        # finally load the contract
        self.load_contract()

    def next_block(self):
        return int(self.sc.functions.nextSettlementBlock().call())

    def is_enabled(self):
        return self.sc.functions.isSettlementEnabled().call()


class MoCConnector(Contract):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCConnector.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCConnector.bin'))

    def __init__(self, connection_manager, contract_address=None, contract_abi=None, contract_bin=None):

        if not contract_address:
            # load from connection manager
            network = connection_manager.network
            contract_address = connection_manager.options['networks'][network]['addresses']['MoCConnector']

        super().__init__(connection_manager,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

        # finally load the contract
        self.load_contract()

    def contracts_addresses(self):

        d_addresses = dict()
        d_addresses['MoC'] = self.sc.functions.moc().call()
        d_addresses['DoCToken'] = self.sc.functions.docToken().call()
        d_addresses['BProToken'] = self.sc.functions.bproToken().call()
        d_addresses['MoCBProxManager'] = self.sc.functions.bproxManager().call()
        d_addresses['MoCState'] = self.sc.functions.mocState().call()
        d_addresses['MoCConverter'] = self.sc.functions.mocConverter().call()
        d_addresses['MoCSettlement'] = self.sc.functions.mocSettlement().call()
        d_addresses['MoCExchange'] = self.sc.functions.mocExchange().call()
        d_addresses['MoCInrate'] = self.sc.functions.mocInrate().call()
        d_addresses['MoCBurnout'] = self.sc.functions.mocBurnout().call()

        return d_addresses


class MoC(Contract):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoC.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoC.bin'))

    precision = 10 ** 18

    def __init__(self, connection_manager,
                 contract_address=None,
                 contract_abi=None,
                 contract_bin=None,
                 contract_address_moc_state=None,
                 contract_address_moc_inrate=None,
                 contract_address_moc_exchange=None,
                 contract_address_moc_connector=None,
                 contract_address_moc_settlement=None):

        network = connection_manager.network
        if not contract_address:
            # load from connection manager
            contract_address = connection_manager.options['networks'][network]['addresses']['MoC']

        super().__init__(connection_manager,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

        # load main contract
        self.load_contract()

        # load contract moc state
        self.sc_moc_state = self.load_moc_state_contract(contract_address_moc_state)

        # load contract moc inrate
        self.sc_moc_inrate = self.load_moc_inrate_contract(contract_address_moc_inrate)

        # load contract moc exchange
        self.sc_moc_exchange = self.load_moc_exchange_contract(contract_address_moc_exchange)

        # load contract moc connector
        self.sc_moc_connector = self.load_moc_connector_contract(contract_address_moc_connector)

        # load contract moc settlement
        self.sc_moc_settlement = self.load_moc_settlement_contract(contract_address_moc_settlement)

    def load_moc_inrate_contract(self, contract_address):

        network = self.connection_manager.network
        if not contract_address:
            contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCInrate']

        sc = MoCInrate(self.connection_manager,
                       contract_address=contract_address)

        return sc

    def load_moc_state_contract(self, contract_address):

        network = self.connection_manager.network
        if not contract_address:
            contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCState']

        sc = MoCState(self.connection_manager,
                      contract_address=contract_address)

        return sc

    def load_moc_exchange_contract(self, contract_address):

        network = self.connection_manager.network
        if not contract_address:
            contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCExchange']

        sc = MoCExchange(self.connection_manager,
                         contract_address=contract_address)

        return sc

    def load_moc_connector_contract(self, contract_address):

        network = self.connection_manager.network
        if not contract_address:
            contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCConnector']

        sc = MoCConnector(self.connection_manager,
                          contract_address=contract_address)

        return sc

    def load_moc_settlement_contract(self, contract_address):

        network = self.connection_manager.network
        if not contract_address:
            contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCSettlement']

        sc = MoCSettlement(self.connection_manager,
                           contract_address=contract_address)

        return sc

    def connector(self):

        return self.sc.functions.connector().call()

    def connector_addresses(self):

        return self.sc_moc_connector.contracts_addresses()

    def settlement_remaining(self):

        def convert(seconds):
            min, sec = divmod(seconds, 60)
            hour, min = divmod(min, 60)
            return "%d:%02d:%02d" % (hour, min, sec)

        blocks_to_settlement = self.sc_moc_state.blocks_to_settlement()
        current_block_number = int(self.connection_manager.block_number)
        avg_block_time = 33.60  # this info is from  https://stats.testnet.rsk.co/
        remainin_estimated_seconds = avg_block_time * blocks_to_settlement
        estimated_time = datetime.datetime.now() + datetime.timedelta(seconds=remainin_estimated_seconds)

        print("Current Block: {0}".format(current_block_number))
        print("Current avg block time (seconds): {0}".format(avg_block_time))
        print("Blocks to settlement: {0}".format(blocks_to_settlement))
        print("Estimated remaining to settlement: {0}".format(convert(remainin_estimated_seconds)))
        print("Estimated settlement: {0}".format(estimated_time.strftime("%Y-%m-%d %H:%M:%S")))
        print("Next settlement block:{0}".format(self.sc_moc_settlement.next_block()))
        print("Is settlement enabled:{0}".format(self.sc_moc_settlement.is_enabled()))

    def bitcoin_price(self, formatted: bool = True,
                      block_identifier: BlockIdentifier = 'latest'):
        """Bitcoin price in USD"""

        result = self.sc_moc_state.bitcoin_price(formatted=formatted,
                                                 block_identifier=block_identifier)

        return result

    def bpro_price(self, formatted: bool = True,
                   block_identifier: BlockIdentifier = 'latest'):
        """BPro price in USD"""

        result = self.sc_moc_state.bpro_price(formatted=formatted,
                                              block_identifier=block_identifier)

        return result

    def btc2x_tec_price(self, formatted: bool = True,
                        block_identifier: BlockIdentifier = 'latest'):
        """BTC2x price in USD"""

        result = self.sc_moc_state.btc2x_tec_price(formatted=formatted,
                                                   block_identifier=block_identifier)

        return result

    def bpro_amount_in_usd(self, amount: Decimal):

        return self.bpro_price() * amount

    def btc2x_amount_in_usd(self, amount: Decimal):

        return self.btc2x_tec_price() * amount

    def paused(self, formatted: bool = True,
               block_identifier: BlockIdentifier = 'latest'):
        """is Paused"""

        result = self.sc.functions.paused().call(
            block_identifier=block_identifier)

        return result

    def amount_mint_bpro(self, amount: Decimal):
        """Final amount need it to mint bitpro in RBTC"""

        commission_value = self.sc_moc_inrate.calc_commission_value(amount)
        total_amount = amount + commission_value

        return total_amount, commission_value

    def amount_mint_doc(self, amount: Decimal):
        """Final amount need it to mint doc"""

        commission_value = self.sc_moc_inrate.calc_commission_value(amount)
        total_amount = amount + commission_value

        return total_amount, commission_value

    def amount_mint_btc2x(self, amount: Decimal):
        """Final amount need it to mint btc2x"""

        commission_value = self.sc_moc_inrate.calc_commission_value(amount)
        interest_value = self.sc_moc_inrate.calc_mint_interest_value(amount)
        total_amount = amount + commission_value + interest_value

        return total_amount, commission_value, interest_value

    def mint_bpro(self, amount: Decimal, default_account=None, wait_receipt=True):
        """ Mint amount bitpro
        NOTE: amount is in RBTC value
        """

        if amount <= Decimal(0.00000001):
            raise Exception("Value too low")

        total_amount, commission_value = self.amount_mint_bpro(amount)
        tx_hash = self.connection_manager.fnx_transaction(self.sc, 'mintBPro', int(amount * self.precision),
                                                          tx_params={'value': int(total_amount * self.precision)},
                                                          default_account=default_account)

        tx_receipt = None
        tx_logs = None
        if wait_receipt:
            # wait to transaction be mined
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            tx_logs = self.sc_moc_exchange.events.RiskProMint().processReceipt(tx_receipt)

        return tx_hash, tx_receipt, tx_logs

    def mint_doc(self, amount: Decimal, default_account=None, wait_receipt=True):
        """ Mint amount DOC
        NOTE: amount is in RBTC value
        """

        if amount <= Decimal(0.00000001):
            raise Exception("Value too low")

        total_amount, commission_value = self.amount_mint_doc(amount)
        tx_hash = self.connection_manager.fnx_transaction(self.sc, 'mintDoc', int(amount * self.precision),
                                                          tx_params={'value': int(total_amount * self.precision)},
                                                          default_account=default_account)

        tx_receipt = None
        tx_logs = None
        if wait_receipt:
            # wait to transaction be mined
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            tx_logs = self.sc_moc_exchange.events.StableTokenMint().processReceipt(tx_receipt)

        return tx_hash, tx_receipt, tx_logs

    def mint_btc2x(self, amount: Decimal, default_account=None, wait_receipt=True):
        """ Mint amount BTC2X
        NOTE: amount is in RBTC value
        """

        if amount <= Decimal(0.00000001):
            raise Exception("Value too low")

        total_amount, commission_value, interest_value = self.amount_mint_btc2x(amount)
        bucket = str.encode('X2')

        tx_hash = self.connection_manager.fnx_transaction(self.sc, 'mintBProx', bucket, int(amount * self.precision),
                                                          tx_params={'value': int(total_amount * self.precision)},
                                                          default_account=default_account)

        tx_receipt = None
        tx_logs = None
        if wait_receipt:
            # wait to transaction be mined
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            tx_logs = self.sc_moc_exchange.events.RiskProxMint().processReceipt(tx_receipt)

        return tx_hash, tx_receipt, tx_logs

    def reedeem_bpro(self, amount_token: Decimal, default_account=None, wait_receipt=True):
        """ Reedem BitPro amount of token """

        if amount_token <= Decimal(0.00000001):
            raise Exception("Value too low")

        tx_hash = self.connection_manager.fnx_transaction(self.sc, 'redeemBPro', int(amount_token * self.precision),
                                                          default_account=default_account)

        tx_receipt = None
        tx_logs = None
        if wait_receipt:
            # wait to transaction be mined
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            tx_logs = self.sc_moc_exchange.events.RiskProRedeem().processReceipt(tx_receipt)

        return tx_hash, tx_receipt, tx_logs

    def reedeem_free_doc(self, amount_token: Decimal, default_account=None, wait_receipt=True):
        """
        Reedem Free DOC amount of token
        Free Doc is Doc you can reedeem outside of settlement.
        """

        if amount_token <= Decimal(0.00000001):
            raise Exception("Value too low")

        tx_hash = self.connection_manager.fnx_transaction(self.sc, 'redeemFreeDoc', int(amount_token * self.precision),
                                                          default_account=default_account)

        tx_receipt = None
        tx_logs = None
        if wait_receipt:
            # wait to transaction be mined
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            tx_logs = self.sc_moc_exchange.events.FreeStableTokenRedeem().processReceipt(tx_receipt)

        return tx_hash, tx_receipt, tx_logs

    def reedeem_doc_request(self, amount_token: Decimal, default_account=None, wait_receipt=True):
        """
        Reedem DOC request amount of token
        This is the amount of doc you want to reedem on settlement.
        """

        if amount_token <= Decimal(0.00000001):
            raise Exception("Value too low")

        tx_hash = self.connection_manager.fnx_transaction(self.sc, 'redeemDocRequest',
                                                          int(amount_token * self.precision),
                                                          default_account=default_account)

        tx_receipt = None
        tx_logs = None
        if wait_receipt:
            # wait to transaction be mined
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            #tx_logs = self.sc_moc_exchange.events.FreeStableTokenRedeem().processReceipt(tx_receipt)

        return tx_hash, tx_receipt, tx_logs

    def reedeem_btc2x(self, amount_token: Decimal, default_account=None, wait_receipt=True):
        """ Reedem BTC2X amount of token """

        if amount_token <= 0.00000001:
            raise Exception("Value too low")

        bucket = str.encode('X2')

        tx_hash = self.connection_manager.fnx_transaction(self.sc, 'redeemBProx', bucket,
                                                          int(amount_token * self.precision),
                                                          default_account=default_account)

        tx_receipt = None
        tx_logs = None
        if wait_receipt:
            # wait to transaction be mined
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            tx_logs = self.sc_moc_exchange.events.RiskProxRedeem().processReceipt(tx_receipt)

        return tx_hash, tx_receipt, tx_logs
