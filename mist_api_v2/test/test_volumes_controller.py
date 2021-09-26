import pytest

from misttests import config
from misttests.integration.api.helpers import *
from misttests.integration.api.mistrequests import MistRequests

DELETE_KEYWORDS = ['delete', 'destroy', 'remove']


class TestVolumesController:
    """VolumesController integration test stubs"""

    def test_create_volume(self, pretty_print, mist_core, owner_api_token):
        """Test case for create_volume

        Create volume
        """
        create_volume_request = {
  "name" : "example_volume",
  "size" : "example_size"
}
        config.inject_vault_credentials(create_volume_request)
        uri = mist_core.uri + '/api/v2/volumes' 
        request = MistRequests(api_token=owner_api_token, uri=uri, json=create_volume_request)
        request_method = getattr(request, 'POST'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_delete_volume(self, pretty_print, mist_core, owner_api_token):
        """Test case for delete_volume

        Delete volume
        """
        uri = mist_core.uri + '/api/v2/volumes/{volume}'.format(volume="example_volume") 
        request = MistRequests(api_token=owner_api_token, uri=uri)
        request_method = getattr(request, 'DELETE'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_edit_volume(self, pretty_print, mist_core, owner_api_token):
        """Test case for edit_volume

        Edit volume
        """
        query_string = [('name', "renamed_example_volume")]
        uri = mist_core.uri + '/api/v2/volumes/{volume}'.format(volume="example_volume") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'PUT'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_get_volume(self, pretty_print, mist_core, owner_api_token):
        """Test case for get_volume

        Get volume
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/volumes/{volume}'.format(volume="example_volume") 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")

    def test_list_volumes(self, pretty_print, mist_core, owner_api_token):
        """Test case for list_volumes

        List volumes
        """
        query_string = [('cloud', "0194030499e74b02bdf68fa7130fb0b2"),
                        ('search', "location:Amsterdam"),
                        ('sort', "-name"),
                        ('start', "50"),
                        ('limit', "56"),
                        ('only', "id"),
                        ('deref', "auto")]
        uri = mist_core.uri + '/api/v2/volumes' 
        request = MistRequests(api_token=owner_api_token, uri=uri, params=query_string)
        request_method = getattr(request, 'GET'.lower())
        response = request_method()
        assert_response_ok(response)
        print("Success!!!")


# Mark delete-related test methods as last to be run
for key in vars(TestVolumesController):
    attr = getattr(TestVolumesController, key)
    if callable(attr) and any(k in key for k in DELETE_KEYWORDS):
        setattr(TestVolumesController, key, pytest.mark.last(attr))
