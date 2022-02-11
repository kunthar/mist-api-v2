# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class AmazonClusterRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, provider=None, name=None, role_arn=None, vpc_id=None, subnet_ids=None, security_group_ids=None, desired_nodes=None, nodegroup_role_arn=None, nodegroup_size=None, nodegroup_disk_size=None):  # noqa: E501
        """AmazonClusterRequest - a model defined in OpenAPI

        :param provider: The provider of this AmazonClusterRequest.  # noqa: E501
        :type provider: str
        :param name: The name of this AmazonClusterRequest.  # noqa: E501
        :type name: str
        :param role_arn: The role_arn of this AmazonClusterRequest.  # noqa: E501
        :type role_arn: str
        :param vpc_id: The vpc_id of this AmazonClusterRequest.  # noqa: E501
        :type vpc_id: str
        :param subnet_ids: The subnet_ids of this AmazonClusterRequest.  # noqa: E501
        :type subnet_ids: List[str]
        :param security_group_ids: The security_group_ids of this AmazonClusterRequest.  # noqa: E501
        :type security_group_ids: List[str]
        :param desired_nodes: The desired_nodes of this AmazonClusterRequest.  # noqa: E501
        :type desired_nodes: float
        :param nodegroup_role_arn: The nodegroup_role_arn of this AmazonClusterRequest.  # noqa: E501
        :type nodegroup_role_arn: str
        :param nodegroup_size: The nodegroup_size of this AmazonClusterRequest.  # noqa: E501
        :type nodegroup_size: str
        :param nodegroup_disk_size: The nodegroup_disk_size of this AmazonClusterRequest.  # noqa: E501
        :type nodegroup_disk_size: float
        """
        self.openapi_types = {
            'provider': str,
            'name': str,
            'role_arn': str,
            'vpc_id': str,
            'subnet_ids': List[str],
            'security_group_ids': List[str],
            'desired_nodes': float,
            'nodegroup_role_arn': str,
            'nodegroup_size': str,
            'nodegroup_disk_size': float
        }

        self.attribute_map = {
            'provider': 'provider',
            'name': 'name',
            'role_arn': 'role_arn',
            'vpc_id': 'vpc_id',
            'subnet_ids': 'subnet_ids',
            'security_group_ids': 'security_group_ids',
            'desired_nodes': 'desired_nodes',
            'nodegroup_role_arn': 'nodegroup_role_arn',
            'nodegroup_size': 'nodegroup_size',
            'nodegroup_disk_size': 'nodegroup_disk_size'
        }

        self._provider = provider
        self._name = name
        self._role_arn = role_arn
        self._vpc_id = vpc_id
        self._subnet_ids = subnet_ids
        self._security_group_ids = security_group_ids
        self._desired_nodes = desired_nodes
        self._nodegroup_role_arn = nodegroup_role_arn
        self._nodegroup_size = nodegroup_size
        self._nodegroup_disk_size = nodegroup_disk_size

    @classmethod
    def from_dict(cls, dikt) -> 'AmazonClusterRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AmazonClusterRequest of this AmazonClusterRequest.  # noqa: E501
        :rtype: AmazonClusterRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provider(self):
        """Gets the provider of this AmazonClusterRequest.


        :return: The provider of this AmazonClusterRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this AmazonClusterRequest.


        :param provider: The provider of this AmazonClusterRequest.
        :type provider: str
        """
        allowed_values = ["amazon"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def name(self):
        """Gets the name of this AmazonClusterRequest.

        The cluster's name  # noqa: E501

        :return: The name of this AmazonClusterRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AmazonClusterRequest.

        The cluster's name  # noqa: E501

        :param name: The name of this AmazonClusterRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def role_arn(self):
        """Gets the role_arn of this AmazonClusterRequest.

        The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf  # noqa: E501

        :return: The role_arn of this AmazonClusterRequest.
        :rtype: str
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        """Sets the role_arn of this AmazonClusterRequest.

        The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf  # noqa: E501

        :param role_arn: The role_arn of this AmazonClusterRequest.
        :type role_arn: str
        """
        if role_arn is None:
            raise ValueError("Invalid value for `role_arn`, must not be `None`")  # noqa: E501

        self._role_arn = role_arn

    @property
    def vpc_id(self):
        """Gets the vpc_id of this AmazonClusterRequest.

        The VPC associated with the cluster  # noqa: E501

        :return: The vpc_id of this AmazonClusterRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this AmazonClusterRequest.

        The VPC associated with the cluster  # noqa: E501

        :param vpc_id: The vpc_id of this AmazonClusterRequest.
        :type vpc_id: str
        """
        if vpc_id is None:
            raise ValueError("Invalid value for `vpc_id`, must not be `None`")  # noqa: E501

        self._vpc_id = vpc_id

    @property
    def subnet_ids(self):
        """Gets the subnet_ids of this AmazonClusterRequest.

        The subnets associated with the cluster  # noqa: E501

        :return: The subnet_ids of this AmazonClusterRequest.
        :rtype: List[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """Sets the subnet_ids of this AmazonClusterRequest.

        The subnets associated with the cluster  # noqa: E501

        :param subnet_ids: The subnet_ids of this AmazonClusterRequest.
        :type subnet_ids: List[str]
        """
        if subnet_ids is None:
            raise ValueError("Invalid value for `subnet_ids`, must not be `None`")  # noqa: E501

        self._subnet_ids = subnet_ids

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this AmazonClusterRequest.

        The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your nodes and the Kubernetes control plane  # noqa: E501

        :return: The security_group_ids of this AmazonClusterRequest.
        :rtype: List[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this AmazonClusterRequest.

        The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your nodes and the Kubernetes control plane  # noqa: E501

        :param security_group_ids: The security_group_ids of this AmazonClusterRequest.
        :type security_group_ids: List[str]
        """
        if security_group_ids is None:
            raise ValueError("Invalid value for `security_group_ids`, must not be `None`")  # noqa: E501

        self._security_group_ids = security_group_ids

    @property
    def desired_nodes(self):
        """Gets the desired_nodes of this AmazonClusterRequest.

        The initial number of nodes to provision for the nodegroup. Defaults to 2  # noqa: E501

        :return: The desired_nodes of this AmazonClusterRequest.
        :rtype: float
        """
        return self._desired_nodes

    @desired_nodes.setter
    def desired_nodes(self, desired_nodes):
        """Sets the desired_nodes of this AmazonClusterRequest.

        The initial number of nodes to provision for the nodegroup. Defaults to 2  # noqa: E501

        :param desired_nodes: The desired_nodes of this AmazonClusterRequest.
        :type desired_nodes: float
        """

        self._desired_nodes = desired_nodes

    @property
    def nodegroup_role_arn(self):
        """Gets the nodegroup_role_arn of this AmazonClusterRequest.

        The Amazon Resource Name (ARN) of the IAM role to associate with the node group  # noqa: E501

        :return: The nodegroup_role_arn of this AmazonClusterRequest.
        :rtype: str
        """
        return self._nodegroup_role_arn

    @nodegroup_role_arn.setter
    def nodegroup_role_arn(self, nodegroup_role_arn):
        """Sets the nodegroup_role_arn of this AmazonClusterRequest.

        The Amazon Resource Name (ARN) of the IAM role to associate with the node group  # noqa: E501

        :param nodegroup_role_arn: The nodegroup_role_arn of this AmazonClusterRequest.
        :type nodegroup_role_arn: str
        """

        self._nodegroup_role_arn = nodegroup_role_arn

    @property
    def nodegroup_size(self):
        """Gets the nodegroup_size of this AmazonClusterRequest.

        Name or ID of size to use for the nodes. If not provided, the t3.medium size will be used  # noqa: E501

        :return: The nodegroup_size of this AmazonClusterRequest.
        :rtype: str
        """
        return self._nodegroup_size

    @nodegroup_size.setter
    def nodegroup_size(self, nodegroup_size):
        """Sets the nodegroup_size of this AmazonClusterRequest.

        Name or ID of size to use for the nodes. If not provided, the t3.medium size will be used  # noqa: E501

        :param nodegroup_size: The nodegroup_size of this AmazonClusterRequest.
        :type nodegroup_size: str
        """

        self._nodegroup_size = nodegroup_size

    @property
    def nodegroup_disk_size(self):
        """Gets the nodegroup_disk_size of this AmazonClusterRequest.

        The disk size for the nodegroup. Defaults to 20 GBs  # noqa: E501

        :return: The nodegroup_disk_size of this AmazonClusterRequest.
        :rtype: float
        """
        return self._nodegroup_disk_size

    @nodegroup_disk_size.setter
    def nodegroup_disk_size(self, nodegroup_disk_size):
        """Sets the nodegroup_disk_size of this AmazonClusterRequest.

        The disk size for the nodegroup. Defaults to 20 GBs  # noqa: E501

        :param nodegroup_disk_size: The nodegroup_disk_size of this AmazonClusterRequest.
        :type nodegroup_disk_size: float
        """

        self._nodegroup_disk_size = nodegroup_disk_size
