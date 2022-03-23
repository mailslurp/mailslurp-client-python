# mailslurp_client.InboxRulesetControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_inbox_ruleset**](InboxRulesetControllerApi#create_new_inbox_ruleset) | **POST** /rulesets | Create an inbox ruleset
[**delete_inbox_ruleset**](InboxRulesetControllerApi#delete_inbox_ruleset) | **DELETE** /rulesets/{id} | Delete an inbox ruleset
[**delete_inbox_rulesets**](InboxRulesetControllerApi#delete_inbox_rulesets) | **DELETE** /rulesets | Delete inbox rulesets
[**get_inbox_ruleset**](InboxRulesetControllerApi#get_inbox_ruleset) | **GET** /rulesets/{id} | Get an inbox ruleset
[**get_inbox_rulesets**](InboxRulesetControllerApi#get_inbox_rulesets) | **GET** /rulesets | List inbox rulesets
[**test_inbox_ruleset**](InboxRulesetControllerApi#test_inbox_ruleset) | **POST** /rulesets/{id}/test | Test an inbox ruleset
[**test_inbox_rulesets_for_inbox**](InboxRulesetControllerApi#test_inbox_rulesets_for_inbox) | **PUT** /rulesets | Test inbox rulesets for inbox
[**test_new_inbox_ruleset**](InboxRulesetControllerApi#test_new_inbox_ruleset) | **PATCH** /rulesets | Test new inbox ruleset


# **create_new_inbox_ruleset**
> InboxRulesetDto create_new_inbox_ruleset(inbox_id, create_inbox_ruleset_options)

Create an inbox ruleset

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
    api_instance = mailslurp_client.InboxRulesetControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | Inbox id to attach ruleset to
create_inbox_ruleset_options = mailslurp_client.CreateInboxRulesetOptions() # CreateInboxRulesetOptions | 

    try:
        # Create an inbox ruleset
        api_response = api_instance.create_new_inbox_ruleset(inbox_id, create_inbox_ruleset_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxRulesetControllerApi->create_new_inbox_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| Inbox id to attach ruleset to | 
 **create_inbox_ruleset_options** | [**CreateInboxRulesetOptions**](CreateInboxRulesetOptions)|  | 

### Return type

[**InboxRulesetDto**](InboxRulesetDto)

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

# **delete_inbox_ruleset**
> delete_inbox_ruleset(id)

Delete an inbox ruleset

Delete inbox ruleset

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
    api_instance = mailslurp_client.InboxRulesetControllerApi(api_client)
    id = 'id_example' # str | ID of inbox ruleset

    try:
        # Delete an inbox ruleset
        api_instance.delete_inbox_ruleset(id)
    except ApiException as e:
        print("Exception when calling InboxRulesetControllerApi->delete_inbox_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**]()| ID of inbox ruleset | 

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

# **delete_inbox_rulesets**
> delete_inbox_rulesets(inbox_id=inbox_id)

Delete inbox rulesets

Delete inbox rulesets. Accepts optional inboxId filter.

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
    api_instance = mailslurp_client.InboxRulesetControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | Optional inbox id to attach ruleset to (optional)

    try:
        # Delete inbox rulesets
        api_instance.delete_inbox_rulesets(inbox_id=inbox_id)
    except ApiException as e:
        print("Exception when calling InboxRulesetControllerApi->delete_inbox_rulesets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| Optional inbox id to attach ruleset to | [optional] 

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

# **get_inbox_ruleset**
> InboxRulesetDto get_inbox_ruleset(id)

Get an inbox ruleset

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
    api_instance = mailslurp_client.InboxRulesetControllerApi(api_client)
    id = 'id_example' # str | ID of inbox ruleset

    try:
        # Get an inbox ruleset
        api_response = api_instance.get_inbox_ruleset(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxRulesetControllerApi->get_inbox_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**]()| ID of inbox ruleset | 

### Return type

[**InboxRulesetDto**](InboxRulesetDto)

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

# **get_inbox_rulesets**
> PageInboxRulesetDto get_inbox_rulesets(inbox_id=inbox_id, page=page, size=size, sort=sort, search_filter=search_filter, since=since, before=before)

List inbox rulesets

List all rulesets attached to an inbox

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
    api_instance = mailslurp_client.InboxRulesetControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | Optional inbox id to get rulesets from (optional)
page = 0 # int | Optional page index in inbox ruleset list pagination (optional) (default to 0)
size = 20 # int | Optional page size in inbox ruleset list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')
search_filter = 'search_filter_example' # str | Optional search filter (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at after the given timestamp (optional)
before = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at before the given timestamp (optional)

    try:
        # List inbox rulesets
        api_response = api_instance.get_inbox_rulesets(inbox_id=inbox_id, page=page, size=size, sort=sort, search_filter=search_filter, since=since, before=before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxRulesetControllerApi->get_inbox_rulesets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| Optional inbox id to get rulesets from | [optional] 
 **page** | **int**| Optional page index in inbox ruleset list pagination | [optional] [default to 0]
 **size** | **int**| Optional page size in inbox ruleset list pagination | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]
 **search_filter** | **str**| Optional search filter | [optional] 
 **since** | **datetime**| Filter by created at after the given timestamp | [optional] 
 **before** | **datetime**| Filter by created at before the given timestamp | [optional] 

### Return type

[**PageInboxRulesetDto**](PageInboxRulesetDto)

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

# **test_inbox_ruleset**
> InboxRulesetTestResult test_inbox_ruleset(id, inbox_ruleset_test_options)

Test an inbox ruleset

Test an inbox ruleset

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
    api_instance = mailslurp_client.InboxRulesetControllerApi(api_client)
    id = 'id_example' # str | ID of inbox ruleset
inbox_ruleset_test_options = mailslurp_client.InboxRulesetTestOptions() # InboxRulesetTestOptions | 

    try:
        # Test an inbox ruleset
        api_response = api_instance.test_inbox_ruleset(id, inbox_ruleset_test_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxRulesetControllerApi->test_inbox_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**]()| ID of inbox ruleset | 
 **inbox_ruleset_test_options** | [**InboxRulesetTestOptions**](InboxRulesetTestOptions)|  | 

### Return type

[**InboxRulesetTestResult**](InboxRulesetTestResult)

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

# **test_inbox_rulesets_for_inbox**
> InboxRulesetTestResult test_inbox_rulesets_for_inbox(inbox_id, inbox_ruleset_test_options)

Test inbox rulesets for inbox

Test inbox rulesets for inbox

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
    api_instance = mailslurp_client.InboxRulesetControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | ID of inbox
inbox_ruleset_test_options = mailslurp_client.InboxRulesetTestOptions() # InboxRulesetTestOptions | 

    try:
        # Test inbox rulesets for inbox
        api_response = api_instance.test_inbox_rulesets_for_inbox(inbox_id, inbox_ruleset_test_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxRulesetControllerApi->test_inbox_rulesets_for_inbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| ID of inbox | 
 **inbox_ruleset_test_options** | [**InboxRulesetTestOptions**](InboxRulesetTestOptions)|  | 

### Return type

[**InboxRulesetTestResult**](InboxRulesetTestResult)

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

# **test_new_inbox_ruleset**
> InboxRulesetTestResult test_new_inbox_ruleset(test_new_inbox_ruleset_options)

Test new inbox ruleset

Test new inbox ruleset

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
    api_instance = mailslurp_client.InboxRulesetControllerApi(api_client)
    test_new_inbox_ruleset_options = mailslurp_client.TestNewInboxRulesetOptions() # TestNewInboxRulesetOptions | 

    try:
        # Test new inbox ruleset
        api_response = api_instance.test_new_inbox_ruleset(test_new_inbox_ruleset_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxRulesetControllerApi->test_new_inbox_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_new_inbox_ruleset_options** | [**TestNewInboxRulesetOptions**](TestNewInboxRulesetOptions)|  | 

### Return type

[**InboxRulesetTestResult**](InboxRulesetTestResult)

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

