# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.15.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from argo_client.models.io_k8s_api_core_v1_component_condition import IoK8sApiCoreV1ComponentCondition  # noqa: F401,E501
from argo_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_object_meta import IoK8sApimachineryPkgApisMetaV1ObjectMeta  # noqa: F401,E501


class IoK8sApiCoreV1ComponentStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'api_version': 'str',
        'conditions': 'list[IoK8sApiCoreV1ComponentCondition]',
        'kind': 'str',
        'metadata': 'IoK8sApimachineryPkgApisMetaV1ObjectMeta'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'conditions': 'conditions',
        'kind': 'kind',
        'metadata': 'metadata'
    }

    def __init__(self, api_version=None, conditions=None, kind=None, metadata=None):  # noqa: E501
        """IoK8sApiCoreV1ComponentStatus - a model defined in Swagger"""  # noqa: E501

        self._api_version = None
        self._conditions = None
        self._kind = None
        self._metadata = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if conditions is not None:
            self.conditions = conditions
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata

    @property
    def api_version(self):
        """Gets the api_version of this IoK8sApiCoreV1ComponentStatus.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this IoK8sApiCoreV1ComponentStatus.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this IoK8sApiCoreV1ComponentStatus.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this IoK8sApiCoreV1ComponentStatus.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def conditions(self):
        """Gets the conditions of this IoK8sApiCoreV1ComponentStatus.  # noqa: E501

        List of component conditions observed  # noqa: E501

        :return: The conditions of this IoK8sApiCoreV1ComponentStatus.  # noqa: E501
        :rtype: list[IoK8sApiCoreV1ComponentCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this IoK8sApiCoreV1ComponentStatus.

        List of component conditions observed  # noqa: E501

        :param conditions: The conditions of this IoK8sApiCoreV1ComponentStatus.  # noqa: E501
        :type: list[IoK8sApiCoreV1ComponentCondition]
        """

        self._conditions = conditions

    @property
    def kind(self):
        """Gets the kind of this IoK8sApiCoreV1ComponentStatus.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this IoK8sApiCoreV1ComponentStatus.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this IoK8sApiCoreV1ComponentStatus.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this IoK8sApiCoreV1ComponentStatus.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this IoK8sApiCoreV1ComponentStatus.  # noqa: E501

        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata  # noqa: E501

        :return: The metadata of this IoK8sApiCoreV1ComponentStatus.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoK8sApiCoreV1ComponentStatus.

        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata  # noqa: E501

        :param metadata: The metadata of this IoK8sApiCoreV1ComponentStatus.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """

        self._metadata = metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IoK8sApiCoreV1ComponentStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
