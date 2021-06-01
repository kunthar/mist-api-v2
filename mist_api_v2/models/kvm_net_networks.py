# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class KVMNetNetworks(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, network=None, ip=None, gateway=None, primary=None):  # noqa: E501
        """KVMNetNetworks - a model defined in OpenAPI

        :param network: The network of this KVMNetNetworks.  # noqa: E501
        :type network: str
        :param ip: The ip of this KVMNetNetworks.  # noqa: E501
        :type ip: str
        :param gateway: The gateway of this KVMNetNetworks.  # noqa: E501
        :type gateway: str
        :param primary: The primary of this KVMNetNetworks.  # noqa: E501
        :type primary: str
        """
        self.openapi_types = {
            'network': str,
            'ip': str,
            'gateway': str,
            'primary': str
        }

        self.attribute_map = {
            'network': 'network',
            'ip': 'ip',
            'gateway': 'gateway',
            'primary': 'primary'
        }

        self._network = network
        self._ip = ip
        self._gateway = gateway
        self._primary = primary

    @classmethod
    def from_dict(cls, dikt) -> 'KVMNetNetworks':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The KVMNet_networks of this KVMNetNetworks.  # noqa: E501
        :rtype: KVMNetNetworks
        """
        return util.deserialize_model(dikt, cls)

    @property
    def network(self):
        """Gets the network of this KVMNetNetworks.

        Name or ID of the network, if only this field is provided a dynamic IP address will be assigned  # noqa: E501

        :return: The network of this KVMNetNetworks.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this KVMNetNetworks.

        Name or ID of the network, if only this field is provided a dynamic IP address will be assigned  # noqa: E501

        :param network: The network of this KVMNetNetworks.
        :type network: str
        """
        if network is None:
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def ip(self):
        """Gets the ip of this KVMNetNetworks.

        The IPv4 address to statically assign to the interface  # noqa: E501

        :return: The ip of this KVMNetNetworks.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this KVMNetNetworks.

        The IPv4 address to statically assign to the interface  # noqa: E501

        :param ip: The ip of this KVMNetNetworks.
        :type ip: str
        """

        self._ip = ip

    @property
    def gateway(self):
        """Gets the gateway of this KVMNetNetworks.

        The IPv4 address for the default Gateway  # noqa: E501

        :return: The gateway of this KVMNetNetworks.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this KVMNetNetworks.

        The IPv4 address for the default Gateway  # noqa: E501

        :param gateway: The gateway of this KVMNetNetworks.
        :type gateway: str
        """

        self._gateway = gateway

    @property
    def primary(self):
        """Gets the primary of this KVMNetNetworks.

        The primary interface, which will be assigned a routing rule for the default GW  # noqa: E501

        :return: The primary of this KVMNetNetworks.
        :rtype: str
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this KVMNetNetworks.

        The primary interface, which will be assigned a routing rule for the default GW  # noqa: E501

        :param primary: The primary of this KVMNetNetworks.
        :type primary: str
        """

        self._primary = primary
