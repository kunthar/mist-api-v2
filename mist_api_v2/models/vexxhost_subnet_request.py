# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class VexxhostSubnetRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, provider=None, gateway_ip=None, ip_version=None, enable_dhcp=None, allocation_pools=None):  # noqa: E501
        """VexxhostSubnetRequest - a model defined in OpenAPI

        :param provider: The provider of this VexxhostSubnetRequest.  # noqa: E501
        :type provider: str
        :param gateway_ip: The gateway_ip of this VexxhostSubnetRequest.  # noqa: E501
        :type gateway_ip: str
        :param ip_version: The ip_version of this VexxhostSubnetRequest.  # noqa: E501
        :type ip_version: str
        :param enable_dhcp: The enable_dhcp of this VexxhostSubnetRequest.  # noqa: E501
        :type enable_dhcp: bool
        :param allocation_pools: The allocation_pools of this VexxhostSubnetRequest.  # noqa: E501
        :type allocation_pools: object
        """
        self.openapi_types = {
            'provider': str,
            'gateway_ip': str,
            'ip_version': str,
            'enable_dhcp': bool,
            'allocation_pools': object
        }

        self.attribute_map = {
            'provider': 'provider',
            'gateway_ip': 'gateway_ip',
            'ip_version': 'ip_version',
            'enable_dhcp': 'enable_dhcp',
            'allocation_pools': 'allocation_pools'
        }

        self._provider = provider
        self._gateway_ip = gateway_ip
        self._ip_version = ip_version
        self._enable_dhcp = enable_dhcp
        self._allocation_pools = allocation_pools

    @classmethod
    def from_dict(cls, dikt) -> 'VexxhostSubnetRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VexxhostSubnetRequest of this VexxhostSubnetRequest.  # noqa: E501
        :rtype: VexxhostSubnetRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provider(self):
        """Gets the provider of this VexxhostSubnetRequest.


        :return: The provider of this VexxhostSubnetRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this VexxhostSubnetRequest.


        :param provider: The provider of this VexxhostSubnetRequest.
        :type provider: str
        """
        allowed_values = ["vexxhost"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this VexxhostSubnetRequest.


        :return: The gateway_ip of this VexxhostSubnetRequest.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this VexxhostSubnetRequest.


        :param gateway_ip: The gateway_ip of this VexxhostSubnetRequest.
        :type gateway_ip: str
        """

        self._gateway_ip = gateway_ip

    @property
    def ip_version(self):
        """Gets the ip_version of this VexxhostSubnetRequest.


        :return: The ip_version of this VexxhostSubnetRequest.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this VexxhostSubnetRequest.


        :param ip_version: The ip_version of this VexxhostSubnetRequest.
        :type ip_version: str
        """
        allowed_values = ["IPv4", "IPv6"]  # noqa: E501
        if ip_version not in allowed_values:
            raise ValueError(
                "Invalid value for `ip_version` ({0}), must be one of {1}"
                .format(ip_version, allowed_values)
            )

        self._ip_version = ip_version

    @property
    def enable_dhcp(self):
        """Gets the enable_dhcp of this VexxhostSubnetRequest.


        :return: The enable_dhcp of this VexxhostSubnetRequest.
        :rtype: bool
        """
        return self._enable_dhcp

    @enable_dhcp.setter
    def enable_dhcp(self, enable_dhcp):
        """Sets the enable_dhcp of this VexxhostSubnetRequest.


        :param enable_dhcp: The enable_dhcp of this VexxhostSubnetRequest.
        :type enable_dhcp: bool
        """

        self._enable_dhcp = enable_dhcp

    @property
    def allocation_pools(self):
        """Gets the allocation_pools of this VexxhostSubnetRequest.


        :return: The allocation_pools of this VexxhostSubnetRequest.
        :rtype: object
        """
        return self._allocation_pools

    @allocation_pools.setter
    def allocation_pools(self, allocation_pools):
        """Sets the allocation_pools of this VexxhostSubnetRequest.


        :param allocation_pools: The allocation_pools of this VexxhostSubnetRequest.
        :type allocation_pools: object
        """

        self._allocation_pools = allocation_pools
