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

from argo_client.models.io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1beta1_custom_resource_column_definition import IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceColumnDefinition  # noqa: F401,E501
from argo_client.models.io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1beta1_custom_resource_subresources import IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresources  # noqa: F401,E501
from argo_client.models.io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1beta1_custom_resource_validation import IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceValidation  # noqa: F401,E501


class IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion(object):
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
        'additional_printer_columns': 'list[IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceColumnDefinition]',
        'name': 'str',
        'schema': 'IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceValidation',
        'served': 'bool',
        'storage': 'bool',
        'subresources': 'IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresources'
    }

    attribute_map = {
        'additional_printer_columns': 'additionalPrinterColumns',
        'name': 'name',
        'schema': 'schema',
        'served': 'served',
        'storage': 'storage',
        'subresources': 'subresources'
    }

    def __init__(self, additional_printer_columns=None, name=None, schema=None, served=None, storage=None, subresources=None):  # noqa: E501
        """IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion - a model defined in Swagger"""  # noqa: E501

        self._additional_printer_columns = None
        self._name = None
        self._schema = None
        self._served = None
        self._storage = None
        self._subresources = None
        self.discriminator = None

        if additional_printer_columns is not None:
            self.additional_printer_columns = additional_printer_columns
        self.name = name
        if schema is not None:
            self.schema = schema
        self.served = served
        self.storage = storage
        if subresources is not None:
            self.subresources = subresources

    @property
    def additional_printer_columns(self):
        """Gets the additional_printer_columns of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501

        AdditionalPrinterColumns are additional columns shown e.g. in kubectl next to the name. Defaults to a created-at column. Top-level and per-version columns are mutually exclusive. Per-version columns must not all be set to identical values (top-level columns should be used instead) This field is alpha-level and is only honored by servers that enable the CustomResourceWebhookConversion feature. NOTE: CRDs created prior to 1.13 populated the top-level additionalPrinterColumns field by default. To apply an update that changes to per-version additionalPrinterColumns, the top-level additionalPrinterColumns field must be explicitly set to null  # noqa: E501

        :return: The additional_printer_columns of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :rtype: list[IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceColumnDefinition]
        """
        return self._additional_printer_columns

    @additional_printer_columns.setter
    def additional_printer_columns(self, additional_printer_columns):
        """Sets the additional_printer_columns of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.

        AdditionalPrinterColumns are additional columns shown e.g. in kubectl next to the name. Defaults to a created-at column. Top-level and per-version columns are mutually exclusive. Per-version columns must not all be set to identical values (top-level columns should be used instead) This field is alpha-level and is only honored by servers that enable the CustomResourceWebhookConversion feature. NOTE: CRDs created prior to 1.13 populated the top-level additionalPrinterColumns field by default. To apply an update that changes to per-version additionalPrinterColumns, the top-level additionalPrinterColumns field must be explicitly set to null  # noqa: E501

        :param additional_printer_columns: The additional_printer_columns of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :type: list[IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceColumnDefinition]
        """

        self._additional_printer_columns = additional_printer_columns

    @property
    def name(self):
        """Gets the name of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501

        Name is the version name, e.g. “v1”, “v2beta1”, etc.  # noqa: E501

        :return: The name of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.

        Name is the version name, e.g. “v1”, “v2beta1”, etc.  # noqa: E501

        :param name: The name of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def schema(self):
        """Gets the schema of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501

        Schema describes the schema for CustomResource used in validation, pruning, and defaulting. Top-level and per-version schemas are mutually exclusive. Per-version schemas must not all be set to identical values (top-level validation schema should be used instead) This field is alpha-level and is only honored by servers that enable the CustomResourceWebhookConversion feature.  # noqa: E501

        :return: The schema of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :rtype: IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceValidation
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.

        Schema describes the schema for CustomResource used in validation, pruning, and defaulting. Top-level and per-version schemas are mutually exclusive. Per-version schemas must not all be set to identical values (top-level validation schema should be used instead) This field is alpha-level and is only honored by servers that enable the CustomResourceWebhookConversion feature.  # noqa: E501

        :param schema: The schema of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :type: IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceValidation
        """

        self._schema = schema

    @property
    def served(self):
        """Gets the served of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501

        Served is a flag enabling/disabling this version from being served via REST APIs  # noqa: E501

        :return: The served of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :rtype: bool
        """
        return self._served

    @served.setter
    def served(self, served):
        """Sets the served of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.

        Served is a flag enabling/disabling this version from being served via REST APIs  # noqa: E501

        :param served: The served of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :type: bool
        """
        if served is None:
            raise ValueError("Invalid value for `served`, must not be `None`")  # noqa: E501

        self._served = served

    @property
    def storage(self):
        """Gets the storage of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501

        Storage flags the version as storage version. There must be exactly one flagged as storage version.  # noqa: E501

        :return: The storage of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :rtype: bool
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.

        Storage flags the version as storage version. There must be exactly one flagged as storage version.  # noqa: E501

        :param storage: The storage of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :type: bool
        """
        if storage is None:
            raise ValueError("Invalid value for `storage`, must not be `None`")  # noqa: E501

        self._storage = storage

    @property
    def subresources(self):
        """Gets the subresources of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501

        Subresources describes the subresources for CustomResource Top-level and per-version subresources are mutually exclusive. Per-version subresources must not all be set to identical values (top-level subresources should be used instead) This field is alpha-level and is only honored by servers that enable the CustomResourceWebhookConversion feature.  # noqa: E501

        :return: The subresources of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :rtype: IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresources
        """
        return self._subresources

    @subresources.setter
    def subresources(self, subresources):
        """Sets the subresources of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.

        Subresources describes the subresources for CustomResource Top-level and per-version subresources are mutually exclusive. Per-version subresources must not all be set to identical values (top-level subresources should be used instead) This field is alpha-level and is only honored by servers that enable the CustomResourceWebhookConversion feature.  # noqa: E501

        :param subresources: The subresources of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion.  # noqa: E501
        :type: IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresources
        """

        self._subresources = subresources

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
        if not isinstance(other, IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceDefinitionVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
