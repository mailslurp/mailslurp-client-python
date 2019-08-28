# mailslurp_client.ExtraOperationsApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_inboxes**](ExtraOperationsApi.md#bulk_create_inboxes) | **POST** /bulk/inboxes | Bulk create Inboxes (email addresses)
[**bulk_delete_inboxes**](ExtraOperationsApi.md#bulk_delete_inboxes) | **DELETE** /bulk/inboxes | Bulk Delete Inboxes
[**bulk_send_emails**](ExtraOperationsApi.md#bulk_send_emails) | **POST** /bulk/send | Bulk Send Emails
[**create_inbox**](ExtraOperationsApi.md#create_inbox) | **POST** /inboxes | Create an Inbox (email address)
[**create_webhook**](ExtraOperationsApi.md#create_webhook) | **POST** /inboxes/{inboxId}/webhooks | Attach a WebHook URL to an inbox
[**delete_email**](ExtraOperationsApi.md#delete_email) | **DELETE** /emails/{emailId} | Delete Email
[**delete_inbox**](ExtraOperationsApi.md#delete_inbox) | **DELETE** /inboxes/{inboxId} | Delete Inbox / Email Address
[**delete_webhook**](ExtraOperationsApi.md#delete_webhook) | **DELETE** /inboxes/{inboxId}/webhooks/{webhookId} | Delete and disable a WebHook for an Inbox
[**download_attachment**](ExtraOperationsApi.md#download_attachment) | **GET** /emails/{emailId}/attachments/{attachmentId} | Get email attachment
[**get_email**](ExtraOperationsApi.md#get_email) | **GET** /emails/{emailId} | Get Email Content
[**get_emails**](ExtraOperationsApi.md#get_emails) | **GET** /inboxes/{inboxId}/emails | List Emails in an Inbox / EmailAddress
[**get_inbox**](ExtraOperationsApi.md#get_inbox) | **GET** /inboxes/{inboxId} | Get Inbox / EmailAddress
[**get_inboxes**](ExtraOperationsApi.md#get_inboxes) | **GET** /inboxes | List Inboxes / Email Addresses
[**get_raw_email_contents**](ExtraOperationsApi.md#get_raw_email_contents) | **GET** /emails/{emailId}/raw | Get Raw Email Content
[**get_webhooks**](ExtraOperationsApi.md#get_webhooks) | **GET** /inboxes/{inboxId}/webhooks | Get all WebHooks for an Inbox
[**send_email**](ExtraOperationsApi.md#send_email) | **POST** /inboxes/{inboxId} | Send Email


# **bulk_create_inboxes**
> list[Inbox] bulk_create_inboxes(count)

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
    api_response = api_instance.bulk_create_inboxes(count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->bulk_create_inboxes: %s\n" % e)
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

# **bulk_delete_inboxes**
> bulk_delete_inboxes(request_body)

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
    api_instance.bulk_delete_inboxes(request_body)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->bulk_delete_inboxes: %s\n" % e)
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

# **bulk_send_emails**
> bulk_send_emails(bulk_send_email_options)

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
    api_instance.bulk_send_emails(bulk_send_email_options)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->bulk_send_emails: %s\n" % e)
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

# **create_inbox**
> Inbox create_inbox()

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
    api_response = api_instance.create_inbox()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->create_inbox: %s\n" % e)
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

# **create_webhook**
> Webhook create_webhook(inbox_id, create_webhook_options)

Attach a WebHook URL to an inbox

Get notified whenever an inbox receives an email via a WebHook URL. An emailID will be posted to this URL every time an email is received for this inbox. The URL must be publicly reachable by the MailSlurp server. You can provide basicAuth values if you wish to secure this endpoint.

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
create_webhook_options = mailslurp_client.CreateWebhookOptions() # CreateWebhookOptions | options

try:
    # Attach a WebHook URL to an inbox
    api_response = api_instance.create_webhook(inbox_id, create_webhook_options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**](.md)| inboxId | 
 **create_webhook_options** | [**CreateWebhookOptions**](CreateWebhookOptions.md)| options | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email**
> delete_email(email_id)

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
    api_instance.delete_email(email_id)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->delete_email: %s\n" % e)
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

# **delete_inbox**
> delete_inbox(inbox_id)

Delete Inbox / Email Address

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
    # Delete Inbox / Email Address
    api_instance.delete_inbox(inbox_id)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->delete_inbox: %s\n" % e)
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

# **delete_webhook**
> delete_webhook(inbox_id, webhook_id)

Delete and disable a WebHook for an Inbox

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
webhook_id = 'webhook_id_example' # str | webhookId

try:
    # Delete and disable a WebHook for an Inbox
    api_instance.delete_webhook(inbox_id, webhook_id)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->delete_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**](.md)| inboxId | 
 **webhook_id** | [**str**](.md)| webhookId | 

### Return type

void (empty response body)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_attachment**
> download_attachment(attachment_id, email_id)

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
    api_instance.download_attachment(attachment_id, email_id)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->download_attachment: %s\n" % e)
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

# **get_email**
> Email get_email(email_id)

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
    api_response = api_instance.get_email(email_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->get_email: %s\n" % e)
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

# **get_emails**
> list[EmailPreview] get_emails(inbox_id, limit=limit, min_count=min_count, retry_timeout=retry_timeout, since=since)

List Emails in an Inbox / EmailAddress

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
    # List Emails in an Inbox / EmailAddress
    api_response = api_instance.get_emails(inbox_id, limit=limit, min_count=min_count, retry_timeout=retry_timeout, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->get_emails: %s\n" % e)
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

# **get_inbox**
> Inbox get_inbox(inbox_id)

Get Inbox / EmailAddress

Returns an inbox's properties, including its email address and ID.

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
    # Get Inbox / EmailAddress
    api_response = api_instance.get_inbox(inbox_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->get_inbox: %s\n" % e)
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

# **get_inboxes**
> list[Inbox] get_inboxes()

List Inboxes / Email Addresses

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
    # List Inboxes / Email Addresses
    api_response = api_instance.get_inboxes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->get_inboxes: %s\n" % e)
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

# **get_raw_email_contents**
> str get_raw_email_contents(email_id)

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
    api_response = api_instance.get_raw_email_contents(email_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->get_raw_email_contents: %s\n" % e)
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

# **get_webhooks**
> list[Webhook] get_webhooks(inbox_id)

Get all WebHooks for an Inbox

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
    # Get all WebHooks for an Inbox
    api_response = api_instance.get_webhooks(inbox_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->get_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**](.md)| inboxId | 

### Return type

[**list[Webhook]**](Webhook.md)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email**
> send_email(inbox_id, send_email_options)

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
    api_instance.send_email(inbox_id, send_email_options)
except ApiException as e:
    print("Exception when calling ExtraOperationsApi->send_email: %s\n" % e)
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

