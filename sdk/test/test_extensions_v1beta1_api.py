# coding: utf-8

"""
    Argo API Client

    Generated python client for the Argo Workflows  # noqa: E501

    OpenAPI spec version: v1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import argo.sdk
from api.extensions_v1beta1_api import ExtensionsV1beta1Api  # noqa: E501
from argo.sdk.rest import ApiException


class TestExtensionsV1beta1Api(unittest.TestCase):
    """ExtensionsV1beta1Api unit test stubs"""

    def setUp(self):
        self.api = api.extensions_v1beta1_api.ExtensionsV1beta1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_extensions_v1beta1_namespaced_daemon_set(self):
        """Test case for create_extensions_v1beta1_namespaced_daemon_set

        """
        pass

    def test_create_extensions_v1beta1_namespaced_deployment(self):
        """Test case for create_extensions_v1beta1_namespaced_deployment

        """
        pass

    def test_create_extensions_v1beta1_namespaced_deployment_rollback(self):
        """Test case for create_extensions_v1beta1_namespaced_deployment_rollback

        """
        pass

    def test_create_extensions_v1beta1_namespaced_ingress(self):
        """Test case for create_extensions_v1beta1_namespaced_ingress

        """
        pass

    def test_create_extensions_v1beta1_namespaced_network_policy(self):
        """Test case for create_extensions_v1beta1_namespaced_network_policy

        """
        pass

    def test_create_extensions_v1beta1_namespaced_replica_set(self):
        """Test case for create_extensions_v1beta1_namespaced_replica_set

        """
        pass

    def test_create_extensions_v1beta1_pod_security_policy(self):
        """Test case for create_extensions_v1beta1_pod_security_policy

        """
        pass

    def test_delete_extensions_v1beta1_collection_namespaced_daemon_set(self):
        """Test case for delete_extensions_v1beta1_collection_namespaced_daemon_set

        """
        pass

    def test_delete_extensions_v1beta1_collection_namespaced_deployment(self):
        """Test case for delete_extensions_v1beta1_collection_namespaced_deployment

        """
        pass

    def test_delete_extensions_v1beta1_collection_namespaced_ingress(self):
        """Test case for delete_extensions_v1beta1_collection_namespaced_ingress

        """
        pass

    def test_delete_extensions_v1beta1_collection_namespaced_network_policy(self):
        """Test case for delete_extensions_v1beta1_collection_namespaced_network_policy

        """
        pass

    def test_delete_extensions_v1beta1_collection_namespaced_replica_set(self):
        """Test case for delete_extensions_v1beta1_collection_namespaced_replica_set

        """
        pass

    def test_delete_extensions_v1beta1_collection_pod_security_policy(self):
        """Test case for delete_extensions_v1beta1_collection_pod_security_policy

        """
        pass

    def test_delete_extensions_v1beta1_namespaced_daemon_set(self):
        """Test case for delete_extensions_v1beta1_namespaced_daemon_set

        """
        pass

    def test_delete_extensions_v1beta1_namespaced_deployment(self):
        """Test case for delete_extensions_v1beta1_namespaced_deployment

        """
        pass

    def test_delete_extensions_v1beta1_namespaced_ingress(self):
        """Test case for delete_extensions_v1beta1_namespaced_ingress

        """
        pass

    def test_delete_extensions_v1beta1_namespaced_network_policy(self):
        """Test case for delete_extensions_v1beta1_namespaced_network_policy

        """
        pass

    def test_delete_extensions_v1beta1_namespaced_replica_set(self):
        """Test case for delete_extensions_v1beta1_namespaced_replica_set

        """
        pass

    def test_delete_extensions_v1beta1_pod_security_policy(self):
        """Test case for delete_extensions_v1beta1_pod_security_policy

        """
        pass

    def test_get_extensions_v1beta1_api_resources(self):
        """Test case for get_extensions_v1beta1_api_resources

        """
        pass

    def test_list_extensions_v1beta1_daemon_set_for_all_namespaces(self):
        """Test case for list_extensions_v1beta1_daemon_set_for_all_namespaces

        """
        pass

    def test_list_extensions_v1beta1_deployment_for_all_namespaces(self):
        """Test case for list_extensions_v1beta1_deployment_for_all_namespaces

        """
        pass

    def test_list_extensions_v1beta1_ingress_for_all_namespaces(self):
        """Test case for list_extensions_v1beta1_ingress_for_all_namespaces

        """
        pass

    def test_list_extensions_v1beta1_namespaced_daemon_set(self):
        """Test case for list_extensions_v1beta1_namespaced_daemon_set

        """
        pass

    def test_list_extensions_v1beta1_namespaced_deployment(self):
        """Test case for list_extensions_v1beta1_namespaced_deployment

        """
        pass

    def test_list_extensions_v1beta1_namespaced_ingress(self):
        """Test case for list_extensions_v1beta1_namespaced_ingress

        """
        pass

    def test_list_extensions_v1beta1_namespaced_network_policy(self):
        """Test case for list_extensions_v1beta1_namespaced_network_policy

        """
        pass

    def test_list_extensions_v1beta1_namespaced_replica_set(self):
        """Test case for list_extensions_v1beta1_namespaced_replica_set

        """
        pass

    def test_list_extensions_v1beta1_network_policy_for_all_namespaces(self):
        """Test case for list_extensions_v1beta1_network_policy_for_all_namespaces

        """
        pass

    def test_list_extensions_v1beta1_pod_security_policy(self):
        """Test case for list_extensions_v1beta1_pod_security_policy

        """
        pass

    def test_list_extensions_v1beta1_replica_set_for_all_namespaces(self):
        """Test case for list_extensions_v1beta1_replica_set_for_all_namespaces

        """
        pass

    def test_patch_extensions_v1beta1_namespaced_daemon_set(self):
        """Test case for patch_extensions_v1beta1_namespaced_daemon_set

        """
        pass

    def test_patch_extensions_v1beta1_namespaced_daemon_set_status(self):
        """Test case for patch_extensions_v1beta1_namespaced_daemon_set_status

        """
        pass

    def test_patch_extensions_v1beta1_namespaced_deployment(self):
        """Test case for patch_extensions_v1beta1_namespaced_deployment

        """
        pass

    def test_patch_extensions_v1beta1_namespaced_deployment_scale(self):
        """Test case for patch_extensions_v1beta1_namespaced_deployment_scale

        """
        pass

    def test_patch_extensions_v1beta1_namespaced_deployment_status(self):
        """Test case for patch_extensions_v1beta1_namespaced_deployment_status

        """
        pass

    def test_patch_extensions_v1beta1_namespaced_ingress(self):
        """Test case for patch_extensions_v1beta1_namespaced_ingress

        """
        pass

    def test_patch_extensions_v1beta1_namespaced_ingress_status(self):
        """Test case for patch_extensions_v1beta1_namespaced_ingress_status

        """
        pass

    def test_patch_extensions_v1beta1_namespaced_network_policy(self):
        """Test case for patch_extensions_v1beta1_namespaced_network_policy

        """
        pass

    def test_patch_extensions_v1beta1_namespaced_replica_set(self):
        """Test case for patch_extensions_v1beta1_namespaced_replica_set

        """
        pass

    def test_patch_extensions_v1beta1_namespaced_replica_set_scale(self):
        """Test case for patch_extensions_v1beta1_namespaced_replica_set_scale

        """
        pass

    def test_patch_extensions_v1beta1_namespaced_replica_set_status(self):
        """Test case for patch_extensions_v1beta1_namespaced_replica_set_status

        """
        pass

    def test_patch_extensions_v1beta1_namespaced_replication_controller_dummy_scale(self):
        """Test case for patch_extensions_v1beta1_namespaced_replication_controller_dummy_scale

        """
        pass

    def test_patch_extensions_v1beta1_pod_security_policy(self):
        """Test case for patch_extensions_v1beta1_pod_security_policy

        """
        pass

    def test_read_extensions_v1beta1_namespaced_daemon_set(self):
        """Test case for read_extensions_v1beta1_namespaced_daemon_set

        """
        pass

    def test_read_extensions_v1beta1_namespaced_daemon_set_status(self):
        """Test case for read_extensions_v1beta1_namespaced_daemon_set_status

        """
        pass

    def test_read_extensions_v1beta1_namespaced_deployment(self):
        """Test case for read_extensions_v1beta1_namespaced_deployment

        """
        pass

    def test_read_extensions_v1beta1_namespaced_deployment_scale(self):
        """Test case for read_extensions_v1beta1_namespaced_deployment_scale

        """
        pass

    def test_read_extensions_v1beta1_namespaced_deployment_status(self):
        """Test case for read_extensions_v1beta1_namespaced_deployment_status

        """
        pass

    def test_read_extensions_v1beta1_namespaced_ingress(self):
        """Test case for read_extensions_v1beta1_namespaced_ingress

        """
        pass

    def test_read_extensions_v1beta1_namespaced_ingress_status(self):
        """Test case for read_extensions_v1beta1_namespaced_ingress_status

        """
        pass

    def test_read_extensions_v1beta1_namespaced_network_policy(self):
        """Test case for read_extensions_v1beta1_namespaced_network_policy

        """
        pass

    def test_read_extensions_v1beta1_namespaced_replica_set(self):
        """Test case for read_extensions_v1beta1_namespaced_replica_set

        """
        pass

    def test_read_extensions_v1beta1_namespaced_replica_set_scale(self):
        """Test case for read_extensions_v1beta1_namespaced_replica_set_scale

        """
        pass

    def test_read_extensions_v1beta1_namespaced_replica_set_status(self):
        """Test case for read_extensions_v1beta1_namespaced_replica_set_status

        """
        pass

    def test_read_extensions_v1beta1_namespaced_replication_controller_dummy_scale(self):
        """Test case for read_extensions_v1beta1_namespaced_replication_controller_dummy_scale

        """
        pass

    def test_read_extensions_v1beta1_pod_security_policy(self):
        """Test case for read_extensions_v1beta1_pod_security_policy

        """
        pass

    def test_replace_extensions_v1beta1_namespaced_daemon_set(self):
        """Test case for replace_extensions_v1beta1_namespaced_daemon_set

        """
        pass

    def test_replace_extensions_v1beta1_namespaced_daemon_set_status(self):
        """Test case for replace_extensions_v1beta1_namespaced_daemon_set_status

        """
        pass

    def test_replace_extensions_v1beta1_namespaced_deployment(self):
        """Test case for replace_extensions_v1beta1_namespaced_deployment

        """
        pass

    def test_replace_extensions_v1beta1_namespaced_deployment_scale(self):
        """Test case for replace_extensions_v1beta1_namespaced_deployment_scale

        """
        pass

    def test_replace_extensions_v1beta1_namespaced_deployment_status(self):
        """Test case for replace_extensions_v1beta1_namespaced_deployment_status

        """
        pass

    def test_replace_extensions_v1beta1_namespaced_ingress(self):
        """Test case for replace_extensions_v1beta1_namespaced_ingress

        """
        pass

    def test_replace_extensions_v1beta1_namespaced_ingress_status(self):
        """Test case for replace_extensions_v1beta1_namespaced_ingress_status

        """
        pass

    def test_replace_extensions_v1beta1_namespaced_network_policy(self):
        """Test case for replace_extensions_v1beta1_namespaced_network_policy

        """
        pass

    def test_replace_extensions_v1beta1_namespaced_replica_set(self):
        """Test case for replace_extensions_v1beta1_namespaced_replica_set

        """
        pass

    def test_replace_extensions_v1beta1_namespaced_replica_set_scale(self):
        """Test case for replace_extensions_v1beta1_namespaced_replica_set_scale

        """
        pass

    def test_replace_extensions_v1beta1_namespaced_replica_set_status(self):
        """Test case for replace_extensions_v1beta1_namespaced_replica_set_status

        """
        pass

    def test_replace_extensions_v1beta1_namespaced_replication_controller_dummy_scale(self):
        """Test case for replace_extensions_v1beta1_namespaced_replication_controller_dummy_scale

        """
        pass

    def test_replace_extensions_v1beta1_pod_security_policy(self):
        """Test case for replace_extensions_v1beta1_pod_security_policy

        """
        pass

    def test_watch_extensions_v1beta1_daemon_set_list_for_all_namespaces(self):
        """Test case for watch_extensions_v1beta1_daemon_set_list_for_all_namespaces

        """
        pass

    def test_watch_extensions_v1beta1_deployment_list_for_all_namespaces(self):
        """Test case for watch_extensions_v1beta1_deployment_list_for_all_namespaces

        """
        pass

    def test_watch_extensions_v1beta1_ingress_list_for_all_namespaces(self):
        """Test case for watch_extensions_v1beta1_ingress_list_for_all_namespaces

        """
        pass

    def test_watch_extensions_v1beta1_namespaced_daemon_set(self):
        """Test case for watch_extensions_v1beta1_namespaced_daemon_set

        """
        pass

    def test_watch_extensions_v1beta1_namespaced_daemon_set_list(self):
        """Test case for watch_extensions_v1beta1_namespaced_daemon_set_list

        """
        pass

    def test_watch_extensions_v1beta1_namespaced_deployment(self):
        """Test case for watch_extensions_v1beta1_namespaced_deployment

        """
        pass

    def test_watch_extensions_v1beta1_namespaced_deployment_list(self):
        """Test case for watch_extensions_v1beta1_namespaced_deployment_list

        """
        pass

    def test_watch_extensions_v1beta1_namespaced_ingress(self):
        """Test case for watch_extensions_v1beta1_namespaced_ingress

        """
        pass

    def test_watch_extensions_v1beta1_namespaced_ingress_list(self):
        """Test case for watch_extensions_v1beta1_namespaced_ingress_list

        """
        pass

    def test_watch_extensions_v1beta1_namespaced_network_policy(self):
        """Test case for watch_extensions_v1beta1_namespaced_network_policy

        """
        pass

    def test_watch_extensions_v1beta1_namespaced_network_policy_list(self):
        """Test case for watch_extensions_v1beta1_namespaced_network_policy_list

        """
        pass

    def test_watch_extensions_v1beta1_namespaced_replica_set(self):
        """Test case for watch_extensions_v1beta1_namespaced_replica_set

        """
        pass

    def test_watch_extensions_v1beta1_namespaced_replica_set_list(self):
        """Test case for watch_extensions_v1beta1_namespaced_replica_set_list

        """
        pass

    def test_watch_extensions_v1beta1_network_policy_list_for_all_namespaces(self):
        """Test case for watch_extensions_v1beta1_network_policy_list_for_all_namespaces

        """
        pass

    def test_watch_extensions_v1beta1_pod_security_policy(self):
        """Test case for watch_extensions_v1beta1_pod_security_policy

        """
        pass

    def test_watch_extensions_v1beta1_pod_security_policy_list(self):
        """Test case for watch_extensions_v1beta1_pod_security_policy_list

        """
        pass

    def test_watch_extensions_v1beta1_replica_set_list_for_all_namespaces(self):
        """Test case for watch_extensions_v1beta1_replica_set_list_for_all_namespaces

        """
        pass


if __name__ == '__main__':
    unittest.main()