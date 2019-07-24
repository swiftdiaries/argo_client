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
from argo.sdk.models.io_k8s_api_storage_v1beta1_volume_error import IoK8sApiStorageV1beta1VolumeError  # noqa: F401,E501


class IoK8sApiStorageV1beta1VolumeAttachmentStatus(object):
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
        'attach_error': 'IoK8sApiStorageV1beta1VolumeError',
        'attached': 'bool',
        'attachment_metadata': 'dict(str, str)',
        'detach_error': 'IoK8sApiStorageV1beta1VolumeError'
    }

    attribute_map = {
        'attach_error': 'attachError',
        'attached': 'attached',
        'attachment_metadata': 'attachmentMetadata',
        'detach_error': 'detachError'
    }

    def __init__(self, attach_error=None, attached=None, attachment_metadata=None, detach_error=None):  # noqa: E501
        """IoK8sApiStorageV1beta1VolumeAttachmentStatus - a model defined in Swagger"""  # noqa: E501
        self._attach_error = None
        self._attached = None
        self._attachment_metadata = None
        self._detach_error = None
        self.discriminator = None
        if attach_error is not None:
            self.attach_error = attach_error
        self.attached = attached
        if attachment_metadata is not None:
            self.attachment_metadata = attachment_metadata
        if detach_error is not None:
            self.detach_error = detach_error

    @property
    def attach_error(self):
        """Gets the attach_error of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.  # noqa: E501


        :return: The attach_error of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.  # noqa: E501
        :rtype: IoK8sApiStorageV1beta1VolumeError
        """
        return self._attach_error

    @attach_error.setter
    def attach_error(self, attach_error):
        """Sets the attach_error of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.


        :param attach_error: The attach_error of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.  # noqa: E501
        :type: IoK8sApiStorageV1beta1VolumeError
        """

        self._attach_error = attach_error

    @property
    def attached(self):
        """Gets the attached of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.  # noqa: E501

        Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.  # noqa: E501

        :return: The attached of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.  # noqa: E501
        :rtype: bool
        """
        return self._attached

    @attached.setter
    def attached(self, attached):
        """Sets the attached of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.

        Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.  # noqa: E501

        :param attached: The attached of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.  # noqa: E501
        :type: bool
        """
        if attached is None:
            raise ValueError("Invalid value for `attached`, must not be `None`")  # noqa: E501

        self._attached = attached

    @property
    def attachment_metadata(self):
        """Gets the attachment_metadata of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.  # noqa: E501

        Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.  # noqa: E501

        :return: The attachment_metadata of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._attachment_metadata

    @attachment_metadata.setter
    def attachment_metadata(self, attachment_metadata):
        """Sets the attachment_metadata of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.

        Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.  # noqa: E501

        :param attachment_metadata: The attachment_metadata of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._attachment_metadata = attachment_metadata

    @property
    def detach_error(self):
        """Gets the detach_error of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.  # noqa: E501


        :return: The detach_error of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.  # noqa: E501
        :rtype: IoK8sApiStorageV1beta1VolumeError
        """
        return self._detach_error

    @detach_error.setter
    def detach_error(self, detach_error):
        """Sets the detach_error of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.


        :param detach_error: The detach_error of this IoK8sApiStorageV1beta1VolumeAttachmentStatus.  # noqa: E501
        :type: IoK8sApiStorageV1beta1VolumeError
        """

        self._detach_error = detach_error

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
        if issubclass(IoK8sApiStorageV1beta1VolumeAttachmentStatus, dict):
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
        if not isinstance(other, IoK8sApiStorageV1beta1VolumeAttachmentStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other