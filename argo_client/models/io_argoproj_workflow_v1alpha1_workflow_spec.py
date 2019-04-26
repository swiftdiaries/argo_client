# coding: utf-8

"""
    Argo

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v2.3.0-rc2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from argo_client.models.io_argoproj_workflow_v1alpha1_arguments import IoArgoprojWorkflowV1alpha1Arguments  # noqa: F401,E501
from argo_client.models.io_argoproj_workflow_v1alpha1_template import IoArgoprojWorkflowV1alpha1Template  # noqa: F401,E501
from argo_client.models.io_k8s_api_core_v1_affinity import IoK8sApiCoreV1Affinity  # noqa: F401,E501
from argo_client.models.io_k8s_api_core_v1_local_object_reference import IoK8sApiCoreV1LocalObjectReference  # noqa: F401,E501
from argo_client.models.io_k8s_api_core_v1_persistent_volume_claim import IoK8sApiCoreV1PersistentVolumeClaim  # noqa: F401,E501
from argo_client.models.io_k8s_api_core_v1_pod_dns_config import IoK8sApiCoreV1PodDNSConfig  # noqa: F401,E501
from argo_client.models.io_k8s_api_core_v1_toleration import IoK8sApiCoreV1Toleration  # noqa: F401,E501
from argo_client.models.io_k8s_api_core_v1_volume import IoK8sApiCoreV1Volume  # noqa: F401,E501


class IoArgoprojWorkflowV1alpha1WorkflowSpec(object):
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
        'active_deadline_seconds': 'int',
        'affinity': 'IoK8sApiCoreV1Affinity',
        'arguments': 'IoArgoprojWorkflowV1alpha1Arguments',
        'dns_config': 'IoK8sApiCoreV1PodDNSConfig',
        'dns_policy': 'str',
        'entrypoint': 'str',
        'host_network': 'bool',
        'image_pull_secrets': 'list[IoK8sApiCoreV1LocalObjectReference]',
        'node_selector': 'dict(str, str)',
        'on_exit': 'str',
        'parallelism': 'int',
        'pod_priority': 'int',
        'pod_priority_class_name': 'str',
        'priority': 'int',
        'scheduler_name': 'str',
        'service_account_name': 'str',
        'suspend': 'bool',
        'templates': 'list[IoArgoprojWorkflowV1alpha1Template]',
        'tolerations': 'list[IoK8sApiCoreV1Toleration]',
        'ttl_seconds_after_finished': 'int',
        'volume_claim_templates': 'list[IoK8sApiCoreV1PersistentVolumeClaim]',
        'volumes': 'list[IoK8sApiCoreV1Volume]'
    }

    attribute_map = {
        'active_deadline_seconds': 'activeDeadlineSeconds',
        'affinity': 'affinity',
        'arguments': 'arguments',
        'dns_config': 'dnsConfig',
        'dns_policy': 'dnsPolicy',
        'entrypoint': 'entrypoint',
        'host_network': 'hostNetwork',
        'image_pull_secrets': 'imagePullSecrets',
        'node_selector': 'nodeSelector',
        'on_exit': 'onExit',
        'parallelism': 'parallelism',
        'pod_priority': 'podPriority',
        'pod_priority_class_name': 'podPriorityClassName',
        'priority': 'priority',
        'scheduler_name': 'schedulerName',
        'service_account_name': 'serviceAccountName',
        'suspend': 'suspend',
        'templates': 'templates',
        'tolerations': 'tolerations',
        'ttl_seconds_after_finished': 'ttlSecondsAfterFinished',
        'volume_claim_templates': 'volumeClaimTemplates',
        'volumes': 'volumes'
    }

    def __init__(self, active_deadline_seconds=None, affinity=None, arguments=None, dns_config=None, dns_policy=None, entrypoint=None, host_network=None, image_pull_secrets=None, node_selector=None, on_exit=None, parallelism=None, pod_priority=None, pod_priority_class_name=None, priority=None, scheduler_name=None, service_account_name=None, suspend=None, templates=None, tolerations=None, ttl_seconds_after_finished=None, volume_claim_templates=None, volumes=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1WorkflowSpec - a model defined in Swagger"""  # noqa: E501

        self._active_deadline_seconds = None
        self._affinity = None
        self._arguments = None
        self._dns_config = None
        self._dns_policy = None
        self._entrypoint = None
        self._host_network = None
        self._image_pull_secrets = None
        self._node_selector = None
        self._on_exit = None
        self._parallelism = None
        self._pod_priority = None
        self._pod_priority_class_name = None
        self._priority = None
        self._scheduler_name = None
        self._service_account_name = None
        self._suspend = None
        self._templates = None
        self._tolerations = None
        self._ttl_seconds_after_finished = None
        self._volume_claim_templates = None
        self._volumes = None
        self.discriminator = None

        if active_deadline_seconds is not None:
            self.active_deadline_seconds = active_deadline_seconds
        if affinity is not None:
            self.affinity = affinity
        if arguments is not None:
            self.arguments = arguments
        if dns_config is not None:
            self.dns_config = dns_config
        if dns_policy is not None:
            self.dns_policy = dns_policy
        self.entrypoint = entrypoint
        if host_network is not None:
            self.host_network = host_network
        if image_pull_secrets is not None:
            self.image_pull_secrets = image_pull_secrets
        if node_selector is not None:
            self.node_selector = node_selector
        if on_exit is not None:
            self.on_exit = on_exit
        if parallelism is not None:
            self.parallelism = parallelism
        if pod_priority is not None:
            self.pod_priority = pod_priority
        if pod_priority_class_name is not None:
            self.pod_priority_class_name = pod_priority_class_name
        if priority is not None:
            self.priority = priority
        if scheduler_name is not None:
            self.scheduler_name = scheduler_name
        if service_account_name is not None:
            self.service_account_name = service_account_name
        if suspend is not None:
            self.suspend = suspend
        self.templates = templates
        if tolerations is not None:
            self.tolerations = tolerations
        if ttl_seconds_after_finished is not None:
            self.ttl_seconds_after_finished = ttl_seconds_after_finished
        if volume_claim_templates is not None:
            self.volume_claim_templates = volume_claim_templates
        if volumes is not None:
            self.volumes = volumes

    @property
    def active_deadline_seconds(self):
        """Gets the active_deadline_seconds of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        Optional duration in seconds relative to the workflow start time which the workflow is allowed to run before the controller terminates the workflow. A value of zero is used to terminate a Running workflow  # noqa: E501

        :return: The active_deadline_seconds of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: int
        """
        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds):
        """Sets the active_deadline_seconds of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        Optional duration in seconds relative to the workflow start time which the workflow is allowed to run before the controller terminates the workflow. A value of zero is used to terminate a Running workflow  # noqa: E501

        :param active_deadline_seconds: The active_deadline_seconds of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: int
        """

        self._active_deadline_seconds = active_deadline_seconds

    @property
    def affinity(self):
        """Gets the affinity of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        Affinity sets the scheduling constraints for all pods in the workflow. Can be overridden by an affinity specified in the template  # noqa: E501

        :return: The affinity of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: IoK8sApiCoreV1Affinity
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        Affinity sets the scheduling constraints for all pods in the workflow. Can be overridden by an affinity specified in the template  # noqa: E501

        :param affinity: The affinity of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: IoK8sApiCoreV1Affinity
        """

        self._affinity = affinity

    @property
    def arguments(self):
        """Gets the arguments of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        Arguments contain the parameters and artifacts sent to the workflow entrypoint Parameters are referencable globally using the 'workflow' variable prefix. e.g. {{workflow.parameters.myparam}}  # noqa: E501

        :return: The arguments of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: IoArgoprojWorkflowV1alpha1Arguments
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        Arguments contain the parameters and artifacts sent to the workflow entrypoint Parameters are referencable globally using the 'workflow' variable prefix. e.g. {{workflow.parameters.myparam}}  # noqa: E501

        :param arguments: The arguments of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: IoArgoprojWorkflowV1alpha1Arguments
        """

        self._arguments = arguments

    @property
    def dns_config(self):
        """Gets the dns_config of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        PodDNSConfig defines the DNS parameters of a pod in addition to those generated from DNSPolicy.  # noqa: E501

        :return: The dns_config of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: IoK8sApiCoreV1PodDNSConfig
        """
        return self._dns_config

    @dns_config.setter
    def dns_config(self, dns_config):
        """Sets the dns_config of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        PodDNSConfig defines the DNS parameters of a pod in addition to those generated from DNSPolicy.  # noqa: E501

        :param dns_config: The dns_config of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: IoK8sApiCoreV1PodDNSConfig
        """

        self._dns_config = dns_config

    @property
    def dns_policy(self):
        """Gets the dns_policy of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        Set DNS policy for the pod. Defaults to \"ClusterFirst\". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.  # noqa: E501

        :return: The dns_policy of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._dns_policy

    @dns_policy.setter
    def dns_policy(self, dns_policy):
        """Sets the dns_policy of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        Set DNS policy for the pod. Defaults to \"ClusterFirst\". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.  # noqa: E501

        :param dns_policy: The dns_policy of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """

        self._dns_policy = dns_policy

    @property
    def entrypoint(self):
        """Gets the entrypoint of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        Entrypoint is a template reference to the starting point of the workflow  # noqa: E501

        :return: The entrypoint of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        """Sets the entrypoint of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        Entrypoint is a template reference to the starting point of the workflow  # noqa: E501

        :param entrypoint: The entrypoint of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """
        if entrypoint is None:
            raise ValueError("Invalid value for `entrypoint`, must not be `None`")  # noqa: E501

        self._entrypoint = entrypoint

    @property
    def host_network(self):
        """Gets the host_network of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        Host networking requested for this workflow pod. Default to false.  # noqa: E501

        :return: The host_network of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: bool
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """Sets the host_network of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        Host networking requested for this workflow pod. Default to false.  # noqa: E501

        :param host_network: The host_network of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: bool
        """

        self._host_network = host_network

    @property
    def image_pull_secrets(self):
        """Gets the image_pull_secrets of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod  # noqa: E501

        :return: The image_pull_secrets of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: list[IoK8sApiCoreV1LocalObjectReference]
        """
        return self._image_pull_secrets

    @image_pull_secrets.setter
    def image_pull_secrets(self, image_pull_secrets):
        """Sets the image_pull_secrets of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod  # noqa: E501

        :param image_pull_secrets: The image_pull_secrets of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: list[IoK8sApiCoreV1LocalObjectReference]
        """

        self._image_pull_secrets = image_pull_secrets

    @property
    def node_selector(self):
        """Gets the node_selector of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        NodeSelector is a selector which will result in all pods of the workflow to be scheduled on the selected node(s). This is able to be overridden by a nodeSelector specified in the template.  # noqa: E501

        :return: The node_selector of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        NodeSelector is a selector which will result in all pods of the workflow to be scheduled on the selected node(s). This is able to be overridden by a nodeSelector specified in the template.  # noqa: E501

        :param node_selector: The node_selector of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def on_exit(self):
        """Gets the on_exit of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        OnExit is a template reference which is invoked at the end of the workflow, irrespective of the success, failure, or error of the primary workflow.  # noqa: E501

        :return: The on_exit of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._on_exit

    @on_exit.setter
    def on_exit(self, on_exit):
        """Sets the on_exit of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        OnExit is a template reference which is invoked at the end of the workflow, irrespective of the success, failure, or error of the primary workflow.  # noqa: E501

        :param on_exit: The on_exit of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """

        self._on_exit = on_exit

    @property
    def parallelism(self):
        """Gets the parallelism of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        Parallelism limits the max total parallel pods that can execute at the same time in a workflow  # noqa: E501

        :return: The parallelism of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: int
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """Sets the parallelism of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        Parallelism limits the max total parallel pods that can execute at the same time in a workflow  # noqa: E501

        :param parallelism: The parallelism of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: int
        """

        self._parallelism = parallelism

    @property
    def pod_priority(self):
        """Gets the pod_priority of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        Priority to apply to workflow pods.  # noqa: E501

        :return: The pod_priority of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: int
        """
        return self._pod_priority

    @pod_priority.setter
    def pod_priority(self, pod_priority):
        """Sets the pod_priority of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        Priority to apply to workflow pods.  # noqa: E501

        :param pod_priority: The pod_priority of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: int
        """

        self._pod_priority = pod_priority

    @property
    def pod_priority_class_name(self):
        """Gets the pod_priority_class_name of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        PriorityClassName to apply to workflow pods.  # noqa: E501

        :return: The pod_priority_class_name of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._pod_priority_class_name

    @pod_priority_class_name.setter
    def pod_priority_class_name(self, pod_priority_class_name):
        """Sets the pod_priority_class_name of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        PriorityClassName to apply to workflow pods.  # noqa: E501

        :param pod_priority_class_name: The pod_priority_class_name of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """

        self._pod_priority_class_name = pod_priority_class_name

    @property
    def priority(self):
        """Gets the priority of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        Priority is used if controller is configured to process limited number of workflows in parallel. Workflows with higher priority are processed first.  # noqa: E501

        :return: The priority of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        Priority is used if controller is configured to process limited number of workflows in parallel. Workflows with higher priority are processed first.  # noqa: E501

        :param priority: The priority of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def scheduler_name(self):
        """Gets the scheduler_name of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        Set scheduler name for all pods. Will be overridden if container/script template's scheduler name is set. Default scheduler will be used if neither specified.  # noqa: E501

        :return: The scheduler_name of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._scheduler_name

    @scheduler_name.setter
    def scheduler_name(self, scheduler_name):
        """Sets the scheduler_name of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        Set scheduler name for all pods. Will be overridden if container/script template's scheduler name is set. Default scheduler will be used if neither specified.  # noqa: E501

        :param scheduler_name: The scheduler_name of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """

        self._scheduler_name = scheduler_name

    @property
    def service_account_name(self):
        """Gets the service_account_name of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        ServiceAccountName is the name of the ServiceAccount to run all pods of the workflow as.  # noqa: E501

        :return: The service_account_name of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """Sets the service_account_name of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        ServiceAccountName is the name of the ServiceAccount to run all pods of the workflow as.  # noqa: E501

        :param service_account_name: The service_account_name of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: str
        """

        self._service_account_name = service_account_name

    @property
    def suspend(self):
        """Gets the suspend of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        Suspend will suspend the workflow and prevent execution of any future steps in the workflow  # noqa: E501

        :return: The suspend of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: bool
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """Sets the suspend of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        Suspend will suspend the workflow and prevent execution of any future steps in the workflow  # noqa: E501

        :param suspend: The suspend of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: bool
        """

        self._suspend = suspend

    @property
    def templates(self):
        """Gets the templates of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        Templates is a list of workflow templates used in a workflow  # noqa: E501

        :return: The templates of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: list[IoArgoprojWorkflowV1alpha1Template]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        Templates is a list of workflow templates used in a workflow  # noqa: E501

        :param templates: The templates of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: list[IoArgoprojWorkflowV1alpha1Template]
        """
        if templates is None:
            raise ValueError("Invalid value for `templates`, must not be `None`")  # noqa: E501

        self._templates = templates

    @property
    def tolerations(self):
        """Gets the tolerations of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        Tolerations to apply to workflow pods.  # noqa: E501

        :return: The tolerations of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: list[IoK8sApiCoreV1Toleration]
        """
        return self._tolerations

    @tolerations.setter
    def tolerations(self, tolerations):
        """Sets the tolerations of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        Tolerations to apply to workflow pods.  # noqa: E501

        :param tolerations: The tolerations of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: list[IoK8sApiCoreV1Toleration]
        """

        self._tolerations = tolerations

    @property
    def ttl_seconds_after_finished(self):
        """Gets the ttl_seconds_after_finished of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        TTLSecondsAfterFinished limits the lifetime of a Workflow that has finished execution (Succeeded, Failed, Error). If this field is set, once the Workflow finishes, it will be deleted after ttlSecondsAfterFinished expires. If this field is unset, ttlSecondsAfterFinished will not expire. If this field is set to zero, ttlSecondsAfterFinished expires immediately after the Workflow finishes.  # noqa: E501

        :return: The ttl_seconds_after_finished of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: int
        """
        return self._ttl_seconds_after_finished

    @ttl_seconds_after_finished.setter
    def ttl_seconds_after_finished(self, ttl_seconds_after_finished):
        """Sets the ttl_seconds_after_finished of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        TTLSecondsAfterFinished limits the lifetime of a Workflow that has finished execution (Succeeded, Failed, Error). If this field is set, once the Workflow finishes, it will be deleted after ttlSecondsAfterFinished expires. If this field is unset, ttlSecondsAfterFinished will not expire. If this field is set to zero, ttlSecondsAfterFinished expires immediately after the Workflow finishes.  # noqa: E501

        :param ttl_seconds_after_finished: The ttl_seconds_after_finished of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: int
        """

        self._ttl_seconds_after_finished = ttl_seconds_after_finished

    @property
    def volume_claim_templates(self):
        """Gets the volume_claim_templates of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        VolumeClaimTemplates is a list of claims that containers are allowed to reference. The Workflow controller will create the claims at the beginning of the workflow and delete the claims upon completion of the workflow  # noqa: E501

        :return: The volume_claim_templates of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: list[IoK8sApiCoreV1PersistentVolumeClaim]
        """
        return self._volume_claim_templates

    @volume_claim_templates.setter
    def volume_claim_templates(self, volume_claim_templates):
        """Sets the volume_claim_templates of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        VolumeClaimTemplates is a list of claims that containers are allowed to reference. The Workflow controller will create the claims at the beginning of the workflow and delete the claims upon completion of the workflow  # noqa: E501

        :param volume_claim_templates: The volume_claim_templates of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: list[IoK8sApiCoreV1PersistentVolumeClaim]
        """

        self._volume_claim_templates = volume_claim_templates

    @property
    def volumes(self):
        """Gets the volumes of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501

        Volumes is a list of volumes that can be mounted by containers in a workflow.  # noqa: E501

        :return: The volumes of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :rtype: list[IoK8sApiCoreV1Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this IoArgoprojWorkflowV1alpha1WorkflowSpec.

        Volumes is a list of volumes that can be mounted by containers in a workflow.  # noqa: E501

        :param volumes: The volumes of this IoArgoprojWorkflowV1alpha1WorkflowSpec.  # noqa: E501
        :type: list[IoK8sApiCoreV1Volume]
        """

        self._volumes = volumes

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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1WorkflowSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
