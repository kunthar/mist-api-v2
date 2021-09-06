# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mist_api_v2.models.get_org_response import GetOrgResponse  # noqa: E501
from mist_api_v2.test import BaseTestCase


class TestNameController(BaseTestCase):
    """NameController integration test stubs"""

    def test_get_org(self):
        """Test case for get_org

        Get Org
        """
        query_string = [('only', "id"),
                        ('deref', "auto")]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'special-key',
        }
        response = self.client.open(
            '/api/v2/orgs/{org}'.format(org='org_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
