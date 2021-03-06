# coding: utf-8

"""
    Argo API Client

    Generated python client for the Argo Workflows  # noqa: E501

    OpenAPI spec version: v1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from argo.sdk.models.io_k8s_api_autoscaling_v2beta2_external_metric_source import IoK8sApiAutoscalingV2beta2ExternalMetricSource  # noqa: F401,E501
from argo.sdk.models.io_k8s_api_autoscaling_v2beta2_object_metric_source import IoK8sApiAutoscalingV2beta2ObjectMetricSource  # noqa: F401,E501
from argo.sdk.models.io_k8s_api_autoscaling_v2beta2_pods_metric_source import IoK8sApiAutoscalingV2beta2PodsMetricSource  # noqa: F401,E501
from argo.sdk.models.io_k8s_api_autoscaling_v2beta2_resource_metric_source import IoK8sApiAutoscalingV2beta2ResourceMetricSource  # noqa: F401,E501


class IoK8sApiAutoscalingV2beta2MetricSpec(object):
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
        'external': 'IoK8sApiAutoscalingV2beta2ExternalMetricSource',
        'object': 'IoK8sApiAutoscalingV2beta2ObjectMetricSource',
        'pods': 'IoK8sApiAutoscalingV2beta2PodsMetricSource',
        'resource': 'IoK8sApiAutoscalingV2beta2ResourceMetricSource',
        'type': 'str'
    }

    attribute_map = {
        'external': 'external',
        'object': 'object',
        'pods': 'pods',
        'resource': 'resource',
        'type': 'type'
    }

    def __init__(self, external=None, object=None, pods=None, resource=None, type=None):  # noqa: E501
        """IoK8sApiAutoscalingV2beta2MetricSpec - a model defined in Swagger"""  # noqa: E501
        self._external = None
        self._object = None
        self._pods = None
        self._resource = None
        self._type = None
        self.discriminator = None
        if external is not None:
            self.external = external
        if object is not None:
            self.object = object
        if pods is not None:
            self.pods = pods
        if resource is not None:
            self.resource = resource
        self.type = type

    @property
    def external(self):
        """Gets the external of this IoK8sApiAutoscalingV2beta2MetricSpec.  # noqa: E501


        :return: The external of this IoK8sApiAutoscalingV2beta2MetricSpec.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2beta2ExternalMetricSource
        """
        return self._external

    @external.setter
    def external(self, external):
        """Sets the external of this IoK8sApiAutoscalingV2beta2MetricSpec.


        :param external: The external of this IoK8sApiAutoscalingV2beta2MetricSpec.  # noqa: E501
        :type: IoK8sApiAutoscalingV2beta2ExternalMetricSource
        """

        self._external = external

    @property
    def object(self):
        """Gets the object of this IoK8sApiAutoscalingV2beta2MetricSpec.  # noqa: E501


        :return: The object of this IoK8sApiAutoscalingV2beta2MetricSpec.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2beta2ObjectMetricSource
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this IoK8sApiAutoscalingV2beta2MetricSpec.


        :param object: The object of this IoK8sApiAutoscalingV2beta2MetricSpec.  # noqa: E501
        :type: IoK8sApiAutoscalingV2beta2ObjectMetricSource
        """

        self._object = object

    @property
    def pods(self):
        """Gets the pods of this IoK8sApiAutoscalingV2beta2MetricSpec.  # noqa: E501


        :return: The pods of this IoK8sApiAutoscalingV2beta2MetricSpec.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2beta2PodsMetricSource
        """
        return self._pods

    @pods.setter
    def pods(self, pods):
        """Sets the pods of this IoK8sApiAutoscalingV2beta2MetricSpec.


        :param pods: The pods of this IoK8sApiAutoscalingV2beta2MetricSpec.  # noqa: E501
        :type: IoK8sApiAutoscalingV2beta2PodsMetricSource
        """

        self._pods = pods

    @property
    def resource(self):
        """Gets the resource of this IoK8sApiAutoscalingV2beta2MetricSpec.  # noqa: E501


        :return: The resource of this IoK8sApiAutoscalingV2beta2MetricSpec.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2beta2ResourceMetricSource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this IoK8sApiAutoscalingV2beta2MetricSpec.


        :param resource: The resource of this IoK8sApiAutoscalingV2beta2MetricSpec.  # noqa: E501
        :type: IoK8sApiAutoscalingV2beta2ResourceMetricSource
        """

        self._resource = resource

    @property
    def type(self):
        """Gets the type of this IoK8sApiAutoscalingV2beta2MetricSpec.  # noqa: E501

        type is the type of metric source.  It should be one of \"Object\", \"Pods\" or \"Resource\", each mapping to a matching field in the object.  # noqa: E501

        :return: The type of this IoK8sApiAutoscalingV2beta2MetricSpec.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoK8sApiAutoscalingV2beta2MetricSpec.

        type is the type of metric source.  It should be one of \"Object\", \"Pods\" or \"Resource\", each mapping to a matching field in the object.  # noqa: E501

        :param type: The type of this IoK8sApiAutoscalingV2beta2MetricSpec.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(IoK8sApiAutoscalingV2beta2MetricSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IoK8sApiAutoscalingV2beta2MetricSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
