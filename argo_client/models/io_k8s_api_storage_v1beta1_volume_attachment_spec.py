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

from argo_client.models.io_k8s_api_storage_v1beta1_volume_attachment_source import IoK8sApiStorageV1beta1VolumeAttachmentSource  # noqa: F401,E501


class IoK8sApiStorageV1beta1VolumeAttachmentSpec(object):
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
        'attacher': 'str',
        'node_name': 'str',
        'source': 'IoK8sApiStorageV1beta1VolumeAttachmentSource'
    }

    attribute_map = {
        'attacher': 'attacher',
        'node_name': 'nodeName',
        'source': 'source'
    }

    def __init__(self, attacher=None, node_name=None, source=None):  # noqa: E501
        """IoK8sApiStorageV1beta1VolumeAttachmentSpec - a model defined in Swagger"""  # noqa: E501

        self._attacher = None
        self._node_name = None
        self._source = None
        self.discriminator = None

        self.attacher = attacher
        self.node_name = node_name
        self.source = source

    @property
    def attacher(self):
        """Gets the attacher of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.  # noqa: E501

        Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().  # noqa: E501

        :return: The attacher of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.  # noqa: E501
        :rtype: str
        """
        return self._attacher

    @attacher.setter
    def attacher(self, attacher):
        """Sets the attacher of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.

        Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().  # noqa: E501

        :param attacher: The attacher of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.  # noqa: E501
        :type: str
        """
        if attacher is None:
            raise ValueError("Invalid value for `attacher`, must not be `None`")  # noqa: E501

        self._attacher = attacher

    @property
    def node_name(self):
        """Gets the node_name of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.  # noqa: E501

        The node that the volume should be attached to.  # noqa: E501

        :return: The node_name of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.  # noqa: E501
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.

        The node that the volume should be attached to.  # noqa: E501

        :param node_name: The node_name of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.  # noqa: E501
        :type: str
        """
        if node_name is None:
            raise ValueError("Invalid value for `node_name`, must not be `None`")  # noqa: E501

        self._node_name = node_name

    @property
    def source(self):
        """Gets the source of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.  # noqa: E501

        Source represents the volume that should be attached.  # noqa: E501

        :return: The source of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.  # noqa: E501
        :rtype: IoK8sApiStorageV1beta1VolumeAttachmentSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.

        Source represents the volume that should be attached.  # noqa: E501

        :param source: The source of this IoK8sApiStorageV1beta1VolumeAttachmentSpec.  # noqa: E501
        :type: IoK8sApiStorageV1beta1VolumeAttachmentSource
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

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
        if not isinstance(other, IoK8sApiStorageV1beta1VolumeAttachmentSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
