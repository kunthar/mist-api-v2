import connexion
import six
import mongoengine as me

from mist.api import config

from mist_api_v2.models.create_machine_request import CreateMachineRequest  # noqa: E501
from mist_api_v2.models.create_machine_response import CreateMachineResponse  # noqa: E501
from mist_api_v2.models.get_machine_response import GetMachineResponse  # noqa: E501
from mist_api_v2.models.list_machines_response import ListMachinesResponse  # noqa: E501
from mist_api_v2 import util

from .base import list_resources


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


def _select_create_machine_cloud(auth_context, cloud_id=None, provider=None):
    """ Helper function to determine in which cloud machine should be created.
    """
    if cloud_id is not None:
        from mist.api.clouds.models import Cloud
        try:
            cloud = Cloud.objects.get(owner=auth_context.owner, id=cloud_id,
                                      deleted=None)
        except me.DoesNotExist:
            return None
    else:
        from mist.api.methods import list_resources
        search = f"provider:{provider}" if provider is not None else ''
        clouds, _ = list_resources(auth_context, 'cloud', search=search)
        # TODO select cloud based on some metrics
        # for the moment use the first cloud as placeholder
        if clouds:
            cloud = clouds[0]
        else:
            return None
    # READ permission required on cloud.
    # CREATE_RESOURCES permission required on cloud.
    auth_context.check_perm('cloud', 'read', cloud.id)
    auth_context.check_perm('cloud', 'create_resources', cloud.id)
    return cloud


def _select_create_machine_location(auth_context, cloud, location_id=None):
    """ Helper function to determine in which location machine should be created.
    """
    from mist.api.clouds.models import CloudLocation
    if location_id is not None:
        try:
            location = CloudLocation.objects.get(id=location_id)
        except me.DoesNotExist:
            return None
    else:
        try:
            # TODO select location based on some metrics
            # for the moment use the first location as placeholder
            locations = CloudLocation.objects(cloud=cloud)
            location = locations[0]
        except me.DoesNotExist:
            return None
    # READ permission required on location.
    # CREATE_RESOURCES permission required on location.
    auth_context.check_perm('location', 'read', location.id)
    auth_context.check_perm('location', 'create_resources', location.id)
    return location


def _select_create_machine_size(cloud, size_dict=None):
    """ Helper function to determine machine's size.

        :keyword size_dict
        :type dict

        :rtype: CloudSize
    """
    # TODO check also for `name` or some other similar key
    from mist.api.clouds.models import CloudSize

    size_id = size_dict.get("id", None)
    if size_id is not None:
        try:
            size = CloudSize.objects.get(id=size_id)
        except me.DoesNotExist:
            return None
    else:
        try:
            sizes = CloudSize.objects(cloud=cloud)
            # TODO select size based on some metrics
            # for the moment use the first size as placeholder
            size = sizes[0]
        except me.DoesNotExist:
            return None

    return size


def _select_create_machine_image(cloud, image_dict=None):
    """ Helper function to determine which image to boot machine from.

        :keyword image_dict
        :type dict

        :rtype: CloudSize
    """
    from mist.api.images.models import CloudImage
    image_id = image_dict.get("id", None)
    if image_id is not None:
        try:
            image = CloudImage.objects.get(id=image_id)
        except me.DoesNotExist:
            return None
    else:
        try:
            images = CloudImage.objects(cloud=cloud)
            # TODO select size based on some metrics
            # for the moment use the first size as placeholder
            image = images[0]
        except me.DoesNotExist:
            return None
    return image


def _select_create_machine_key(auth_context, cloud, key_id=None):
    # TODO handle key name as well
    from mist.api.keys.models import Key
    key = None
    private_key = None
    public_key = None
    if key_id:
        # READ permission required on key.
        auth_context.check_perm("key", "read", key_id)
        key = Key.objects.get(owner=auth_context.owner,
                              id=key_id, deleted=None)
    if cloud.ctl.provider not in config.PROVIDERS_WITHOUT_DEFAULT_KEY:
        if not key_id:
            try:
                key = Key.objects.get(owner=auth_context.owner,
                                      default=True, deleted=None)
            except me.DoesNotExist:
                pass
            key_id = key.name
    if key:
        private_key = key.private
        public_key = key.public.replace('\n', '')
    else:
        public_key = None

    return key, public_key, private_key


def _apply_tags(auth_context, tags=None, request_tags=None):
    from mist.api.exceptions import BadRequestError, ForbiddenError
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
    # CREATE permission required on machine.
    cloud_id = create_machine_request.cloud
    provider = create_machine_request.provider
    cloud = _select_create_machine_cloud(
        auth_context, cloud_id=cloud_id, provider=provider)
    if cloud is None:
        return 'Cloud does not exist', 404

    from mist.api.machines.methods import machine_name_validator
    from mist.api.exceptions import MachineNameValidationError
    machine_name = create_machine_request.name
    try:
        machine_name = machine_name_validator(cloud.ctl.provider, machine_name)
    except MachineNameValidationError as err:
        return err.args[0], 400
    # TODO this could also be a `name` for datacenter, region etc.
    location_id = create_machine_request.location
    location = _select_create_machine_location(
        auth_context, cloud, location_id=location_id)
    if location is None:
        return 'Location does not exist', 404

    size_dict = create_machine_request.size
    size = _select_create_machine_size(cloud, size_dict=size_dict)
    if size is None:
        return 'Size does not exist', 404

    image_dict = create_machine_request.image
    image = _select_create_machine_image(cloud, image_dict=image_dict)
    if image is None:
        return 'Image does not exist', 404

    # scripts_dict = create_machine_request.scripts
    key_dict = create_machine_request.key or {}
    key_id = key_dict.get('id')
    key, public_key, private_key = _select_create_machine_key(
        auth_context, cloud, key_id=key_id)

    tags, constraints = auth_context.check_perm('machine', 'create', None)

    request_tags = create_machine_request.tags or {}
    tags = _apply_tags(auth_context, tags=tags, request_tags=request_tags)

    expiration = create_machine_request.expiration or {}
    _check_constraints(auth_context, expiration, constraints=constraints)
    # TODO
    # RUN permission required on script.

    plan = {
        'name': machine_name,
        'cloud': cloud.title,
        'location': location.name,
        'image': image.name,
        'size': size.name,
        'tags': tags
    }
    if key is not None:
        plan['key'] = key.name
    return CreateMachineResponse(plan=plan)


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


def list_machines(cloud=None, search=None, sort=None, start=None, limit=None, only=None, deref=None):  # noqa: E501
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
