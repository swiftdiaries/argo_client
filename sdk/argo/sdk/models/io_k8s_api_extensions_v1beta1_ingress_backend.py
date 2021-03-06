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
from argo.sdk.models.io_k8s_apimachinery_pkg_util_intstr_int_or_string import IoK8sApimachineryPkgUtilIntstrIntOrString  # noqa: F401,E501


class IoK8sApiExtensionsV1beta1IngressBackend(object):
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
        'service_name': 'str',
        'service_port': 'IoK8sApimachineryPkgUtilIntstrIntOrString'
    }

    attribute_map = {
        'service_name': 'serviceName',
        'service_port': 'servicePort'
    }

    def __init__(self, service_name=None, service_port=None):  # noqa: E501
        """IoK8sApiExtensionsV1beta1IngressBackend - a model defined in Swagger"""  # noqa: E501
        self._service_name = None
        self._service_port = None
        self.discriminator = None
        self.service_name = service_name
        self.service_port = service_port

    @property
    def service_name(self):
        """Gets the service_name of this IoK8sApiExtensionsV1beta1IngressBackend.  # noqa: E501

        Specifies the name of the referenced service.  # noqa: E501

        :return: The service_name of this IoK8sApiExtensionsV1beta1IngressBackend.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this IoK8sApiExtensionsV1beta1IngressBackend.

        Specifies the name of the referenced service.  # noqa: E501

        :param service_name: The service_name of this IoK8sApiExtensionsV1beta1IngressBackend.  # noqa: E501
        :type: str
        """
        if service_name is None:
            raise ValueError("Invalid value for `service_name`, must not be `None`")  # noqa: E501

        self._service_name = service_name

    @property
    def service_port(self):
        """Gets the service_port of this IoK8sApiExtensionsV1beta1IngressBackend.  # noqa: E501


        :return: The service_port of this IoK8sApiExtensionsV1beta1IngressBackend.  # noqa: E501
        :rtype: IoK8sApimachineryPkgUtilIntstrIntOrString
        """
        return self._service_port

    @service_port.setter
    def service_port(self, service_port):
        """Sets the service_port of this IoK8sApiExtensionsV1beta1IngressBackend.


        :param service_port: The service_port of this IoK8sApiExtensionsV1beta1IngressBackend.  # noqa: E501
        :type: IoK8sApimachineryPkgUtilIntstrIntOrString
        """
        if service_port is None:
            raise ValueError("Invalid value for `service_port`, must not be `None`")  # noqa: E501

        self._service_port = service_port

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
        if issubclass(IoK8sApiExtensionsV1beta1IngressBackend, dict):
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
        if not isinstance(other, IoK8sApiExtensionsV1beta1IngressBackend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
