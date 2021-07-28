# mailslurp_client.BounceControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bounced_email**](BounceControllerApi#get_bounced_email) | **GET** /bounce/emails/{id} | Get a bounced email.
[**get_bounced_emails**](BounceControllerApi#get_bounced_emails) | **GET** /bounce/emails | Get paginated list of bounced emails.
[**get_bounced_recipient**](BounceControllerApi#get_bounced_recipient) | **GET** /bounce/recipients/{id} | Get a bounced email.
[**get_bounced_recipients**](BounceControllerApi#get_bounced_recipients) | **GET** /bounce/recipients | Get paginated list of bounced recipients.


# **get_bounced_email**
> BouncedEmailDto get_bounced_email(id)

Get a bounced email.

Bounced emails are email you have sent that were rejected by a recipient

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
    api_instance = mailslurp_client.BounceControllerApi(api_client)
    id = 'id_example' # str | ID of the bounced email to fetch

    try:
        # Get a bounced email.
        api_response = api_instance.get_bounced_email(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BounceControllerApi->get_bounced_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**]()| ID of the bounced email to fetch | 

### Return type

[**BouncedEmailDto**](BouncedEmailDto)

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

# **get_bounced_emails**
> PageBouncedEmail get_bounced_emails(page=page, size=size, sort=sort)

Get paginated list of bounced emails.

Bounced emails are email you have sent that were rejected by a recipient

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
    api_instance = mailslurp_client.BounceControllerApi(api_client)
    page = 0 # int | Optional page index  (optional) (default to 0)
size = 20 # int | Optional page size  (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')

    try:
        # Get paginated list of bounced emails.
        api_response = api_instance.get_bounced_emails(page=page, size=size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BounceControllerApi->get_bounced_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional page index  | [optional] [default to 0]
 **size** | **int**| Optional page size  | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]

### Return type

[**PageBouncedEmail**](PageBouncedEmail)

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

# **get_bounced_recipient**
> BouncedRecipientDto get_bounced_recipient(id)

Get a bounced email.

Bounced emails are email you have sent that were rejected by a recipient

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
    api_instance = mailslurp_client.BounceControllerApi(api_client)
    id = 'id_example' # str | ID of the bounced recipient

    try:
        # Get a bounced email.
        api_response = api_instance.get_bounced_recipient(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BounceControllerApi->get_bounced_recipient: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**]()| ID of the bounced recipient | 

### Return type

[**BouncedRecipientDto**](BouncedRecipientDto)

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

# **get_bounced_recipients**
> PageBouncedRecipients get_bounced_recipients(page=page, size=size, sort=sort)

Get paginated list of bounced recipients.

Bounced recipients are email addresses that you have sent emails to that did not accept the sent email. Once a recipient is bounced you cannot send emails to that address.

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
    api_instance = mailslurp_client.BounceControllerApi(api_client)
    page = 0 # int | Optional page index  (optional) (default to 0)
size = 20 # int | Optional page size  (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')

    try:
        # Get paginated list of bounced recipients.
        api_response = api_instance.get_bounced_recipients(page=page, size=size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BounceControllerApi->get_bounced_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional page index  | [optional] [default to 0]
 **size** | **int**| Optional page size  | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]

### Return type

[**PageBouncedRecipients**](PageBouncedRecipients)

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

