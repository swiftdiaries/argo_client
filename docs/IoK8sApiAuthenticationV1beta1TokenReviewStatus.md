# IoK8sApiAuthenticationV1beta1TokenReviewStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | **list[str]** | Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token&#39;s audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is \&quot;true\&quot;, the token is valid against the audience of the Kubernetes API server. | [optional] 
**authenticated** | **bool** | Authenticated indicates that the token was associated with a known user. | [optional] 
**error** | **str** | Error indicates that the token couldn&#39;t be checked | [optional] 
**user** | [**IoK8sApiAuthenticationV1beta1UserInfo**](IoK8sApiAuthenticationV1beta1UserInfo.md) | User is the UserInfo associated with the provided token. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

