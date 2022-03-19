# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class TagResourcesRequestTag(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, key=None, value=None, op=None):  # noqa: E501
        """TagResourcesRequestTag - a model defined in OpenAPI

        :param key: The key of this TagResourcesRequestTag.  # noqa: E501
        :type key: str
        :param value: The value of this TagResourcesRequestTag.  # noqa: E501
        :type value: str
        :param op: The op of this TagResourcesRequestTag.  # noqa: E501
        :type op: str
        """
        self.openapi_types = {
            'key': str,
            'value': str,
            'op': str
        }

        self.attribute_map = {
            'key': 'key',
            'value': 'value',
            'op': 'op'
        }

        self._key = key
        self._value = value
        self._op = op

    @classmethod
    def from_dict(cls, dikt) -> 'TagResourcesRequestTag':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TagResourcesRequest_tag of this TagResourcesRequestTag.  # noqa: E501
        :rtype: TagResourcesRequestTag
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self):
        """Gets the key of this TagResourcesRequestTag.


        :return: The key of this TagResourcesRequestTag.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TagResourcesRequestTag.


        :param key: The key of this TagResourcesRequestTag.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def value(self):
        """Gets the value of this TagResourcesRequestTag.


        :return: The value of this TagResourcesRequestTag.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TagResourcesRequestTag.


        :param value: The value of this TagResourcesRequestTag.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def op(self):
        """Gets the op of this TagResourcesRequestTag.


        :return: The op of this TagResourcesRequestTag.
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this TagResourcesRequestTag.


        :param op: The op of this TagResourcesRequestTag.
        :type op: str
        """
        allowed_values = ["+", "-"]  # noqa: E501
        if op not in allowed_values:
            raise ValueError(
                "Invalid value for `op` ({0}), must be one of {1}"
                .format(op, allowed_values)
            )

        self._op = op
