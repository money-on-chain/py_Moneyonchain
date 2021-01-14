"""
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 THIS IS A PART OF MONEY ON CHAIN PACKAGE
 by Martin Mulone (martin.mulone@moneyonchain.com)

"""

import logging
from web3 import Web3
from web3.exceptions import BlockNotFound
import datetime


class BaseEvent(object):
    name = "BaseEvent"
    hours_delta = 0

    @staticmethod
    def columns():
        raise NotImplementedError("Subclass must implement 'columns()' method")

    @staticmethod
    def row():
        raise NotImplementedError("Subclass must implement 'row()' method")

    def print_row(self):
        print('\t'.join(self.columns()))
        print('\t'.join(str(v) for v in self.row()))


class MoCExchangeRiskProMint(BaseEvent):

    name = "RiskProMint"

    def __init__(self, connection_manager, event):

        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None
        self.account = event['args']['account']
        self.amount = event['args']['amount']
        self.reserveTotal = event['args']['reserveTotal']
        self.commission = event['args']['commission']
        self.reservePrice = event['args']['reservePrice']
        self.mocCommissionValue = event['args']['mocCommissionValue']
        self.mocPrice = event['args']['mocPrice']
        self.btcMarkup = event['args']['btcMarkup']
        self.mocMarkup = event['args']['mocMarkup']
        self.vendorAccount = event['args']['vendorAccount']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'Account', 'Amount', 'reserveTotal', 'commission', 'reservePrice', 'mocCommissionValue', 'mocPrice', 'btcMarkup', 'mocMarkup', 'vendorAccount']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['account'] = self.account
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['reserveTotal'] = Web3.fromWei(self.reserveTotal, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')
        d_event['mocCommissionValue'] = Web3.fromWei(self.mocCommissionValue, 'ether')
        d_event['mocPrice'] = Web3.fromWei(self.mocPrice, 'ether')
        d_event['btcMarkup'] = Web3.fromWei(self.btcMarkup, 'ether')
        d_event['mocMarkup'] = Web3.fromWei(self.mocMarkup, 'ether')
        d_event['vendorAccount'] = self.vendorAccount

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account'],
                format(float(d_event['amount']), '.18f'),
                format(float(d_event['reserveTotal']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['reservePrice']), '.18f'),
                format(float(d_event['mocCommissionValue']), '.18f'),
                format(float(d_event['mocPrice']), '.18f'),
                format(float(d_event['btcMarkup']), '.18f'),
                format(float(d_event['mocMarkup']), '.18f'),
                d_event['vendorAccount']]

class MoCExchangeRiskProWithDiscountMint(BaseEvent):
    name = "RiskProWithDiscountMint"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  # dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None
        self.riskProTecPrice = event['args']['riskProTecPrice']
        self.riskProDiscountPrice = event['args']['riskProDiscountPrice']
        self.amount = event['args']['amount']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'riskProTecPrice', 'riskProDiscountPrice', 'amount']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['riskProTecPrice'] = Web3.fromWei(self.riskProTecPrice, 'ether')
        d_event['riskProDiscountPrice'] = Web3.fromWei(self.riskProDiscountPrice, 'ether')
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                format(float(d_event['riskProTecPrice']), '.18f'),
                format(float(d_event['riskProDiscountPrice']), '.18f'),
                format(float(d_event['amount']), '.18f')]


