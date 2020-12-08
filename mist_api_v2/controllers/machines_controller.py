import uuid
import connexion
import six
import mongoengine as me

from mist.api import config
from mist.api.exceptions import BadRequestError
from mist.api.exceptions import NotFoundError
from mist.api.exceptions import ForbiddenError
from mist.api.exceptions import MachineNameValidationError
from mist.api.exceptions import PolicyUnauthorizedError

from mist.api.machines.methods import machine_name_validator
from mist.api.methods import list_resources
from mist.api.dramatiq_tasks import dramatiq_create_machine_async

from mist_api_v2.models.create_machine_request import CreateMachineRequest  # noqa: E501
from mist_api_v2.models.create_machine_response import CreateMachineResponse  # noqa: E501
from mist_api_v2.models.get_machine_response import GetMachineResponse  # noqa: E501
from mist_api_v2.models.list_machines_response import ListMachinesResponse  # noqa: E501
from mist_api_v2 import util

# from .base import list_resources


def clone_machine(machine):  # noqa: E501
    """Clone machine

    Clone target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    return 'do some magic!'


def console(machine):  # noqa: E501
    """Open console

    Open VNC console on target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    return 'do some magic!'


def _compute_tags(auth_context, tags=None, request_tags=None):
    security_tags = auth_context.get_security_tags()
    for mt in request_tags:
        if mt in security_tags:
            raise ForbiddenError(
                'You may not assign tags included in a Team access policy:'
                ' `%s`' % mt)
    tags.update(request_tags)
    return tags


def _check_constraints(auth_context, expiration, constraints=None):
    constraints = constraints or {}
    # check expiration constraint
    exp_constraint = constraints.get('expiration', {})
    if exp_constraint:
        try:
            from mist.rbac.methods import check_expiration

            check_expiration(expiration, exp_constraint)
        except ImportError:
            pass

    # check cost constraint
    cost_constraint = constraints.get('cost', {})
    if cost_constraint:
        try:
            from mist.rbac.methods import check_cost

            check_cost(auth_context.org, cost_constraint)
        except ImportError:
            pass


def create_machine(create_machine_request=None):  # noqa: E501
    """Create machine

    Creates one or more machines on the specified cloud. If async is true, a jobId will be returned. READ permission required on cloud. CREATE_RESOURCES permission required on cloud. READ permission required on location. CREATE_RESOURCES permission required on location. CREATE permission required on machine. RUN permission required on script. READ permission required on key. # noqa: E501

    :param create_machine_request:
    :type create_machine_request: dict | bytes

    :rtype: CreateMachineResponse
    """

    if connexion.request.is_json:
        create_machine_request = CreateMachineRequest.from_dict(connexion.request.get_json())  # noqa: E501

    auth_context = connexion.context['token_info']['auth_context']
    plan = {}

    if create_machine_request.cloud:
        cloud_search = create_machine_request.cloud
    elif create_machine_request.provider:
        cloud_search = f'provider:{create_machine_request.provider}'
    else:
        cloud_search = ''
    # TODO handle multiple clouds
    # TODO add permissions constraint to list_resources
    try:
        [cloud], _ = list_resources(
            auth_context, 'cloud', search=cloud_search, limit=1
        )
    except ValueError:
        return 'Cloud does not exist', 404
    try:
        auth_context.check_perm('cloud', 'create_resources', cloud.id)
    except PolicyUnauthorizedError as exc:
        return exc.args[0], 403

    plan['cloud'] = cloud.id

    try:
        machine_name = machine_name_validator(
                        cloud.ctl.provider,
                        create_machine_request.name)
    except MachineNameValidationError as exc:
        return exc.args[0], 400

    plan['machine_name'] = machine_name

    try:
        tags, constraints = auth_context.check_perm('machine', 'create', None)
    except PolicyUnauthorizedError as exc:
        return exc.args[0], 403

    request_tags = create_machine_request.tags or {}
    try:
        tags = _compute_tags(
            auth_context, tags=tags, request_tags=request_tags
        )
    except ForbiddenError as err:
        return err.args[0], 403

    if tags:
        plan['tags'] = tags

    expiration = create_machine_request.expiration or {}
    try:
        _check_constraints(auth_context, expiration, constraints=constraints)
    except BadRequestError as exc:
        return exc.args[0], 400
    except PolicyUnauthorizedError as exc:
        return exc.args[0], 400

    if expiration:
        plan['expiration'] = expiration

    kwargs = {
        'image': create_machine_request.image or {},
        'location': create_machine_request.location or '',
        'size': create_machine_request.size or {},
        'key': create_machine_request.key or {},
        'networks': create_machine_request.net or {},
        'volumes': create_machine_request.volumes or {},
        'disks': create_machine_request.disks or {},
        'extra': create_machine_request.extra or {},
        'cloudinit': create_machine_request.cloudinit or '',
        'fqdn': create_machine_request.fqdn or '',
        'monitoring': create_machine_request.monitoring,
        'quantity': create_machine_request.quantity or 1
    }

    try:
        cloud.ctl.compute.generate_plan(auth_context, plan, **kwargs)
    except NotFoundError as exc:
        return exc.args[0], 404
    except PolicyUnauthorizedError as exc:
        return exc.args[0], 400
    except BadRequestError as exc:
        return exc.args[0], 400

    # TODO save
    # TODO template

    if create_machine_request.dry is not None:
        dry = create_machine_request.dry
    else:
        dry = True

    if dry:
        return CreateMachineResponse(plan=plan)
    else:
        # TODO job,job_id could also be passed as parameter
        job_id = uuid.uuid4().hex
        job = 'create_machine'
        # TODO add countdown=2
        dramatiq_create_machine_async.send(
            auth_context.serialize(), job_id, plan, job=job
        )
        return CreateMachineResponse(plan=plan, job_id=job_id)


