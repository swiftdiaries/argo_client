# IoK8sApiAutoscalingV2beta1ExternalMetricSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_name** | **str** | metricName is the name of the metric in question. | 
**metric_selector** | [**IoK8sApimachineryPkgApisMetaV1LabelSelector**](IoK8sApimachineryPkgApisMetaV1LabelSelector.md) | metricSelector is used to identify a specific time series within a given metric. | [optional] 
**target_average_value** | [**IoK8sApimachineryPkgApiResourceQuantity**](IoK8sApimachineryPkgApiResourceQuantity.md) | targetAverageValue is the target per-pod value of global metric (as a quantity). Mutually exclusive with TargetValue. | [optional] 
**target_value** | [**IoK8sApimachineryPkgApiResourceQuantity**](IoK8sApimachineryPkgApiResourceQuantity.md) | targetValue is the target value of the metric (as a quantity). Mutually exclusive with TargetAverageValue. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


