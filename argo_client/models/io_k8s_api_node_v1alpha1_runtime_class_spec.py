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


class IoK8sApiNodeV1alpha1RuntimeClassSpec(object):
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
        'runtime_handler': 'str'
    }

    attribute_map = {
        'runtime_handler': 'runtimeHandler'
    }

    def __init__(self, runtime_handler=None):  # noqa: E501
        """IoK8sApiNodeV1alpha1RuntimeClassSpec - a model defined in Swagger"""  # noqa: E501

        self._runtime_handler = None
        self.discriminator = None

        self.runtime_handler = runtime_handler

    @property
    def runtime_handler(self):
        """Gets the runtime_handler of this IoK8sApiNodeV1alpha1RuntimeClassSpec.  # noqa: E501

        RuntimeHandler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called \"runc\" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The RuntimeHandler must conform to the DNS Label (RFC 1123) requirements and is immutable.  # noqa: E501

        :return: The runtime_handler of this IoK8sApiNodeV1alpha1RuntimeClassSpec.  # noqa: E501
        :rtype: str
        """
        return self._runtime_handler

    @runtime_handler.setter
    def runtime_handler(self, runtime_handler):
        """Sets the runtime_handler of this IoK8sApiNodeV1alpha1RuntimeClassSpec.

        RuntimeHandler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called \"runc\" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The RuntimeHandler must conform to the DNS Label (RFC 1123) requirements and is immutable.  # noqa: E501

        :param runtime_handler: The runtime_handler of this IoK8sApiNodeV1alpha1RuntimeClassSpec.  # noqa: E501
        :type: str
        """
        if runtime_handler is None:
            raise ValueError("Invalid value for `runtime_handler`, must not be `None`")  # noqa: E501

        self._runtime_handler = runtime_handler

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
        if not isinstance(other, IoK8sApiNodeV1alpha1RuntimeClassSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
