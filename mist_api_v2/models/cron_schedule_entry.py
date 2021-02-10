# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class CronScheduleEntry(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, minute=None, hour=None, day_of_month=None, month_of_year=None, day_of_week=None):  # noqa: E501
        """CronScheduleEntry - a model defined in OpenAPI

        :param minute: The minute of this CronScheduleEntry.  # noqa: E501
        :type minute: str
        :param hour: The hour of this CronScheduleEntry.  # noqa: E501
        :type hour: str
        :param day_of_month: The day_of_month of this CronScheduleEntry.  # noqa: E501
        :type day_of_month: str
        :param month_of_year: The month_of_year of this CronScheduleEntry.  # noqa: E501
        :type month_of_year: str
        :param day_of_week: The day_of_week of this CronScheduleEntry.  # noqa: E501
        :type day_of_week: str
        """
        self.openapi_types = {
            'minute': str,
            'hour': str,
            'day_of_month': str,
            'month_of_year': str,
            'day_of_week': str
        }

        self.attribute_map = {
            'minute': 'minute',
            'hour': 'hour',
            'day_of_month': 'day_of_month',
            'month_of_year': 'month_of_year',
            'day_of_week': 'day_of_week'
        }

        self._minute = minute
        self._hour = hour
        self._day_of_month = day_of_month
        self._month_of_year = month_of_year
        self._day_of_week = day_of_week

    @classmethod
    def from_dict(cls, dikt) -> 'CronScheduleEntry':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CronSchedule_entry of this CronScheduleEntry.  # noqa: E501
        :rtype: CronScheduleEntry
        """
        return util.deserialize_model(dikt, cls)

    @property
    def minute(self):
        """Gets the minute of this CronScheduleEntry.


        :return: The minute of this CronScheduleEntry.
        :rtype: str
        """
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Sets the minute of this CronScheduleEntry.


        :param minute: The minute of this CronScheduleEntry.
        :type minute: str
        """

        self._minute = minute

    @property
    def hour(self):
        """Gets the hour of this CronScheduleEntry.


        :return: The hour of this CronScheduleEntry.
        :rtype: str
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Sets the hour of this CronScheduleEntry.


        :param hour: The hour of this CronScheduleEntry.
        :type hour: str
        """

        self._hour = hour

    @property
    def day_of_month(self):
        """Gets the day_of_month of this CronScheduleEntry.


        :return: The day_of_month of this CronScheduleEntry.
        :rtype: str
        """
        return self._day_of_month

    @day_of_month.setter
    def day_of_month(self, day_of_month):
        """Sets the day_of_month of this CronScheduleEntry.


        :param day_of_month: The day_of_month of this CronScheduleEntry.
        :type day_of_month: str
        """

        self._day_of_month = day_of_month

    @property
    def month_of_year(self):
        """Gets the month_of_year of this CronScheduleEntry.


        :return: The month_of_year of this CronScheduleEntry.
        :rtype: str
        """
        return self._month_of_year

    @month_of_year.setter
    def month_of_year(self, month_of_year):
        """Sets the month_of_year of this CronScheduleEntry.


        :param month_of_year: The month_of_year of this CronScheduleEntry.
        :type month_of_year: str
        """

        self._month_of_year = month_of_year

    @property
    def day_of_week(self):
        """Gets the day_of_week of this CronScheduleEntry.


        :return: The day_of_week of this CronScheduleEntry.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """Sets the day_of_week of this CronScheduleEntry.


        :param day_of_week: The day_of_week of this CronScheduleEntry.
        :type day_of_week: str
        """

        self._day_of_week = day_of_week
