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
from api.settings_v1alpha1_api import SettingsV1alpha1Api  # noqa: E501
from argo.sdk.rest import ApiException


class TestSettingsV1alpha1Api(unittest.TestCase):
    """SettingsV1alpha1Api unit test stubs"""

    def setUp(self):
        self.api = api.settings_v1alpha1_api.SettingsV1alpha1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_settings_v1alpha1_namespaced_pod_preset(self):
        """Test case for create_settings_v1alpha1_namespaced_pod_preset

        """
        pass

    def test_delete_settings_v1alpha1_collection_namespaced_pod_preset(self):
        """Test case for delete_settings_v1alpha1_collection_namespaced_pod_preset

        """
        pass

    def test_delete_settings_v1alpha1_namespaced_pod_preset(self):
        """Test case for delete_settings_v1alpha1_namespaced_pod_preset

        """
        pass

    def test_get_settings_v1alpha1_api_resources(self):
        """Test case for get_settings_v1alpha1_api_resources

        """
        pass

    def test_list_settings_v1alpha1_namespaced_pod_preset(self):
        """Test case for list_settings_v1alpha1_namespaced_pod_preset

        """
        pass

    def test_list_settings_v1alpha1_pod_preset_for_all_namespaces(self):
        """Test case for list_settings_v1alpha1_pod_preset_for_all_namespaces

        """
        pass

    def test_patch_settings_v1alpha1_namespaced_pod_preset(self):
        """Test case for patch_settings_v1alpha1_namespaced_pod_preset

        """
        pass

    def test_read_settings_v1alpha1_namespaced_pod_preset(self):
        """Test case for read_settings_v1alpha1_namespaced_pod_preset

        """
        pass

    def test_replace_settings_v1alpha1_namespaced_pod_preset(self):
        """Test case for replace_settings_v1alpha1_namespaced_pod_preset

        """
        pass

    def test_watch_settings_v1alpha1_namespaced_pod_preset(self):
        """Test case for watch_settings_v1alpha1_namespaced_pod_preset

        """
        pass

    def test_watch_settings_v1alpha1_namespaced_pod_preset_list(self):
        """Test case for watch_settings_v1alpha1_namespaced_pod_preset_list

        """
        pass

    def test_watch_settings_v1alpha1_pod_preset_list_for_all_namespaces(self):
        """Test case for watch_settings_v1alpha1_pod_preset_list_for_all_namespaces

        """
        pass


if __name__ == '__main__':
    unittest.main()