def destroy_machine(machine):  # noqa: E501
    """Destroy machine

    Destroy target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    return 'do some magic!'


def edit_machine(machine, name=None):  # noqa: E501
    """Edit machine

    Edit target machine # noqa: E501

    :param machine:
    :type machine: str
    :param name: New machine name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def expose_machine(machine):  # noqa: E501
    """Expose machine

    Expose target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    return 'do some magic!'


def get_machine(machine):  # noqa: E501
    """Get machine

    Get details about target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: GetMachineResponse
    """
    return 'do some magic!'


def list_machines(cloud=None, search=None, sort=None, start=0, limit=100, only=None, deref='auto'):  # noqa: E501
    """List machines

    List machines owned by the active org. READ permission required on machine &amp; cloud. # noqa: E501

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

    :rtype: ListMachinesResponse
    """
    auth_context = connexion.context['token_info']['auth_context']
    return list_resources(
        auth_context, 'machine', cloud=cloud, search=search, only=only,
        sort=sort, start=start, limit=limit, deref=deref
    )


def reboot_machine(machine):  # noqa: E501
    """Reboot machine

    Reboot target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    return 'do some magic!'


def rename_machine(machine):  # noqa: E501
    """Rename machine

    Rename target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    return 'do some magic!'


def resize_machine(machine):  # noqa: E501
    """Resize machine

    Resize target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    return 'do some magic!'


def resume_machine(machine):  # noqa: E501
    """Resume machine

    Resume target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    return 'do some magic!'


def ssh(machine):  # noqa: E501
    """Open secure shell

    Open secure shell on target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    return 'do some magic!'


def start_machine(machine):  # noqa: E501
    """Start machine

    Start target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    return 'do some magic!'


def stop_machine(machine):  # noqa: E501
    """Stop machine

    Stop target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    return 'do some magic!'


def suspend_machine(machine):  # noqa: E501
    """Suspend machine

    Suspend target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    return 'do some magic!'


def undefine_machine(machine):  # noqa: E501
    """Undefine machine

    Undefine target machine # noqa: E501

    :param machine:
    :type machine: str

    :rtype: None
    """
    return 'do some magic!'
