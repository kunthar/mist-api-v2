# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class ExpirationNotify(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None, period=None):  # noqa: E501
        """ExpirationNotify - a model defined in OpenAPI

        :param value: The value of this ExpirationNotify.  # noqa: E501
        :type value: int
        :param period: The period of this ExpirationNotify.  # noqa: E501
        :type period: str
        """
        self.openapi_types = {
            'value': int,
            'period': str
        }

        self.attribute_map = {
            'value': 'value',
            'period': 'period'
        }

        self._value = value
        self._period = period

    @classmethod
    def from_dict(cls, dikt) -> 'ExpirationNotify':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Expiration_notify of this ExpirationNotify.  # noqa: E501
        :rtype: ExpirationNotify
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self):
        """Gets the value of this ExpirationNotify.


        :return: The value of this ExpirationNotify.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ExpirationNotify.


        :param value: The value of this ExpirationNotify.
        :type value: int
        """

        self._value = value

    @property
    def period(self):
        """Gets the period of this ExpirationNotify.


        :return: The period of this ExpirationNotify.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ExpirationNotify.


        :param period: The period of this ExpirationNotify.
        :type period: str
        """
        allowed_values = ["minutes", "hours", "days"]  # noqa: E501
        if period not in allowed_values:
            raise ValueError(
                "Invalid value for `period` ({0}), must be one of {1}"
                .format(period, allowed_values)
            )

        self._period = period
