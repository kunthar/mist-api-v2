# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.selector import Selector
from mist_api_v2 import util

from mist_api_v2.models.selector import Selector  # noqa: E501

class AddScheduleRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, description=None, task_enabled=None, action=None, params=None, resource_type=None, selectors=None, schedule_type=None, schedule_entry=None, start_after=None, run_immediately=None):  # noqa: E501
        """AddScheduleRequest - a model defined in OpenAPI

        :param name: The name of this AddScheduleRequest.  # noqa: E501
        :type name: str
        :param description: The description of this AddScheduleRequest.  # noqa: E501
        :type description: str
        :param task_enabled: The task_enabled of this AddScheduleRequest.  # noqa: E501
        :type task_enabled: bool
        :param action: The action of this AddScheduleRequest.  # noqa: E501
        :type action: str
        :param params: The params of this AddScheduleRequest.  # noqa: E501
        :type params: str
        :param resource_type: The resource_type of this AddScheduleRequest.  # noqa: E501
        :type resource_type: str
        :param selectors: The selectors of this AddScheduleRequest.  # noqa: E501
        :type selectors: List[Selector]
        :param schedule_type: The schedule_type of this AddScheduleRequest.  # noqa: E501
        :type schedule_type: str
        :param schedule_entry: The schedule_entry of this AddScheduleRequest.  # noqa: E501
        :type schedule_entry: str
        :param start_after: The start_after of this AddScheduleRequest.  # noqa: E501
        :type start_after: str
        :param run_immediately: The run_immediately of this AddScheduleRequest.  # noqa: E501
        :type run_immediately: bool
        """
        self.openapi_types = {
            'name': str,
            'description': str,
            'task_enabled': bool,
            'action': str,
            'params': str,
            'resource_type': str,
            'selectors': List[Selector],
            'schedule_type': str,
            'schedule_entry': str,
            'start_after': str,
            'run_immediately': bool
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'task_enabled': 'task_enabled',
            'action': 'action',
            'params': 'params',
            'resource_type': 'resource_type',
            'selectors': 'selectors',
            'schedule_type': 'schedule_type',
            'schedule_entry': 'schedule_entry',
            'start_after': 'start_after',
            'run_immediately': 'run_immediately'
        }

        self._name = name
        self._description = description
        self._task_enabled = task_enabled
        self._action = action
        self._params = params
        self._resource_type = resource_type
        self._selectors = selectors
        self._schedule_type = schedule_type
        self._schedule_entry = schedule_entry
        self._start_after = start_after
        self._run_immediately = run_immediately

    @classmethod
    def from_dict(cls, dikt) -> 'AddScheduleRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AddScheduleRequest of this AddScheduleRequest.  # noqa: E501
        :rtype: AddScheduleRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this AddScheduleRequest.


        :return: The name of this AddScheduleRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddScheduleRequest.


        :param name: The name of this AddScheduleRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this AddScheduleRequest.


        :return: The description of this AddScheduleRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddScheduleRequest.


        :param description: The description of this AddScheduleRequest.
        :type description: str
        """

        self._description = description

    @property
    def task_enabled(self):
        """Gets the task_enabled of this AddScheduleRequest.


        :return: The task_enabled of this AddScheduleRequest.
        :rtype: bool
        """
        return self._task_enabled

    @task_enabled.setter
    def task_enabled(self, task_enabled):
        """Sets the task_enabled of this AddScheduleRequest.


        :param task_enabled: The task_enabled of this AddScheduleRequest.
        :type task_enabled: bool
        """

        self._task_enabled = task_enabled

    @property
    def action(self):
        """Gets the action of this AddScheduleRequest.


        :return: The action of this AddScheduleRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AddScheduleRequest.


        :param action: The action of this AddScheduleRequest.
        :type action: str
        """
        allowed_values = ["reboot", "destroy", "notify", "start", "stop", "delete"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def params(self):
        """Gets the params of this AddScheduleRequest.


        :return: The params of this AddScheduleRequest.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this AddScheduleRequest.


        :param params: The params of this AddScheduleRequest.
        :type params: str
        """

        self._params = params

    @property
    def resource_type(self):
        """Gets the resource_type of this AddScheduleRequest.


        :return: The resource_type of this AddScheduleRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AddScheduleRequest.


        :param resource_type: The resource_type of this AddScheduleRequest.
        :type resource_type: str
        """
        allowed_values = ["machines", "volumes", "clusters", "networks"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def selectors(self):
        """Gets the selectors of this AddScheduleRequest.


        :return: The selectors of this AddScheduleRequest.
        :rtype: List[Selector]
        """
        return self._selectors

    @selectors.setter
    def selectors(self, selectors):
        """Sets the selectors of this AddScheduleRequest.


        :param selectors: The selectors of this AddScheduleRequest.
        :type selectors: List[Selector]
        """

        self._selectors = selectors

    @property
    def schedule_type(self):
        """Gets the schedule_type of this AddScheduleRequest.


        :return: The schedule_type of this AddScheduleRequest.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this AddScheduleRequest.


        :param schedule_type: The schedule_type of this AddScheduleRequest.
        :type schedule_type: str
        """
        allowed_values = ["crontab", "interval", "one_off"]  # noqa: E501
        if schedule_type not in allowed_values:
            raise ValueError(
                "Invalid value for `schedule_type` ({0}), must be one of {1}"
                .format(schedule_type, allowed_values)
            )

        self._schedule_type = schedule_type

    @property
    def schedule_entry(self):
        """Gets the schedule_entry of this AddScheduleRequest.

        format should be ΥΥΥΥ-ΜΜ-DD HH:MM:SS  # noqa: E501

        :return: The schedule_entry of this AddScheduleRequest.
        :rtype: str
        """
        return self._schedule_entry

    @schedule_entry.setter
    def schedule_entry(self, schedule_entry):
        """Sets the schedule_entry of this AddScheduleRequest.

        format should be ΥΥΥΥ-ΜΜ-DD HH:MM:SS  # noqa: E501

        :param schedule_entry: The schedule_entry of this AddScheduleRequest.
        :type schedule_entry: str
        """

        self._schedule_entry = schedule_entry

    @property
    def start_after(self):
        """Gets the start_after of this AddScheduleRequest.

        format should be ΥΥΥΥ-ΜΜ-DD HH:MM:SS  # noqa: E501

        :return: The start_after of this AddScheduleRequest.
        :rtype: str
        """
        return self._start_after

    @start_after.setter
    def start_after(self, start_after):
        """Sets the start_after of this AddScheduleRequest.

        format should be ΥΥΥΥ-ΜΜ-DD HH:MM:SS  # noqa: E501

        :param start_after: The start_after of this AddScheduleRequest.
        :type start_after: str
        """

        self._start_after = start_after

    @property
    def run_immediately(self):
        """Gets the run_immediately of this AddScheduleRequest.


        :return: The run_immediately of this AddScheduleRequest.
        :rtype: bool
        """
        return self._run_immediately

    @run_immediately.setter
    def run_immediately(self, run_immediately):
        """Sets the run_immediately of this AddScheduleRequest.


        :param run_immediately: The run_immediately of this AddScheduleRequest.
        :type run_immediately: bool
        """

        self._run_immediately = run_immediately
