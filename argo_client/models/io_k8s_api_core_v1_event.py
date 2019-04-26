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

from argo_client.models.io_k8s_api_core_v1_event_series import IoK8sApiCoreV1EventSeries  # noqa: F401,E501
from argo_client.models.io_k8s_api_core_v1_event_source import IoK8sApiCoreV1EventSource  # noqa: F401,E501
from argo_client.models.io_k8s_api_core_v1_object_reference import IoK8sApiCoreV1ObjectReference  # noqa: F401,E501
from argo_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_micro_time import IoK8sApimachineryPkgApisMetaV1MicroTime  # noqa: F401,E501
from argo_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_object_meta import IoK8sApimachineryPkgApisMetaV1ObjectMeta  # noqa: F401,E501
from argo_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_time import IoK8sApimachineryPkgApisMetaV1Time  # noqa: F401,E501


class IoK8sApiCoreV1Event(object):
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
        'action': 'str',
        'api_version': 'str',
        'count': 'int',
        'event_time': 'IoK8sApimachineryPkgApisMetaV1MicroTime',
        'first_timestamp': 'IoK8sApimachineryPkgApisMetaV1Time',
        'involved_object': 'IoK8sApiCoreV1ObjectReference',
        'kind': 'str',
        'last_timestamp': 'IoK8sApimachineryPkgApisMetaV1Time',
        'message': 'str',
        'metadata': 'IoK8sApimachineryPkgApisMetaV1ObjectMeta',
        'reason': 'str',
        'related': 'IoK8sApiCoreV1ObjectReference',
        'reporting_component': 'str',
        'reporting_instance': 'str',
        'series': 'IoK8sApiCoreV1EventSeries',
        'source': 'IoK8sApiCoreV1EventSource',
        'type': 'str'
    }

    attribute_map = {
        'action': 'action',
        'api_version': 'apiVersion',
        'count': 'count',
        'event_time': 'eventTime',
        'first_timestamp': 'firstTimestamp',
        'involved_object': 'involvedObject',
        'kind': 'kind',
        'last_timestamp': 'lastTimestamp',
        'message': 'message',
        'metadata': 'metadata',
        'reason': 'reason',
        'related': 'related',
        'reporting_component': 'reportingComponent',
        'reporting_instance': 'reportingInstance',
        'series': 'series',
        'source': 'source',
        'type': 'type'
    }

    def __init__(self, action=None, api_version=None, count=None, event_time=None, first_timestamp=None, involved_object=None, kind=None, last_timestamp=None, message=None, metadata=None, reason=None, related=None, reporting_component=None, reporting_instance=None, series=None, source=None, type=None):  # noqa: E501
        """IoK8sApiCoreV1Event - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._api_version = None
        self._count = None
        self._event_time = None
        self._first_timestamp = None
        self._involved_object = None
        self._kind = None
        self._last_timestamp = None
        self._message = None
        self._metadata = None
        self._reason = None
        self._related = None
        self._reporting_component = None
        self._reporting_instance = None
        self._series = None
        self._source = None
        self._type = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if api_version is not None:
            self.api_version = api_version
        if count is not None:
            self.count = count
        if event_time is not None:
            self.event_time = event_time
        if first_timestamp is not None:
            self.first_timestamp = first_timestamp
        self.involved_object = involved_object
        if kind is not None:
            self.kind = kind
        if last_timestamp is not None:
            self.last_timestamp = last_timestamp
        if message is not None:
            self.message = message
        self.metadata = metadata
        if reason is not None:
            self.reason = reason
        if related is not None:
            self.related = related
        if reporting_component is not None:
            self.reporting_component = reporting_component
        if reporting_instance is not None:
            self.reporting_instance = reporting_instance
        if series is not None:
            self.series = series
        if source is not None:
            self.source = source
        if type is not None:
            self.type = type

    @property
    def action(self):
        """Gets the action of this IoK8sApiCoreV1Event.  # noqa: E501

        What action was taken/failed regarding to the Regarding object.  # noqa: E501

        :return: The action of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this IoK8sApiCoreV1Event.

        What action was taken/failed regarding to the Regarding object.  # noqa: E501

        :param action: The action of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def api_version(self):
        """Gets the api_version of this IoK8sApiCoreV1Event.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this IoK8sApiCoreV1Event.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def count(self):
        """Gets the count of this IoK8sApiCoreV1Event.  # noqa: E501

        The number of times this event has occurred.  # noqa: E501

        :return: The count of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this IoK8sApiCoreV1Event.

        The number of times this event has occurred.  # noqa: E501

        :param count: The count of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def event_time(self):
        """Gets the event_time of this IoK8sApiCoreV1Event.  # noqa: E501

        Time when this Event was first observed.  # noqa: E501

        :return: The event_time of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1MicroTime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this IoK8sApiCoreV1Event.

        Time when this Event was first observed.  # noqa: E501

        :param event_time: The event_time of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1MicroTime
        """

        self._event_time = event_time

    @property
    def first_timestamp(self):
        """Gets the first_timestamp of this IoK8sApiCoreV1Event.  # noqa: E501

        The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)  # noqa: E501

        :return: The first_timestamp of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._first_timestamp

    @first_timestamp.setter
    def first_timestamp(self, first_timestamp):
        """Sets the first_timestamp of this IoK8sApiCoreV1Event.

        The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)  # noqa: E501

        :param first_timestamp: The first_timestamp of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._first_timestamp = first_timestamp

    @property
    def involved_object(self):
        """Gets the involved_object of this IoK8sApiCoreV1Event.  # noqa: E501

        The object that this event is about.  # noqa: E501

        :return: The involved_object of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: IoK8sApiCoreV1ObjectReference
        """
        return self._involved_object

    @involved_object.setter
    def involved_object(self, involved_object):
        """Sets the involved_object of this IoK8sApiCoreV1Event.

        The object that this event is about.  # noqa: E501

        :param involved_object: The involved_object of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: IoK8sApiCoreV1ObjectReference
        """
        if involved_object is None:
            raise ValueError("Invalid value for `involved_object`, must not be `None`")  # noqa: E501

        self._involved_object = involved_object

    @property
    def kind(self):
        """Gets the kind of this IoK8sApiCoreV1Event.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this IoK8sApiCoreV1Event.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def last_timestamp(self):
        """Gets the last_timestamp of this IoK8sApiCoreV1Event.  # noqa: E501

        The time at which the most recent occurrence of this event was recorded.  # noqa: E501

        :return: The last_timestamp of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, last_timestamp):
        """Sets the last_timestamp of this IoK8sApiCoreV1Event.

        The time at which the most recent occurrence of this event was recorded.  # noqa: E501

        :param last_timestamp: The last_timestamp of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._last_timestamp = last_timestamp

    @property
    def message(self):
        """Gets the message of this IoK8sApiCoreV1Event.  # noqa: E501

        A human-readable description of the status of this operation.  # noqa: E501

        :return: The message of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this IoK8sApiCoreV1Event.

        A human-readable description of the status of this operation.  # noqa: E501

        :param message: The message of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def metadata(self):
        """Gets the metadata of this IoK8sApiCoreV1Event.  # noqa: E501

        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata  # noqa: E501

        :return: The metadata of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoK8sApiCoreV1Event.

        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata  # noqa: E501

        :param metadata: The metadata of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def reason(self):
        """Gets the reason of this IoK8sApiCoreV1Event.  # noqa: E501

        This should be a short, machine understandable string that gives the reason for the transition into the object's current status.  # noqa: E501

        :return: The reason of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this IoK8sApiCoreV1Event.

        This should be a short, machine understandable string that gives the reason for the transition into the object's current status.  # noqa: E501

        :param reason: The reason of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def related(self):
        """Gets the related of this IoK8sApiCoreV1Event.  # noqa: E501

        Optional secondary object for more complex actions.  # noqa: E501

        :return: The related of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: IoK8sApiCoreV1ObjectReference
        """
        return self._related

    @related.setter
    def related(self, related):
        """Sets the related of this IoK8sApiCoreV1Event.

        Optional secondary object for more complex actions.  # noqa: E501

        :param related: The related of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: IoK8sApiCoreV1ObjectReference
        """

        self._related = related

    @property
    def reporting_component(self):
        """Gets the reporting_component of this IoK8sApiCoreV1Event.  # noqa: E501

        Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.  # noqa: E501

        :return: The reporting_component of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._reporting_component

    @reporting_component.setter
    def reporting_component(self, reporting_component):
        """Sets the reporting_component of this IoK8sApiCoreV1Event.

        Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.  # noqa: E501

        :param reporting_component: The reporting_component of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: str
        """

        self._reporting_component = reporting_component

    @property
    def reporting_instance(self):
        """Gets the reporting_instance of this IoK8sApiCoreV1Event.  # noqa: E501

        ID of the controller instance, e.g. `kubelet-xyzf`.  # noqa: E501

        :return: The reporting_instance of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._reporting_instance

    @reporting_instance.setter
    def reporting_instance(self, reporting_instance):
        """Sets the reporting_instance of this IoK8sApiCoreV1Event.

        ID of the controller instance, e.g. `kubelet-xyzf`.  # noqa: E501

        :param reporting_instance: The reporting_instance of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: str
        """

        self._reporting_instance = reporting_instance

    @property
    def series(self):
        """Gets the series of this IoK8sApiCoreV1Event.  # noqa: E501

        Data about the Event series this event represents or nil if it's a singleton Event.  # noqa: E501

        :return: The series of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: IoK8sApiCoreV1EventSeries
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this IoK8sApiCoreV1Event.

        Data about the Event series this event represents or nil if it's a singleton Event.  # noqa: E501

        :param series: The series of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: IoK8sApiCoreV1EventSeries
        """

        self._series = series

    @property
    def source(self):
        """Gets the source of this IoK8sApiCoreV1Event.  # noqa: E501

        The component reporting this event. Should be a short machine understandable string.  # noqa: E501

        :return: The source of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: IoK8sApiCoreV1EventSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this IoK8sApiCoreV1Event.

        The component reporting this event. Should be a short machine understandable string.  # noqa: E501

        :param source: The source of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: IoK8sApiCoreV1EventSource
        """

        self._source = source

    @property
    def type(self):
        """Gets the type of this IoK8sApiCoreV1Event.  # noqa: E501

        Type of this event (Normal, Warning), new types could be added in the future  # noqa: E501

        :return: The type of this IoK8sApiCoreV1Event.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoK8sApiCoreV1Event.

        Type of this event (Normal, Warning), new types could be added in the future  # noqa: E501

        :param type: The type of this IoK8sApiCoreV1Event.  # noqa: E501
        :type: str
        """

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IoK8sApiCoreV1Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
