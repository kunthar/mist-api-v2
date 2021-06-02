# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.alibaba_credentials import AlibabaCredentials
from mist_api_v2 import util

from mist_api_v2.models.alibaba_credentials import AlibabaCredentials  # noqa: E501

class AlibabaCloudRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, provider=None, credentials=None):  # noqa: E501
        """AlibabaCloudRequest - a model defined in OpenAPI

        :param provider: The provider of this AlibabaCloudRequest.  # noqa: E501
        :type provider: str
        :param credentials: The credentials of this AlibabaCloudRequest.  # noqa: E501
        :type credentials: AlibabaCredentials
        """
        self.openapi_types = {
            'provider': str,
            'credentials': AlibabaCredentials
        }

        self.attribute_map = {
            'provider': 'provider',
            'credentials': 'credentials'
        }

        self._provider = provider
        self._credentials = credentials

    @classmethod
    def from_dict(cls, dikt) -> 'AlibabaCloudRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AlibabaCloudRequest of this AlibabaCloudRequest.  # noqa: E501
        :rtype: AlibabaCloudRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provider(self):
        """Gets the provider of this AlibabaCloudRequest.


        :return: The provider of this AlibabaCloudRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this AlibabaCloudRequest.


        :param provider: The provider of this AlibabaCloudRequest.
        :type provider: str
        """
        allowed_values = ["alibaba"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def credentials(self):
        """Gets the credentials of this AlibabaCloudRequest.


        :return: The credentials of this AlibabaCloudRequest.
        :rtype: AlibabaCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this AlibabaCloudRequest.


        :param credentials: The credentials of this AlibabaCloudRequest.
        :type credentials: AlibabaCredentials
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials
