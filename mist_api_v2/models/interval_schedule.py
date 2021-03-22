# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class IntervalSchedule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, schedule_type=None, every=None, period=None, start_after=None, expires=None, max_run_count=None):  # noqa: E501
        """IntervalSchedule - a model defined in OpenAPI

        :param schedule_type: The schedule_type of this IntervalSchedule.  # noqa: E501
        :type schedule_type: str
        :param every: The every of this IntervalSchedule.  # noqa: E501
        :type every: int
        :param period: The period of this IntervalSchedule.  # noqa: E501
        :type period: str
        :param start_after: The start_after of this IntervalSchedule.  # noqa: E501
        :type start_after: datetime
        :param expires: The expires of this IntervalSchedule.  # noqa: E501
        :type expires: datetime
        :param max_run_count: The max_run_count of this IntervalSchedule.  # noqa: E501
        :type max_run_count: int
        """
        self.openapi_types = {
            'schedule_type': str,
            'every': int,
            'period': str,
            'start_after': datetime,
            'expires': datetime,
            'max_run_count': int
        }

        self.attribute_map = {
            'schedule_type': 'schedule_type',
            'every': 'every',
            'period': 'period',
            'start_after': 'start_after',
            'expires': 'expires',
            'max_run_count': 'max_run_count'
        }

        self._schedule_type = schedule_type
        self._every = every
        self._period = period
        self._start_after = start_after
        self._expires = expires
        self._max_run_count = max_run_count

    @classmethod
    def from_dict(cls, dikt) -> 'IntervalSchedule':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IntervalSchedule of this IntervalSchedule.  # noqa: E501
        :rtype: IntervalSchedule
        """
        return util.deserialize_model(dikt, cls)

    @property
    def schedule_type(self):
        """Gets the schedule_type of this IntervalSchedule.


        :return: The schedule_type of this IntervalSchedule.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this IntervalSchedule.


        :param schedule_type: The schedule_type of this IntervalSchedule.
        :type schedule_type: str
        """
        allowed_values = ["interval"]  # noqa: E501
        if schedule_type not in allowed_values:
            raise ValueError(
                "Invalid value for `schedule_type` ({0}), must be one of {1}"
                .format(schedule_type, allowed_values)
            )

        self._schedule_type = schedule_type

    @property
    def every(self):
        """Gets the every of this IntervalSchedule.


        :return: The every of this IntervalSchedule.
        :rtype: int
        """
        return self._every

    @every.setter
    def every(self, every):
        """Sets the every of this IntervalSchedule.


        :param every: The every of this IntervalSchedule.
        :type every: int
        """
        if every is None:
            raise ValueError("Invalid value for `every`, must not be `None`")  # noqa: E501

        self._every = every

    @property
    def period(self):
        """Gets the period of this IntervalSchedule.


        :return: The period of this IntervalSchedule.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this IntervalSchedule.


        :param period: The period of this IntervalSchedule.
        :type period: str
        """
        allowed_values = ["minutes", "hours", "days"]  # noqa: E501
        if period not in allowed_values:
            raise ValueError(
                "Invalid value for `period` ({0}), must be one of {1}"
                .format(period, allowed_values)
            )

        self._period = period

    @property
    def start_after(self):
        """Gets the start_after of this IntervalSchedule.

        The datetime when schedule should start running, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :return: The start_after of this IntervalSchedule.
        :rtype: datetime
        """
        return self._start_after

    @start_after.setter
    def start_after(self, start_after):
        """Sets the start_after of this IntervalSchedule.

        The datetime when schedule should start running, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :param start_after: The start_after of this IntervalSchedule.
        :type start_after: datetime
        """

        self._start_after = start_after

    @property
    def expires(self):
        """Gets the expires of this IntervalSchedule.

        The datetime when schedule should expire, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :return: The expires of this IntervalSchedule.
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this IntervalSchedule.

        The datetime when schedule should expire, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :param expires: The expires of this IntervalSchedule.
        :type expires: datetime
        """

        self._expires = expires

    @property
    def max_run_count(self):
        """Gets the max_run_count of this IntervalSchedule.


        :return: The max_run_count of this IntervalSchedule.
        :rtype: int
        """
        return self._max_run_count

    @max_run_count.setter
    def max_run_count(self, max_run_count):
        """Sets the max_run_count of this IntervalSchedule.


        :param max_run_count: The max_run_count of this IntervalSchedule.
        :type max_run_count: int
        """
        if max_run_count is not None and max_run_count < 1:  # noqa: E501
            raise ValueError("Invalid value for `max_run_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_run_count = max_run_count
