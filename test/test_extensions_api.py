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
from argo_client.api.extensions_api import ExtensionsApi  # noqa: E501
from argo_client.rest import ApiException


class TestExtensionsApi(unittest.TestCase):
    """ExtensionsApi unit test stubs"""

    def setUp(self):
        self.api = argo_client.api.extensions_api.ExtensionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_extensions_api_group(self):
        """Test case for get_extensions_api_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
