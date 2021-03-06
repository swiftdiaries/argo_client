# argo.sdk.SettingsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_settings_api_group**](SettingsApi.md#get_settings_api_group) | **GET** /apis/settings.k8s.io/ | 

# **get_settings_api_group**
> IoK8sApimachineryPkgApisMetaV1APIGroup get_settings_api_group()



get information of a group

### Example
```python
from __future__ import print_function
import time
import argo.sdk
from argo.sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.sdk.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.sdk.SettingsApi(argo.sdk.ApiClient(configuration))

try:
    api_response = api_instance.get_settings_api_group()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_settings_api_group: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IoK8sApimachineryPkgApisMetaV1APIGroup**](IoK8sApimachineryPkgApisMetaV1APIGroup.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