class MoCExchangeRiskProRedeem(BaseEvent):
    name = "RiskProRedeem"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None
        self.account = event['args']['account']
        self.amount = event['args']['amount']
        self.reserveTotal = event['args']['reserveTotal']
        self.commission = event['args']['commission']
        self.reservePrice = event['args']['reservePrice']
        self.mocCommissionValue = event['args']['mocCommissionValue']
        self.mocPrice = event['args']['mocPrice']
        self.btcMarkup = event['args']['btcMarkup']
        self.mocMarkup = event['args']['mocMarkup']
        self.vendorAccount = event['args']['vendorAccount']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'Account', 'amount', 'reserveTotal', 'commission', 'reservePrice', 'mocCommissionValue', 'mocPrice', 'btcMarkup', 'mocMarkup', 'vendorAccount']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['account'] = self.account
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['reserveTotal'] = Web3.fromWei(self.reserveTotal, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')
        d_event['mocCommissionValue'] = Web3.fromWei(self.mocCommissionValue, 'ether')
        d_event['mocPrice'] = Web3.fromWei(self.mocPrice, 'ether')
        d_event['btcMarkup'] = Web3.fromWei(self.btcMarkup, 'ether')
        d_event['mocMarkup'] = Web3.fromWei(self.mocMarkup, 'ether')
        d_event['vendorAccount'] = self.vendorAccount

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account'],
                format(float(d_event['amount']), '.18f'),
                format(float(d_event['reserveTotal']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['reservePrice']), '.18f'),
                format(float(d_event['mocCommissionValue']), '.18f'),
                format(float(d_event['mocPrice']), '.18f'),
                format(float(d_event['btcMarkup']), '.18f'),
                format(float(d_event['mocMarkup']), '.18f'),
                d_event['vendorAccount']]

class MoCExchangeStableTokenMint(BaseEvent):
    name = "StableTokenMint"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None
        self.account = event['args']['account']
        self.amount = event['args']['amount']
        self.reserveTotal = event['args']['reserveTotal']
        self.commission = event['args']['commission']
        self.reservePrice = event['args']['reservePrice']
        self.mocCommissionValue = event['args']['mocCommissionValue']
        self.mocPrice = event['args']['mocPrice']
        self.btcMarkup = event['args']['btcMarkup']
        self.mocMarkup = event['args']['mocMarkup']
        self.vendorAccount = event['args']['vendorAccount']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'Account', 'amount', 'reserveTotal', 'commission', 'reservePrice', 'mocCommissionValue', 'mocPrice', 'btcMarkup', 'mocMarkup', 'vendorAccount']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['account'] = self.account
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['reserveTotal'] = Web3.fromWei(self.reserveTotal, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')
        d_event['mocCommissionValue'] = Web3.fromWei(self.mocCommissionValue, 'ether')
        d_event['mocPrice'] = Web3.fromWei(self.mocPrice, 'ether')
        d_event['btcMarkup'] = Web3.fromWei(self.btcMarkup, 'ether')
        d_event['mocMarkup'] = Web3.fromWei(self.mocMarkup, 'ether')
        d_event['vendorAccount'] = self.vendorAccount

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account'],
                format(float(d_event['amount']), '.18f'),
                format(float(d_event['reserveTotal']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['reservePrice']), '.18f'),
                format(float(d_event['mocCommissionValue']), '.18f'),
                format(float(d_event['mocPrice']), '.18f'),
                format(float(d_event['btcMarkup']), '.18f'),
                format(float(d_event['mocMarkup']), '.18f'),
                d_event['vendorAccount']]

class MoCExchangeStableTokenRedeem(BaseEvent):
    name = "StableTokenRedeem"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt #  dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None
        self.account = event['args']['account']
        self.amount = event['args']['amount']
        self.reserveTotal = event['args']['reserveTotal']
        self.commission = event['args']['commission']
        self.reservePrice = event['args']['reservePrice']
        self.mocCommissionValue = event['args']['mocCommissionValue']
        self.mocPrice = event['args']['mocPrice']
        self.btcMarkup = event['args']['btcMarkup']
        self.mocMarkup = event['args']['mocMarkup']
        self.vendorAccount = event['args']['vendorAccount']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'Account', 'amount', 'reserveTotal', 'commission', 'reservePrice', 'mocCommissionValue', 'mocPrice', 'btcMarkup', 'mocMarkup', 'vendorAccount']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['account'] = self.account
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['reserveTotal'] = Web3.fromWei(self.reserveTotal, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')
        d_event['mocCommissionValue'] = Web3.fromWei(self.mocCommissionValue, 'ether')
        d_event['mocPrice'] = Web3.fromWei(self.mocPrice, 'ether')
        d_event['btcMarkup'] = Web3.fromWei(self.btcMarkup, 'ether')
        d_event['mocMarkup'] = Web3.fromWei(self.mocMarkup, 'ether')
        d_event['vendorAccount'] = self.vendorAccount

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account'],
                format(float(d_event['amount']), '.18f'),
                format(float(d_event['reserveTotal']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['reservePrice']), '.18f'),
                format(float(d_event['mocCommissionValue']), '.18f'),
                format(float(d_event['mocPrice']), '.18f'),
                format(float(d_event['btcMarkup']), '.18f'),
                format(float(d_event['mocMarkup']), '.18f'),
                d_event['vendorAccount']]

