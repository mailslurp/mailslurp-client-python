# mailslurp_client.CommonActionsControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_email_address**](CommonActionsControllerApi#create_new_email_address) | **POST** /createInbox | Create new random inbox
[**create_new_email_address1**](CommonActionsControllerApi#create_new_email_address1) | **POST** /newEmailAddress | Create new random inbox
[**empty_inbox**](CommonActionsControllerApi#empty_inbox) | **DELETE** /emptyInbox | Delete all emails in an inbox
[**send_email_simple**](CommonActionsControllerApi#send_email_simple) | **POST** /sendEmail | Send an email


# **create_new_email_address**
> Inbox create_new_email_address(allow_team_access=allow_team_access, description=description, email_address=email_address, expires_at=expires_at, expires_in=expires_in, favourite=favourite, inbox_type=inbox_type, name=name, tags=tags, use_domain_pool=use_domain_pool)

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
    api_instance = mailslurp_client.CommonActionsControllerApi(api_client)
    allow_team_access = True # bool | allowTeamAccess (optional)
description = 'description_example' # str | description (optional)
email_address = 'email_address_example' # str | emailAddress (optional)
expires_at = '2013-10-20T19:20:30+01:00' # datetime | expiresAt (optional)
expires_in = 56 # int | expiresIn (optional)
favourite = True # bool | favourite (optional)
inbox_type = 'inbox_type_example' # str | inboxType (optional)
name = 'name_example' # str | name (optional)
tags = ['tags_example'] # list[str] | tags (optional)
use_domain_pool = True # bool | useDomainPool (optional)

    try:
        # Create new random inbox
        api_response = api_instance.create_new_email_address(allow_team_access=allow_team_access, description=description, email_address=email_address, expires_at=expires_at, expires_in=expires_in, favourite=favourite, inbox_type=inbox_type, name=name, tags=tags, use_domain_pool=use_domain_pool)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommonActionsControllerApi->create_new_email_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_team_access** | **bool**| allowTeamAccess | [optional] 
 **description** | **str**| description | [optional] 
 **email_address** | **str**| emailAddress | [optional] 
 **expires_at** | **datetime**| expiresAt | [optional] 
 **expires_in** | **int**| expiresIn | [optional] 
 **favourite** | **bool**| favourite | [optional] 
 **inbox_type** | **str**| inboxType | [optional] 
 **name** | **str**| name | [optional] 
 **tags** | [**list[str]**](str)| tags | [optional] 
 **use_domain_pool** | **bool**| useDomainPool | [optional] 

### Return type

[**Inbox**](Inbox)

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

# **create_new_email_address1**
> Inbox create_new_email_address1(allow_team_access=allow_team_access, description=description, email_address=email_address, expires_at=expires_at, expires_in=expires_in, favourite=favourite, inbox_type=inbox_type, name=name, tags=tags, use_domain_pool=use_domain_pool)

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
    api_instance = mailslurp_client.CommonActionsControllerApi(api_client)
    allow_team_access = True # bool | allowTeamAccess (optional)
description = 'description_example' # str | description (optional)
email_address = 'email_address_example' # str | emailAddress (optional)
expires_at = '2013-10-20T19:20:30+01:00' # datetime | expiresAt (optional)
expires_in = 56 # int | expiresIn (optional)
favourite = True # bool | favourite (optional)
inbox_type = 'inbox_type_example' # str | inboxType (optional)
name = 'name_example' # str | name (optional)
tags = ['tags_example'] # list[str] | tags (optional)
use_domain_pool = True # bool | useDomainPool (optional)

    try:
        # Create new random inbox
        api_response = api_instance.create_new_email_address1(allow_team_access=allow_team_access, description=description, email_address=email_address, expires_at=expires_at, expires_in=expires_in, favourite=favourite, inbox_type=inbox_type, name=name, tags=tags, use_domain_pool=use_domain_pool)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommonActionsControllerApi->create_new_email_address1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_team_access** | **bool**| allowTeamAccess | [optional] 
 **description** | **str**| description | [optional] 
 **email_address** | **str**| emailAddress | [optional] 
 **expires_at** | **datetime**| expiresAt | [optional] 
 **expires_in** | **int**| expiresIn | [optional] 
 **favourite** | **bool**| favourite | [optional] 
 **inbox_type** | **str**| inboxType | [optional] 
 **name** | **str**| name | [optional] 
 **tags** | [**list[str]**](str)| tags | [optional] 
 **use_domain_pool** | **bool**| useDomainPool | [optional] 

### Return type

[**Inbox**](Inbox)

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
 **inbox_id** | [**str**]()| inboxId | 

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

# **send_email_simple**
> send_email_simple(email_options)

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
    api_instance = mailslurp_client.CommonActionsControllerApi(api_client)
    email_options = mailslurp_client.SimpleSendEmailOptions() # SimpleSendEmailOptions | emailOptions

    try:
        # Send an email
        api_instance.send_email_simple(email_options)
    except ApiException as e:
        print("Exception when calling CommonActionsControllerApi->send_email_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_options** | [**SimpleSendEmailOptions**](SimpleSendEmailOptions)| emailOptions | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

