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
from argo.sdk.models.io_k8s_apimachinery_pkg_api_resource_quantity import IoK8sApimachineryPkgApiResourceQuantity  # noqa: F401,E501


class IoK8sApiAutoscalingV2beta1ResourceMetricStatus(object):
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
        'current_average_utilization': 'int',
        'current_average_value': 'IoK8sApimachineryPkgApiResourceQuantity',
        'name': 'str'
    }

    attribute_map = {
        'current_average_utilization': 'currentAverageUtilization',
        'current_average_value': 'currentAverageValue',
        'name': 'name'
    }

    def __init__(self, current_average_utilization=None, current_average_value=None, name=None):  # noqa: E501
        """IoK8sApiAutoscalingV2beta1ResourceMetricStatus - a model defined in Swagger"""  # noqa: E501
        self._current_average_utilization = None
        self._current_average_value = None
        self._name = None
        self.discriminator = None
        if current_average_utilization is not None:
            self.current_average_utilization = current_average_utilization
        self.current_average_value = current_average_value
        self.name = name

    @property
    def current_average_utilization(self):
        """Gets the current_average_utilization of this IoK8sApiAutoscalingV2beta1ResourceMetricStatus.  # noqa: E501

        currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  It will only be present if `targetAverageValue` was set in the corresponding metric specification.  # noqa: E501

        :return: The current_average_utilization of this IoK8sApiAutoscalingV2beta1ResourceMetricStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_average_utilization

    @current_average_utilization.setter
    def current_average_utilization(self, current_average_utilization):
        """Sets the current_average_utilization of this IoK8sApiAutoscalingV2beta1ResourceMetricStatus.

        currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  It will only be present if `targetAverageValue` was set in the corresponding metric specification.  # noqa: E501

        :param current_average_utilization: The current_average_utilization of this IoK8sApiAutoscalingV2beta1ResourceMetricStatus.  # noqa: E501
        :type: int
        """

        self._current_average_utilization = current_average_utilization

    @property
    def current_average_value(self):
        """Gets the current_average_value of this IoK8sApiAutoscalingV2beta1ResourceMetricStatus.  # noqa: E501


        :return: The current_average_value of this IoK8sApiAutoscalingV2beta1ResourceMetricStatus.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApiResourceQuantity
        """
        return self._current_average_value

    @current_average_value.setter
    def current_average_value(self, current_average_value):
        """Sets the current_average_value of this IoK8sApiAutoscalingV2beta1ResourceMetricStatus.


        :param current_average_value: The current_average_value of this IoK8sApiAutoscalingV2beta1ResourceMetricStatus.  # noqa: E501
        :type: IoK8sApimachineryPkgApiResourceQuantity
        """
        if current_average_value is None:
            raise ValueError("Invalid value for `current_average_value`, must not be `None`")  # noqa: E501

        self._current_average_value = current_average_value

    @property
    def name(self):
        """Gets the name of this IoK8sApiAutoscalingV2beta1ResourceMetricStatus.  # noqa: E501

        name is the name of the resource in question.  # noqa: E501

        :return: The name of this IoK8sApiAutoscalingV2beta1ResourceMetricStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoK8sApiAutoscalingV2beta1ResourceMetricStatus.

        name is the name of the resource in question.  # noqa: E501

        :param name: The name of this IoK8sApiAutoscalingV2beta1ResourceMetricStatus.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(IoK8sApiAutoscalingV2beta1ResourceMetricStatus, dict):
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
        if not isinstance(other, IoK8sApiAutoscalingV2beta1ResourceMetricStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
