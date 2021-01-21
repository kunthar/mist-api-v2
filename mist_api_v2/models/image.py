# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class Image(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, external_id=None, name=None, cloud=None, starred=None, os_type=None, tags=None, created_by=None, owned_by=None, extra=None):  # noqa: E501
        """Image - a model defined in OpenAPI

        :param id: The id of this Image.  # noqa: E501
        :type id: str
        :param external_id: The external_id of this Image.  # noqa: E501
        :type external_id: str
        :param name: The name of this Image.  # noqa: E501
        :type name: str
        :param cloud: The cloud of this Image.  # noqa: E501
        :type cloud: str
        :param starred: The starred of this Image.  # noqa: E501
        :type starred: bool
        :param os_type: The os_type of this Image.  # noqa: E501
        :type os_type: str
        :param tags: The tags of this Image.  # noqa: E501
        :type tags: object
        :param created_by: The created_by of this Image.  # noqa: E501
        :type created_by: str
        :param owned_by: The owned_by of this Image.  # noqa: E501
        :type owned_by: str
        :param extra: The extra of this Image.  # noqa: E501
        :type extra: object
        """
        self.openapi_types = {
            'id': str,
            'external_id': str,
            'name': str,
            'cloud': str,
            'starred': bool,
            'os_type': str,
            'tags': object,
            'created_by': str,
            'owned_by': str,
            'extra': object
        }

        self.attribute_map = {
            'id': 'id',
            'external_id': 'external_id',
            'name': 'name',
            'cloud': 'cloud',
            'starred': 'starred',
            'os_type': 'os_type',
            'tags': 'tags',
            'created_by': 'created_by',
            'owned_by': 'owned_by',
            'extra': 'extra'
        }

        self._id = id
        self._external_id = external_id
        self._name = name
        self._cloud = cloud
        self._starred = starred
        self._os_type = os_type
        self._tags = tags
        self._created_by = created_by
        self._owned_by = owned_by
        self._extra = extra

    @classmethod
    def from_dict(cls, dikt) -> 'Image':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Image of this Image.  # noqa: E501
        :rtype: Image
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Image.


        :return: The id of this Image.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Image.


        :param id: The id of this Image.
        :type id: str
        """

        self._id = id

    @property
    def external_id(self):
        """Gets the external_id of this Image.


        :return: The external_id of this Image.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Image.


        :param external_id: The external_id of this Image.
        :type external_id: str
        """

        self._external_id = external_id

    @property
    def name(self):
        """Gets the name of this Image.


        :return: The name of this Image.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Image.


        :param name: The name of this Image.
        :type name: str
        """

        self._name = name

    @property
    def cloud(self):
        """Gets the cloud of this Image.


        :return: The cloud of this Image.
        :rtype: str
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this Image.


        :param cloud: The cloud of this Image.
        :type cloud: str
        """

        self._cloud = cloud

    @property
    def starred(self):
        """Gets the starred of this Image.


        :return: The starred of this Image.
        :rtype: bool
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        """Sets the starred of this Image.


        :param starred: The starred of this Image.
        :type starred: bool
        """

        self._starred = starred

    @property
    def os_type(self):
        """Gets the os_type of this Image.


        :return: The os_type of this Image.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this Image.


        :param os_type: The os_type of this Image.
        :type os_type: str
        """

        self._os_type = os_type

    @property
    def tags(self):
        """Gets the tags of this Image.


        :return: The tags of this Image.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Image.


        :param tags: The tags of this Image.
        :type tags: object
        """

        self._tags = tags

    @property
    def created_by(self):
        """Gets the created_by of this Image.


        :return: The created_by of this Image.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Image.


        :param created_by: The created_by of this Image.
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def owned_by(self):
        """Gets the owned_by of this Image.


        :return: The owned_by of this Image.
        :rtype: str
        """
        return self._owned_by

    @owned_by.setter
    def owned_by(self, owned_by):
        """Sets the owned_by of this Image.


        :param owned_by: The owned_by of this Image.
        :type owned_by: str
        """

        self._owned_by = owned_by

    @property
    def extra(self):
        """Gets the extra of this Image.


        :return: The extra of this Image.
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this Image.


        :param extra: The extra of this Image.
        :type extra: object
        """

        self._extra = extra
