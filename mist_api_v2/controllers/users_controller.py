import connexion
import six
import logging

from mist.api import config

from mist_api_v2.models.list_users_response import ListUsersResponse  # noqa: E501
from mist_api_v2 import util

from .base import list_resources, get_resource

logging.basicConfig(level=config.PY_LOG_LEVEL,
                    format=config.PY_LOG_FORMAT,
                    datefmt=config.PY_LOG_FORMAT_DATE)


log = logging.getLogger(__name__)

def list_users(search=None, sort=None, start=None, limit=None, only=None, deref=None):  # noqa: E501
    """List users

    Return current user if requester is not admin. Return all users for admin. # noqa: E501

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

    :rtype: ListUsersResponse
    """

    auth_context = connexion.context['token_info']['auth_context']
    if auth_context.user.role == "Admin":
        result = list_resources(
            auth_context, 'users', search=search, only=only,
            sort=sort, start=start, limit=limit, deref=deref)
    else:
        search = "id={}".format(auth_context.user.id)
        result = get_resource(auth_context, 'users', search=search)
    return result
