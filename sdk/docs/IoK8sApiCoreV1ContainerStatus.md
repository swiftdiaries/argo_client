# IoK8sApiCoreV1ContainerStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_id** | **str** | Container&#x27;s ID in the format &#x27;docker://&lt;container_id&gt;&#x27;. | [optional] 
**image** | **str** | The image the container is running. More info: https://kubernetes.io/docs/concepts/containers/images | 
**image_id** | **str** | ImageID of the container&#x27;s image. | 
**last_state** | [**IoK8sApiCoreV1ContainerState**](IoK8sApiCoreV1ContainerState.md) |  | [optional] 
**name** | **str** | This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated. | 
**ready** | **bool** | Specifies whether the container has passed its readiness probe. | 
**restart_count** | **int** | The number of times the container has been restarted, currently based on the number of dead containers that have not yet been removed. Note that this is calculated from dead containers. But those containers are subject to garbage collection. This value will get capped at 5 by GC. | 
**state** | [**IoK8sApiCoreV1ContainerState**](IoK8sApiCoreV1ContainerState.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

