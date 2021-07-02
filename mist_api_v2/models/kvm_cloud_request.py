# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.cloud_features import CloudFeatures
from mist_api_v2 import util

from mist_api_v2.models.cloud_features import CloudFeatures  # noqa: E501

class KvmCloudRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, provider=None, credentials=None, features=None):  # noqa: E501
        """KvmCloudRequest - a model defined in OpenAPI

        :param provider: The provider of this KvmCloudRequest.  # noqa: E501
        :type provider: str
        :param credentials: The credentials of this KvmCloudRequest.  # noqa: E501
        :type credentials: object
        :param features: The features of this KvmCloudRequest.  # noqa: E501
        :type features: CloudFeatures
        """
        self.openapi_types = {
            'provider': str,
            'credentials': object,
            'features': CloudFeatures
        }

        self.attribute_map = {
            'provider': 'provider',
            'credentials': 'credentials',
            'features': 'features'
        }

        self._provider = provider
        self._credentials = credentials
        self._features = features

    @classmethod
    def from_dict(cls, dikt) -> 'KvmCloudRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The KvmCloudRequest of this KvmCloudRequest.  # noqa: E501
        :rtype: KvmCloudRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provider(self):
        """Gets the provider of this KvmCloudRequest.


        :return: The provider of this KvmCloudRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this KvmCloudRequest.


        :param provider: The provider of this KvmCloudRequest.
        :type provider: str
        """
        allowed_values = ["kvm"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def credentials(self):
        """Gets the credentials of this KvmCloudRequest.


        :return: The credentials of this KvmCloudRequest.
        :rtype: object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this KvmCloudRequest.


        :param credentials: The credentials of this KvmCloudRequest.
        :type credentials: object
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    @property
    def features(self):
        """Gets the features of this KvmCloudRequest.


        :return: The features of this KvmCloudRequest.
        :rtype: CloudFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this KvmCloudRequest.


        :param features: The features of this KvmCloudRequest.
        :type features: CloudFeatures
        """

        self._features = features
