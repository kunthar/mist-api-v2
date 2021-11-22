import json
import time
import importlib

import pytest

from misttests.config import inject_vault_credentials
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

resource_name = 'CloudsController'.replace('Controller', '').lower()
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
def conditional_delay(request):
    yield
    method_name = request._pyfuncitem._obj.__name__
    s = setup_data.get(method_name, {}).get('sleep')
    if s:
        time.sleep(s)


class TestCloudsController:
    """CloudsController integration test stubs"""

    def test_add_cloud(self, pretty_print, mist_core, owner_api_token):
        """Test case for add_cloud

        Add cloud
        """
        add_cloud_request = json.loads("""{
  "name" : "my-cloud",
  "provider" : "google",
  "credentials" : {
    "projectId" : "projectId",
    "privateKey" : "privateKey",
    "email" : "email"
  }
}""", strict=False)
        request_body = setup_data.get('add_cloud', {}).get(
            'request_body')
        if request_body:
            add_cloud_request = request_body
        else:
            for k in add_cloud_request:
                if k in setup_data:
                    add_cloud_request[k] = setup_data[k]
                elif k == 'name' and resource_name_singular in setup_data:
                    add_cloud_request[k] = setup_data[
                        resource_name_singular]
        inject_vault_credentials(add_cloud_request)
        uri = mist_core.uri + '/api/v2/clouds'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=add_cloud_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_edit_cloud(self, pretty_print, mist_core, owner_api_token):
        """Test case for edit_cloud

        Edit cloud
        """
        edit_cloud_request = json.loads("""{
  "name" : "my-renamed-cloud"
}""", strict=False)
        request_body = setup_data.get('edit_cloud', {}).get(
            'request_body')
        if request_body:
            edit_cloud_request = request_body
        else:
            for k in edit_cloud_request:
                if k in setup_data:
                    edit_cloud_request[k] = setup_data[k]
                elif k == 'name' and resource_name_singular in setup_data:
                    edit_cloud_request[k] = setup_data[
                        resource_name_singular]
        inject_vault_credentials(edit_cloud_request)
        uri = mist_core.uri + '/api/v2/clouds/{cloud}'.format(
            cloud=setup_data.get('edit_cloud', {}).get('cloud') or setup_data.get('cloud') or 'my-cloud')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            json=edit_cloud_request)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_get_cloud(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_cloud

        Get cloud
        """
        query_string = setup_data.get('get_cloud', {}).get('query_string') or [('sort', '-name'),
                        ('only', 'id'),
                        ('deref', 'auto')]
        uri = mist_core.uri + '/api/v2/clouds/{cloud}'.format(
            cloud=setup_data.get('get_cloud', {}).get('cloud') or setup_data.get('cloud') or 'my-cloud')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_list_clouds(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_clouds

        List clouds
        """
        query_string = setup_data.get('list_clouds', {}).get('query_string') or [('search', 'provider:amazon'),
                        ('sort', '-name'),
                        ('start', '50'),
                        ('limit', '56'),
                        ('only', 'id'),
                        ('deref', 'auto')]
        uri = mist_core.uri + '/api/v2/clouds'
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri,
            params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_remove_cloud(self, pretty_print, mist_core, owner_api_token):
        """Test case for remove_cloud

        Remove cloud
        """
        uri = mist_core.uri + '/api/v2/clouds/{cloud}'.format(
            cloud=setup_data.get('remove_cloud', {}).get('cloud') or setup_data.get('cloud') or 'my-cloud')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')


if resource_name == 'machines':
    # Impose custom ordering of machines test methods
    for order, k in enumerate(_setup_module.TEST_METHOD_ORDERING):
        method_name = k if k.startswith('test_') else f'test_{k}'
        method = getattr(TestCloudsController, method_name)
        setattr(TestCloudsController, method_name,
                pytest.mark.order(order + 1)(method))
else:
    # Mark delete-related test methods as last to be run
    for key in vars(TestCloudsController):
        attr = getattr(TestCloudsController, key)
        if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
            setattr(TestCloudsController, key, pytest.mark.order('last')(attr))

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
    TestCloudsController = pytest.mark.usefixtures('setup')(
        TestCloudsController)
