# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.age_selector import AgeSelector
from mist_api_v2.models.field_selector import FieldSelector
from mist_api_v2.models.resource_selector import ResourceSelector
from mist_api_v2.models.tagging_selector import TaggingSelector
from mist_api_v2 import util

from mist_api_v2.models.age_selector import AgeSelector  # noqa: E501
from mist_api_v2.models.field_selector import FieldSelector  # noqa: E501
from mist_api_v2.models.resource_selector import ResourceSelector  # noqa: E501
from mist_api_v2.models.tagging_selector import TaggingSelector  # noqa: E501

class Selector(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, ids=None, field=None, value=None, operator=None, include=None, minutes=None):  # noqa: E501
        """Selector - a model defined in OpenAPI

        :param type: The type of this Selector.  # noqa: E501
        :type type: str
        :param ids: The ids of this Selector.  # noqa: E501
        :type ids: List[str]
        :param field: The field of this Selector.  # noqa: E501
        :type field: str
        :param value: The value of this Selector.  # noqa: E501
        :type value: object
        :param operator: The operator of this Selector.  # noqa: E501
        :type operator: str
        :param include: The include of this Selector.  # noqa: E501
        :type include: List[str]
        :param minutes: The minutes of this Selector.  # noqa: E501
        :type minutes: int
        """
        self.openapi_types = {
            'type': str,
            'ids': List[str],
            'field': str,
            'value': object,
            'operator': str,
            'include': List[str],
            'minutes': int
        }

        self.attribute_map = {
            'type': 'type',
            'ids': 'ids',
            'field': 'field',
            'value': 'value',
            'operator': 'operator',
            'include': 'include',
            'minutes': 'minutes'
        }

        self._type = type
        self._ids = ids
        self._field = field
        self._value = value
        self._operator = operator
        self._include = include
        self._minutes = minutes

    @classmethod
    def from_dict(cls, dikt) -> 'Selector':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Selector of this Selector.  # noqa: E501
        :rtype: Selector
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this Selector.

        age type  # noqa: E501

        :return: The type of this Selector.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Selector.

        age type  # noqa: E501

        :param type: The type of this Selector.
        :type type: str
        """
        allowed_values = ["machines", "volumes", "clusters", "networks", "field", "tags", "age"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def ids(self):
        """Gets the ids of this Selector.

        a list of UUIDs in case type is resource like \"machines\", \"volumes\", \"clusters\" or \"networks\"  # noqa: E501

        :return: The ids of this Selector.
        :rtype: List[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this Selector.

        a list of UUIDs in case type is resource like \"machines\", \"volumes\", \"clusters\" or \"networks\"  # noqa: E501

        :param ids: The ids of this Selector.
        :type ids: List[str]
        """

        self._ids = ids

    @property
    def field(self):
        """Gets the field of this Selector.

        the name of the field  # noqa: E501

        :return: The field of this Selector.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this Selector.

        the name of the field  # noqa: E501

        :param field: The field of this Selector.
        :type field: str
        """

        self._field = field

    @property
    def value(self):
        """Gets the value of this Selector.

        the value of the field  # noqa: E501

        :return: The value of this Selector.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Selector.

        the value of the field  # noqa: E501

        :param value: The value of this Selector.
        :type value: object
        """

        self._value = value

    @property
    def operator(self):
        """Gets the operator of this Selector.

        one of equal (eq) and regular expression (regex) operators type  # noqa: E501

        :return: The operator of this Selector.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this Selector.

        one of equal (eq) and regular expression (regex) operators type  # noqa: E501

        :param operator: The operator of this Selector.
        :type operator: str
        """
        allowed_values = ["eq", "regex"]  # noqa: E501
        if operator not in allowed_values:
            raise ValueError(
                "Invalid value for `operator` ({0}), must be one of {1}"
                .format(operator, allowed_values)
            )

        self._operator = operator

    @property
    def include(self):
        """Gets the include of this Selector.

        a list of tags in case type is \"tags\"  # noqa: E501

        :return: The include of this Selector.
        :rtype: List[str]
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this Selector.

        a list of tags in case type is \"tags\"  # noqa: E501

        :param include: The include of this Selector.
        :type include: List[str]
        """

        self._include = include

    @property
    def minutes(self):
        """Gets the minutes of this Selector.

        an integer that represents the minutes passed from the creation of the resource  # noqa: E501

        :return: The minutes of this Selector.
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this Selector.

        an integer that represents the minutes passed from the creation of the resource  # noqa: E501

        :param minutes: The minutes of this Selector.
        :type minutes: int
        """

        self._minutes = minutes
