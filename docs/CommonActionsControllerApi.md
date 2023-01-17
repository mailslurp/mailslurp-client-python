# mailslurp_client.CommonActionsControllerApi

All URIs are relative to *https://python.api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_email_address**](CommonActionsControllerApi#create_new_email_address) | **POST** /newEmailAddress | Create new random inbox
[**create_random_inbox**](CommonActionsControllerApi#create_random_inbox) | **POST** /createInbox | Create new random inbox
[**delete_email_address**](CommonActionsControllerApi#delete_email_address) | **DELETE** /deleteEmailAddress | Delete inbox email address by inbox id
[**empty_inbox**](CommonActionsControllerApi#empty_inbox) | **DELETE** /emptyInbox | Delete all emails in an inbox
[**send_email_simple**](CommonActionsControllerApi#send_email_simple) | **POST** /sendEmail | Send an email


# **create_new_email_address**
> InboxDto create_new_email_address(allow_team_access=allow_team_access, use_domain_pool=use_domain_pool, expires_at=expires_at, expires_in=expires_in, email_address=email_address, inbox_type=inbox_type, description=description, name=name, tags=tags, favourite=favourite, virtual_inbox=virtual_inbox, use_short_address=use_short_address)

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
    api_instance = mailslurp_client.CommonActionsControllerApi(api_client)
    allow_team_access = True # bool |  (optional)
use_domain_pool = True # bool |  (optional)
expires_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
expires_in = 56 # int |  (optional)
email_address = 'email_address_example' # str |  (optional)
inbox_type = 'inbox_type_example' # str |  (optional)
description = 'description_example' # str |  (optional)
name = 'name_example' # str |  (optional)
tags = ['tags_example'] # list[str] |  (optional)
favourite = True # bool |  (optional)
virtual_inbox = True # bool |  (optional)
use_short_address = True # bool |  (optional)

    try:
        # Create new random inbox
        api_response = api_instance.create_new_email_address(allow_team_access=allow_team_access, use_domain_pool=use_domain_pool, expires_at=expires_at, expires_in=expires_in, email_address=email_address, inbox_type=inbox_type, description=description, name=name, tags=tags, favourite=favourite, virtual_inbox=virtual_inbox, use_short_address=use_short_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommonActionsControllerApi->create_new_email_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_team_access** | **bool**|  | [optional] 
 **use_domain_pool** | **bool**|  | [optional] 
 **expires_at** | **datetime**|  | [optional] 
 **expires_in** | **int**|  | [optional] 
 **email_address** | **str**|  | [optional] 
 **inbox_type** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **tags** | [**list[str]**](str)|  | [optional] 
 **favourite** | **bool**|  | [optional] 
 **virtual_inbox** | **bool**|  | [optional] 
 **use_short_address** | **bool**|  | [optional] 

### Return type

[**InboxDto**](InboxDto)

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

# **create_random_inbox**
> InboxDto create_random_inbox(allow_team_access=allow_team_access, use_domain_pool=use_domain_pool, expires_at=expires_at, expires_in=expires_in, email_address=email_address, inbox_type=inbox_type, description=description, name=name, tags=tags, favourite=favourite, virtual_inbox=virtual_inbox, use_short_address=use_short_address)

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
    api_instance = mailslurp_client.CommonActionsControllerApi(api_client)
    allow_team_access = True # bool |  (optional)
use_domain_pool = True # bool |  (optional)
expires_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
expires_in = 56 # int |  (optional)
email_address = 'email_address_example' # str |  (optional)
inbox_type = 'inbox_type_example' # str |  (optional)
description = 'description_example' # str |  (optional)
name = 'name_example' # str |  (optional)
tags = ['tags_example'] # list[str] |  (optional)
favourite = True # bool |  (optional)
virtual_inbox = True # bool |  (optional)
use_short_address = True # bool |  (optional)

    try:
        # Create new random inbox
        api_response = api_instance.create_random_inbox(allow_team_access=allow_team_access, use_domain_pool=use_domain_pool, expires_at=expires_at, expires_in=expires_in, email_address=email_address, inbox_type=inbox_type, description=description, name=name, tags=tags, favourite=favourite, virtual_inbox=virtual_inbox, use_short_address=use_short_address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommonActionsControllerApi->create_random_inbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_team_access** | **bool**|  | [optional] 
 **use_domain_pool** | **bool**|  | [optional] 
 **expires_at** | **datetime**|  | [optional] 
 **expires_in** | **int**|  | [optional] 
 **email_address** | **str**|  | [optional] 
 **inbox_type** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **tags** | [**list[str]**](str)|  | [optional] 
 **favourite** | **bool**|  | [optional] 
 **virtual_inbox** | **bool**|  | [optional] 
 **use_short_address** | **bool**|  | [optional] 

### Return type

[**InboxDto**](InboxDto)

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

# **delete_email_address**
> delete_email_address(inbox_id)

Delete inbox email address by inbox id

Deletes inbox email address

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
    api_instance = mailslurp_client.CommonActionsControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | 

    try:
        # Delete inbox email address by inbox id
        api_instance.delete_email_address(inbox_id)
    except ApiException as e:
        print("Exception when calling CommonActionsControllerApi->delete_email_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()|  | 

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
    api_instance = mailslurp_client.CommonActionsControllerApi(api_client)
    inbox_id = 'inbox_id_example' # str | 

    try:
        # Delete all emails in an inbox
        api_instance.empty_inbox(inbox_id)
    except ApiException as e:
        print("Exception when calling CommonActionsControllerApi->empty_inbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_id** | [**str**]()|  | 

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

# **send_email_simple**
> send_email_simple(simple_send_email_options)

Send an email

If no senderId or inboxId provided a random email address will be used to send from.

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
    api_instance = mailslurp_client.CommonActionsControllerApi(api_client)
    simple_send_email_options = mailslurp_client.SimpleSendEmailOptions() # SimpleSendEmailOptions | 

    try:
        # Send an email
        api_instance.send_email_simple(simple_send_email_options)
    except ApiException as e:
        print("Exception when calling CommonActionsControllerApi->send_email_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simple_send_email_options** | [**SimpleSendEmailOptions**](SimpleSendEmailOptions)|  | 

### Return type

void (empty response body)

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