class MoCExchangeFreeStableTokenRedeem(BaseEvent):
    name = "FreeStableTokenRedeem"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  # dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None
        self.account = event['args']['account']
        self.amount = event['args']['amount']
        self.reserveTotal = event['args']['reserveTotal']
        self.commission = event['args']['commission']
        self.interests = event['args']['interests']
        self.reservePrice = event['args']['reservePrice']
        self.mocCommissionValue = event['args']['mocCommissionValue']
        self.mocPrice = event['args']['mocPrice']
        self.btcMarkup = event['args']['btcMarkup']
        self.mocMarkup = event['args']['mocMarkup']
        self.vendorAccount = event['args']['vendorAccount']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'Account', 'Amount', 'ReserveTotal', 'Commission', 'Interests', 'ReservePrice', 'MoCCommission', 'MoCPrice', 'BtcMarkup', 'MoCMarkup', 'VendorAccount']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['account'] = self.account
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['reserveTotal'] = Web3.fromWei(self.reserveTotal, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['interests'] = Web3.fromWei(self.interests, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')
        d_event['mocCommissionValue'] = Web3.fromWei(self.mocCommissionValue, 'ether')
        d_event['mocPrice'] = Web3.fromWei(self.mocPrice, 'ether')
        d_event['btcMarkup'] = Web3.fromWei(self.btcMarkup, 'ether')
        d_event['mocMarkup'] = Web3.fromWei(self.mocMarkup, 'ether')
        d_event['vendorAccount'] = self.vendorAccount

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account'],
                format(float(d_event['amount']), '.18f'),
                format(float(d_event['reserveTotal']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['interests']), '.18f'),
                format(float(d_event['reservePrice']), '.18f'),
                format(float(d_event['mocCommissionValue']), '.18f'),
                format(float(d_event['mocPrice']), '.18f'),
                format(float(d_event['btcMarkup']), '.18f'),
                format(float(d_event['mocMarkup']), '.18f'),
                d_event['vendorAccount']]

class MoCExchangeRiskProxMint(BaseEvent):
    name = "RiskProxMint"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None
        self.bucket = 'X2'
        self.account = event['args']['account']
        self.amount = event['args']['amount']
        self.reserveTotal = event['args']['reserveTotal']
        self.interests = event['args']['interests']
        self.leverage = event['args']['leverage']
        self.commission = event['args']['commission']
        self.reservePrice = event['args']['reservePrice']
        self.mocCommissionValue = event['args']['mocCommissionValue']
        self.mocPrice = event['args']['mocPrice']
        self.btcMarkup = event['args']['btcMarkup']
        self.mocMarkup = event['args']['mocMarkup']
        self.vendorAccount = event['args']['vendorAccount']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'Bucket', 'Account', 'Amount', 'Reserve Total', 'Interests',  'Leverage',  'Commission',  'Reserve Price', 'MoC Commission', 'MoC Price', 'Btc Markup', 'MoC Markup', 'Vendor Account']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['bucket'] = self.bucket
        d_event['account'] = self.account
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['reserveTotal'] = Web3.fromWei(self.reserveTotal, 'ether')
        d_event['interests'] = Web3.fromWei(self.interests, 'ether')
        d_event['leverage'] = Web3.fromWei(self.leverage, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')
        d_event['mocCommissionValue'] = Web3.fromWei(self.mocCommissionValue, 'ether')
        d_event['mocPrice'] = Web3.fromWei(self.mocPrice, 'ether')
        d_event['btcMarkup'] = Web3.fromWei(self.btcMarkup, 'ether')
        d_event['mocMarkup'] = Web3.fromWei(self.mocMarkup, 'ether')
        d_event['vendorAccount'] = self.vendorAccount

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['bucket'],
                d_event['account'],
                format(float(d_event['amount']), '.18f'),
                format(float(d_event['reserveTotal']), '.18f'),
                format(float(d_event['interests']), '.18f'),
                format(float(d_event['leverage']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['reservePrice']), '.18f'),
                format(float(d_event['mocCommissionValue']), '.18f'),
                format(float(d_event['mocPrice']), '.18f'),
                format(float(d_event['btcMarkup']), '.18f'),
                format(float(d_event['mocMarkup']), '.18f'),
                d_event['vendorAccount']]

