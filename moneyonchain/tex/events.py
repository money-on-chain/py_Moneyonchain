"""
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 THIS IS A PART OF MONEY ON CHAIN PACKAGE
 by Martin Mulone (martin.mulone@moneyonchain.com)

"""

from web3 import Web3
from web3.exceptions import BlockNotFound
import datetime

from moneyonchain.events import BaseEvent


# MoCDecentralizedExchange.sol


class DEXNewOrderAddedToPendingQueue(BaseEvent):

    name = "NewOrderAddedToPendingQueue"

    def __init__(self, connection_manager, event):

        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt #dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = None
        self.id = event['args']['id']
        self.notIndexedArgumentSoTheThingDoesntBreak = event['args']['notIndexedArgumentSoTheThingDoesntBreak']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'id', 'notIndexedArgumentSoTheThingDoesntBreak']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['id'] = self.id
        d_event['notIndexedArgumentSoTheThingDoesntBreak'] = self.notIndexedArgumentSoTheThingDoesntBreak

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['id'],
                d_event['notIndexedArgumentSoTheThingDoesntBreak']]


class DEXBuyerMatch(BaseEvent):
    name = "BuyerMatch"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            self.timestamp = ts - datetime.timedelta(hours=self.hours_delta)
        except BlockNotFound:
            self.timestamp = None

        self.orderId = event['args']['orderId']
        self.amountSent = event['args']['amountSent']
        self.commission = event['args']['commission']
        self.change = event['args']['change']
        self.received = event['args']['received']
        self.remainingAmount = event['args']['remainingAmount']
        self.matchPrice = event['args']['matchPrice']
        self.tickNumber = event['args']['tickNumber']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp',  'orderId', 'amountSent', 'commission', 'change', 'received',
                   'remainingAmount', 'matchPrice', 'tickNumber']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['orderId'] = self.orderId
        d_event['amountSent'] = Web3.fromWei(self.amountSent, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['change'] = Web3.fromWei(self.change, 'ether')
        d_event['received'] = Web3.fromWei(self.received, 'ether')
        d_event['remainingAmount'] = Web3.fromWei(self.remainingAmount, 'ether')
        d_event['matchPrice'] = Web3.fromWei(self.matchPrice, 'ether')
        d_event['tickNumber'] = self.tickNumber

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['orderId'],
                format(float(d_event['amountSent']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['change']), '.18f'),
                format(float(d_event['received']), '.18f'),
                format(float(d_event['remainingAmount']), '.18f'),
                format(float(d_event['matchPrice']), '.18f'),
                d_event['tickNumber']
                ]


class DEXSellerMatch(BaseEvent):
    name = "SellerMatch"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            self.timestamp = ts - datetime.timedelta(hours=self.hours_delta)
        except BlockNotFound:
            self.timestamp = None

        self.orderId = event['args']['orderId']
        self.amountSent = event['args']['amountSent']
        self.commission = event['args']['commission']
        self.received = event['args']['received']
        self.surplus = event['args']['surplus']
        self.remainingAmount = event['args']['remainingAmount']
        self.matchPrice = event['args']['matchPrice']
        self.tickNumber = event['args']['tickNumber']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp',  'orderId', 'amountSent', 'commission', 'received', 'surplus',
                   'remainingAmount', 'matchPrice', 'tickNumber']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['orderId'] = self.orderId
        d_event['amountSent'] = Web3.fromWei(self.amountSent, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['received'] = Web3.fromWei(self.received, 'ether')
        d_event['surplus'] = Web3.fromWei(self.surplus, 'ether')
        d_event['remainingAmount'] = Web3.fromWei(self.remainingAmount, 'ether')
        d_event['matchPrice'] = Web3.fromWei(self.matchPrice, 'ether')
        d_event['tickNumber'] = self.tickNumber

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['orderId'],
                format(float(d_event['amountSent']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['received']), '.18f'),
                format(float(d_event['surplus']), '.18f'),
                format(float(d_event['remainingAmount']), '.18f'),
                format(float(d_event['matchPrice']), '.18f'),
                d_event['tickNumber']
                ]


