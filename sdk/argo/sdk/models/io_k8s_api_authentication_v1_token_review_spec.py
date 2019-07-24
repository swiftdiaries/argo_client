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


class IoK8sApiAuthenticationV1TokenReviewSpec(object):
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
        'audiences': 'list[str]',
        'token': 'str'
    }

    attribute_map = {
        'audiences': 'audiences',
        'token': 'token'
    }

    def __init__(self, audiences=None, token=None):  # noqa: E501
        """IoK8sApiAuthenticationV1TokenReviewSpec - a model defined in Swagger"""  # noqa: E501
        self._audiences = None
        self._token = None
        self.discriminator = None
        if audiences is not None:
            self.audiences = audiences
        if token is not None:
            self.token = token

    @property
    def audiences(self):
        """Gets the audiences of this IoK8sApiAuthenticationV1TokenReviewSpec.  # noqa: E501

        Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver.  # noqa: E501

        :return: The audiences of this IoK8sApiAuthenticationV1TokenReviewSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._audiences

    @audiences.setter
    def audiences(self, audiences):
        """Sets the audiences of this IoK8sApiAuthenticationV1TokenReviewSpec.

        Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver.  # noqa: E501

        :param audiences: The audiences of this IoK8sApiAuthenticationV1TokenReviewSpec.  # noqa: E501
        :type: list[str]
        """

        self._audiences = audiences

    @property
    def token(self):
        """Gets the token of this IoK8sApiAuthenticationV1TokenReviewSpec.  # noqa: E501

        Token is the opaque bearer token.  # noqa: E501

        :return: The token of this IoK8sApiAuthenticationV1TokenReviewSpec.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this IoK8sApiAuthenticationV1TokenReviewSpec.

        Token is the opaque bearer token.  # noqa: E501

        :param token: The token of this IoK8sApiAuthenticationV1TokenReviewSpec.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if issubclass(IoK8sApiAuthenticationV1TokenReviewSpec, dict):
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
        if not isinstance(other, IoK8sApiAuthenticationV1TokenReviewSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other