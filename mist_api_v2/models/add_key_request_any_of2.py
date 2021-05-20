# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class AddKeyRequestAnyOf2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dry=None, generate=None):  # noqa: E501
        """AddKeyRequestAnyOf2 - a model defined in OpenAPI

        :param dry: The dry of this AddKeyRequestAnyOf2.  # noqa: E501
        :type dry: bool
        :param generate: The generate of this AddKeyRequestAnyOf2.  # noqa: E501
        :type generate: bool
        """
        self.openapi_types = {
            'dry': bool,
            'generate': bool
        }

        self.attribute_map = {
            'dry': 'dry',
            'generate': 'generate'
        }

        self._dry = dry
        self._generate = generate

    @classmethod
    def from_dict(cls, dikt) -> 'AddKeyRequestAnyOf2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AddKeyRequest_anyOf_2 of this AddKeyRequestAnyOf2.  # noqa: E501
        :rtype: AddKeyRequestAnyOf2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dry(self):
        """Gets the dry of this AddKeyRequestAnyOf2.

        Return generated key without actually adding it  # noqa: E501

        :return: The dry of this AddKeyRequestAnyOf2.
        :rtype: bool
        """
        return self._dry

    @dry.setter
    def dry(self, dry):
        """Sets the dry of this AddKeyRequestAnyOf2.

        Return generated key without actually adding it  # noqa: E501

        :param dry: The dry of this AddKeyRequestAnyOf2.
        :type dry: bool
        """
        if dry is None:
            raise ValueError("Invalid value for `dry`, must not be `None`")  # noqa: E501

        self._dry = dry

    @property
    def generate(self):
        """Gets the generate of this AddKeyRequestAnyOf2.

        Generate a keypair instead of providing one  # noqa: E501

        :return: The generate of this AddKeyRequestAnyOf2.
        :rtype: bool
        """
        return self._generate

    @generate.setter
    def generate(self, generate):
        """Sets the generate of this AddKeyRequestAnyOf2.

        Generate a keypair instead of providing one  # noqa: E501

        :param generate: The generate of this AddKeyRequestAnyOf2.
        :type generate: bool
        """
        if generate is None:
            raise ValueError("Invalid value for `generate`, must not be `None`")  # noqa: E501

        self._generate = generate
