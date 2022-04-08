# mailslurp_client.MissedEmailControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_missed_emails**](MissedEmailControllerApi#get_all_missed_emails) | **GET** /missed-emails | Get all MissedEmails in paginated format
[**get_all_unknown_missed_emails**](MissedEmailControllerApi#get_all_unknown_missed_emails) | **GET** /missed-emails/unknown | Get all unknown missed emails in paginated format
[**get_missed_email**](MissedEmailControllerApi#get_missed_email) | **GET** /missed-emails/{missedEmailId} | Get MissedEmail
[**wait_for_nth_missed_email**](MissedEmailControllerApi#wait_for_nth_missed_email) | **GET** /missed-emails/waitForNthMissedEmail | Wait for Nth missed email


# **get_all_missed_emails**
> PageMissedEmailProjection get_all_missed_emails(page=page, size=size, sort=sort, search_filter=search_filter, since=since, before=before, inbox_id=inbox_id)

Get all MissedEmails in paginated format

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
    api_instance = mailslurp_client.MissedEmailControllerApi(api_client)
    page = 0 # int | Optional page index in list pagination (optional) (default to 0)
size = 20 # int | Optional page size in list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')
search_filter = 'search_filter_example' # str | Optional search filter (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at after the given timestamp (optional)
before = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at before the given timestamp (optional)
inbox_id = 'inbox_id_example' # str | Optional inbox ID filter (optional)

    try:
        # Get all MissedEmails in paginated format
        api_response = api_instance.get_all_missed_emails(page=page, size=size, sort=sort, search_filter=search_filter, since=since, before=before, inbox_id=inbox_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MissedEmailControllerApi->get_all_missed_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional page index in list pagination | [optional] [default to 0]
 **size** | **int**| Optional page size in list pagination | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]
 **search_filter** | **str**| Optional search filter | [optional] 
 **since** | **datetime**| Filter by created at after the given timestamp | [optional] 
 **before** | **datetime**| Filter by created at before the given timestamp | [optional] 
 **inbox_id** | [**str**]()| Optional inbox ID filter | [optional] 

### Return type

[**PageMissedEmailProjection**](PageMissedEmailProjection)

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

# **get_all_unknown_missed_emails**
> PageUnknownMissedEmailProjection get_all_unknown_missed_emails(page=page, size=size, sort=sort, search_filter=search_filter, since=since, before=before, inbox_id=inbox_id)

Get all unknown missed emails in paginated format

Unknown missed emails are emails that were sent to MailSlurp but could not be assigned to an existing inbox.

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
    api_instance = mailslurp_client.MissedEmailControllerApi(api_client)
    page = 0 # int | Optional page index in list pagination (optional) (default to 0)
size = 20 # int | Optional page size in list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')
search_filter = 'search_filter_example' # str | Optional search filter (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at after the given timestamp (optional)
before = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at before the given timestamp (optional)
inbox_id = 'inbox_id_example' # str | Optional inbox ID filter (optional)

    try:
        # Get all unknown missed emails in paginated format
        api_response = api_instance.get_all_unknown_missed_emails(page=page, size=size, sort=sort, search_filter=search_filter, since=since, before=before, inbox_id=inbox_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MissedEmailControllerApi->get_all_unknown_missed_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional page index in list pagination | [optional] [default to 0]
 **size** | **int**| Optional page size in list pagination | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]
 **search_filter** | **str**| Optional search filter | [optional] 
 **since** | **datetime**| Filter by created at after the given timestamp | [optional] 
 **before** | **datetime**| Filter by created at before the given timestamp | [optional] 
 **inbox_id** | [**str**]()| Optional inbox ID filter | [optional] 

### Return type

[**PageUnknownMissedEmailProjection**](PageUnknownMissedEmailProjection)

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

# **get_missed_email**
> MissedEmail get_missed_email(missed_email_id)

Get MissedEmail

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
    api_instance = mailslurp_client.MissedEmailControllerApi(api_client)
    missed_email_id = 'missed_email_id_example' # str | 

    try:
        # Get MissedEmail
        api_response = api_instance.get_missed_email(missed_email_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MissedEmailControllerApi->get_missed_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **missed_email_id** | [**str**]()|  | 

### Return type

[**MissedEmail**](MissedEmail)

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

# **wait_for_nth_missed_email**
> MissedEmail wait_for_nth_missed_email(index, inbox_id=inbox_id, timeout=timeout, since=since, before=before)

Wait for Nth missed email

Wait for 0 based index missed email

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
    api_instance = mailslurp_client.MissedEmailControllerApi(api_client)
    index = 56 # int | Zero based index of the email to wait for. If 1 missed email already and you want to wait for the 2nd email pass index=1
inbox_id = 'inbox_id_example' # str | Optional inbox ID filter (optional)
timeout = 56 # int | Optional timeout milliseconds (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at after the given timestamp (optional)
before = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at before the given timestamp (optional)

    try:
        # Wait for Nth missed email
        api_response = api_instance.wait_for_nth_missed_email(index, inbox_id=inbox_id, timeout=timeout, since=since, before=before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MissedEmailControllerApi->wait_for_nth_missed_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| Zero based index of the email to wait for. If 1 missed email already and you want to wait for the 2nd email pass index&#x3D;1 | 
 **inbox_id** | [**str**]()| Optional inbox ID filter | [optional] 
 **timeout** | **int**| Optional timeout milliseconds | [optional] 
 **since** | **datetime**| Filter by created at after the given timestamp | [optional] 
 **before** | **datetime**| Filter by created at before the given timestamp | [optional] 

### Return type

[**MissedEmail**](MissedEmail)

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

