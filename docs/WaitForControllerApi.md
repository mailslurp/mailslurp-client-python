# mailslurp_client.WaitForControllerApi

All URIs are relative to *https://python.api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wait_for**](WaitForControllerApi#wait_for) | **POST** /waitFor | Wait for an email to match the provided filter conditions such as subject contains keyword.
[**wait_for_email_count**](WaitForControllerApi#wait_for_email_count) | **GET** /waitForEmailCount | Wait for and return count number of emails. Hold connection until inbox count matches expected or timeout occurs
[**wait_for_latest_email**](WaitForControllerApi#wait_for_latest_email) | **GET** /waitForLatestEmail | Fetch inbox&#39;s latest email or if empty wait for an email to arrive
[**wait_for_matching_emails**](WaitForControllerApi#wait_for_matching_emails) | **POST** /waitForMatchingEmails | Wait or return list of emails that match simple matching patterns
[**wait_for_matching_first_email**](WaitForControllerApi#wait_for_matching_first_email) | **POST** /waitForMatchingFirstEmail | Wait for or return the first email that matches provided MatchOptions array
[**wait_for_nth_email**](WaitForControllerApi#wait_for_nth_email) | **GET** /waitForNthEmail | Wait for or fetch the email with a given index in the inbox specified. If index doesn&#39;t exist waits for it to exist or timeout to occur.
[**wait_for_sms**](WaitForControllerApi#wait_for_sms) | **POST** /waitForSms | Wait for an SMS message to match the provided filter conditions such as body contains keyword.


# **wait_for**
> list[EmailPreview] wait_for(wait_for_conditions)

Wait for an email to match the provided filter conditions such as subject contains keyword.

Generic waitFor method that will wait until an inbox meets given conditions or return immediately if already met

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
    api_instance = mailslurp_client.WaitForControllerApi(api_client)
    wait_for_conditions = mailslurp_client.WaitForConditions() # WaitForConditions | 

    try:
        # Wait for an email to match the provided filter conditions such as subject contains keyword.
        api_response = api_instance.wait_for(wait_for_conditions)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WaitForControllerApi->wait_for: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wait_for_conditions** | [**WaitForConditions**](WaitForConditions)|  | 

### Return type

[**list[EmailPreview]**](EmailPreview)

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

# **wait_for_email_count**
> list[EmailPreview] wait_for_email_count(inbox_id, count, timeout=timeout, unread_only=unread_only, before=before, since=since, sort=sort, delay=delay)

Wait for and return count number of emails. Hold connection until inbox count matches expected or timeout occurs

If inbox contains count or more emails at time of request then return count worth of emails. If not wait until the count is reached and return those or return an error if timeout is exceeded.

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
    api_instance = mailslurp_client.WaitForControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | Id of the inbox we are fetching emails from
count = 56 # int | Number of emails to wait for. Must be greater that 1
timeout = 56 # int | Max milliseconds to wait (optional)
unread_only = False # bool | Optional filter for unread only (optional) (default to False)
before = '2013-10-20T19:20:30+01:00' # datetime | Filter for emails that were received before the given timestamp (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter for emails that were received after the given timestamp (optional)
sort = 'sort_example' # str | Sort direction (optional)
delay = 56 # int | Max milliseconds delay between calls (optional)

    try:
        # Wait for and return count number of emails. Hold connection until inbox count matches expected or timeout occurs
        api_response = api_instance.wait_for_email_count(inbox_id, count, timeout=timeout, unread_only=unread_only, before=before, since=since, sort=sort, delay=delay)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WaitForControllerApi->wait_for_email_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| Id of the inbox we are fetching emails from | 
 **count** | **int**| Number of emails to wait for. Must be greater that 1 | 
 **timeout** | **int**| Max milliseconds to wait | [optional] 
 **unread_only** | **bool**| Optional filter for unread only | [optional] [default to False]
 **before** | **datetime**| Filter for emails that were received before the given timestamp | [optional] 
 **since** | **datetime**| Filter for emails that were received after the given timestamp | [optional] 
 **sort** | **str**| Sort direction | [optional] 
 **delay** | **int**| Max milliseconds delay between calls | [optional] 

### Return type

[**list[EmailPreview]**](EmailPreview)

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

# **wait_for_latest_email**
> Email wait_for_latest_email(inbox_id=inbox_id, timeout=timeout, unread_only=unread_only, before=before, since=since, sort=sort, delay=delay)

Fetch inbox's latest email or if empty wait for an email to arrive

Will return either the last received email or wait for an email to arrive and return that. If you need to wait for an email for a non-empty inbox set `unreadOnly=true` or see the other receive methods such as `waitForNthEmail` or `waitForEmailCount`.

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
    api_instance = mailslurp_client.WaitForControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | Id of the inbox we are fetching emails from (optional)
timeout = 56 # int | Max milliseconds to wait (optional)
unread_only = False # bool | Optional filter for unread only. (optional) (default to False)
before = '2013-10-20T19:20:30+01:00' # datetime | Filter for emails that were before after the given timestamp (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter for emails that were received after the given timestamp (optional)
sort = 'sort_example' # str | Sort direction (optional)
delay = 56 # int | Max milliseconds delay between calls (optional)

    try:
        # Fetch inbox's latest email or if empty wait for an email to arrive
        api_response = api_instance.wait_for_latest_email(inbox_id=inbox_id, timeout=timeout, unread_only=unread_only, before=before, since=since, sort=sort, delay=delay)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WaitForControllerApi->wait_for_latest_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| Id of the inbox we are fetching emails from | [optional] 
 **timeout** | **int**| Max milliseconds to wait | [optional] 
 **unread_only** | **bool**| Optional filter for unread only. | [optional] [default to False]
 **before** | **datetime**| Filter for emails that were before after the given timestamp | [optional] 
 **since** | **datetime**| Filter for emails that were received after the given timestamp | [optional] 
 **sort** | **str**| Sort direction | [optional] 
 **delay** | **int**| Max milliseconds delay between calls | [optional] 

### Return type

[**Email**](Email)

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

# **wait_for_matching_emails**
> list[EmailPreview] wait_for_matching_emails(inbox_id, count, match_options, before=before, since=since, sort=sort, delay=delay, timeout=timeout, unread_only=unread_only)

Wait or return list of emails that match simple matching patterns

Perform a search of emails in an inbox with the given patterns. If results match expected count then return or else retry the search until results are found or timeout is reached. Match options allow simple CONTAINS or EQUALS filtering on SUBJECT, TO, BCC, CC, and FROM. See the `MatchOptions` object for options. An example payload is `{ matches: [{field: 'SUBJECT',should:'CONTAIN',value:'needle'}] }`. You can use an array of matches and they will be applied sequentially to filter out emails. If you want to perform matches and extractions of content using Regex patterns see the EmailController `getEmailContentMatch` method.

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
    api_instance = mailslurp_client.WaitForControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | Id of the inbox we are fetching emails from
count = 56 # int | Number of emails to wait for. Must be greater or equal to 1
match_options = mailslurp_client.MatchOptions() # MatchOptions | 
before = '2013-10-20T19:20:30+01:00' # datetime | Filter for emails that were received before the given timestamp (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter for emails that were received after the given timestamp (optional)
sort = 'sort_example' # str | Sort direction (optional)
delay = 56 # int | Max milliseconds delay between calls (optional)
timeout = 56 # int | Max milliseconds to wait (optional)
unread_only = False # bool | Optional filter for unread only (optional) (default to False)

    try:
        # Wait or return list of emails that match simple matching patterns
        api_response = api_instance.wait_for_matching_emails(inbox_id, count, match_options, before=before, since=since, sort=sort, delay=delay, timeout=timeout, unread_only=unread_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WaitForControllerApi->wait_for_matching_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| Id of the inbox we are fetching emails from | 
 **count** | **int**| Number of emails to wait for. Must be greater or equal to 1 | 
 **match_options** | [**MatchOptions**](MatchOptions)|  | 
 **before** | **datetime**| Filter for emails that were received before the given timestamp | [optional] 
 **since** | **datetime**| Filter for emails that were received after the given timestamp | [optional] 
 **sort** | **str**| Sort direction | [optional] 
 **delay** | **int**| Max milliseconds delay between calls | [optional] 
 **timeout** | **int**| Max milliseconds to wait | [optional] 
 **unread_only** | **bool**| Optional filter for unread only | [optional] [default to False]

### Return type

[**list[EmailPreview]**](EmailPreview)

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

# **wait_for_matching_first_email**
> Email wait_for_matching_first_email(inbox_id, match_options, timeout=timeout, unread_only=unread_only, since=since, before=before, sort=sort, delay=delay)

Wait for or return the first email that matches provided MatchOptions array

Perform a search of emails in an inbox with the given patterns. If a result if found then return or else retry the search until a result is found or timeout is reached. Match options allow simple CONTAINS or EQUALS filtering on SUBJECT, TO, BCC, CC, and FROM. See the `MatchOptions` object for options. An example payload is `{ matches: [{field: 'SUBJECT',should:'CONTAIN',value:'needle'}] }`. You can use an array of matches and they will be applied sequentially to filter out emails. If you want to perform matches and extractions of content using Regex patterns see the EmailController `getEmailContentMatch` method.

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
    api_instance = mailslurp_client.WaitForControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | Id of the inbox we are matching an email for
match_options = mailslurp_client.MatchOptions() # MatchOptions | 
timeout = 56 # int | Max milliseconds to wait (optional)
unread_only = False # bool | Optional filter for unread only (optional) (default to False)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter for emails that were received after the given timestamp (optional)
before = '2013-10-20T19:20:30+01:00' # datetime | Filter for emails that were received before the given timestamp (optional)
sort = 'sort_example' # str | Sort direction (optional)
delay = 56 # int | Max milliseconds delay between calls (optional)

    try:
        # Wait for or return the first email that matches provided MatchOptions array
        api_response = api_instance.wait_for_matching_first_email(inbox_id, match_options, timeout=timeout, unread_only=unread_only, since=since, before=before, sort=sort, delay=delay)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WaitForControllerApi->wait_for_matching_first_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| Id of the inbox we are matching an email for | 
 **match_options** | [**MatchOptions**](MatchOptions)|  | 
 **timeout** | **int**| Max milliseconds to wait | [optional] 
 **unread_only** | **bool**| Optional filter for unread only | [optional] [default to False]
 **since** | **datetime**| Filter for emails that were received after the given timestamp | [optional] 
 **before** | **datetime**| Filter for emails that were received before the given timestamp | [optional] 
 **sort** | **str**| Sort direction | [optional] 
 **delay** | **int**| Max milliseconds delay between calls | [optional] 

### Return type

[**Email**](Email)

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

# **wait_for_nth_email**
> Email wait_for_nth_email(inbox_id=inbox_id, index=index, timeout=timeout, unread_only=unread_only, since=since, before=before, sort=sort, delay=delay)

Wait for or fetch the email with a given index in the inbox specified. If index doesn't exist waits for it to exist or timeout to occur.

If nth email is already present in inbox then return it. If not hold the connection open until timeout expires or the nth email is received and returned.

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
    api_instance = mailslurp_client.WaitForControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | Id of the inbox you are fetching emails from (optional)
index = 0 # int | Zero based index of the email to wait for. If an inbox has 1 email already and you want to wait for the 2nd email pass index=1 (optional) (default to 0)
timeout = 56 # int | Max milliseconds to wait for the nth email if not already present (optional)
unread_only = False # bool | Optional filter for unread only (optional) (default to False)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter for emails that were received after the given timestamp (optional)
before = '2013-10-20T19:20:30+01:00' # datetime | Filter for emails that were received before the given timestamp (optional)
sort = 'sort_example' # str | Sort direction (optional)
delay = 56 # int | Max milliseconds delay between calls (optional)

    try:
        # Wait for or fetch the email with a given index in the inbox specified. If index doesn't exist waits for it to exist or timeout to occur.
        api_response = api_instance.wait_for_nth_email(inbox_id=inbox_id, index=index, timeout=timeout, unread_only=unread_only, since=since, before=before, sort=sort, delay=delay)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WaitForControllerApi->wait_for_nth_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| Id of the inbox you are fetching emails from | [optional] 
 **index** | **int**| Zero based index of the email to wait for. If an inbox has 1 email already and you want to wait for the 2nd email pass index&#x3D;1 | [optional] [default to 0]
 **timeout** | **int**| Max milliseconds to wait for the nth email if not already present | [optional] 
 **unread_only** | **bool**| Optional filter for unread only | [optional] [default to False]
 **since** | **datetime**| Filter for emails that were received after the given timestamp | [optional] 
 **before** | **datetime**| Filter for emails that were received before the given timestamp | [optional] 
 **sort** | **str**| Sort direction | [optional] 
 **delay** | **int**| Max milliseconds delay between calls | [optional] 

### Return type

[**Email**](Email)

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

# **wait_for_sms**
> list[SmsPreview] wait_for_sms(wait_for_sms_conditions)

Wait for an SMS message to match the provided filter conditions such as body contains keyword.

Generic waitFor method that will wait until a phone number meets given conditions or return immediately if already met

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
    api_instance = mailslurp_client.WaitForControllerApi(api_client)
    wait_for_sms_conditions = mailslurp_client.WaitForSmsConditions() # WaitForSmsConditions | 

    try:
        # Wait for an SMS message to match the provided filter conditions such as body contains keyword.
        api_response = api_instance.wait_for_sms(wait_for_sms_conditions)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WaitForControllerApi->wait_for_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wait_for_sms_conditions** | [**WaitForSmsConditions**](WaitForSmsConditions)|  | 

### Return type

[**list[SmsPreview]**](SmsPreview)

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

