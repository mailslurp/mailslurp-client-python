# mailslurp_client.SmsControllerApi

All URIs are relative to *https://python.api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sms_message**](SmsControllerApi#delete_sms_message) | **DELETE** /sms/{smsId} | Delete SMS message.
[**delete_sms_messages**](SmsControllerApi#delete_sms_messages) | **DELETE** /sms | Delete all SMS messages
[**get_sms_message**](SmsControllerApi#get_sms_message) | **GET** /sms/{smsId} | Get SMS content including body. Expects SMS to exist by ID. For SMS that may not have arrived yet use the WaitForController.
[**get_sms_messages_paginated**](SmsControllerApi#get_sms_messages_paginated) | **GET** /sms | Get all SMS messages in all phone numbers in paginated form. .


# **delete_sms_message**
> delete_sms_message(sms_id)

Delete SMS message.

Delete an SMS message

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
    api_instance = mailslurp_client.SmsControllerApi(api_client)
    sms_id = 'sms_id_example' # str | 

    try:
        # Delete SMS message.
        api_instance.delete_sms_message(sms_id)
    except ApiException as e:
        print("Exception when calling SmsControllerApi->delete_sms_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_id** | [**str**]()|  | 

### Return type

void (empty response body)

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

# **delete_sms_messages**
> delete_sms_messages(phone_number_id=phone_number_id)

Delete all SMS messages

Delete all SMS messages or all messages for a given phone number

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
    api_instance = mailslurp_client.SmsControllerApi(api_client)
    phone_number_id = 'phone_number_id_example' # str |  (optional)

    try:
        # Delete all SMS messages
        api_instance.delete_sms_messages(phone_number_id=phone_number_id)
    except ApiException as e:
        print("Exception when calling SmsControllerApi->delete_sms_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | [**str**]()|  | [optional] 

### Return type

void (empty response body)

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

# **get_sms_message**
> SmsMessage get_sms_message(sms_id)

Get SMS content including body. Expects SMS to exist by ID. For SMS that may not have arrived yet use the WaitForController.

Returns a SMS summary object with content.

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
    api_instance = mailslurp_client.SmsControllerApi(api_client)
    sms_id = 'sms_id_example' # str | 

    try:
        # Get SMS content including body. Expects SMS to exist by ID. For SMS that may not have arrived yet use the WaitForController.
        api_response = api_instance.get_sms_message(sms_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmsControllerApi->get_sms_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_id** | [**str**]()|  | 

### Return type

[**SmsMessage**](SmsMessage)

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

# **get_sms_messages_paginated**
> PageSmsProjection get_sms_messages_paginated(phone_number=phone_number, page=page, size=size, sort=sort, unread_only=unread_only, since=since, before=before)

Get all SMS messages in all phone numbers in paginated form. .

By default returns all SMS messages across all phone numbers sorted by ascending created at date. Responses are paginated. You can restrict results to a list of phone number IDs. You can also filter out read messages

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
    api_instance = mailslurp_client.SmsControllerApi(api_client)
    phone_number = 'phone_number_example' # str | Optional receiving phone number to filter SMS messages for (optional)
page = 0 # int | Optional page index in SMS list pagination (optional) (default to 0)
size = 20 # int | Optional page size in SMS list pagination. Maximum size is 100. Use page index and sort to page through larger results (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')
unread_only = False # bool | Optional filter for unread SMS only. All SMS are considered unread until they are viewed in the dashboard or requested directly (optional) (default to False)
since = '2013-10-20T19:20:30+01:00' # datetime | Optional filter SMSs received after given date time (optional)
before = '2013-10-20T19:20:30+01:00' # datetime | Optional filter SMSs received before given date time (optional)

    try:
        # Get all SMS messages in all phone numbers in paginated form. .
        api_response = api_instance.get_sms_messages_paginated(phone_number=phone_number, page=page, size=size, sort=sort, unread_only=unread_only, since=since, before=before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmsControllerApi->get_sms_messages_paginated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | [**str**]()| Optional receiving phone number to filter SMS messages for | [optional] 
 **page** | **int**| Optional page index in SMS list pagination | [optional] [default to 0]
 **size** | **int**| Optional page size in SMS list pagination. Maximum size is 100. Use page index and sort to page through larger results | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]
 **unread_only** | **bool**| Optional filter for unread SMS only. All SMS are considered unread until they are viewed in the dashboard or requested directly | [optional] [default to False]
 **since** | **datetime**| Optional filter SMSs received after given date time | [optional] 
 **before** | **datetime**| Optional filter SMSs received before given date time | [optional] 

### Return type

[**PageSmsProjection**](PageSmsProjection)

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

