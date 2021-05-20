# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class Zone(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cloud=None, created_by=None, external_id=None, id=None, name=None, owned_by=None, tags=None):  # noqa: E501
        """Zone - a model defined in OpenAPI

        :param cloud: The cloud of this Zone.  # noqa: E501
        :type cloud: str
        :param created_by: The created_by of this Zone.  # noqa: E501
        :type created_by: str
        :param external_id: The external_id of this Zone.  # noqa: E501
        :type external_id: str
        :param id: The id of this Zone.  # noqa: E501
        :type id: str
        :param name: The name of this Zone.  # noqa: E501
        :type name: str
        :param owned_by: The owned_by of this Zone.  # noqa: E501
        :type owned_by: str
        :param tags: The tags of this Zone.  # noqa: E501
        :type tags: object
        """
        self.openapi_types = {
            'cloud': str,
            'created_by': str,
            'external_id': str,
            'id': str,
            'name': str,
            'owned_by': str,
            'tags': object
        }

        self.attribute_map = {
            'cloud': 'cloud',
            'created_by': 'created_by',
            'external_id': 'external_id',
            'id': 'id',
            'name': 'name',
            'owned_by': 'owned_by',
            'tags': 'tags'
        }

        self._cloud = cloud
        self._created_by = created_by
        self._external_id = external_id
        self._id = id
        self._name = name
        self._owned_by = owned_by
        self._tags = tags

    @classmethod
    def from_dict(cls, dikt) -> 'Zone':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Zone of this Zone.  # noqa: E501
        :rtype: Zone
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cloud(self):
        """Gets the cloud of this Zone.


        :return: The cloud of this Zone.
        :rtype: str
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this Zone.


        :param cloud: The cloud of this Zone.
        :type cloud: str
        """

        self._cloud = cloud

    @property
    def created_by(self):
        """Gets the created_by of this Zone.


        :return: The created_by of this Zone.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Zone.


        :param created_by: The created_by of this Zone.
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def external_id(self):
        """Gets the external_id of this Zone.


        :return: The external_id of this Zone.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Zone.


        :param external_id: The external_id of this Zone.
        :type external_id: str
        """

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this Zone.


        :return: The id of this Zone.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Zone.


        :param id: The id of this Zone.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Zone.


        :return: The name of this Zone.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Zone.


        :param name: The name of this Zone.
        :type name: str
        """

        self._name = name

    @property
    def owned_by(self):
        """Gets the owned_by of this Zone.


        :return: The owned_by of this Zone.
        :rtype: str
        """
        return self._owned_by

    @owned_by.setter
    def owned_by(self, owned_by):
        """Sets the owned_by of this Zone.


        :param owned_by: The owned_by of this Zone.
        :type owned_by: str
        """

        self._owned_by = owned_by

    @property
    def tags(self):
        """Gets the tags of this Zone.


        :return: The tags of this Zone.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Zone.


        :param tags: The tags of this Zone.
        :type tags: object
        """

        self._tags = tags
