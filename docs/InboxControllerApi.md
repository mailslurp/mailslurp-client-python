# mailslurp_client.InboxControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_inbox**](InboxControllerApi.md#create_inbox) | **POST** /inboxes | Create an Inbox (email address)
[**delete_all_inboxes**](InboxControllerApi.md#delete_all_inboxes) | **DELETE** /inboxes | Delete all inboxes
[**delete_inbox**](InboxControllerApi.md#delete_inbox) | **DELETE** /inboxes/{inboxId} | Delete Inbox / Email Address
[**get_all_inboxes**](InboxControllerApi.md#get_all_inboxes) | **GET** /inboxes/paginated | List Inboxes Paginated
[**get_emails**](InboxControllerApi.md#get_emails) | **GET** /inboxes/{inboxId}/emails | Get emails in an Inbox
[**get_inbox**](InboxControllerApi.md#get_inbox) | **GET** /inboxes/{inboxId} | Get Inbox / EmailAddress
[**get_inbox_emails_paginated**](InboxControllerApi.md#get_inbox_emails_paginated) | **GET** /inboxes/{inboxId}/emails/paginated | Get inbox emails paginated
[**get_inboxes**](InboxControllerApi.md#get_inboxes) | **GET** /inboxes | List Inboxes / Email Addresses
[**send_email**](InboxControllerApi.md#send_email) | **POST** /inboxes/{inboxId} | Send Email
[**set_inbox_favourited**](InboxControllerApi.md#set_inbox_favourited) | **PUT** /inboxes/{inboxId}/favourite | Set inbox favourited state


# **create_inbox**
> Inbox create_inbox(description=description, email_address=email_address, expires_at=expires_at, favourite=favourite, name=name, tags=tags)

Create an Inbox (email address)

Create a new inbox and with a ranmdomized email address to send and receive from. Pass emailAddress parameter if you wish to use a specific email address. Creating an inbox is required before sending or receiving emails. If writing tests it is recommended that you create a new inbox during each test method so that it is unique and empty. 

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
    api_instance = mailslurp_client.InboxControllerApi(api_client)
    description = 'description_example' # str | Optional description for an inbox. (optional)
email_address = 'email_address_example' # str | Optional email address including domain you wish inbox to use (eg: test123@mydomain.com). Only supports domains that you have registered and verified with MailSlurp using dashboard or `createDomain` method. (optional)
expires_at = '2013-10-20T19:20:30+01:00' # datetime | Optional expires at timestamp. If your plan supports this feature you can specify when an inbox should expire. If left empty inbox will exist permanently or expire when your plan dictates (optional)
favourite = True # bool | Is inbox favourited. (optional)
name = 'name_example' # str | Optional name for an inbox. (optional)
tags = ['tags_example'] # list[str] | Optional tags for an inbox. Can be used for searching and filtering inboxes. (optional)

    try:
        # Create an Inbox (email address)
        api_response = api_instance.create_inbox(description=description, email_address=email_address, expires_at=expires_at, favourite=favourite, name=name, tags=tags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxControllerApi->create_inbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| Optional description for an inbox. | [optional] 
 **email_address** | **str**| Optional email address including domain you wish inbox to use (eg: test123@mydomain.com). Only supports domains that you have registered and verified with MailSlurp using dashboard or &#x60;createDomain&#x60; method. | [optional] 
 **expires_at** | **datetime**| Optional expires at timestamp. If your plan supports this feature you can specify when an inbox should expire. If left empty inbox will exist permanently or expire when your plan dictates | [optional] 
 **favourite** | **bool**| Is inbox favourited. | [optional] 
 **name** | **str**| Optional name for an inbox. | [optional] 
 **tags** | [**list[str]**](str.md)| Optional tags for an inbox. Can be used for searching and filtering inboxes. | [optional] 

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

# **delete_all_inboxes**
> delete_all_inboxes()

Delete all inboxes

Permanently delete all inboxes and associated email addresses and all emails within the given inboxes

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
    api_instance = mailslurp_client.InboxControllerApi(api_client)
    
    try:
        # Delete all inboxes
        api_instance.delete_all_inboxes()
    except ApiException as e:
        print("Exception when calling InboxControllerApi->delete_all_inboxes: %s\n" % e)
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

# **delete_inbox**
> delete_inbox(inbox_id)

Delete Inbox / Email Address

Permanently delete an inbox and associated email address and all emails within the given inboxes

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
    api_instance = mailslurp_client.InboxControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | inboxId

    try:
        # Delete Inbox / Email Address
        api_instance.delete_inbox(inbox_id)
    except ApiException as e:
        print("Exception when calling InboxControllerApi->delete_inbox: %s\n" % e)
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

# **get_all_inboxes**
> PageInboxProjection get_all_inboxes(favourite=favourite, page=page, search=search, size=size, sort=sort)

List Inboxes Paginated

List inboxes in paginated form. Allows for page index, page size, and sort direction. Can also filter by favourited or email address like pattern.

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
    api_instance = mailslurp_client.InboxControllerApi(api_client)
    favourite = False # bool | Optionally filter results for favourites only (optional) (default to False)
page = 0 # int | Optional page index in inbox list pagination (optional) (default to 0)
search = 'search_example' # str | Optionally filter by search words partial matching ID, tags, name, and email address (optional)
size = 20 # int | Optional page size in inbox list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')

    try:
        # List Inboxes Paginated
        api_response = api_instance.get_all_inboxes(favourite=favourite, page=page, search=search, size=size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxControllerApi->get_all_inboxes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **favourite** | **bool**| Optionally filter results for favourites only | [optional] [default to False]
 **page** | **int**| Optional page index in inbox list pagination | [optional] [default to 0]
 **search** | **str**| Optionally filter by search words partial matching ID, tags, name, and email address | [optional] 
 **size** | **int**| Optional page size in inbox list pagination | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]

### Return type

[**PageInboxProjection**](PageInboxProjection.md)

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

# **get_emails**
> list[EmailPreview] get_emails(inbox_id, limit=limit, min_count=min_count, retry_timeout=retry_timeout, since=since, sort=sort)

Get emails in an Inbox

List emails that an inbox has received. Only emails that are sent to the inbox's email address will appear in the inbox. It may take several seconds for any email you send to an inbox's email address to appear in the inbox. To make this endpoint wait for a minimum number of emails use the `minCount` parameter. The server will retry the inbox database until the `minCount` is satisfied or the `retryTimeout` is reached

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
    api_instance = mailslurp_client.InboxControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | Id of inbox that emails belongs to
limit = 56 # int | Limit the result set, ordered by received date time sort direction (optional)
min_count = 56 # int | Minimum acceptable email count. Will cause request to hang (and retry) until minCount is satisfied or retryTimeout is reached. (optional)
retry_timeout = 56 # int | Maximum milliseconds to spend retrying inbox database until minCount emails are returned (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Exclude emails received before this ISO 8601 date time (optional)
sort = 'sort_example' # str | Sort the results by received date and direction ASC or DESC (optional)

    try:
        # Get emails in an Inbox
        api_response = api_instance.get_emails(inbox_id, limit=limit, min_count=min_count, retry_timeout=retry_timeout, since=since, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxControllerApi->get_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**](.md)| Id of inbox that emails belongs to | 
 **limit** | **int**| Limit the result set, ordered by received date time sort direction | [optional] 
 **min_count** | **int**| Minimum acceptable email count. Will cause request to hang (and retry) until minCount is satisfied or retryTimeout is reached. | [optional] 
 **retry_timeout** | **int**| Maximum milliseconds to spend retrying inbox database until minCount emails are returned | [optional] 
 **since** | **datetime**| Exclude emails received before this ISO 8601 date time | [optional] 
 **sort** | **str**| Sort the results by received date and direction ASC or DESC | [optional] 

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
    api_instance = mailslurp_client.InboxControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | inboxId

    try:
        # Get Inbox / EmailAddress
        api_response = api_instance.get_inbox(inbox_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxControllerApi->get_inbox: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbox_emails_paginated**
> PageEmailPreview get_inbox_emails_paginated(inbox_id, page=page, size=size, sort=sort)

Get inbox emails paginated

Get a paginated list of emails in an inbox. Does not hold connections open.

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
    api_instance = mailslurp_client.InboxControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | Id of inbox that emails belongs to
page = 0 # int | Optional page index in inbox emails list pagination (optional) (default to 0)
size = 20 # int | Optional page size in inbox emails list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')

    try:
        # Get inbox emails paginated
        api_response = api_instance.get_inbox_emails_paginated(inbox_id, page=page, size=size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxControllerApi->get_inbox_emails_paginated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**](.md)| Id of inbox that emails belongs to | 
 **page** | **int**| Optional page index in inbox emails list pagination | [optional] [default to 0]
 **size** | **int**| Optional page size in inbox emails list pagination | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]

### Return type

[**PageEmailPreview**](PageEmailPreview.md)

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
    api_instance = mailslurp_client.InboxControllerApi(api_client)
    
    try:
        # List Inboxes / Email Addresses
        api_response = api_instance.get_inboxes()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxControllerApi->get_inboxes: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email**
> send_email(inbox_id, send_email_options=send_email_options)

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
    api_instance = mailslurp_client.InboxControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | ID of the inbox you want to send the email from
send_email_options = mailslurp_client.SendEmailOptions() # SendEmailOptions | Options for the email (optional)

    try:
        # Send Email
        api_instance.send_email(inbox_id, send_email_options=send_email_options)
    except ApiException as e:
        print("Exception when calling InboxControllerApi->send_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**](.md)| ID of the inbox you want to send the email from | 
 **send_email_options** | [**SendEmailOptions**](SendEmailOptions.md)| Options for the email | [optional] 

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

# **set_inbox_favourited**
> Inbox set_inbox_favourited(inbox_id, set_inbox_favourited_options)

Set inbox favourited state

Set and return new favourite state for an inbox

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
    api_instance = mailslurp_client.InboxControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | inboxId
set_inbox_favourited_options = mailslurp_client.SetInboxFavouritedOptions() # SetInboxFavouritedOptions | setInboxFavouritedOptions

    try:
        # Set inbox favourited state
        api_response = api_instance.set_inbox_favourited(inbox_id, set_inbox_favourited_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InboxControllerApi->set_inbox_favourited: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**](.md)| inboxId | 
 **set_inbox_favourited_options** | [**SetInboxFavouritedOptions**](SetInboxFavouritedOptions.md)| setInboxFavouritedOptions | 

### Return type

[**Inbox**](Inbox.md)

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

