# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.15.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import argo_client
from argo_client.api.apis_api import ApisApi  # noqa: E501
from argo_client.rest import ApiException


class TestApisApi(unittest.TestCase):
    """ApisApi unit test stubs"""

    def setUp(self):
        self.api = argo_client.api.apis_api.ApisApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_versions(self):
        """Test case for get_api_versions

        """
        pass


if __name__ == '__main__':
    unittest.main()
