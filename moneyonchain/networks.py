"""
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 THIS IS A PART OF MONEY ON CHAIN PACKAGE
 by Martin Mulone (martin.mulone@moneyonchain.com)

"""

from pathlib import Path

import yaml
import logging

from brownie._config import _get_data_folder


USED_NETWORKS = {
    'development': [],
    'live': [
        {
            'chainid': 31,
            'explorer': 'https://blockscout.com/rsk/mainnet/api',
            'host': 'https://public-node.testnet.rsk.co',
            'id': 'rskTesnetPublic',
            'name': 'RSK Tesnet Public'
        },
        {
            'chainid': 31,
            'explorer': 'https://blockscout.com/rsk/mainnet/api',
            'host': 'http://moc-rsk-node-testnet.moneyonchain.com:4454/',
            'id': 'rskTesnetPrivate',
            'name': 'RSK Tesnet Private'
        },
        {
            'chainid': 31,
            'explorer': 'https://blockscout.com/rsk/mainnet/api',
            'host': 'http://localhost:4444',
            'id': 'rskTesnetLocal',
            'name': 'RSK Tesnet Local'
        },
        {
            'chainid': 30,
            'explorer': 'https://blockscout.com/rsk/mainnet/api',
            'host': 'https://public-node.rsk.co',
            'id': 'rskMainnetPublic',
            'name': 'RSK Mainnet Public'
        },
        {
            'chainid': 30,
            'explorer': 'https://blockscout.com/rsk/mainnet/api',
            'host': 'http://moc-rsk-node-mainnet.moneyonchain.com:4454/',
            'id': 'rskMainnetPrivate',
            'name': 'RSK Mainnet Private'
        },
        {
            'chainid': 30,
            'explorer': 'https://blockscout.com/rsk/mainnet/api',
            'host': 'http://localhost:4444',
            'id': 'rskMainnetLocal',
            'name': 'RSK Mainnet Local'
        }
    ]
}


TYPE_NETWORK_GROUP = ('live', 'development', 'both')


class NetworkManager(object):

    log = logging.getLogger()

    @staticmethod
    def load_networks():

        networks = None
        with _get_data_folder().joinpath("network-config.yaml").open() as fp:
            networks = yaml.safe_load(fp)

        return networks

    def install(self,
                network_group='live',
                network_group_name="RskNetwork",
                force=False):

        if network_group not in TYPE_NETWORK_GROUP:
            raise Exception("Not valid type: Network group")

        current_networks = self.load_networks()

        u_networks = USED_NETWORKS[network_group]
        #d_used_networks = dict()
        #for u_network in u_networks:
        #    d_used_networks[u_network['id']] = u_network

        # check if already exist the networks
        exist = False
        n_networks = list()
        for c_networks in current_networks[network_group]:
            if c_networks['name'] == network_group_name and not force:
                self.log.info("Already exist! Exitting....")
                return
            elif c_networks['name'] == network_group_name and force:
                self.log.info("Already exist! Deleting....")
                pass

            n_networks.append(c_networks)

        # install the network group name
        n_networks.append({"name": network_group_name, "networks": []})
        target = n_networks[-1]["networks"]

        # install all the networks id
        target.append(u_networks)

        # save to yaml
        with _get_data_folder().joinpath("network-config.yaml").open("w") as fp:
            yaml.dump(current_networks, fp)
