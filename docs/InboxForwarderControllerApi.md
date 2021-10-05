# mailslurp_client.InboxForwarderControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_inbox_forwarder**](InboxForwarderControllerApi#create_new_inbox_forwarder) | **POST** /forwarders | Create an inbox forwarder
[**delete_inbox_forwarder**](InboxForwarderControllerApi#delete_inbox_forwarder) | **DELETE** /forwarders/{id} | Delete an inbox forwarder
[**delete_inbox_forwarders**](InboxForwarderControllerApi#delete_inbox_forwarders) | **DELETE** /forwarders | Delete inbox forwarders
[**get_inbox_forwarder**](InboxForwarderControllerApi#get_inbox_forwarder) | **GET** /forwarders/{id} | Get an inbox forwarder
[**get_inbox_forwarders**](InboxForwarderControllerApi#get_inbox_forwarders) | **GET** /forwarders | List inbox forwarders
[**test_inbox_forwarder**](InboxForwarderControllerApi#test_inbox_forwarder) | **POST** /forwarders/{id}/test | Test an inbox forwarder
[**test_inbox_forwarders_for_inbox**](InboxForwarderControllerApi#test_inbox_forwarders_for_inbox) | **PUT** /forwarders | Test inbox forwarders for inbox
[**test_new_inbox_forwarder**](InboxForwarderControllerApi#test_new_inbox_forwarder) | **PATCH** /forwarders | Test new inbox forwarder


# **create_new_inbox_forwarder**
> InboxForwarderDto create_new_inbox_forwarder(create_inbox_forwarder_options, inbox_id=inbox_id)

Create an inbox forwarder

Create a new inbox rule for forwarding, blocking, and allowing emails when sending and receiving

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
    api_instance = mailslurp_client.InboxForwarderControllerApi(api_client)
    create_inbox_forwarder_options = mailslurp_client.CreateInboxForwarderOptions() # CreateInboxForwarderOptions | createInboxForwarderOptions
inbox_id = 'inbox_id_example' # str | Inbox id to attach forwarder to (optional)

    try:
        # Create an inbox forwarder
        api_response = api_instance.create_new_inbox_forwarder(create_inbox_forwarder_options, inbox_id=inbox_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxForwarderControllerApi->create_new_inbox_forwarder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_inbox_forwarder_options** | [**CreateInboxForwarderOptions**](CreateInboxForwarderOptions)| createInboxForwarderOptions | 
 **inbox_id** | [**str**]()| Inbox id to attach forwarder to | [optional] 

### Return type

[**InboxForwarderDto**](InboxForwarderDto)

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

# **delete_inbox_forwarder**
> delete_inbox_forwarder(id)

Delete an inbox forwarder

Delete inbox forwarder

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
    api_instance = mailslurp_client.InboxForwarderControllerApi(api_client)
    id = 'id_example' # str | ID of inbox forwarder

    try:
        # Delete an inbox forwarder
        api_instance.delete_inbox_forwarder(id)
    except ApiException as e:
        print("Exception when calling InboxForwarderControllerApi->delete_inbox_forwarder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**]()| ID of inbox forwarder | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

# **delete_inbox_forwarders**
> delete_inbox_forwarders(inbox_id=inbox_id)

Delete inbox forwarders

Delete inbox forwarders. Accepts optional inboxId filter.

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
    api_instance = mailslurp_client.InboxForwarderControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | Optional inbox id to attach forwarder to (optional)

    try:
        # Delete inbox forwarders
        api_instance.delete_inbox_forwarders(inbox_id=inbox_id)
    except ApiException as e:
        print("Exception when calling InboxForwarderControllerApi->delete_inbox_forwarders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| Optional inbox id to attach forwarder to | [optional] 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

# **get_inbox_forwarder**
> InboxForwarderDto get_inbox_forwarder(id)

Get an inbox forwarder

Get inbox ruleset

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
    api_instance = mailslurp_client.InboxForwarderControllerApi(api_client)
    id = 'id_example' # str | ID of inbox forwarder

    try:
        # Get an inbox forwarder
        api_response = api_instance.get_inbox_forwarder(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxForwarderControllerApi->get_inbox_forwarder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**]()| ID of inbox forwarder | 

### Return type

[**InboxForwarderDto**](InboxForwarderDto)

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

# **get_inbox_forwarders**
> PageInboxForwarderDto get_inbox_forwarders(before=before, inbox_id=inbox_id, page=page, search_filter=search_filter, since=since, size=size, sort=sort)

List inbox forwarders

List all forwarders attached to an inbox

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
    api_instance = mailslurp_client.InboxForwarderControllerApi(api_client)
    before = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at before the given timestamp (optional)
inbox_id = 'inbox_id_example' # str | Optional inbox id to get forwarders from (optional)
page = 0 # int | Optional page index in inbox forwarder list pagination (optional) (default to 0)
search_filter = 'search_filter_example' # str | Optional search filter (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at after the given timestamp (optional)
size = 20 # int | Optional page size in inbox forwarder list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')

    try:
        # List inbox forwarders
        api_response = api_instance.get_inbox_forwarders(before=before, inbox_id=inbox_id, page=page, search_filter=search_filter, since=since, size=size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxForwarderControllerApi->get_inbox_forwarders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before** | **datetime**| Filter by created at before the given timestamp | [optional] 
 **inbox_id** | [**str**]()| Optional inbox id to get forwarders from | [optional] 
 **page** | **int**| Optional page index in inbox forwarder list pagination | [optional] [default to 0]
 **search_filter** | **str**| Optional search filter | [optional] 
 **since** | **datetime**| Filter by created at after the given timestamp | [optional] 
 **size** | **int**| Optional page size in inbox forwarder list pagination | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]

### Return type

[**PageInboxForwarderDto**](PageInboxForwarderDto)

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

# **test_inbox_forwarder**
> InboxForwarderTestResult test_inbox_forwarder(id, inbox_forwarder_test_options)

Test an inbox forwarder

Test an inbox forwarder

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
    api_instance = mailslurp_client.InboxForwarderControllerApi(api_client)
    id = 'id_example' # str | ID of inbox forwarder
inbox_forwarder_test_options = mailslurp_client.InboxForwarderTestOptions() # InboxForwarderTestOptions | inboxForwarderTestOptions

    try:
        # Test an inbox forwarder
        api_response = api_instance.test_inbox_forwarder(id, inbox_forwarder_test_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxForwarderControllerApi->test_inbox_forwarder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**]()| ID of inbox forwarder | 
 **inbox_forwarder_test_options** | [**InboxForwarderTestOptions**](InboxForwarderTestOptions)| inboxForwarderTestOptions | 

### Return type

[**InboxForwarderTestResult**](InboxForwarderTestResult)

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

# **test_inbox_forwarders_for_inbox**
> InboxForwarderTestResult test_inbox_forwarders_for_inbox(inbox_id, inbox_forwarder_test_options)

Test inbox forwarders for inbox

Test inbox forwarders for inbox

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
    api_instance = mailslurp_client.InboxForwarderControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | ID of inbox
inbox_forwarder_test_options = mailslurp_client.InboxForwarderTestOptions() # InboxForwarderTestOptions | inboxForwarderTestOptions

    try:
        # Test inbox forwarders for inbox
        api_response = api_instance.test_inbox_forwarders_for_inbox(inbox_id, inbox_forwarder_test_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxForwarderControllerApi->test_inbox_forwarders_for_inbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| ID of inbox | 
 **inbox_forwarder_test_options** | [**InboxForwarderTestOptions**](InboxForwarderTestOptions)| inboxForwarderTestOptions | 

### Return type

[**InboxForwarderTestResult**](InboxForwarderTestResult)

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

# **test_new_inbox_forwarder**
> InboxForwarderTestResult test_new_inbox_forwarder(test_new_inbox_forwarder_options)

Test new inbox forwarder

Test new inbox forwarder

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
    api_instance = mailslurp_client.InboxForwarderControllerApi(api_client)
    test_new_inbox_forwarder_options = mailslurp_client.TestNewInboxForwarderOptions() # TestNewInboxForwarderOptions | testNewInboxForwarderOptions

    try:
        # Test new inbox forwarder
        api_response = api_instance.test_new_inbox_forwarder(test_new_inbox_forwarder_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxForwarderControllerApi->test_new_inbox_forwarder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_new_inbox_forwarder_options** | [**TestNewInboxForwarderOptions**](TestNewInboxForwarderOptions)| testNewInboxForwarderOptions | 

### Return type

[**InboxForwarderTestResult**](InboxForwarderTestResult)

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

