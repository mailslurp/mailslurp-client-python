# mailslurp_client.WebhookControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhookControllerApi#create_webhook) | **POST** /inboxes/{inboxId}/webhooks | Attach a WebHook URL to an inbox
[**delete_all_webhooks**](WebhookControllerApi#delete_all_webhooks) | **DELETE** /webhooks | Delete all webhooks
[**delete_webhook**](WebhookControllerApi#delete_webhook) | **DELETE** /inboxes/{inboxId}/webhooks/{webhookId} | Delete and disable a Webhook for an Inbox
[**get_all_webhook_results**](WebhookControllerApi#get_all_webhook_results) | **GET** /webhooks/results | Get results for all webhooks
[**get_all_webhooks**](WebhookControllerApi#get_all_webhooks) | **GET** /webhooks/paginated | List Webhooks Paginated
[**get_inbox_webhooks_paginated**](WebhookControllerApi#get_inbox_webhooks_paginated) | **GET** /inboxes/{inboxId}/webhooks/paginated | Get paginated webhooks for an Inbox
[**get_json_schema_for_webhook_payload**](WebhookControllerApi#get_json_schema_for_webhook_payload) | **POST** /webhooks/{webhookId}/schema | Get JSON Schema definition for webhook payload
[**get_test_webhook_payload**](WebhookControllerApi#get_test_webhook_payload) | **GET** /webhooks/test | Get test webhook payload example. Response content depends on eventName passed. Uses &#x60;EMAIL_RECEIVED&#x60; as default.
[**get_test_webhook_payload_email_opened**](WebhookControllerApi#get_test_webhook_payload_email_opened) | **GET** /webhooks/test/email-opened-payload | Get webhook test payload for email opened event
[**get_test_webhook_payload_email_read**](WebhookControllerApi#get_test_webhook_payload_email_read) | **GET** /webhooks/test/email-read-payload | Get webhook test payload for email opened event
[**get_test_webhook_payload_for_webhook**](WebhookControllerApi#get_test_webhook_payload_for_webhook) | **POST** /webhooks/{webhookId}/example | Get example payload for webhook
[**get_test_webhook_payload_new_attachment**](WebhookControllerApi#get_test_webhook_payload_new_attachment) | **GET** /webhooks/test/new-attachment-payload | Get webhook test payload for new attachment event
[**get_test_webhook_payload_new_contact**](WebhookControllerApi#get_test_webhook_payload_new_contact) | **GET** /webhooks/test/new-contact-payload | Get webhook test payload for new contact event
[**get_test_webhook_payload_new_email**](WebhookControllerApi#get_test_webhook_payload_new_email) | **GET** /webhooks/test/new-email-payload | Get webhook test payload for new email event
[**get_webhook**](WebhookControllerApi#get_webhook) | **GET** /webhooks/{webhookId} | Get a webhook for an Inbox
[**get_webhook_result**](WebhookControllerApi#get_webhook_result) | **GET** /webhooks/results/{webhookResultId} | Get a webhook result for a webhook
[**get_webhook_results**](WebhookControllerApi#get_webhook_results) | **GET** /webhooks/{webhookId}/results | Get a webhook results for a webhook
[**get_webhook_results_unseen_error_count**](WebhookControllerApi#get_webhook_results_unseen_error_count) | **GET** /webhooks/results/unseen-count | Get count of unseen webhook results with error status
[**get_webhooks**](WebhookControllerApi#get_webhooks) | **GET** /inboxes/{inboxId}/webhooks | Get all webhooks for an Inbox
[**redrive_webhook_result**](WebhookControllerApi#redrive_webhook_result) | **POST** /webhooks/results/{webhookResultId}/redrive | Get a webhook result and try to resend the original webhook payload
[**send_test_data**](WebhookControllerApi#send_test_data) | **POST** /webhooks/{webhookId}/test | Send webhook test data


# **create_webhook**
> WebhookDto create_webhook(inbox_id, webhook_options)

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | inboxId
webhook_options = mailslurp_client.CreateWebhookOptions() # CreateWebhookOptions | webhookOptions

    try:
        # Attach a WebHook URL to an inbox
        api_response = api_instance.create_webhook(inbox_id, webhook_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| inboxId | 
 **webhook_options** | [**CreateWebhookOptions**](CreateWebhookOptions)| webhookOptions | 

### Return type

[**WebhookDto**](WebhookDto)

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

# **delete_all_webhooks**
> delete_all_webhooks()

Delete all webhooks

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    
    try:
        # Delete all webhooks
        api_instance.delete_all_webhooks()
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->delete_all_webhooks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **delete_webhook**
> delete_webhook(inbox_id, webhook_id)

Delete and disable a Webhook for an Inbox

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | inboxId
webhook_id = 'webhook_id_example' # str | webhookId

    try:
        # Delete and disable a Webhook for an Inbox
        api_instance.delete_webhook(inbox_id, webhook_id)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->delete_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| inboxId | 
 **webhook_id** | [**str**]()| webhookId | 

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

# **get_all_webhook_results**
> PageWebhookResult get_all_webhook_results(before=before, page=page, search_filter=search_filter, since=since, size=size, sort=sort, unseen_only=unseen_only)

Get results for all webhooks

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    before = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at before the given timestamp (optional)
page = 0 # int | Optional page index in list pagination (optional) (default to 0)
search_filter = 'search_filter_example' # str | Optional search filter (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at after the given timestamp (optional)
size = 20 # int | Optional page size in list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')
unseen_only = True # bool | Filter for unseen exceptions only (optional)

    try:
        # Get results for all webhooks
        api_response = api_instance.get_all_webhook_results(before=before, page=page, search_filter=search_filter, since=since, size=size, sort=sort, unseen_only=unseen_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_all_webhook_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before** | **datetime**| Filter by created at before the given timestamp | [optional] 
 **page** | **int**| Optional page index in list pagination | [optional] [default to 0]
 **search_filter** | **str**| Optional search filter | [optional] 
 **since** | **datetime**| Filter by created at after the given timestamp | [optional] 
 **size** | **int**| Optional page size in list pagination | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]
 **unseen_only** | **bool**| Filter for unseen exceptions only | [optional] 

### Return type

[**PageWebhookResult**](PageWebhookResult)

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

# **get_all_webhooks**
> PageWebhookProjection get_all_webhooks(before=before, page=page, search_filter=search_filter, since=since, size=size, sort=sort)

List Webhooks Paginated

List webhooks in paginated form. Allows for page index, page size, and sort direction.

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    before = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at before the given timestamp (optional)
page = 0 # int | Optional page index in list pagination (optional) (default to 0)
search_filter = 'search_filter_example' # str | Optional search filter (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at after the given timestamp (optional)
size = 20 # int | Optional page size for paginated result list. (optional) (default to 20)
sort = 'DESC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'DESC')

    try:
        # List Webhooks Paginated
        api_response = api_instance.get_all_webhooks(before=before, page=page, search_filter=search_filter, since=since, size=size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_all_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before** | **datetime**| Filter by created at before the given timestamp | [optional] 
 **page** | **int**| Optional page index in list pagination | [optional] [default to 0]
 **search_filter** | **str**| Optional search filter | [optional] 
 **since** | **datetime**| Filter by created at after the given timestamp | [optional] 
 **size** | **int**| Optional page size for paginated result list. | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;DESC&#39;]

### Return type

[**PageWebhookProjection**](PageWebhookProjection)

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

# **get_inbox_webhooks_paginated**
> PageWebhookProjection get_inbox_webhooks_paginated(inbox_id, before=before, page=page, search_filter=search_filter, since=since, size=size, sort=sort)

Get paginated webhooks for an Inbox

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | inboxId
before = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at before the given timestamp (optional)
page = 0 # int | Optional page index in list pagination (optional) (default to 0)
search_filter = 'search_filter_example' # str | Optional search filter (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at after the given timestamp (optional)
size = 20 # int | Optional page size in list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')

    try:
        # Get paginated webhooks for an Inbox
        api_response = api_instance.get_inbox_webhooks_paginated(inbox_id, before=before, page=page, search_filter=search_filter, since=since, size=size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_inbox_webhooks_paginated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| inboxId | 
 **before** | **datetime**| Filter by created at before the given timestamp | [optional] 
 **page** | **int**| Optional page index in list pagination | [optional] [default to 0]
 **search_filter** | **str**| Optional search filter | [optional] 
 **since** | **datetime**| Filter by created at after the given timestamp | [optional] 
 **size** | **int**| Optional page size in list pagination | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]

### Return type

[**PageWebhookProjection**](PageWebhookProjection)

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

# **get_json_schema_for_webhook_payload**
> JSONSchemaDto get_json_schema_for_webhook_payload(webhook_id)

Get JSON Schema definition for webhook payload

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    webhook_id = 'webhook_id_example' # str | webhookId

    try:
        # Get JSON Schema definition for webhook payload
        api_response = api_instance.get_json_schema_for_webhook_payload(webhook_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_json_schema_for_webhook_payload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | [**str**]()| webhookId | 

### Return type

[**JSONSchemaDto**](JSONSchemaDto)

### Authorization

[API_KEY](../README#API_KEY)

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

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

# **get_test_webhook_payload**
> AbstractWebhookPayload get_test_webhook_payload(event_name=event_name)

Get test webhook payload example. Response content depends on eventName passed. Uses `EMAIL_RECEIVED` as default.

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    event_name = 'event_name_example' # str | eventName (optional)

    try:
        # Get test webhook payload example. Response content depends on eventName passed. Uses `EMAIL_RECEIVED` as default.
        api_response = api_instance.get_test_webhook_payload(event_name=event_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_test_webhook_payload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| eventName | [optional] 

### Return type

[**AbstractWebhookPayload**](AbstractWebhookPayload)

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

# **get_test_webhook_payload_email_opened**
> WebhookEmailOpenedPayload get_test_webhook_payload_email_opened()

Get webhook test payload for email opened event

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    
    try:
        # Get webhook test payload for email opened event
        api_response = api_instance.get_test_webhook_payload_email_opened()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_test_webhook_payload_email_opened: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebhookEmailOpenedPayload**](WebhookEmailOpenedPayload)

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

# **get_test_webhook_payload_email_read**
> WebhookEmailReadPayload get_test_webhook_payload_email_read()

Get webhook test payload for email opened event

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    
    try:
        # Get webhook test payload for email opened event
        api_response = api_instance.get_test_webhook_payload_email_read()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_test_webhook_payload_email_read: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebhookEmailReadPayload**](WebhookEmailReadPayload)

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

# **get_test_webhook_payload_for_webhook**
> AbstractWebhookPayload get_test_webhook_payload_for_webhook(webhook_id)

Get example payload for webhook

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    webhook_id = 'webhook_id_example' # str | webhookId

    try:
        # Get example payload for webhook
        api_response = api_instance.get_test_webhook_payload_for_webhook(webhook_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_test_webhook_payload_for_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | [**str**]()| webhookId | 

### Return type

[**AbstractWebhookPayload**](AbstractWebhookPayload)

### Authorization

[API_KEY](../README#API_KEY)

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

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

# **get_test_webhook_payload_new_attachment**
> WebhookNewAttachmentPayload get_test_webhook_payload_new_attachment()

Get webhook test payload for new attachment event

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    
    try:
        # Get webhook test payload for new attachment event
        api_response = api_instance.get_test_webhook_payload_new_attachment()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_test_webhook_payload_new_attachment: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebhookNewAttachmentPayload**](WebhookNewAttachmentPayload)

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

# **get_test_webhook_payload_new_contact**
> WebhookNewContactPayload get_test_webhook_payload_new_contact()

Get webhook test payload for new contact event

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    
    try:
        # Get webhook test payload for new contact event
        api_response = api_instance.get_test_webhook_payload_new_contact()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_test_webhook_payload_new_contact: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebhookNewContactPayload**](WebhookNewContactPayload)

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

# **get_test_webhook_payload_new_email**
> WebhookNewEmailPayload get_test_webhook_payload_new_email()

Get webhook test payload for new email event

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    
    try:
        # Get webhook test payload for new email event
        api_response = api_instance.get_test_webhook_payload_new_email()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_test_webhook_payload_new_email: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebhookNewEmailPayload**](WebhookNewEmailPayload)

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

# **get_webhook**
> WebhookDto get_webhook(webhook_id)

Get a webhook for an Inbox

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    webhook_id = 'webhook_id_example' # str | webhookId

    try:
        # Get a webhook for an Inbox
        api_response = api_instance.get_webhook(webhook_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | [**str**]()| webhookId | 

### Return type

[**WebhookDto**](WebhookDto)

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

# **get_webhook_result**
> WebhookResultDto get_webhook_result(webhook_result_id)

Get a webhook result for a webhook

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    webhook_result_id = 'webhook_result_id_example' # str | Webhook Result ID

    try:
        # Get a webhook result for a webhook
        api_response = api_instance.get_webhook_result(webhook_result_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_webhook_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_result_id** | [**str**]()| Webhook Result ID | 

### Return type

[**WebhookResultDto**](WebhookResultDto)

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

# **get_webhook_results**
> PageWebhookResult get_webhook_results(webhook_id, before=before, page=page, search_filter=search_filter, since=since, size=size, sort=sort, unseen_only=unseen_only)

Get a webhook results for a webhook

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    webhook_id = 'webhook_id_example' # str | ID of webhook to get results for
before = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at before the given timestamp (optional)
page = 0 # int | Optional page index in list pagination (optional) (default to 0)
search_filter = 'search_filter_example' # str | Optional search filter (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at after the given timestamp (optional)
size = 20 # int | Optional page size in list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')
unseen_only = True # bool | Filter for unseen exceptions only (optional)

    try:
        # Get a webhook results for a webhook
        api_response = api_instance.get_webhook_results(webhook_id, before=before, page=page, search_filter=search_filter, since=since, size=size, sort=sort, unseen_only=unseen_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_webhook_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | [**str**]()| ID of webhook to get results for | 
 **before** | **datetime**| Filter by created at before the given timestamp | [optional] 
 **page** | **int**| Optional page index in list pagination | [optional] [default to 0]
 **search_filter** | **str**| Optional search filter | [optional] 
 **since** | **datetime**| Filter by created at after the given timestamp | [optional] 
 **size** | **int**| Optional page size in list pagination | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]
 **unseen_only** | **bool**| Filter for unseen exceptions only | [optional] 

### Return type

[**PageWebhookResult**](PageWebhookResult)

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

# **get_webhook_results_unseen_error_count**
> UnseenErrorCountDto get_webhook_results_unseen_error_count(inbox_id)

Get count of unseen webhook results with error status

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | inboxId

    try:
        # Get count of unseen webhook results with error status
        api_response = api_instance.get_webhook_results_unseen_error_count(inbox_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_webhook_results_unseen_error_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| inboxId | 

### Return type

[**UnseenErrorCountDto**](UnseenErrorCountDto)

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

# **get_webhooks**
> list[WebhookDto] get_webhooks(inbox_id)

Get all webhooks for an Inbox

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | inboxId

    try:
        # Get all webhooks for an Inbox
        api_response = api_instance.get_webhooks(inbox_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->get_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()| inboxId | 

### Return type

[**list[WebhookDto]**](WebhookDto)

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

# **redrive_webhook_result**
> WebhookRedriveResult redrive_webhook_result(webhook_result_id)

Get a webhook result and try to resend the original webhook payload

Allows you to resend a webhook payload that was already sent. Webhooks that fail are retried automatically for 24 hours and then put in a dead letter queue. You can retry results manually using this method.

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    webhook_result_id = 'webhook_result_id_example' # str | Webhook Result ID

    try:
        # Get a webhook result and try to resend the original webhook payload
        api_response = api_instance.redrive_webhook_result(webhook_result_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->redrive_webhook_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_result_id** | [**str**]()| Webhook Result ID | 

### Return type

[**WebhookRedriveResult**](WebhookRedriveResult)

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **send_test_data**
> WebhookTestResult send_test_data(webhook_id)

Send webhook test data

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
    api_instance = mailslurp_client.WebhookControllerApi(api_client)
    webhook_id = 'webhook_id_example' # str | webhookId

    try:
        # Send webhook test data
        api_response = api_instance.send_test_data(webhook_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookControllerApi->send_test_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | [**str**]()| webhookId | 

### Return type

[**WebhookTestResult**](WebhookTestResult)

### Authorization

[API_KEY](../README#API_KEY)

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

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