class DEXExpiredOrderProcessed(BaseEvent):
    name = "ExpiredOrderProcessed"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            self.timestamp = ts - datetime.timedelta(hours=self.hours_delta)
        except BlockNotFound:
            self.timestamp = None

        self.orderId = event['args']['orderId']
        self.owner = event['args']['owner']
        self.returnedAmount = event['args']['returnedAmount']
        self.commission = event['args']['commission']
        self.returnedCommission = event['args']['returnedCommission']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp',  'orderId', 'owner', 'returnedAmount', 'commission', 'returnedCommission']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['orderId'] = self.orderId
        d_event['owner'] = self.owner
        d_event['returnedAmount'] = Web3.fromWei(self.returnedAmount, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['returnedCommission'] = Web3.fromWei(self.returnedCommission, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['orderId'],
                d_event['owner'],
                format(float(d_event['returnedAmount']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['returnedCommission']), '.18f')
                ]


class DEXTickStart(BaseEvent):
    name = "TickStart"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            self.timestamp = ts - datetime.timedelta(hours=self.hours_delta)
        except BlockNotFound:
            self.timestamp = None

        self.baseTokenAddress = event['args']['baseTokenAddress']
        self.secondaryTokenAddress = event['args']['secondaryTokenAddress']
        self.number = event['args']['number']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'baseTokenAddress', 'secondaryTokenAddress', 'number']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['baseTokenAddress'] = self.baseTokenAddress
        d_event['secondaryTokenAddress'] = self.secondaryTokenAddress
        d_event['number'] = self.number

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['baseTokenAddress'],
                d_event['secondaryTokenAddress'],
                d_event['number']
                ]


class DEXTickEnd(BaseEvent):
    name = "TickEnd"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            self.timestamp = ts - datetime.timedelta(hours=self.hours_delta)
        except BlockNotFound:
            self.timestamp = None

        self.baseTokenAddress = event['args']['baseTokenAddress']
        self.secondaryTokenAddress = event['args']['secondaryTokenAddress']
        self.number = event['args']['number']
        self.nextTickBlock = event['args']['nextTickBlock']
        self.closingPrice = event['args']['closingPrice']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'baseTokenAddress', 'secondaryTokenAddress', 'number',
                   'nextTickBlock', 'closingPrice']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['baseTokenAddress'] = self.baseTokenAddress
        d_event['secondaryTokenAddress'] = self.secondaryTokenAddress
        d_event['number'] = self.number
        d_event['nextTickBlock'] = self.nextTickBlock
        d_event['closingPrice'] = Web3.fromWei(self.closingPrice, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['baseTokenAddress'],
                d_event['secondaryTokenAddress'],
                d_event['number'],
                d_event['nextTickBlock'],
                format(float(d_event['closingPrice']), '.18f')
                ]


class DEXNewOrderInserted(BaseEvent):
    name = "NewOrderInserted"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            self.timestamp = ts - datetime.timedelta(hours=self.hours_delta)
        except BlockNotFound:
            self.timestamp = None

        self.id = event['args']['id']
        self.sender = event['args']['sender']
        self.baseTokenAddress = event['args']['baseTokenAddress']
        self.secondaryTokenAddress = event['args']['secondaryTokenAddress']
        self.exchangeableAmount = event['args']['exchangeableAmount']
        self.reservedCommission = event['args']['reservedCommission']
        self.price = event['args']['price']
        self.multiplyFactor = event['args']['multiplyFactor']
        self.expiresInTick = event['args']['expiresInTick']
        self.isBuy = event['args']['isBuy']
        self.orderType = event['args']['orderType']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'id', 'sender', 'baseTokenAddress',
                   'secondaryTokenAddress', 'exchangeableAmount', 'reservedCommission',
                   'price', 'multiplyFactor', 'expiresInTick', 'isBuy', 'orderType']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['id'] = self.id
        d_event['sender'] = self.sender
        d_event['baseTokenAddress'] = self.baseTokenAddress
        d_event['secondaryTokenAddress'] = self.secondaryTokenAddress
        d_event['exchangeableAmount'] = Web3.fromWei(self.exchangeableAmount, 'ether')
        d_event['reservedCommission'] = Web3.fromWei(self.reservedCommission, 'ether')
        d_event['price'] = Web3.fromWei(self.price, 'ether')
        d_event['multiplyFactor'] = self.multiplyFactor
        d_event['expiresInTick'] = self.expiresInTick
        d_event['isBuy'] = self.isBuy
        d_event['orderType'] = self.orderType

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['id'],
                d_event['sender'],
                d_event['baseTokenAddress'],
                d_event['secondaryTokenAddress'],
                format(float(d_event['exchangeableAmount']), '.18f'),
                format(float(d_event['reservedCommission']), '.18f'),
                format(float(d_event['price']), '.18f'),
                d_event['multiplyFactor'],
                d_event['expiresInTick'],
                d_event['isBuy'],
                d_event['orderType']
                ]