class MoCExchangeRiskProxRedeem(BaseEvent):
    name = "RiskProxRedeem"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None
        self.bucket = 'X2'
        self.account = event['args']['account']
        self.commission = event['args']['commission']
        self.amount = event['args']['amount']
        self.reserveTotal = event['args']['reserveTotal']
        self.interests = event['args']['interests']
        self.leverage = event['args']['leverage']
        self.reservePrice = event['args']['reservePrice']
        self.mocCommissionValue = event['args']['mocCommissionValue']
        self.mocPrice = event['args']['mocPrice']
        self.btcMarkup = event['args']['btcMarkup']
        self.mocMarkup = event['args']['mocMarkup']
        self.vendorAccount = event['args']['vendorAccount']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'Bucket', 'Account', 'Amount', 'Reserve Total', 'Interests',  'Leverage',  'Commission',  'Reserve Price', 'MoC Commission', 'MoC Price', 'Btc Markup', 'MoC Markup', 'Vendor Account']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['bucket'] = self.bucket
        d_event['account'] = self.account
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['reserveTotal'] = Web3.fromWei(self.reserveTotal, 'ether')
        d_event['interests'] = Web3.fromWei(self.interests, 'ether')
        d_event['leverage'] = Web3.fromWei(self.leverage, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')
        d_event['mocCommissionValue'] = Web3.fromWei(self.mocCommissionValue, 'ether')
        d_event['mocPrice'] = Web3.fromWei(self.mocPrice, 'ether')
        d_event['btcMarkup'] = Web3.fromWei(self.btcMarkup, 'ether')
        d_event['mocMarkup'] = Web3.fromWei(self.mocMarkup, 'ether')
        d_event['vendorAccount'] = self.vendorAccount

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['bucket'],
                d_event['account'],
                format(float(d_event['amount']), '.18f'),
                format(float(d_event['reserveTotal']), '.18f'),
                format(float(d_event['interests']), '.18f'),
                format(float(d_event['leverage']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['reservePrice']), '.18f'),
                format(float(d_event['mocCommissionValue']), '.18f'),
                format(float(d_event['mocPrice']), '.18f'),
                format(float(d_event['btcMarkup']), '.18f'),
                format(float(d_event['mocMarkup']), '.18f'),
                d_event['vendorAccount']]

# SETTLEMENT

class MoCSettlementRedeemRequestProcessed(BaseEvent):
    name = "RedeemRequestProcessed"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.redeemer = event['args']['redeemer']
        self.commission = event['args']['commission']
        self.amount = event['args']['amount']

    @staticmethod
    def columns():
        columns = ['Block Nº',  'Timestamp', 'Account', 'Commission', 'Amount']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['redeemer'] = self.redeemer
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['redeemer'],
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['amount']), '.18f')]


class MoCSettlementSettlementRedeemStableToken(BaseEvent):
    name = "SettlementRedeemStableToken"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.queueSize = event['args']['queueSize']
        self.accumCommissions = event['args']['accumCommissions']
        self.reservePrice = event['args']['reservePrice']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'queueSize', 'accumCommissions', 'reservePrice']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['queueSize'] = self.queueSize
        d_event['accumCommissions'] = Web3.fromWei(self.accumCommissions, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['queueSize'],
                format(float(d_event['accumCommissions']), '.18f'),
                format(float(d_event['reservePrice']), '.18f')]


class MoCSettlementSettlementCompleted(BaseEvent):
    name = "SettlementCompleted"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None
        self.commissionsPayed = event['args']['commissionsPayed']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'commissionsPayed']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['commissionsPayed'] = Web3.fromWei(self.commissionsPayed, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                format(float(d_event['commissionsPayed']), '.18f')]


