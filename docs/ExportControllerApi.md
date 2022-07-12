# mailslurp_client.ExportControllerApi

All URIs are relative to *https://python.api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_entities**](ExportControllerApi#export_entities) | **GET** /export | Export inboxes link callable via browser
[**get_export_link**](ExportControllerApi#get_export_link) | **POST** /export | Get export link


# **export_entities**
> list[str] export_entities(export_type, api_key, output_format, filter=filter, list_separator_token=list_separator_token, exclude_previously_exported=exclude_previously_exported, created_earliest_time=created_earliest_time, created_oldest_time=created_oldest_time)

Export inboxes link callable via browser

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
    api_instance = mailslurp_client.ExportControllerApi(api_client)
    export_type = 'export_type_example' # str | 
api_key = 'api_key_example' # str | 
output_format = 'output_format_example' # str | 
filter = 'filter_example' # str |  (optional)
list_separator_token = 'list_separator_token_example' # str |  (optional)
exclude_previously_exported = True # bool |  (optional)
created_earliest_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
created_oldest_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Export inboxes link callable via browser
        api_response = api_instance.export_entities(export_type, api_key, output_format, filter=filter, list_separator_token=list_separator_token, exclude_previously_exported=exclude_previously_exported, created_earliest_time=created_earliest_time, created_oldest_time=created_oldest_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExportControllerApi->export_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_type** | **str**|  | 
 **api_key** | **str**|  | 
 **output_format** | **str**|  | 
 **filter** | **str**|  | [optional] 
 **list_separator_token** | **str**|  | [optional] 
 **exclude_previously_exported** | **bool**|  | [optional] 
 **created_earliest_time** | **datetime**|  | [optional] 
 **created_oldest_time** | **datetime**|  | [optional] 

### Return type

**list[str]**

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

# **get_export_link**
> ExportLink get_export_link(export_type, export_options, api_key=api_key)

Get export link

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
    api_instance = mailslurp_client.ExportControllerApi(api_client)
    export_type = 'export_type_example' # str | 
export_options = mailslurp_client.ExportOptions() # ExportOptions | 
api_key = 'api_key_example' # str |  (optional)

    try:
        # Get export link
        api_response = api_instance.get_export_link(export_type, export_options, api_key=api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExportControllerApi->get_export_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_type** | **str**|  | 
 **export_options** | [**ExportOptions**](ExportOptions)|  | 
 **api_key** | **str**|  | [optional] 

### Return type

[**ExportLink**](ExportLink)

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

