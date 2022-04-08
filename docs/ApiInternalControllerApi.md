# mailslurp_client.ApiInternalControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_saml_user_or_create**](ApiInternalControllerApi#get_saml_user_or_create) | **POST** /internal/saml/user | 


# **get_saml_user_or_create**
> UserDto get_saml_user_or_create(key, get_or_create_saml_user_options)



### Example

* Api Key Authentication (API_KEY):
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mailslurp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailslurp_client.Configuration(
    host = "https://api.mailslurp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration(
    host = "https://api.mailslurp.com",
    api_key = {
        'x-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with mailslurp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailslurp_client.ApiInternalControllerApi(api_client)
    key = 'key_example' # str | 
get_or_create_saml_user_options = mailslurp_client.GetOrCreateSamlUserOptions() # GetOrCreateSamlUserOptions | 

    try:
        api_response = api_instance.get_saml_user_or_create(key, get_or_create_saml_user_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiInternalControllerApi->get_saml_user_or_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **get_or_create_saml_user_options** | [**GetOrCreateSamlUserOptions**](GetOrCreateSamlUserOptions)|  | 

### Return type

[**UserDto**](UserDto)

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

