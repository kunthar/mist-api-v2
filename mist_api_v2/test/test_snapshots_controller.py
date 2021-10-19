import time
import importlib

import pytest

from misttests.config import inject_vault_credentials
from misttests.integration.api.helpers import assert_response_ok
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']

resource_name = 'SnapshotsController'.replace('Controller', '').lower()
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
    if method_name == 'test_create_cluster':
        time.sleep(200)


class TestSnapshotsController:
    """SnapshotsController integration test stubs"""

    def test_create_snapshot(self, pretty_print, mist_core, owner_api_token):
        """Test case for create_snapshot

        Create snapshot
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/snapshots'.format(
            machine=setup_data.get('machine') or 'example-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_list_snapshots(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_snapshots

        List machine snapshots
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/snapshots'.format(
            machine=setup_data.get('machine') or 'example-machine')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_remove_snapshot(self, pretty_print, mist_core, owner_api_token):
        """Test case for remove_snapshot

        Remove snapshot
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/snapshots/{snapshot}'.format(
            machine=setup_data.get('machine') or 'example-machine', snapshot=setup_data.get('snapshot') or 'example-snapshot')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')

    def test_revert_to_snapshot(self, pretty_print, mist_core, owner_api_token):
        """Test case for revert_to_snapshot

        Revert to snapshot
        """
        uri = mist_core.uri + '/api/v2/machines/{machine}/snapshots/{snapshot}'.format(
            machine=setup_data.get('machine') or 'example-machine', snapshot=setup_data.get('snapshot') or 'example-snapshot')
        request = MistRequests(
            api_token=owner_api_token,
            uri=uri)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print('Success!!!')


# Mark delete-related test methods as last to be run
for key in vars(TestSnapshotsController):
    attr = getattr(TestSnapshotsController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestSnapshotsController, key, pytest.mark.order('last')(attr))

if SETUP_MODULE_EXISTS:
    # Add setup and teardown methods to test class
    class_setup_done = False

    @pytest.fixture(scope='class')
    def setup(owner_api_token):
        global class_setup_done
        if class_setup_done:
            yield
        else:
            retval = _setup_module.setup(owner_api_token)
            if isinstance(retval, dict):
                global setup_data
                setup_data = retval
            yield
            _setup_module.teardown(owner_api_token)
            class_setup_done = True
    TestSnapshotsController = pytest.mark.usefixtures('setup')(
        TestSnapshotsController)