class MoCSettlementSettlementDeleveraging(BaseEvent):
    name = "SettlementDeleveraging"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.leverage = event['args']['leverage']
        self.riskProxPrice = event['args']['riskProxPrice']
        self.reservePrice = event['args']['reservePrice']
        self.startBlockNumber = event['args']['startBlockNumber']

    @staticmethod
    def columns():
        columns = ['Block Nº',  'Timestamp', 'leverage', 'riskProxPrice', 'reservePrice', 'startBlockNumber']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['leverage'] = Web3.fromWei(self.leverage, 'ether')
        d_event['riskProxPrice'] = Web3.fromWei(self.riskProxPrice, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')
        d_event['startBlockNumber'] = self.startBlockNumber

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                format(float(d_event['leverage']), '.18f'),
                format(float(d_event['riskProxPrice']), '.18f'),
                format(float(d_event['reservePrice']), '.18f'),
                d_event['startBlockNumber']]


class MoCSettlementSettlementStarted(BaseEvent):
    name = "SettlementStarted"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.stableTokenRedeemCount = event['args']['stableTokenRedeemCount']
        self.deleveragingCount = event['args']['deleveragingCount']
        self.riskProxPrice = event['args']['riskProxPrice']
        self.reservePrice = event['args']['reservePrice']

    @staticmethod
    def columns():
        columns = ['Block Nº',  'Timestamp', 'stableTokenRedeemCount', 'deleveragingCount', 'riskProxPrice', 'reservePrice']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['stableTokenRedeemCount'] = self.stableTokenRedeemCount
        d_event['deleveragingCount'] = self.deleveragingCount
        d_event['riskProxPrice'] = Web3.fromWei(self.riskProxPrice, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['stableTokenRedeemCount'],
                d_event['deleveragingCount'],
                format(float(d_event['riskProxPrice']), '.18f'),
                format(float(d_event['reservePrice']), '.18f')]


class MoCSettlementRedeemRequestAlter(BaseEvent):
    name = "RedeemRequestAlter"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.redeemer = event['args']['redeemer']
        self.isAddition = event['args']['isAddition']
        self.delta = event['args']['delta']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp',  'address', 'isAddition', 'delta']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['redeemer'] = self.redeemer
        d_event['isAddition'] = self.isAddition
        d_event['delta'] = Web3.fromWei(self.delta, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['redeemer'],
                d_event['isAddition'],
                format(float(d_event['delta']), '.18f')]


class MoCInrateDailyPay(BaseEvent):
    name = "InrateDailyPay"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            self.timestamp = ts - datetime.timedelta(hours=self.hours_delta)
            #self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.amount = event['args']['amount']
        self.daysToSettlement = event['args']['daysToSettlement']
        self.nReserveBucketC0 = event['args']['nReserveBucketC0']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp',  'Amount', 'daysToSettlement', 'nReserveBucketC0']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['daysToSettlement'] = self.daysToSettlement
        d_event['nReserveBucketC0'] = Web3.fromWei(self.nReserveBucketC0, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                format(float(d_event['amount']), '.18f'),
                d_event['daysToSettlement'],
                format(float(d_event['nReserveBucketC0']), '.18f')]


class MoCInrateRiskProHoldersInterestPay(BaseEvent):
    name = "RiskProHoldersInterestPay"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            self.timestamp = ts - datetime.timedelta(hours=self.hours_delta)
            # self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.amount = event['args']['amount']
        self.nReserveBucketC0BeforePay = event['args']['nReserveBucketC0BeforePay']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp',  'Amount', 'nReserveBucketC0BeforePay']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['nReserveBucketC0BeforePay'] = Web3.fromWei(self.nReserveBucketC0BeforePay, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                format(float(d_event['amount']), '.18f'),
                format(float(d_event['nReserveBucketC0BeforePay']), '.18f')]


class ERC20Transfer(BaseEvent):
    name = "Transfer"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.value = event['args']['value']
        self.e_from = event['args']['from']
        self.e_to = event['args']['to']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp',  'Value', 'From', 'To']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['value'] = Web3.fromWei(self.value, 'ether')
        d_event['e_from'] = Web3.fromWei(self.e_from, 'ether')
        d_event['e_to'] = Web3.fromWei(self.e_to, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                format(float(d_event['value']), '.18f'),
                d_event['e_from'],
                d_event['e_to']]


