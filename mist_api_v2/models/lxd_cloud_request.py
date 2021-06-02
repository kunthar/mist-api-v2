# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.lxd_credentials import LxdCredentials
from mist_api_v2 import util

from mist_api_v2.models.lxd_credentials import LxdCredentials  # noqa: E501

class LxdCloudRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, provider=None, credentials=None):  # noqa: E501
        """LxdCloudRequest - a model defined in OpenAPI

        :param provider: The provider of this LxdCloudRequest.  # noqa: E501
        :type provider: str
        :param credentials: The credentials of this LxdCloudRequest.  # noqa: E501
        :type credentials: LxdCredentials
        """
        self.openapi_types = {
            'provider': str,
            'credentials': LxdCredentials
        }

        self.attribute_map = {
            'provider': 'provider',
            'credentials': 'credentials'
        }

        self._provider = provider
        self._credentials = credentials

    @classmethod
    def from_dict(cls, dikt) -> 'LxdCloudRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LxdCloudRequest of this LxdCloudRequest.  # noqa: E501
        :rtype: LxdCloudRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provider(self):
        """Gets the provider of this LxdCloudRequest.


        :return: The provider of this LxdCloudRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this LxdCloudRequest.


        :param provider: The provider of this LxdCloudRequest.
        :type provider: str
        """
        allowed_values = ["lxd"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def credentials(self):
        """Gets the credentials of this LxdCloudRequest.


        :return: The credentials of this LxdCloudRequest.
        :rtype: LxdCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this LxdCloudRequest.


        :param credentials: The credentials of this LxdCloudRequest.
        :type credentials: LxdCredentials
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials
