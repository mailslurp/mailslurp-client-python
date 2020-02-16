# mailslurp_client.CommonActionsControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_email_address**](CommonActionsControllerApi.md#create_new_email_address) | **POST** /newEmailAddress | Create new random inbox
[**empty_inbox**](CommonActionsControllerApi.md#empty_inbox) | **DELETE** /emptyInbox | Delete all emails in an inbox
[**send_email_simple**](CommonActionsControllerApi.md#send_email_simple) | **POST** /sendEmail | Send an email from a random email address
[**wait_for_email_count**](CommonActionsControllerApi.md#wait_for_email_count) | **GET** /waitForEmailCount | Wait for and return count number of emails 
[**wait_for_latest_email**](CommonActionsControllerApi.md#wait_for_latest_email) | **GET** /waitForLatestEmail | Fetch inbox&#39;s latest email or if empty wait for email to arrive
[**wait_for_matching_email**](CommonActionsControllerApi.md#wait_for_matching_email) | **POST** /waitForMatchingEmails | Wait or return list of emails that match simple matching patterns
[**wait_for_nth_email**](CommonActionsControllerApi.md#wait_for_nth_email) | **GET** /waitForNthEmail | Wait for or fetch the email with a given index in the inbox specified


# **create_new_email_address**
> Inbox create_new_email_address()

Create new random inbox

Returns an Inbox with an `id` and an `emailAddress`

### Example

* Api Key Authentication (API_KEY):
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint
configuration = mailslurp_client.Configuration()
# Configure API key authorization: API_KEY
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Defining host is optional and default to https://api.mailslurp.com
configuration.host = "https://api.mailslurp.com"
# Enter a context with an instance of the API client
with mailslurp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailslurp_client.CommonActionsControllerApi(api_client)
    
    try:
        # Create new random inbox
        api_response = api_instance.create_new_email_address()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommonActionsControllerApi->create_new_email_address: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Inbox**](Inbox.md)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **empty_inbox**
> empty_inbox(inbox_id)

Delete all emails in an inbox

Deletes all emails

### Example

* Api Key Authentication (API_KEY):
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint
configuration = mailslurp_client.Configuration()
# Configure API key authorization: API_KEY
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Defining host is optional and default to https://api.mailslurp.com
configuration.host = "https://api.mailslurp.com"
# Enter a context with an instance of the API client
with mailslurp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailslurp_client.CommonActionsControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | inboxId

    try:
        # Delete all emails in an inbox
        api_instance.empty_inbox(inbox_id)
    except ApiException as e:
        print("Exception when calling CommonActionsControllerApi->empty_inbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**](.md)| inboxId | 

### Return type

void (empty response body)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_simple**
> send_email_simple(send_email_options)

Send an email from a random email address

To specify an email address first create an inbox and use that with the other send email methods

### Example

* Api Key Authentication (API_KEY):
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint
configuration = mailslurp_client.Configuration()
# Configure API key authorization: API_KEY
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Defining host is optional and default to https://api.mailslurp.com
configuration.host = "https://api.mailslurp.com"
# Enter a context with an instance of the API client
with mailslurp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailslurp_client.CommonActionsControllerApi(api_client)
    send_email_options = mailslurp_client.SendEmailOptions() # SendEmailOptions | sendEmailOptions

    try:
        # Send an email from a random email address
        api_instance.send_email_simple(send_email_options)
    except ApiException as e:
        print("Exception when calling CommonActionsControllerApi->send_email_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_email_options** | [**SendEmailOptions**](SendEmailOptions.md)| sendEmailOptions | 

### Return type

void (empty response body)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wait_for_email_count**
> list[EmailPreview] wait_for_email_count(count=count, inbox_id=inbox_id, timeout=timeout, unread_only=unread_only)

Wait for and return count number of emails 

Will only wait if count is greater that the found emails in given inbox.If you need to wait for an email for a non-empty inbox see the other receive methods.

### Example

* Api Key Authentication (API_KEY):
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint
configuration = mailslurp_client.Configuration()
# Configure API key authorization: API_KEY
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Defining host is optional and default to https://api.mailslurp.com
configuration.host = "https://api.mailslurp.com"
# Enter a context with an instance of the API client
with mailslurp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailslurp_client.CommonActionsControllerApi(api_client)
    count = 56 # int | Number of emails to wait for. Must be greater that 1 (optional)
inbox_id = 'inbox_id_example' # str | Id of the inbox we are fetching emails from (optional)
timeout = 56 # int | Max milliseconds to wait (optional)
unread_only = False # bool | Optional filter for unread only (optional) (default to False)

    try:
        # Wait for and return count number of emails 
        api_response = api_instance.wait_for_email_count(count=count, inbox_id=inbox_id, timeout=timeout, unread_only=unread_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommonActionsControllerApi->wait_for_email_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Number of emails to wait for. Must be greater that 1 | [optional] 
 **inbox_id** | [**str**](.md)| Id of the inbox we are fetching emails from | [optional] 
 **timeout** | **int**| Max milliseconds to wait | [optional] 
 **unread_only** | **bool**| Optional filter for unread only | [optional] [default to False]

### Return type

[**list[EmailPreview]**](EmailPreview.md)

### Authorization

[API_KEY](../README.md#API_KEY)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wait_for_latest_email**
> Email wait_for_latest_email(inbox_id=inbox_id, timeout=timeout, unread_only=unread_only)

Fetch inbox's latest email or if empty wait for email to arrive

Will return either the last received email or wait for an email to arrive and return that. If you need to wait for an email for a non-empty inbox see the other receive methods.

### Example

* Api Key Authentication (API_KEY):
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint
configuration = mailslurp_client.Configuration()
# Configure API key authorization: API_KEY
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Defining host is optional and default to https://api.mailslurp.com
configuration.host = "https://api.mailslurp.com"
# Enter a context with an instance of the API client
with mailslurp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailslurp_client.CommonActionsControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | Id of the inbox we are fetching emails from (optional)
timeout = 56 # int | Max milliseconds to wait (optional)
unread_only = False # bool | Optional filter for unread only (optional) (default to False)

    try:
        # Fetch inbox's latest email or if empty wait for email to arrive
        api_response = api_instance.wait_for_latest_email(inbox_id=inbox_id, timeout=timeout, unread_only=unread_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommonActionsControllerApi->wait_for_latest_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**](.md)| Id of the inbox we are fetching emails from | [optional] 
 **timeout** | **int**| Max milliseconds to wait | [optional] 
 **unread_only** | **bool**| Optional filter for unread only | [optional] [default to False]

### Return type

[**Email**](Email.md)

### Authorization

[API_KEY](../README.md#API_KEY)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wait_for_matching_email**
> list[EmailPreview] wait_for_matching_email(match_options, count=count, inbox_id=inbox_id, timeout=timeout, unread_only=unread_only)

Wait or return list of emails that match simple matching patterns

Results must also meet provided count. Match options allow simple CONTAINS or EQUALS filtering on SUBJECT, TO, BCC, CC, and FROM.

### Example

* Api Key Authentication (API_KEY):
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint
configuration = mailslurp_client.Configuration()
# Configure API key authorization: API_KEY
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Defining host is optional and default to https://api.mailslurp.com
configuration.host = "https://api.mailslurp.com"
# Enter a context with an instance of the API client
with mailslurp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailslurp_client.CommonActionsControllerApi(api_client)
    match_options = mailslurp_client.MatchOptions() # MatchOptions | matchOptions
count = 56 # int | Number of emails to wait for. Must be greater that 1 (optional)
inbox_id = 'inbox_id_example' # str | Id of the inbox we are fetching emails from (optional)
timeout = 56 # int | Max milliseconds to wait (optional)
unread_only = False # bool | Optional filter for unread only (optional) (default to False)

    try:
        # Wait or return list of emails that match simple matching patterns
        api_response = api_instance.wait_for_matching_email(match_options, count=count, inbox_id=inbox_id, timeout=timeout, unread_only=unread_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommonActionsControllerApi->wait_for_matching_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_options** | [**MatchOptions**](MatchOptions.md)| matchOptions | 
 **count** | **int**| Number of emails to wait for. Must be greater that 1 | [optional] 
 **inbox_id** | [**str**](.md)| Id of the inbox we are fetching emails from | [optional] 
 **timeout** | **int**| Max milliseconds to wait | [optional] 
 **unread_only** | **bool**| Optional filter for unread only | [optional] [default to False]

### Return type

[**list[EmailPreview]**](EmailPreview.md)

### Authorization

[API_KEY](../README.md#API_KEY)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wait_for_nth_email**
> Email wait_for_nth_email(inbox_id=inbox_id, index=index, timeout=timeout, unread_only=unread_only)

Wait for or fetch the email with a given index in the inbox specified

### Example

* Api Key Authentication (API_KEY):
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint
configuration = mailslurp_client.Configuration()
# Configure API key authorization: API_KEY
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Defining host is optional and default to https://api.mailslurp.com
configuration.host = "https://api.mailslurp.com"
# Enter a context with an instance of the API client
with mailslurp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailslurp_client.CommonActionsControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | Id of the inbox we are fetching emails from (optional)
index = 56 # int | Zero based index of the email to wait for (optional)
timeout = 56 # int | Max milliseconds to wait (optional)
unread_only = False # bool | Optional filter for unread only (optional) (default to False)

    try:
        # Wait for or fetch the email with a given index in the inbox specified
        api_response = api_instance.wait_for_nth_email(inbox_id=inbox_id, index=index, timeout=timeout, unread_only=unread_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommonActionsControllerApi->wait_for_nth_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**](.md)| Id of the inbox we are fetching emails from | [optional] 
 **index** | **int**| Zero based index of the email to wait for | [optional] 
 **timeout** | **int**| Max milliseconds to wait | [optional] 
 **unread_only** | **bool**| Optional filter for unread only | [optional] [default to False]

### Return type

[**Email**](Email.md)

### Authorization

[API_KEY](../README.md#API_KEY)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

