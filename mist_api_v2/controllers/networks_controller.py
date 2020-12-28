import connexion
import six

from mist_api_v2.models.create_network_request import CreateNetworkRequest  # noqa: E501
from mist_api_v2.models.create_network_response import CreateNetworkResponse  # noqa: E501
from mist_api_v2.models.get_network_response import GetNetworkResponse  # noqa: E501
from mist_api_v2.models.list_networks_response import ListNetworksResponse  # noqa: E501
from mist_api_v2 import util


def create_network(create_network_request=None):  # noqa: E501
    """Create network

    Creates one or more networks on the specified cloud. If async is true, a jobId will be returned. READ permission required on cloud. CREATE_RESOURCES permission required on cloud. CREATE permission required on network. # noqa: E501

    :param create_network_request: 
    :type create_network_request: dict | bytes

    :rtype: CreateNetworkResponse
    """
    if connexion.request.is_json:
        create_network_request = CreateNetworkRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_network(network, name=None):  # noqa: E501
    """Edit network

    Edit target network # noqa: E501

    :param network: 
    :type network: str
    :param name: New network name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def get_network(network):  # noqa: E501
    """Get network

    Get details about target network # noqa: E501

    :param network: 
    :type network: str

    :rtype: GetNetworkResponse
    """
    return 'do some magic!'


def list_networks(cloud=None, search=None, sort=None, start=None, limit=None, only=None, deref=None):  # noqa: E501
    """List networks

    List networks owned by the active org. READ permission required on network &amp; cloud. # noqa: E501

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

    :rtype: ListNetworksResponse
    """
    return 'do some magic!'
