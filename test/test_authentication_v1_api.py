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
from argo_client.api.authentication_v1_api import AuthenticationV1Api  # noqa: E501
from argo_client.rest import ApiException


class TestAuthenticationV1Api(unittest.TestCase):
    """AuthenticationV1Api unit test stubs"""

    def setUp(self):
        self.api = argo_client.api.authentication_v1_api.AuthenticationV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_authentication_v1_token_review(self):
        """Test case for create_authentication_v1_token_review

        """
        pass

    def test_get_authentication_v1_api_resources(self):
        """Test case for get_authentication_v1_api_resources

        """
        pass


if __name__ == '__main__':
    unittest.main()
