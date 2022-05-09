# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.response_metadata import ResponseMetadata
from mist_api_v2.models.schedule import Schedule
from mist_api_v2 import util

from mist_api_v2.models.response_metadata import ResponseMetadata  # noqa: E501
from mist_api_v2.models.schedule import Schedule  # noqa: E501

class ListSchedulesResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data=None, meta=None):  # noqa: E501
        """ListSchedulesResponse - a model defined in OpenAPI

        :param data: The data of this ListSchedulesResponse.  # noqa: E501
        :type data: List[Schedule]
        :param meta: The meta of this ListSchedulesResponse.  # noqa: E501
        :type meta: ResponseMetadata
        """
        self.openapi_types = {
            'data': List[Schedule],
            'meta': ResponseMetadata
        }

        self.attribute_map = {
            'data': 'data',
            'meta': 'meta'
        }

        self._data = data
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt) -> 'ListSchedulesResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListSchedulesResponse of this ListSchedulesResponse.  # noqa: E501
        :rtype: ListSchedulesResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this ListSchedulesResponse.


        :return: The data of this ListSchedulesResponse.
        :rtype: List[Schedule]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListSchedulesResponse.


        :param data: The data of this ListSchedulesResponse.
        :type data: List[Schedule]
        """

        self._data = data

    @property
    def meta(self):
        """Gets the meta of this ListSchedulesResponse.


        :return: The meta of this ListSchedulesResponse.
        :rtype: ResponseMetadata
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ListSchedulesResponse.


        :param meta: The meta of this ListSchedulesResponse.
        :type meta: ResponseMetadata
        """

        self._meta = meta