class ERC20Approval(BaseEvent):
    name = "Approval"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            self.timestamp = ts - datetime.timedelta(hours=self.hours_delta)
        except BlockNotFound:
            self.timestamp = None

        self.owner = event['args']['owner']
        self.spender = event['args']['spender']
        self.value = event['args']['value']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp',  'owner', 'spender', 'value']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['owner'] = self.owner
        d_event['spender'] = self.spender
        d_event['value'] = Web3.fromWei(self.value, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['owner'],
                d_event['spender'],
                format(float(d_event['value']), '.18f')]


class MoCBucketLiquidation(BaseEvent):
    name = "BucketLiquidation"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.bucket = event['args']['bucket']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp',  'bucket']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['bucket'] = self.bucket

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['bucket']
                ]


class MoCStateStateTransition(BaseEvent):
    name = "StateTransition"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.newState = event['args']['newState']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'newState']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['newState'] = self.newState

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['newState']
                ]

class MoCStateBtcPriceProviderUpdated(BaseEvent):
    name = "BtcPriceProviderUpdated"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.oldAddress = event['args']['oldAddress']
        self.newAddress = event['args']['newAddress']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'oldAddress', 'newAddress']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['oldAddress'] = self.oldAddress
        d_event['newAddress'] = self.newAddress

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['oldAddress'],
                d_event['newAddress']
                ]

class MoCStateMoCPriceProviderUpdated(BaseEvent):
    name = "MoCPriceProviderUpdated"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.oldAddress = event['args']['oldAddress']
        self.newAddress = event['args']['newAddress']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'oldAddress', 'newAddress']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['oldAddress'] = self.oldAddress
        d_event['newAddress'] = self.newAddress

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['oldAddress'],
                d_event['newAddress']
                ]

class MoCStateMoCTokenChanged(BaseEvent):
    name = "MoCTokenChanged"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.mocTokenAddress = event['args']['mocTokenAddress']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'mocTokenAddress']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['mocTokenAddress'] = self.mocTokenAddress

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['mocTokenAddress']
                ]

class MoCStateMoCVendorsChanged(BaseEvent):
    name = "MoCVendorsChanged"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.mocVendorsAddress = event['args']['mocVendorsAddress']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'mocVendorsAddress']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['mocVendorsAddress'] = self.mocVendorsAddress

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['mocVendorsAddress']
                ]

class MoCVendorsVendorRegistered(BaseEvent):
    name = "VendorRegistered"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.account = event['args']['account']
        self.markup = event['args']['markup']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'account', 'markup']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['account'] = self.account
        d_event['markup'] = Web3.fromWei(self.markup, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account'],
                format(float(d_event['markup']), '.18f')
                ]

class MoCVendorsVendorUpdated(BaseEvent):
    name = "VendorUpdated"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.account = event['args']['account']
        self.markup = event['args']['markup']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'account', 'markup']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['account'] = self.account
        d_event['markup'] = Web3.fromWei(self.markup, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account'],
                format(float(d_event['markup']), '.18f')
                ]

class MoCVendorsVendorUnregistered(BaseEvent):
    name = "VendorUnregistered"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.account = event['args']['account']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'account']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['account'] = self.account

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account']
                ]

class MoCVendorsVendorStakeAdded(BaseEvent):
    name = "VendorStakeAdded"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.account = event['args']['account']
        self.staking = event['args']['staking']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'account', 'staking']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['account'] = self.account
        d_event['staking'] = Web3.fromWei(self.staking, 'staking')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account'],
                format(float(d_event['staking']), '.18f')
                ]

class MoCVendorsVendorStakeRemoved(BaseEvent):
    name = "VendorStakeRemoved"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.account = event['args']['account']
        self.staking = event['args']['staking']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'account', 'staking']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['account'] = self.account
        d_event['staking'] = Web3.fromWei(self.staking, 'staking')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account'],
                format(float(d_event['staking']), '.18f')
                ]

class MoCVendorsTotalPaidInMoCReset(BaseEvent):
    name = "TotalPaidInMoCReset"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt  #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None

        self.account = event['args']['account']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'account']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['account'] = self.account

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account']
                ]