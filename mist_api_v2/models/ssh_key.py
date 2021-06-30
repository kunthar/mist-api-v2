# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.ssh_key_one_of import SSHKeyOneOf
from mist_api_v2.models.ssh_key_one_of1 import SSHKeyOneOf1
from mist_api_v2.models.ssh_key_one_of2 import SSHKeyOneOf2
from mist_api_v2 import util

from mist_api_v2.models.ssh_key_one_of import SSHKeyOneOf  # noqa: E501
from mist_api_v2.models.ssh_key_one_of1 import SSHKeyOneOf1  # noqa: E501
from mist_api_v2.models.ssh_key_one_of2 import SSHKeyOneOf2  # noqa: E501

class SSHKey(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, key=None, user=None, port=None):  # noqa: E501
        """SSHKey - a model defined in OpenAPI

        :param key: The key of this SSHKey.  # noqa: E501
        :type key: str
        :param user: The user of this SSHKey.  # noqa: E501
        :type user: str
        :param port: The port of this SSHKey.  # noqa: E501
        :type port: int
        """
        self.openapi_types = {
            'key': str,
            'user': str,
            'port': int
        }

        self.attribute_map = {
            'key': 'key',
            'user': 'user',
            'port': 'port'
        }

        self._key = key
        self._user = user
        self._port = port

    @classmethod
    def from_dict(cls, dikt) -> 'SSHKey':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SSHKey of this SSHKey.  # noqa: E501
        :rtype: SSHKey
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self):
        """Gets the key of this SSHKey.

        Name or ID of the SSH key to deploy  # noqa: E501

        :return: The key of this SSHKey.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SSHKey.

        Name or ID of the SSH key to deploy  # noqa: E501

        :param key: The key of this SSHKey.
        :type key: str
        """

        self._key = key

    @property
    def user(self):
        """Gets the user of this SSHKey.

        SSH user  # noqa: E501

        :return: The user of this SSHKey.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SSHKey.

        SSH user  # noqa: E501

        :param user: The user of this SSHKey.
        :type user: str
        """

        self._user = user

    @property
    def port(self):
        """Gets the port of this SSHKey.

        SSH port  # noqa: E501

        :return: The port of this SSHKey.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SSHKey.

        SSH port  # noqa: E501

        :param port: The port of this SSHKey.
        :type port: int
        """

        self._port = port
