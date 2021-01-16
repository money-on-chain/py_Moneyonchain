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
from web3.types import BlockIdentifier
from moneyonchain.moc import MoC, MoCMedianizer
from moneyonchain.rdoc import RDOCMoC, RDOCMoCMedianizer
from moneyonchain.oracle import CoinPairPrice


class PriceProvider:

    log = logging.getLogger()
    precision = 10 ** 18

    def __init__(self, network_manager, contract_address=None):

        config_network = network_manager.config_network
        app_mode = network_manager.options['networks'][config_network]['app_mode']

        if app_mode == "RRC20":
            self.contract_MoC = RDOCMoC(network_manager,
                                        contract_address=contract_address,
                                        contracts_discovery=True)
        else:
            self.contract_MoC = MoC(network_manager,
                                    contract_address=contract_address,
                                    contracts_discovery=True)

        if config_network in ['mocTestnetAlpha', 'mocTestnet', 'rdocTestnetAlpha', 'rdocTestnet']:
            self.sc_Price_Provider = CoinPairPrice(
                network_manager,
                contract_address=self.contract_MoC.sc_moc_state.price_provider())
        else:
            if app_mode == "RRC20":
                self.sc_Price_Provider = MoCMedianizer(
                    network_manager,
                    contract_address=self.contract_MoC.sc_moc_state.price_provider())
            else:
                self.sc_Price_Provider = RDOCMoCMedianizer(
                    network_manager,
                    contract_address=self.contract_MoC.sc_moc_state.price_provider())

    def price(self, formatted: bool = True,
              block_identifier: BlockIdentifier = 'latest'):
        """Get price"""

        result = self.sc_Price_Provider.price(
            formatted=formatted,
            block_identifier=block_identifier)

        return result
