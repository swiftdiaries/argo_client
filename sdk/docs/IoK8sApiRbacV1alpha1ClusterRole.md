# IoK8sApiRbacV1alpha1ClusterRole

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_rule** | [**IoK8sApiRbacV1alpha1AggregationRule**](IoK8sApiRbacV1alpha1AggregationRule.md) |  | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds | [optional] 
**metadata** | [**IoK8sApimachineryPkgApisMetaV1ObjectMeta**](IoK8sApimachineryPkgApisMetaV1ObjectMeta.md) |  | [optional] 
**rules** | [**list[IoK8sApiRbacV1alpha1PolicyRule]**](IoK8sApiRbacV1alpha1PolicyRule.md) | Rules holds all the PolicyRules for this ClusterRole | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

