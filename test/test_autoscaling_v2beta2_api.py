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
from argo_client.api.autoscaling_v2beta2_api import AutoscalingV2beta2Api  # noqa: E501
from argo_client.rest import ApiException


class TestAutoscalingV2beta2Api(unittest.TestCase):
    """AutoscalingV2beta2Api unit test stubs"""

    def setUp(self):
        self.api = argo_client.api.autoscaling_v2beta2_api.AutoscalingV2beta2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler(self):
        """Test case for create_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_delete_autoscaling_v2beta2_collection_namespaced_horizontal_pod_autoscaler(self):
        """Test case for delete_autoscaling_v2beta2_collection_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_delete_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler(self):
        """Test case for delete_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_get_autoscaling_v2beta2_api_resources(self):
        """Test case for get_autoscaling_v2beta2_api_resources

        """
        pass

    def test_list_autoscaling_v2beta2_horizontal_pod_autoscaler_for_all_namespaces(self):
        """Test case for list_autoscaling_v2beta2_horizontal_pod_autoscaler_for_all_namespaces

        """
        pass

    def test_list_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler(self):
        """Test case for list_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_patch_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler(self):
        """Test case for patch_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_patch_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler_status(self):
        """Test case for patch_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler_status

        """
        pass

    def test_read_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler(self):
        """Test case for read_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_read_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler_status(self):
        """Test case for read_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler_status

        """
        pass

    def test_replace_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler(self):
        """Test case for replace_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_replace_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler_status(self):
        """Test case for replace_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler_status

        """
        pass

    def test_watch_autoscaling_v2beta2_horizontal_pod_autoscaler_list_for_all_namespaces(self):
        """Test case for watch_autoscaling_v2beta2_horizontal_pod_autoscaler_list_for_all_namespaces

        """
        pass

    def test_watch_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler(self):
        """Test case for watch_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_watch_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler_list(self):
        """Test case for watch_autoscaling_v2beta2_namespaced_horizontal_pod_autoscaler_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
