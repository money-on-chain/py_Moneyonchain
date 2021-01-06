"""
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 THIS IS A PART OF MONEY ON CHAIN PACKAGE
 by Martin Mulone (martin.mulone@moneyonchain.com)

"""

import yaml
import logging
import os
import json
from web3 import Web3
from web3.types import BlockIdentifier
from typing import Optional, Tuple, Union

from brownie import network, Contract
from brownie._config import _get_data_folder


TYPE_NETWORK_GROUP = ('live', 'development', 'both')


def networks_from_config(filename=None):
    """ Networks from file config.json """

    if not filename:
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'networks.json')

    with open(filename) as f:
        options = json.load(f)

    return options


def content_abi_file(abi_file):

    with open(abi_file) as f:
        abi = json.load(f)

    return abi


def content_bin_file(bin_file):

    with open(bin_file) as f:
        content_bin = f.read()

    return content_bin


class BitPROToken:

    log = logging.getLogger()
    precision = 10 ** 18

    contract_abi = content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/BProToken.abi'))
    contract_bin = content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/BProToken.bin'))

    def __init__(self, contract_name="BitPRO", contract_address=None, contract_abi=None, contract_bin=None):
        self.sc = Contract.from_abi(contract_name, contract_address, self.contract_abi)
        print(self.sc)

    def name(self):
        return self.sc.name()

    def symbol(self):
        return self.sc.symbol()

    def total_supply(self, formatted=True, block_identifier: BlockIdentifier = 'latest'):

        total = self.sc.totalSupply(block_identifier=block_identifier)
        if formatted:
            total = Web3.fromWei(total, 'ether')

        return total


class NetworkManager(object):

    log = logging.getLogger()

    def __init__(self, network_env='rskTesnetPublic'):

        # network enviroment
        self.network_env = network_env

    def connect(self, network_env=None):

        conn_network = network_env
        if not conn_network:
            conn_network = self.network_env

        network.connect(conn_network)

    @staticmethod
    def disconnect():

        network.disconnect()

    @staticmethod
    def is_connected() -> bool:

        return network.is_connected()

    @staticmethod
    def show_active():

        return network.show_active()

    @staticmethod
    def gas_limit(*args: Tuple[Union[int, str, bool, None]]) -> Union[int, bool]:

        return network.gas_limit(*args)

    @staticmethod
    def gas_price(*args: Tuple[Union[int, str, bool, None]]) -> Union[int, bool]:

        return network.gas_price(*args)

    @staticmethod
    def gas_buffer(*args: Tuple[float, None]) -> Union[float, None]:

        return network.gas_buffer(*args)

    @staticmethod
    def load_networks():

        networks = None
        with _get_data_folder().joinpath("network-config.yaml").open() as fp:
            networks = yaml.safe_load(fp)

        return networks

    @staticmethod
    def load_used_networks(filename=None):

        networks = networks_from_config(filename=filename)
        return networks

    def install(self,
                network_group='live',
                network_group_name="RskNetwork",
                path_to_network_config=None,
                force=False):

        if network_group not in TYPE_NETWORK_GROUP:
            raise Exception("Not valid type: Network group")

        # load current brownie networks
        current_networks = self.load_networks()

        used_networks = self.load_used_networks(filename=path_to_network_config)

        u_networks = used_networks[network_group]

        # check if already exist the networks group
        n_networks = list()
        for c_networks in current_networks[network_group]:
            if c_networks['name'] == network_group_name and not force:
                self.log.info("Already exist! Exitting....")
                return
            elif c_networks['name'] == network_group_name and force:
                self.log.info("Already exist! Deleting....")

            n_networks.append(c_networks)

        # install the network group name
        n_networks.append({"name": network_group_name, "networks": u_networks})

        current_networks[network_group] = n_networks

        # save to yaml
        with _get_data_folder().joinpath("network-config.yaml").open("w") as fp:
            yaml.dump(current_networks, fp)
