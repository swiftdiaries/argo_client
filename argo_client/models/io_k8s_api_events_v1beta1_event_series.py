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

from argo_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_micro_time import IoK8sApimachineryPkgApisMetaV1MicroTime  # noqa: F401,E501


class IoK8sApiEventsV1beta1EventSeries(object):
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
        'count': 'int',
        'last_observed_time': 'IoK8sApimachineryPkgApisMetaV1MicroTime',
        'state': 'str'
    }

    attribute_map = {
        'count': 'count',
        'last_observed_time': 'lastObservedTime',
        'state': 'state'
    }

    def __init__(self, count=None, last_observed_time=None, state=None):  # noqa: E501
        """IoK8sApiEventsV1beta1EventSeries - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._last_observed_time = None
        self._state = None
        self.discriminator = None

        self.count = count
        self.last_observed_time = last_observed_time
        self.state = state

    @property
    def count(self):
        """Gets the count of this IoK8sApiEventsV1beta1EventSeries.  # noqa: E501

        Number of occurrences in this series up to the last heartbeat time  # noqa: E501

        :return: The count of this IoK8sApiEventsV1beta1EventSeries.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this IoK8sApiEventsV1beta1EventSeries.

        Number of occurrences in this series up to the last heartbeat time  # noqa: E501

        :param count: The count of this IoK8sApiEventsV1beta1EventSeries.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def last_observed_time(self):
        """Gets the last_observed_time of this IoK8sApiEventsV1beta1EventSeries.  # noqa: E501

        Time when last Event from the series was seen before last heartbeat.  # noqa: E501

        :return: The last_observed_time of this IoK8sApiEventsV1beta1EventSeries.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1MicroTime
        """
        return self._last_observed_time

    @last_observed_time.setter
    def last_observed_time(self, last_observed_time):
        """Sets the last_observed_time of this IoK8sApiEventsV1beta1EventSeries.

        Time when last Event from the series was seen before last heartbeat.  # noqa: E501

        :param last_observed_time: The last_observed_time of this IoK8sApiEventsV1beta1EventSeries.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1MicroTime
        """
        if last_observed_time is None:
            raise ValueError("Invalid value for `last_observed_time`, must not be `None`")  # noqa: E501

        self._last_observed_time = last_observed_time

    @property
    def state(self):
        """Gets the state of this IoK8sApiEventsV1beta1EventSeries.  # noqa: E501

        Information whether this series is ongoing or finished.  # noqa: E501

        :return: The state of this IoK8sApiEventsV1beta1EventSeries.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this IoK8sApiEventsV1beta1EventSeries.

        Information whether this series is ongoing or finished.  # noqa: E501

        :param state: The state of this IoK8sApiEventsV1beta1EventSeries.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

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
        if not isinstance(other, IoK8sApiEventsV1beta1EventSeries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
