# mailslurp_client.SentEmailsControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_sent_tracking_pixels**](SentEmailsControllerApi#get_all_sent_tracking_pixels) | **GET** /sent/tracking-pixels | Get all sent email tracking pixels in paginated form
[**get_sent_email**](SentEmailsControllerApi#get_sent_email) | **GET** /sent/{id} | Get sent email receipt
[**get_sent_email_tracking_pixels**](SentEmailsControllerApi#get_sent_email_tracking_pixels) | **GET** /sent/{id}/tracking-pixels | Get all tracking pixels for a sent email in paginated form
[**get_sent_emails**](SentEmailsControllerApi#get_sent_emails) | **GET** /sent | Get all sent emails in paginated form
[**get_sent_organization_emails**](SentEmailsControllerApi#get_sent_organization_emails) | **GET** /sent/organization | Get all sent organization emails in paginated form


# **get_all_sent_tracking_pixels**
> PageTrackingPixelProjection get_all_sent_tracking_pixels(page=page, search_filter=search_filter, size=size, sort=sort)

Get all sent email tracking pixels in paginated form

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
    api_instance = mailslurp_client.SentEmailsControllerApi(api_client)
    page = 0 # int | Optional page index in sent email tracking pixel list pagination (optional) (default to 0)
search_filter = 'search_filter_example' # str | Optional search filter (optional)
size = 20 # int | Optional page size in sent email tracking pixel list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')

    try:
        # Get all sent email tracking pixels in paginated form
        api_response = api_instance.get_all_sent_tracking_pixels(page=page, search_filter=search_filter, size=size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SentEmailsControllerApi->get_all_sent_tracking_pixels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional page index in sent email tracking pixel list pagination | [optional] [default to 0]
 **search_filter** | **str**| Optional search filter | [optional] 
 **size** | **int**| Optional page size in sent email tracking pixel list pagination | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]

### Return type

[**PageTrackingPixelProjection**](PageTrackingPixelProjection)

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

# **get_sent_email**
> SentEmailDto get_sent_email(id)

Get sent email receipt

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
    api_instance = mailslurp_client.SentEmailsControllerApi(api_client)
    id = 'id_example' # str | id

    try:
        # Get sent email receipt
        api_response = api_instance.get_sent_email(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SentEmailsControllerApi->get_sent_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**]()| id | 

### Return type

[**SentEmailDto**](SentEmailDto)

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

# **get_sent_email_tracking_pixels**
> PageTrackingPixelProjection get_sent_email_tracking_pixels(id, page=page, search_filter=search_filter, size=size, sort=sort)

Get all tracking pixels for a sent email in paginated form

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
    api_instance = mailslurp_client.SentEmailsControllerApi(api_client)
    id = 'id_example' # str | id
page = 0 # int | Optional page index in sent email tracking pixel list pagination (optional) (default to 0)
search_filter = 'search_filter_example' # str | Optional search filter (optional)
size = 20 # int | Optional page size in sent email tracking pixel list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')

    try:
        # Get all tracking pixels for a sent email in paginated form
        api_response = api_instance.get_sent_email_tracking_pixels(id, page=page, search_filter=search_filter, size=size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SentEmailsControllerApi->get_sent_email_tracking_pixels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**]()| id | 
 **page** | **int**| Optional page index in sent email tracking pixel list pagination | [optional] [default to 0]
 **search_filter** | **str**| Optional search filter | [optional] 
 **size** | **int**| Optional page size in sent email tracking pixel list pagination | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]

### Return type

[**PageTrackingPixelProjection**](PageTrackingPixelProjection)

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

# **get_sent_emails**
> PageSentEmailProjection get_sent_emails(inbox_id=inbox_id, page=page, search_filter=search_filter, size=size, sort=sort)

Get all sent emails in paginated form

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
    api_instance = mailslurp_client.SentEmailsControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | Optional inboxId to filter sender of sent emails by (optional)
page = 0 # int | Optional page index in inbox sent email list pagination (optional) (default to 0)
search_filter = 'search_filter_example' # str | Optional search filter (optional)
size = 20 # int | Optional page size in inbox sent email list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')

    try:
        # Get all sent emails in paginated form
        api_response = api_instance.get_sent_emails(inbox_id=inbox_id, page=page, search_filter=search_filter, size=size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SentEmailsControllerApi->get_sent_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| Optional inboxId to filter sender of sent emails by | [optional] 
 **page** | **int**| Optional page index in inbox sent email list pagination | [optional] [default to 0]
 **search_filter** | **str**| Optional search filter | [optional] 
 **size** | **int**| Optional page size in inbox sent email list pagination | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]

### Return type

[**PageSentEmailProjection**](PageSentEmailProjection)

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

# **get_sent_organization_emails**
> PageSentEmailProjection get_sent_organization_emails(inbox_id=inbox_id, page=page, search_filter=search_filter, size=size, sort=sort)

Get all sent organization emails in paginated form

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
    api_instance = mailslurp_client.SentEmailsControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | Optional inboxId to filter sender of sent emails by (optional)
page = 0 # int | Optional page index in sent email list pagination (optional) (default to 0)
search_filter = 'search_filter_example' # str | Optional search filter (optional)
size = 20 # int | Optional page size in sent email list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')

    try:
        # Get all sent organization emails in paginated form
        api_response = api_instance.get_sent_organization_emails(inbox_id=inbox_id, page=page, search_filter=search_filter, size=size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SentEmailsControllerApi->get_sent_organization_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| Optional inboxId to filter sender of sent emails by | [optional] 
 **page** | **int**| Optional page index in sent email list pagination | [optional] [default to 0]
 **search_filter** | **str**| Optional search filter | [optional] 
 **size** | **int**| Optional page size in sent email list pagination | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]

### Return type

[**PageSentEmailProjection**](PageSentEmailProjection)

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

