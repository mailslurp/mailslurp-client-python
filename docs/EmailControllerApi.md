# mailslurp_client.EmailControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all_emails**](EmailControllerApi.md#delete_all_emails) | **DELETE** /emails | Delete all emails
[**delete_email**](EmailControllerApi.md#delete_email) | **DELETE** /emails/{emailId} | Delete an email
[**download_attachment**](EmailControllerApi.md#download_attachment) | **GET** /emails/{emailId}/attachments/{attachmentId} | Get email attachment bytes
[**forward_email**](EmailControllerApi.md#forward_email) | **POST** /emails/{emailId}/forward | Forward email
[**get_attachment_meta_data**](EmailControllerApi.md#get_attachment_meta_data) | **GET** /emails/{emailId}/attachments/{attachmentId}/metadata | Get email attachment metadata
[**get_attachments**](EmailControllerApi.md#get_attachments) | **GET** /emails/{emailId}/attachments | Get all email attachment metadata
[**get_email**](EmailControllerApi.md#get_email) | **GET** /emails/{emailId} | Get email content
[**get_email_html**](EmailControllerApi.md#get_email_html) | **GET** /emails/{emailId}/html | Get email content as HTML
[**get_emails_paginated**](EmailControllerApi.md#get_emails_paginated) | **GET** /emails | Get all emails
[**get_raw_email_contents**](EmailControllerApi.md#get_raw_email_contents) | **GET** /emails/{emailId}/raw | Get raw email string
[**get_raw_email_json**](EmailControllerApi.md#get_raw_email_json) | **GET** /emails/{emailId}/raw/json | Get raw email in JSON
[**get_unread_email_count**](EmailControllerApi.md#get_unread_email_count) | **GET** /emails/unreadCount | Get unread email count
[**validate_email**](EmailControllerApi.md#validate_email) | **POST** /emails/{emailId}/validate | Validate email


# **delete_all_emails**
> delete_all_emails()

Delete all emails

Deletes all emails in your account. Be careful as emails cannot be recovered

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
    api_instance = mailslurp_client.EmailControllerApi(api_client)
    
    try:
        # Delete all emails
        api_instance.delete_all_emails()
    except ApiException as e:
        print("Exception when calling EmailControllerApi->delete_all_emails: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **delete_email**
> delete_email(email_id)

Delete an email

Deletes an email and removes it from the inbox. Deleted emails cannot be recovered.

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
    api_instance = mailslurp_client.EmailControllerApi(api_client)
    email_id = 'email_id_example' # str | emailId

    try:
        # Delete an email
        api_instance.delete_email(email_id)
    except ApiException as e:
        print("Exception when calling EmailControllerApi->delete_email: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_attachment**
> str download_attachment(attachment_id, email_id, api_key=api_key)

Get email attachment bytes

Returns the specified attachment for a given email as a byte stream (file download). You can find attachment ids in email responses endpoint responses. The response type is application/octet-stream.

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
    api_instance = mailslurp_client.EmailControllerApi(api_client)
    attachment_id = 'attachment_id_example' # str | attachmentId
email_id = 'email_id_example' # str | emailId
api_key = 'api_key_example' # str | Can pass apiKey in url for this request if you wish to download the file in a browser (optional)

    try:
        # Get email attachment bytes
        api_response = api_instance.download_attachment(attachment_id, email_id, api_key=api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailControllerApi->download_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| attachmentId | 
 **email_id** | [**str**](.md)| emailId | 
 **api_key** | **str**| Can pass apiKey in url for this request if you wish to download the file in a browser | [optional] 

### Return type

**str**

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forward_email**
> forward_email(email_id, forward_email_options)

Forward email

Forward an existing email to new recipients.

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
    api_instance = mailslurp_client.EmailControllerApi(api_client)
    email_id = 'email_id_example' # str | emailId
forward_email_options = mailslurp_client.ForwardEmailOptions() # ForwardEmailOptions | forwardEmailOptions

    try:
        # Forward email
        api_instance.forward_email(email_id, forward_email_options)
    except ApiException as e:
        print("Exception when calling EmailControllerApi->forward_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | [**str**](.md)| emailId | 
 **forward_email_options** | [**ForwardEmailOptions**](ForwardEmailOptions.md)| forwardEmailOptions | 

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

# **get_attachment_meta_data**
> AttachmentMetaData get_attachment_meta_data(attachment_id, email_id)

Get email attachment metadata

Returns the metadata such as name and content-type for a given attachment and email.

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
    api_instance = mailslurp_client.EmailControllerApi(api_client)
    attachment_id = 'attachment_id_example' # str | attachmentId
email_id = 'email_id_example' # str | emailId

    try:
        # Get email attachment metadata
        api_response = api_instance.get_attachment_meta_data(attachment_id, email_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailControllerApi->get_attachment_meta_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| attachmentId | 
 **email_id** | [**str**](.md)| emailId | 

### Return type

[**AttachmentMetaData**](AttachmentMetaData.md)

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

# **get_attachments**
> list[AttachmentMetaData] get_attachments(email_id)

Get all email attachment metadata

Returns an array of attachment metadata such as name and content-type for a given email if present.

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
    api_instance = mailslurp_client.EmailControllerApi(api_client)
    email_id = 'email_id_example' # str | emailId

    try:
        # Get all email attachment metadata
        api_response = api_instance.get_attachments(email_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailControllerApi->get_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | [**str**](.md)| emailId | 

### Return type

[**list[AttachmentMetaData]**](AttachmentMetaData.md)

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

# **get_email**
> Email get_email(email_id, decode=decode)

Get email content

Returns a email summary object with headers and content. To retrieve the raw unparsed email use the getRawEmail endpoints

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
    api_instance = mailslurp_client.EmailControllerApi(api_client)
    email_id = 'email_id_example' # str | emailId
decode = False # bool | Decode email body quoted-printable encoding to plain text. SMTP servers often encode text using quoted-printable format (for instance `=D7`). This can be a pain for testing (optional) (default to False)

    try:
        # Get email content
        api_response = api_instance.get_email(email_id, decode=decode)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailControllerApi->get_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | [**str**](.md)| emailId | 
 **decode** | **bool**| Decode email body quoted-printable encoding to plain text. SMTP servers often encode text using quoted-printable format (for instance &#x60;&#x3D;D7&#x60;). This can be a pain for testing | [optional] [default to False]

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

# **get_email_html**
> str get_email_html(email_id, decode=decode)

Get email content as HTML

Retrieve email content as HTML response for viewing in browsers. Decodes quoted-printable entities and converts charset to UTF-8. Pass your API KEY as a request parameter when viewing in a browser: `?apiKey=xxx`

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
    api_instance = mailslurp_client.EmailControllerApi(api_client)
    email_id = 'email_id_example' # str | emailId
decode = False # bool | decode (optional) (default to False)

    try:
        # Get email content as HTML
        api_response = api_instance.get_email_html(email_id, decode=decode)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailControllerApi->get_email_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | [**str**](.md)| emailId | 
 **decode** | **bool**| decode | [optional] [default to False]

### Return type

**str**

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_emails_paginated**
> PageEmailProjection get_emails_paginated(inbox_id=inbox_id, page=page, size=size, sort=sort, unread_only=unread_only)

Get all emails

By default returns all emails across all inboxes sorted by ascending created at date. Responses are paginated. You can restrict results to a list of inbox IDs. You can also filter out read messages

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
    api_instance = mailslurp_client.EmailControllerApi(api_client)
    inbox_id = ['inbox_id_example'] # list[str] | Optional inbox ids to filter by. Can be repeated. By default will use all inboxes belonging to your account. (optional)
page = 0 # int | Optional page index in email list pagination (optional) (default to 0)
size = 20 # int | Optional page size in email list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')
unread_only = False # bool | Optional filter for unread emails only. All emails are considered unread until they are viewed in the dashboard or requested directly (optional) (default to False)

    try:
        # Get all emails
        api_response = api_instance.get_emails_paginated(inbox_id=inbox_id, page=page, size=size, sort=sort, unread_only=unread_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailControllerApi->get_emails_paginated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**list[str]**](str.md)| Optional inbox ids to filter by. Can be repeated. By default will use all inboxes belonging to your account. | [optional] 
 **page** | **int**| Optional page index in email list pagination | [optional] [default to 0]
 **size** | **int**| Optional page size in email list pagination | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]
 **unread_only** | **bool**| Optional filter for unread emails only. All emails are considered unread until they are viewed in the dashboard or requested directly | [optional] [default to False]

### Return type

[**PageEmailProjection**](PageEmailProjection.md)

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

# **get_raw_email_contents**
> str get_raw_email_contents(email_id)

Get raw email string

Returns a raw, unparsed, and unprocessed email. If your client has issues processing the response it is likely due to the response content-type which is text/plain. If you need a JSON response content-type use the getRawEmailJson endpoint

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
    api_instance = mailslurp_client.EmailControllerApi(api_client)
    email_id = 'email_id_example' # str | emailId

    try:
        # Get raw email string
        api_response = api_instance.get_raw_email_contents(email_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailControllerApi->get_raw_email_contents: %s\n" % e)
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
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | text/plain raw email |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_email_json**
> RawEmailJson get_raw_email_json(email_id)

Get raw email in JSON

Returns a raw, unparsed, and unprocessed email wrapped in a JSON response object for easier handling when compared with the getRawEmail text/plain response

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
    api_instance = mailslurp_client.EmailControllerApi(api_client)
    email_id = 'email_id_example' # str | emailId

    try:
        # Get raw email in JSON
        api_response = api_instance.get_raw_email_json(email_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailControllerApi->get_raw_email_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | [**str**](.md)| emailId | 

### Return type

[**RawEmailJson**](RawEmailJson.md)

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

# **get_unread_email_count**
> UnreadCount get_unread_email_count()

Get unread email count

Get number of emails unread

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
    api_instance = mailslurp_client.EmailControllerApi(api_client)
    
    try:
        # Get unread email count
        api_response = api_instance.get_unread_email_count()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailControllerApi->get_unread_email_count: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnreadCount**](UnreadCount.md)

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

# **validate_email**
> ValidationDto validate_email(email_id)

Validate email

Validate the HTML content of email if HTML is found. Considered valid if no HTML.

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
    api_instance = mailslurp_client.EmailControllerApi(api_client)
    email_id = 'email_id_example' # str | emailId

    try:
        # Validate email
        api_response = api_instance.validate_email(email_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailControllerApi->validate_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | [**str**](.md)| emailId | 

### Return type

[**ValidationDto**](ValidationDto.md)

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