class DEXOrderCancelled(BaseEvent):
    name = "OrderCancelled"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            self.timestamp = ts - datetime.timedelta(hours=self.hours_delta)
        except BlockNotFound:
            self.timestamp = None

        self.id = event['args']['id']
        self.sender = event['args']['sender']
        self.returnedAmount = event['args']['returnedAmount']
        self.commission = event['args']['commission']
        self.returnedCommission = event['args']['returnedCommission']
        self.isBuy = event['args']['isBuy']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'id', 'sender', 'returnedAmount',
                   'commission', 'returnedCommission', 'isBuy']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['id'] = self.id
        d_event['sender'] = self.sender
        d_event['returnedAmount'] = Web3.fromWei(self.returnedAmount, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['returnedCommission'] = Web3.fromWei(self.returnedCommission, 'ether')
        d_event['isBuy'] = self.isBuy

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['id'],
                d_event['sender'],
                format(float(d_event['returnedAmount']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['returnedCommission']), '.18f'),
                d_event['isBuy']
                ]


class DEXTransferFailed(BaseEvent):
    name = "TransferFailed"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            self.timestamp = ts - datetime.timedelta(hours=self.hours_delta)
        except BlockNotFound:
            self.timestamp = None

        self._tokenAddress = event['args']['_tokenAddress']
        self._to = event['args']['_to']
        self._amount = event['args']['_amount']
        self._isRevert = event['args']['_isRevert']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', '_tokenAddress', '_to', '_amount',
                   '_isRevert']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['_tokenAddress'] = self._tokenAddress
        d_event['_to'] = self._to
        d_event['_amount'] = Web3.fromWei(self._amount, 'ether')
        d_event['_isRevert'] = self._isRevert

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['_tokenAddress'],
                d_event['_to'],
                format(float(d_event['_amount']), '.18f'),
                d_event['_isRevert']
                ]


class DEXCommissionWithdrawn(BaseEvent):
    name = "CommissionWithdrawn"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            self.timestamp = ts - datetime.timedelta(hours=self.hours_delta)
        except BlockNotFound:
            self.timestamp = None

        self.token = event['args']['token']
        self.commissionBeneficiary = event['args']['commissionBeneficiary']
        self.withdrawnAmount = event['args']['withdrawnAmount']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'token', 'commissionBeneficiary', 'withdrawnAmount']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['token'] = self.token
        d_event['commissionBeneficiary'] = self.commissionBeneficiary
        d_event['withdrawnAmount'] = Web3.fromWei(self.withdrawnAmount, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['token'],
                d_event['commissionBeneficiary'],
                format(float(d_event['withdrawnAmount']), '.18f')
                ]


class DEXTokenPairDisabled(BaseEvent):
    name = "TokenPairDisabled"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            self.timestamp = ts - datetime.timedelta(hours=self.hours_delta)
        except BlockNotFound:
            self.timestamp = None

        self.baseToken = event['args']['baseToken']
        self.secondaryToken = event['args']['secondaryToken']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'baseToken', 'secondaryToken']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['baseToken'] = self.baseToken
        d_event['secondaryToken'] = self.secondaryToken

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['baseToken'],
                d_event['secondaryToken']
                ]


class DEXTokenPairEnabled(BaseEvent):
    name = "TokenPairEnabled"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            self.timestamp = ts - datetime.timedelta(hours=self.hours_delta)
        except BlockNotFound:
            self.timestamp = None

        self.baseToken = event['args']['baseToken']
        self.secondaryToken = event['args']['secondaryToken']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'baseToken', 'secondaryToken']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        if self.timestamp:
            d_event['timestamp'] = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            d_event['timestamp'] = ''
        d_event['baseToken'] = self.baseToken
        d_event['secondaryToken'] = self.secondaryToken

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['baseToken'],
                d_event['secondaryToken']
                ]
