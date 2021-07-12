import connexion
import six

from mist_api_v2.models.create_cluster_request import CreateClusterRequest  # noqa: E501
from mist_api_v2.models.get_cluster_response import GetClusterResponse  # noqa: E501
from mist_api_v2.models.inline_response200 import InlineResponse200  # noqa: E501
from mist_api_v2.models.list_clusters_response import ListClustersResponse  # noqa: E501
from mist_api_v2 import util


def create_cluster(create_cluster_request=None):  # noqa: E501
    """Create cluster

    Create a new cluster and return the cluster&#39;s id # noqa: E501

    :param create_cluster_request: 
    :type create_cluster_request: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        create_cluster_request = CreateClusterRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_cluster(cluster):  # noqa: E501
    """Delete cluster

    Delete target clusters # noqa: E501

    :param cluster: 
    :type cluster: str

    :rtype: None
    """
    return 'do some magic!'


def get_cluster(cluster, only=None, deref=None):  # noqa: E501
    """Get cluster

    Get details about target cluster # noqa: E501

    :param cluster: 
    :type cluster: str
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: GetClusterResponse
    """
    return 'do some magic!'


def list_clusters(cloud=None, search=None, sort=None, start=None, limit=None, only=None, deref=None):  # noqa: E501
    """List clusters

    List clusters # noqa: E501

    :param cloud: 
    :type cloud: str
    :param search: Only return results matching search filter
    :type search: str
    :param sort: Order results by
    :type sort: str
    :param start: Start results from index or id
    :type start: str
    :param limit: Limit number of results, 1000 max
    :type limit: int
    :param only: Only return these fields
    :type only: str
    :param deref: Dereference foreign keys
    :type deref: str

    :rtype: ListClustersResponse
    """
    return 'do some magic!'
