# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.base_schedule_entry import BaseScheduleEntry
from mist_api_v2.models.post_deploy_script import PostDeployScript
from mist_api_v2 import util

from mist_api_v2.models.base_schedule_entry import BaseScheduleEntry  # noqa: E501
from mist_api_v2.models.post_deploy_script import PostDeployScript  # noqa: E501

class BaseScheduleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, schedule_type=None, entry=None, script=None, action=None, description=None):  # noqa: E501
        """BaseScheduleAllOf - a model defined in OpenAPI

        :param schedule_type: The schedule_type of this BaseScheduleAllOf.  # noqa: E501
        :type schedule_type: str
        :param entry: The entry of this BaseScheduleAllOf.  # noqa: E501
        :type entry: BaseScheduleEntry
        :param script: The script of this BaseScheduleAllOf.  # noqa: E501
        :type script: PostDeployScript
        :param action: The action of this BaseScheduleAllOf.  # noqa: E501
        :type action: str
        :param description: The description of this BaseScheduleAllOf.  # noqa: E501
        :type description: str
        """
        self.openapi_types = {
            'schedule_type': str,
            'entry': BaseScheduleEntry,
            'script': PostDeployScript,
            'action': str,
            'description': str
        }

        self.attribute_map = {
            'schedule_type': 'schedule_type',
            'entry': 'entry',
            'script': 'script',
            'action': 'action',
            'description': 'description'
        }

        self._schedule_type = schedule_type
        self._entry = entry
        self._script = script
        self._action = action
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'BaseScheduleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BaseSchedule_allOf of this BaseScheduleAllOf.  # noqa: E501
        :rtype: BaseScheduleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def schedule_type(self):
        """Gets the schedule_type of this BaseScheduleAllOf.


        :return: The schedule_type of this BaseScheduleAllOf.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this BaseScheduleAllOf.


        :param schedule_type: The schedule_type of this BaseScheduleAllOf.
        :type schedule_type: str
        """
        allowed_values = ["one_off", "crontab", "interval"]  # noqa: E501
        if schedule_type not in allowed_values:
            raise ValueError(
                "Invalid value for `schedule_type` ({0}), must be one of {1}"
                .format(schedule_type, allowed_values)
            )

        self._schedule_type = schedule_type

    @property
    def entry(self):
        """Gets the entry of this BaseScheduleAllOf.


        :return: The entry of this BaseScheduleAllOf.
        :rtype: BaseScheduleEntry
        """
        return self._entry

    @entry.setter
    def entry(self, entry):
        """Sets the entry of this BaseScheduleAllOf.


        :param entry: The entry of this BaseScheduleAllOf.
        :type entry: BaseScheduleEntry
        """
        if entry is None:
            raise ValueError("Invalid value for `entry`, must not be `None`")  # noqa: E501

        self._entry = entry

    @property
    def script(self):
        """Gets the script of this BaseScheduleAllOf.


        :return: The script of this BaseScheduleAllOf.
        :rtype: PostDeployScript
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this BaseScheduleAllOf.


        :param script: The script of this BaseScheduleAllOf.
        :type script: PostDeployScript
        """

        self._script = script

    @property
    def action(self):
        """Gets the action of this BaseScheduleAllOf.


        :return: The action of this BaseScheduleAllOf.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BaseScheduleAllOf.


        :param action: The action of this BaseScheduleAllOf.
        :type action: str
        """
        allowed_values = ["start", "stop", "reboot", "destroy"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def description(self):
        """Gets the description of this BaseScheduleAllOf.


        :return: The description of this BaseScheduleAllOf.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BaseScheduleAllOf.


        :param description: The description of this BaseScheduleAllOf.
        :type description: str
        """

        self._description = description
