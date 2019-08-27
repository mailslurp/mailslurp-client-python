# mailslurp_client.ExtraOperationsApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_inboxes_using_post**](ExtraOperationsApi.md#bulk_create_inboxes_using_post) | **POST** /bulk/inboxes | Bulk create Inboxes (email addresses)
[**bulk_delete_inboxes_using_delete**](ExtraOperationsApi.md#bulk_delete_inboxes_using_delete) | **DELETE** /bulk/inboxes | Bulk Delete Inboxes
[**bulk_send_emails_using_post**](ExtraOperationsApi.md#bulk_send_emails_using_post) | **POST** /bulk/send | Bulk Send Emails
[**create_inbox_using_post**](ExtraOperationsApi.md#create_inbox_using_post) | **POST** /inboxes | Create an Inbox (email address)
[**delete_email_using_delete**](ExtraOperationsApi.md#delete_email_using_delete) | **DELETE** /emails/{emailId} | Delete Email
[**delete_inbox_using_delete**](ExtraOperationsApi.md#delete_inbox_using_delete) | **DELETE** /inboxes/{inboxId} | Delete Inbox
[**get_email_attachment_using_get**](ExtraOperationsApi.md#get_email_attachment_using_get) | **GET** /emails/{emailId}/attachments/{attachmentId} | Get email attachment
[**get_email_using_get**](ExtraOperationsApi.md#get_email_using_get) | **GET** /emails/{emailId} | Get Email Content
[**get_emails_using_get**](ExtraOperationsApi.md#get_emails_using_get) | **GET** /inboxes/{inboxId}/emails | List an Inbox&#39;s Emails
[**get_inbox_using_get**](ExtraOperationsApi.md#get_inbox_using_get) | **GET** /inboxes/{inboxId} | Get Inbox
[**get_inboxes_using_get**](ExtraOperationsApi.md#get_inboxes_using_get) | **GET** /inboxes | List Inboxes
[**get_raw_email_using_get**](ExtraOperationsApi.md#get_raw_email_using_get) | **GET** /emails/{emailId}/raw | Get Raw Email Content
[**send_email_using_post**](ExtraOperationsApi.md#send_email_using_post) | **POST** /inboxes/{inboxId} | Send Email


# **bulk_create_inboxes_using_post**
> list[Inbox] bulk_create_inboxes_using_post(count)

Bulk create Inboxes (email addresses)

Enterprise Plan Required

### Example

* Api Key Authentication (API_KEY): 
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = mailslurp_client.ExtraOperationsApi(mailslurp_client.ApiClient(configuration))
count = 56 # int | Number of inboxes to be created in bulk

try:
    # Bulk create Inboxes (email addresses)
    api_response = api_instance.bulk_create_inboxes_using_post(count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->bulk_create_inboxes_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Number of inboxes to be created in bulk | 

### Return type

[**list[Inbox]**](Inbox.md)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_inboxes_using_delete**
> bulk_delete_inboxes_using_delete(request_body)

Bulk Delete Inboxes

Enterprise Plan Required

### Example

* Api Key Authentication (API_KEY): 
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = mailslurp_client.ExtraOperationsApi(mailslurp_client.ApiClient(configuration))
request_body = NULL # list[str] | ids

try:
    # Bulk Delete Inboxes
    api_instance.bulk_delete_inboxes_using_delete(request_body)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->bulk_delete_inboxes_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[str]**](list.md)| ids | 

### Return type

void (empty response body)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_send_emails_using_post**
> bulk_send_emails_using_post(bulk_send_email_options)

Bulk Send Emails

Enterprise Plan Required

### Example

* Api Key Authentication (API_KEY): 
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = mailslurp_client.ExtraOperationsApi(mailslurp_client.ApiClient(configuration))
bulk_send_email_options = mailslurp_client.BulkSendEmailOptions() # BulkSendEmailOptions | bulkSendEmailOptions

try:
    # Bulk Send Emails
    api_instance.bulk_send_emails_using_post(bulk_send_email_options)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->bulk_send_emails_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_send_email_options** | [**BulkSendEmailOptions**](BulkSendEmailOptions.md)| bulkSendEmailOptions | 

### Return type

void (empty response body)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inbox_using_post**
> Inbox create_inbox_using_post()

Create an Inbox (email address)

Create a new inbox and ephemeral email address to send and receive from. This is a necessary step before sending or receiving emails. The response contains the inbox's ID and its associated email address. It is recommended that you create a new inbox during each test method so that it is unique and empty

### Example

* Api Key Authentication (API_KEY): 
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = mailslurp_client.ExtraOperationsApi(mailslurp_client.ApiClient(configuration))

try:
    # Create an Inbox (email address)
    api_response = api_instance.create_inbox_using_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->create_inbox_using_post: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_using_delete**
> delete_email_using_delete(email_id)

Delete Email

Deletes an email and removes it from the inbox

### Example

* Api Key Authentication (API_KEY): 
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = mailslurp_client.ExtraOperationsApi(mailslurp_client.ApiClient(configuration))
email_id = 'email_id_example' # str | emailId

try:
    # Delete Email
    api_instance.delete_email_using_delete(email_id)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->delete_email_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | [**str**](.md)| emailId | 

### Return type

void (empty response body)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inbox_using_delete**
> delete_inbox_using_delete(inbox_id)

Delete Inbox

Permanently delete an inbox and associated email address

### Example

* Api Key Authentication (API_KEY): 
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = mailslurp_client.ExtraOperationsApi(mailslurp_client.ApiClient(configuration))
inbox_id = 'inbox_id_example' # str | inboxId

try:
    # Delete Inbox
    api_instance.delete_inbox_using_delete(inbox_id)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->delete_inbox_using_delete: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_attachment_using_get**
> get_email_attachment_using_get(attachment_id, email_id)

Get email attachment

Returns the specified attachment for a given email as a byte stream (file download). Get the attachmentId from the email response. Requires enterprise account.

### Example

* Api Key Authentication (API_KEY): 
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = mailslurp_client.ExtraOperationsApi(mailslurp_client.ApiClient(configuration))
attachment_id = 'attachment_id_example' # str | attachmentId
email_id = 'email_id_example' # str | emailId

try:
    # Get email attachment
    api_instance.get_email_attachment_using_get(attachment_id, email_id)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->get_email_attachment_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| attachmentId | 
 **email_id** | [**str**](.md)| emailId | 

### Return type

void (empty response body)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_using_get**
> Email get_email_using_get(email_id)

Get Email Content

Returns a email summary object with headers and content. To retrieve the raw unparsed email use the getRawMessage endpoint

### Example

* Api Key Authentication (API_KEY): 
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = mailslurp_client.ExtraOperationsApi(mailslurp_client.ApiClient(configuration))
email_id = 'email_id_example' # str | emailId

try:
    # Get Email Content
    api_response = api_instance.get_email_using_get(email_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->get_email_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | [**str**](.md)| emailId | 

### Return type

[**Email**](Email.md)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_emails_using_get**
> list[EmailPreview] get_emails_using_get(inbox_id, limit=limit, min_count=min_count, retry_timeout=retry_timeout, since=since)

List an Inbox's Emails

List emails that an inbox has received. Only emails that are sent to the inbox's email address will appear in the inbox. It may take several seconds for any email you send to an inbox's email address to appear in the inbox. To make this endpoint wait for a minimum number of emails use the `minCount` parameter. The server will retry the inbox database until the `minCount` is satisfied or the `retryTimeout` is reached

### Example

* Api Key Authentication (API_KEY): 
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = mailslurp_client.ExtraOperationsApi(mailslurp_client.ApiClient(configuration))
inbox_id = 'inbox_id_example' # str | Id of inbox that emails belongs to
limit = 56 # int | Limit the result set, ordered by descending received date time (optional)
min_count = 56 # int | Minimum acceptable email count. Will cause request to hang (and retry) until minCount is satisfied or retryTimeout is reached. (optional)
retry_timeout = 56 # int | Maximum milliseconds to spend retrying inbox database until minCount emails are returned (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Exclude emails received before this ISO 8601 date time (optional)

try:
    # List an Inbox's Emails
    api_response = api_instance.get_emails_using_get(inbox_id, limit=limit, min_count=min_count, retry_timeout=retry_timeout, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->get_emails_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**](.md)| Id of inbox that emails belongs to | 
 **limit** | **int**| Limit the result set, ordered by descending received date time | [optional] 
 **min_count** | **int**| Minimum acceptable email count. Will cause request to hang (and retry) until minCount is satisfied or retryTimeout is reached. | [optional] 
 **retry_timeout** | **int**| Maximum milliseconds to spend retrying inbox database until minCount emails are returned | [optional] 
 **since** | **datetime**| Exclude emails received before this ISO 8601 date time | [optional] 

### Return type

[**list[EmailPreview]**](EmailPreview.md)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbox_using_get**
> Inbox get_inbox_using_get(inbox_id)

Get Inbox

Returns an inbox's properties, including its email address and ID

### Example

* Api Key Authentication (API_KEY): 
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = mailslurp_client.ExtraOperationsApi(mailslurp_client.ApiClient(configuration))
inbox_id = 'inbox_id_example' # str | inboxId

try:
    # Get Inbox
    api_response = api_instance.get_inbox_using_get(inbox_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->get_inbox_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**](.md)| inboxId | 

### Return type

[**Inbox**](Inbox.md)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inboxes_using_get**
> list[Inbox] get_inboxes_using_get()

List Inboxes

List the inboxes you have created

### Example

* Api Key Authentication (API_KEY): 
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = mailslurp_client.ExtraOperationsApi(mailslurp_client.ApiClient(configuration))

try:
    # List Inboxes
    api_response = api_instance.get_inboxes_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->get_inboxes_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Inbox]**](Inbox.md)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_email_using_get**
> str get_raw_email_using_get(email_id)

Get Raw Email Content

Returns a raw, unparsed and unprocessed email

### Example

* Api Key Authentication (API_KEY): 
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = mailslurp_client.ExtraOperationsApi(mailslurp_client.ApiClient(configuration))
email_id = 'email_id_example' # str | emailId

try:
    # Get Raw Email Content
    api_response = api_instance.get_raw_email_using_get(email_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->get_raw_email_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | [**str**](.md)| emailId | 

### Return type

**str**

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_using_post**
> send_email_using_post(inbox_id, send_email_options)

Send Email

Send an email from the inbox's email address. Specify the email recipients and contents in the request body. See the `SendEmailOptions` for more information. Note the `inboxId` refers to the inbox's id NOT its email address

### Example

* Api Key Authentication (API_KEY): 
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = mailslurp_client.ExtraOperationsApi(mailslurp_client.ApiClient(configuration))
inbox_id = 'inbox_id_example' # str | inboxId
send_email_options = mailslurp_client.SendEmailOptions() # SendEmailOptions | sendEmailOptions

try:
    # Send Email
    api_instance.send_email_using_post(inbox_id, send_email_options)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->send_email_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**](.md)| inboxId | 
 **send_email_options** | [**SendEmailOptions**](SendEmailOptions.md)| sendEmailOptions | 

### Return type

void (empty response body)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

