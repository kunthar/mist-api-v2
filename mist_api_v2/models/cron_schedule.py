# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.post_deploy_script import PostDeployScript
from mist_api_v2 import util

from mist_api_v2.models.post_deploy_script import PostDeployScript  # noqa: E501

class CronSchedule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, schedule_type=None, action=None, script=None, start_after=None, expires=None, max_run_count=None, description=None):  # noqa: E501
        """CronSchedule - a model defined in OpenAPI

        :param schedule_type: The schedule_type of this CronSchedule.  # noqa: E501
        :type schedule_type: str
        :param action: The action of this CronSchedule.  # noqa: E501
        :type action: str
        :param script: The script of this CronSchedule.  # noqa: E501
        :type script: PostDeployScript
        :param start_after: The start_after of this CronSchedule.  # noqa: E501
        :type start_after: datetime
        :param expires: The expires of this CronSchedule.  # noqa: E501
        :type expires: datetime
        :param max_run_count: The max_run_count of this CronSchedule.  # noqa: E501
        :type max_run_count: int
        :param description: The description of this CronSchedule.  # noqa: E501
        :type description: str
        """
        self.openapi_types = {
            'schedule_type': str,
            'action': str,
            'script': PostDeployScript,
            'start_after': datetime,
            'expires': datetime,
            'max_run_count': int,
            'description': str
        }

        self.attribute_map = {
            'schedule_type': 'schedule_type',
            'action': 'action',
            'script': 'script',
            'start_after': 'start_after',
            'expires': 'expires',
            'max_run_count': 'max_run_count',
            'description': 'description'
        }

        self._schedule_type = schedule_type
        self._action = action
        self._script = script
        self._start_after = start_after
        self._expires = expires
        self._max_run_count = max_run_count
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'CronSchedule':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CronSchedule of this CronSchedule.  # noqa: E501
        :rtype: CronSchedule
        """
        return util.deserialize_model(dikt, cls)

    @property
    def schedule_type(self):
        """Gets the schedule_type of this CronSchedule.


        :return: The schedule_type of this CronSchedule.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this CronSchedule.


        :param schedule_type: The schedule_type of this CronSchedule.
        :type schedule_type: str
        """
        allowed_values = ["crontab"]  # noqa: E501
        if schedule_type not in allowed_values:
            raise ValueError(
                "Invalid value for `schedule_type` ({0}), must be one of {1}"
                .format(schedule_type, allowed_values)
            )

        self._schedule_type = schedule_type

    @property
    def action(self):
        """Gets the action of this CronSchedule.


        :return: The action of this CronSchedule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CronSchedule.


        :param action: The action of this CronSchedule.
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
    def script(self):
        """Gets the script of this CronSchedule.


        :return: The script of this CronSchedule.
        :rtype: PostDeployScript
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this CronSchedule.


        :param script: The script of this CronSchedule.
        :type script: PostDeployScript
        """

        self._script = script

    @property
    def start_after(self):
        """Gets the start_after of this CronSchedule.

        Datetime when schedule should start running.  # noqa: E501

        :return: The start_after of this CronSchedule.
        :rtype: datetime
        """
        return self._start_after

    @start_after.setter
    def start_after(self, start_after):
        """Sets the start_after of this CronSchedule.

        Datetime when schedule should start running.  # noqa: E501

        :param start_after: The start_after of this CronSchedule.
        :type start_after: datetime
        """

        self._start_after = start_after

    @property
    def expires(self):
        """Gets the expires of this CronSchedule.

        Datetime when schedule should expire.  # noqa: E501

        :return: The expires of this CronSchedule.
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this CronSchedule.

        Datetime when schedule should expire.  # noqa: E501

        :param expires: The expires of this CronSchedule.
        :type expires: datetime
        """

        self._expires = expires

    @property
    def max_run_count(self):
        """Gets the max_run_count of this CronSchedule.


        :return: The max_run_count of this CronSchedule.
        :rtype: int
        """
        return self._max_run_count

    @max_run_count.setter
    def max_run_count(self, max_run_count):
        """Sets the max_run_count of this CronSchedule.


        :param max_run_count: The max_run_count of this CronSchedule.
        :type max_run_count: int
        """
        if max_run_count is not None and max_run_count < 1:  # noqa: E501
            raise ValueError("Invalid value for `max_run_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_run_count = max_run_count

    @property
    def description(self):
        """Gets the description of this CronSchedule.


        :return: The description of this CronSchedule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CronSchedule.


        :param description: The description of this CronSchedule.
        :type description: str
        """

        self._description = description
