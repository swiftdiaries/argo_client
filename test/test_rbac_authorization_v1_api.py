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
from argo_client.api.rbac_authorization_v1_api import RbacAuthorizationV1Api  # noqa: E501
from argo_client.rest import ApiException


class TestRbacAuthorizationV1Api(unittest.TestCase):
    """RbacAuthorizationV1Api unit test stubs"""

    def setUp(self):
        self.api = argo_client.api.rbac_authorization_v1_api.RbacAuthorizationV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_rbac_authorization_v1_cluster_role(self):
        """Test case for create_rbac_authorization_v1_cluster_role

        """
        pass

    def test_create_rbac_authorization_v1_cluster_role_binding(self):
        """Test case for create_rbac_authorization_v1_cluster_role_binding

        """
        pass

    def test_create_rbac_authorization_v1_namespaced_role(self):
        """Test case for create_rbac_authorization_v1_namespaced_role

        """
        pass

    def test_create_rbac_authorization_v1_namespaced_role_binding(self):
        """Test case for create_rbac_authorization_v1_namespaced_role_binding

        """
        pass

    def test_delete_rbac_authorization_v1_cluster_role(self):
        """Test case for delete_rbac_authorization_v1_cluster_role

        """
        pass

    def test_delete_rbac_authorization_v1_cluster_role_binding(self):
        """Test case for delete_rbac_authorization_v1_cluster_role_binding

        """
        pass

    def test_delete_rbac_authorization_v1_collection_cluster_role(self):
        """Test case for delete_rbac_authorization_v1_collection_cluster_role

        """
        pass

    def test_delete_rbac_authorization_v1_collection_cluster_role_binding(self):
        """Test case for delete_rbac_authorization_v1_collection_cluster_role_binding

        """
        pass

    def test_delete_rbac_authorization_v1_collection_namespaced_role(self):
        """Test case for delete_rbac_authorization_v1_collection_namespaced_role

        """
        pass

    def test_delete_rbac_authorization_v1_collection_namespaced_role_binding(self):
        """Test case for delete_rbac_authorization_v1_collection_namespaced_role_binding

        """
        pass

    def test_delete_rbac_authorization_v1_namespaced_role(self):
        """Test case for delete_rbac_authorization_v1_namespaced_role

        """
        pass

    def test_delete_rbac_authorization_v1_namespaced_role_binding(self):
        """Test case for delete_rbac_authorization_v1_namespaced_role_binding

        """
        pass

    def test_get_rbac_authorization_v1_api_resources(self):
        """Test case for get_rbac_authorization_v1_api_resources

        """
        pass

    def test_list_rbac_authorization_v1_cluster_role(self):
        """Test case for list_rbac_authorization_v1_cluster_role

        """
        pass

    def test_list_rbac_authorization_v1_cluster_role_binding(self):
        """Test case for list_rbac_authorization_v1_cluster_role_binding

        """
        pass

    def test_list_rbac_authorization_v1_namespaced_role(self):
        """Test case for list_rbac_authorization_v1_namespaced_role

        """
        pass

    def test_list_rbac_authorization_v1_namespaced_role_binding(self):
        """Test case for list_rbac_authorization_v1_namespaced_role_binding

        """
        pass

    def test_list_rbac_authorization_v1_role_binding_for_all_namespaces(self):
        """Test case for list_rbac_authorization_v1_role_binding_for_all_namespaces

        """
        pass

    def test_list_rbac_authorization_v1_role_for_all_namespaces(self):
        """Test case for list_rbac_authorization_v1_role_for_all_namespaces

        """
        pass

    def test_patch_rbac_authorization_v1_cluster_role(self):
        """Test case for patch_rbac_authorization_v1_cluster_role

        """
        pass

    def test_patch_rbac_authorization_v1_cluster_role_binding(self):
        """Test case for patch_rbac_authorization_v1_cluster_role_binding

        """
        pass

    def test_patch_rbac_authorization_v1_namespaced_role(self):
        """Test case for patch_rbac_authorization_v1_namespaced_role

        """
        pass

    def test_patch_rbac_authorization_v1_namespaced_role_binding(self):
        """Test case for patch_rbac_authorization_v1_namespaced_role_binding

        """
        pass

    def test_read_rbac_authorization_v1_cluster_role(self):
        """Test case for read_rbac_authorization_v1_cluster_role

        """
        pass

    def test_read_rbac_authorization_v1_cluster_role_binding(self):
        """Test case for read_rbac_authorization_v1_cluster_role_binding

        """
        pass

    def test_read_rbac_authorization_v1_namespaced_role(self):
        """Test case for read_rbac_authorization_v1_namespaced_role

        """
        pass

    def test_read_rbac_authorization_v1_namespaced_role_binding(self):
        """Test case for read_rbac_authorization_v1_namespaced_role_binding

        """
        pass

    def test_replace_rbac_authorization_v1_cluster_role(self):
        """Test case for replace_rbac_authorization_v1_cluster_role

        """
        pass

    def test_replace_rbac_authorization_v1_cluster_role_binding(self):
        """Test case for replace_rbac_authorization_v1_cluster_role_binding

        """
        pass

    def test_replace_rbac_authorization_v1_namespaced_role(self):
        """Test case for replace_rbac_authorization_v1_namespaced_role

        """
        pass

    def test_replace_rbac_authorization_v1_namespaced_role_binding(self):
        """Test case for replace_rbac_authorization_v1_namespaced_role_binding

        """
        pass

    def test_watch_rbac_authorization_v1_cluster_role(self):
        """Test case for watch_rbac_authorization_v1_cluster_role

        """
        pass

    def test_watch_rbac_authorization_v1_cluster_role_binding(self):
        """Test case for watch_rbac_authorization_v1_cluster_role_binding

        """
        pass

    def test_watch_rbac_authorization_v1_cluster_role_binding_list(self):
        """Test case for watch_rbac_authorization_v1_cluster_role_binding_list

        """
        pass

    def test_watch_rbac_authorization_v1_cluster_role_list(self):
        """Test case for watch_rbac_authorization_v1_cluster_role_list

        """
        pass

    def test_watch_rbac_authorization_v1_namespaced_role(self):
        """Test case for watch_rbac_authorization_v1_namespaced_role

        """
        pass

    def test_watch_rbac_authorization_v1_namespaced_role_binding(self):
        """Test case for watch_rbac_authorization_v1_namespaced_role_binding

        """
        pass

    def test_watch_rbac_authorization_v1_namespaced_role_binding_list(self):
        """Test case for watch_rbac_authorization_v1_namespaced_role_binding_list

        """
        pass

    def test_watch_rbac_authorization_v1_namespaced_role_list(self):
        """Test case for watch_rbac_authorization_v1_namespaced_role_list

        """
        pass

    def test_watch_rbac_authorization_v1_role_binding_list_for_all_namespaces(self):
        """Test case for watch_rbac_authorization_v1_role_binding_list_for_all_namespaces

        """
        pass

    def test_watch_rbac_authorization_v1_role_list_for_all_namespaces(self):
        """Test case for watch_rbac_authorization_v1_role_list_for_all_namespaces

        """
        pass


if __name__ == '__main__':
    unittest.main()
