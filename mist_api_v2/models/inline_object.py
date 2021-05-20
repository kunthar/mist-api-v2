# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.cloud_credentials import CloudCredentials
from mist_api_v2.models.cloud_features import CloudFeatures
from mist_api_v2 import util

from mist_api_v2.models.cloud_credentials import CloudCredentials  # noqa: E501
from mist_api_v2.models.cloud_features import CloudFeatures  # noqa: E501

class InlineObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, credentials=None, features=None, title=None):  # noqa: E501
        """InlineObject - a model defined in OpenAPI

        :param credentials: The credentials of this InlineObject.  # noqa: E501
        :type credentials: CloudCredentials
        :param features: The features of this InlineObject.  # noqa: E501
        :type features: CloudFeatures
        :param title: The title of this InlineObject.  # noqa: E501
        :type title: str
        """
        self.openapi_types = {
            'credentials': CloudCredentials,
            'features': CloudFeatures,
            'title': str
        }

        self.attribute_map = {
            'credentials': 'credentials',
            'features': 'features',
            'title': 'title'
        }

        self._credentials = credentials
        self._features = features
        self._title = title

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object of this InlineObject.  # noqa: E501
        :rtype: InlineObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def credentials(self):
        """Gets the credentials of this InlineObject.


        :return: The credentials of this InlineObject.
        :rtype: CloudCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this InlineObject.


        :param credentials: The credentials of this InlineObject.
        :type credentials: CloudCredentials
        """

        self._credentials = credentials

    @property
    def features(self):
        """Gets the features of this InlineObject.


        :return: The features of this InlineObject.
        :rtype: CloudFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this InlineObject.


        :param features: The features of this InlineObject.
        :type features: CloudFeatures
        """

        self._features = features

    @property
    def title(self):
        """Gets the title of this InlineObject.

        Updated title  # noqa: E501

        :return: The title of this InlineObject.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineObject.

        Updated title  # noqa: E501

        :param title: The title of this InlineObject.
        :type title: str
        """

        self._title = title
