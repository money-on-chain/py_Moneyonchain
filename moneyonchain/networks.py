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
from typing import Tuple, Union
from web3 import Web3
from web3.types import BlockIdentifier

from brownie import network, web3
from brownie.network import accounts
from brownie._config import _get_data_folder


TYPE_NETWORK_GROUP = ('live', 'development', 'both')


def networks_from_config(filename=None):
    """ Networks from file config.json """

    if not filename:
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'networks.json')

    with open(filename) as f:
        options = json.load(f)

    return options


class BaseNetworkManager(object):

    log = logging.getLogger()

    @staticmethod
    def options_from_config(filename=None):
        """ Options from file config.json """

        if not filename:
            filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.json')

        with open(filename) as f:
            options = json.load(f)

        return options


class NetworkManager(BaseNetworkManager):

    log = logging.getLogger()
    options = BaseNetworkManager.options_from_config()
    default_account = 0

    def __init__(self,
                 connection_network='rskTesnetPublic',
                 config_network='mocTestnet',
                 options=None):

        self.connection_network = connection_network
        self.config_network = config_network
        self.accounts = accounts

        # options values
        if options:
            if isinstance(options, dict):
                self.options = options
            elif isinstance(options, str):
                self.options = self.options_from_config(filename=options)
            else:
                raise Exception("Not valid option value")

    def connect(self, connection_network=None):

        if not connection_network:
            connection_network = self.connection_network

        network.connect(connection_network)

        self.scan_accounts()

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

    def scan_accounts(self):
        """ Scan accounts from enviroment """

        self.accounts.clear()

        if 'ACCOUNT_PK_SECRET' in os.environ:
            # obtain from enviroment if exist instead
            private_key = os.environ['ACCOUNT_PK_SECRET']

            l_priv = private_key.split(',')
            if len(l_priv) > 1:
                # this is a method:
                # ACCOUNT_PK_SECRET=PK1,PK2,PK3
                for a_priv in l_priv:
                    self.accounts.add(a_priv)
            else:
                # Simple PK: ACCOUNT_PK_SECRET=PK
                self.accounts.add(private_key)

        if self.accounts:
            for acc in self.accounts:
                self.log.info("Added account address: {0}".format(acc.address))
        else:
            self.log.info("No address account added!")

    def set_default_account(self, index):
        """ Default index account """

        self.default_account = index

    @property
    def block_number(self):
        """ Last block number """
        return web3.eth.blockNumber

    @staticmethod
    def network_balance(address, block_identifier: BlockIdentifier = 'latest'):
        """ Balance of the address """
        return web3.eth.getBalance(Web3.toChecksumAddress(address), block_identifier=block_identifier)

    @staticmethod
    def all_events_from(sc, events_functions=None, from_block=0, to_block='latest'):

        if events_functions:
            if not isinstance(events_functions, list):
                raise Exception(
                    'events_functions must be a list of event functions like ["Event Name 1", "Event Name 2"]'
                )
        else:
            events_functions = list()
            for fn_events in sc.events:
                events_functions.append(fn_events.__name__)

        r_events = dict()
        for fn_events in sc.events:

            if fn_events.__name__ in events_functions:
                l_event = list()
                event_filter = fn_events.createFilter(fromBlock=from_block, toBlock=to_block)
                event_entries = event_filter.get_all_entries()
                for event_entry in event_entries:
                    if event_entry['event'] == fn_events.__name__:
                        l_event.append(event_entry)
                r_events[fn_events.__name__] = l_event
        return r_events

    def logs_from(self, sc, events_functions, from_block, to_block, block_steps=2880):

        last_block_number = int(self.block_number)

        if to_block <= 0:
            to_block = last_block_number  # last block number in the node

        current_block = from_block

        l_events = dict()
        while current_block <= to_block:

            step_end = current_block + block_steps
            if step_end > to_block:
                step_end = to_block

            self.log.info("Scanning blocks steps from {0} to {1}".format(current_block, step_end))

            events = self.all_events_from(sc,
                                          events_functions=events_functions,
                                          from_block=current_block,
                                          to_block=step_end)

            # Adjust current blocks to the next step
            current_block = current_block + block_steps

            # add to the list
            for fnx_name in events_functions:
                if fnx_name in events:
                    if events[fnx_name]:
                        if fnx_name not in l_events:
                            l_events[fnx_name] = list()
                        l_events[fnx_name].append(events[fnx_name])

        return l_events
