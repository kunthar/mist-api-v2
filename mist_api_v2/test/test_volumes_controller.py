import json
import time
import importlib

import pytest

from misttests.config import inject_vault_credentials
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

resource_name = 'VolumesController'.replace('Controller', '').lower()
resource_name_singular = resource_name.strip('s')
try:
    _setup_module = importlib.import_module(
        f'misttests.integration.api.main.v2.setup.{resource_name}')
except ImportError:
    SETUP_MODULE_EXISTS = False
else:
    SETUP_MODULE_EXISTS = True
setup_data = {}


@pytest.fixture(autouse=True)
def sleep_after_test(request):
    yield
    method_name = request._pyfuncitem._obj.__name__
    s = setup_data.get(method_name.replace('test_', ''), {}).get('sleep')
    if s:
        time.sleep(s)


class TestVolumesController:
    """VolumesController integration test stubs"""

    def test_create_volume(self, pretty_print, mist_core, owner_api_token):
        """Test case for create_volume

        Create volume
        """
        create_volume_request = json.loads("""{
  "template" : "{}",
  "quantity" : 0,
  "ex_disk_type" : "pd-standard",
  "ex_volume_type" : "standard",
  "save" : true,
  "dry" : true,
  "tags" : "{}",
  "cloud" : "my-cloud",
  "ex_iops" : "ex_iops",
  "size" : 1,
  "extra" : "{}",
  "name" : "my-volume",
  "location" : "us-central1-a"
}""", strict=False)
        request_body = setup_data.get('create_volume', {}).get(
            'request_body')
        if request_body:
            create_volume_request = request_body
        else:
            for k in create_volume_request:
                if k in setup_data:
                    create_volume_request[k] = setup_data[k]
                elif k == 'name' and resource_name_singular in setup_data:
                    create_volume_request[k] = setup_data[
                        resource_name_singular]
        inject_vault_credentials(create_volume_request)
        uri = mist_core.uri + '/api/v2/volumes'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=create_volume_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_delete_volume(self, pretty_print, mist_core, owner_api_token):
        """Test case for delete_volume

        Delete volume
        """
        uri = mist_core.uri + '/api/v2/volumes/{volume}'.format(
            volume=setup_data.get('delete_volume', {}).get('volume') or setup_data.get('volume') or 'my-volume')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_edit_volume(self, pretty_print, mist_core, owner_api_token):
        """Test case for edit_volume

        Edit volume
        """
        query_string = setup_data.get('edit_volume', {}).get('query_string') or [('name', 'my-renamed-volume')]
        uri = mist_core.uri + '/api/v2/volumes/{volume}'.format(
            volume=setup_data.get('edit_volume', {}).get('volume') or setup_data.get('volume') or 'my-volume')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_get_volume(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_volume

        Get volume
        """
        query_string = setup_data.get('get_volume', {}).get('query_string') or [('only', 'id'),
                        ('deref', 'auto')]
        uri = mist_core.uri + '/api/v2/volumes/{volume}'.format(
            volume=setup_data.get('get_volume', {}).get('volume') or setup_data.get('volume') or 'my-volume')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_list_volumes(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_volumes

        List volumes
        """
        query_string = setup_data.get('list_volumes', {}).get('query_string') or [('cloud', '0194030499e74b02bdf68fa7130fb0b2'),
                        ('search', 'location:Amsterdam'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', '56'),
                        ('only', 'id'),
                        ('deref', 'auto')]
        uri = mist_core.uri + '/api/v2/volumes'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')


if resource_name == 'machines':
    # Impose custom ordering of machines test methods
    for order, k in enumerate(_setup_module.TEST_METHOD_ORDERING):
        method_name = k if k.startswith('test_') else f'test_{k}'
        method = getattr(TestVolumesController, method_name)
        setattr(TestVolumesController, method_name,
                pytest.mark.order(order + 1)(method))
else:
    # Mark delete-related test methods as last to be run
    for key in vars(TestVolumesController):
        attr = getattr(TestVolumesController, key)
        if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
            setattr(TestVolumesController, key, pytest.mark.order('last')(attr))

if SETUP_MODULE_EXISTS:
    # Add setup and teardown methods to test class
    class_setup_done = False

    @pytest.fixture(scope='class')
    def setup(owner_api_token):
        global class_setup_done
        if class_setup_done:
            yield
        else:
            global setup_data
            setup_data = _setup_module.setup(owner_api_token) or {}
            yield
            _setup_module.teardown(owner_api_token, setup_data)
            class_setup_done = True
    TestVolumesController = pytest.mark.usefixtures('setup')(
        TestVolumesController)
