# mailslurp_client.EmailVerificationControllerApi

All URIs are relative to *https://python.api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_validation_requests**](EmailVerificationControllerApi#get_validation_requests) | **GET** /email-verification/validation-requests | Validate a list of email addresses. Per unit billing. See your plan for pricing.
[**validate_email_address_list**](EmailVerificationControllerApi#validate_email_address_list) | **POST** /email-verification/email-address-list | Validate a list of email addresses. Per unit billing. See your plan for pricing.


# **get_validation_requests**
> PageEmailValidationRequest get_validation_requests(page=page, size=size, sort=sort, search_filter=search_filter, since=since, before=before, is_valid=is_valid)

Validate a list of email addresses. Per unit billing. See your plan for pricing.

### Example

* Api Key Authentication (API_KEY):
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://python.api.mailslurp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailslurp_client.Configuration(
    host = "https://python.api.mailslurp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration(
    host = "https://python.api.mailslurp.com",
    api_key = {
        'x-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with mailslurp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailslurp_client.EmailVerificationControllerApi(api_client)
    page = 0 # int | Optional page index in list pagination (optional) (default to 0)
size = 20 # int | Optional page size for paginated result list. (optional) (default to 20)
sort = 'DESC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'DESC')
search_filter = 'search_filter_example' # str | Optional search filter (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at after the given timestamp (optional)
before = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at before the given timestamp (optional)
is_valid = True # bool | Filter where email is valid is true or false (optional)

    try:
        # Validate a list of email addresses. Per unit billing. See your plan for pricing.
        api_response = api_instance.get_validation_requests(page=page, size=size, sort=sort, search_filter=search_filter, since=since, before=before, is_valid=is_valid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailVerificationControllerApi->get_validation_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional page index in list pagination | [optional] [default to 0]
 **size** | **int**| Optional page size for paginated result list. | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;DESC&#39;]
 **search_filter** | **str**| Optional search filter | [optional] 
 **since** | **datetime**| Filter by created at after the given timestamp | [optional] 
 **before** | **datetime**| Filter by created at before the given timestamp | [optional] 
 **is_valid** | **bool**| Filter where email is valid is true or false | [optional] 

### Return type

[**PageEmailValidationRequest**](PageEmailValidationRequest)

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

# **validate_email_address_list**
> ValidateEmailAddressListResult validate_email_address_list(validate_email_address_list_options)

Validate a list of email addresses. Per unit billing. See your plan for pricing.

### Example

* Api Key Authentication (API_KEY):
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://python.api.mailslurp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mailslurp_client.Configuration(
    host = "https://python.api.mailslurp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration(
    host = "https://python.api.mailslurp.com",
    api_key = {
        'x-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with mailslurp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailslurp_client.EmailVerificationControllerApi(api_client)
    validate_email_address_list_options = mailslurp_client.ValidateEmailAddressListOptions() # ValidateEmailAddressListOptions | 

    try:
        # Validate a list of email addresses. Per unit billing. See your plan for pricing.
        api_response = api_instance.validate_email_address_list(validate_email_address_list_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailVerificationControllerApi->validate_email_address_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_email_address_list_options** | [**ValidateEmailAddressListOptions**](ValidateEmailAddressListOptions)|  | 

### Return type

[**ValidateEmailAddressListResult**](ValidateEmailAddressListResult)

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

