# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class PostDeployScript(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, params=None, script=None):  # noqa: E501
        """PostDeployScript - a model defined in OpenAPI

        :param params: The params of this PostDeployScript.  # noqa: E501
        :type params: str
        :param script: The script of this PostDeployScript.  # noqa: E501
        :type script: str
        """
        self.openapi_types = {
            'params': str,
            'script': str
        }

        self.attribute_map = {
            'params': 'params',
            'script': 'script'
        }

        self._params = params
        self._script = script

    @classmethod
    def from_dict(cls, dikt) -> 'PostDeployScript':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PostDeployScript of this PostDeployScript.  # noqa: E501
        :rtype: PostDeployScript
        """
        return util.deserialize_model(dikt, cls)

    @property
    def params(self):
        """Gets the params of this PostDeployScript.


        :return: The params of this PostDeployScript.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this PostDeployScript.


        :param params: The params of this PostDeployScript.
        :type params: str
        """

        self._params = params

    @property
    def script(self):
        """Gets the script of this PostDeployScript.

        Name or ID of the script to run  # noqa: E501

        :return: The script of this PostDeployScript.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this PostDeployScript.

        Name or ID of the script to run  # noqa: E501

        :param script: The script of this PostDeployScript.
        :type script: str
        """
        if script is None:
            raise ValueError("Invalid value for `script`, must not be `None`")  # noqa: E501

        self._script = script
