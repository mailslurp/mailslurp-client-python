# mailslurp_client.CommonOperationsApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_email_address**](CommonOperationsApi.md#create_new_email_address) | **POST** /newEmailAddress | Create new email address
[**send_email_simple**](CommonOperationsApi.md#send_email_simple) | **POST** /sendEmail | Send an email from a random email address
[**wait_for_latest_email**](CommonOperationsApi.md#wait_for_latest_email) | **GET** /fetchLatestEmail | Fetch inbox&#39;s latest email or if empty wait for email to arrive


# **create_new_email_address**
> Inbox create_new_email_address()

Create new email address

Returns an Inbox with an `id` and an `emailAddress`

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
api_instance = mailslurp_client.CommonOperationsApi(mailslurp_client.ApiClient(configuration))

try:
    # Create new email address
    api_response = api_instance.create_new_email_address()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonOperationsApi->create_new_email_address: %s\n" % e)
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

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = mailslurp_client.CommonOperationsApi(mailslurp_client.ApiClient(configuration))
send_email_options = mailslurp_client.SendEmailOptions() # SendEmailOptions | sendEmailOptions

try:
    # Send an email from a random email address
    api_instance.send_email_simple(send_email_options)
except ApiException as e:
    print("Exception when calling CommonOperationsApi->send_email_simple: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wait_for_latest_email**
> Email wait_for_latest_email(inbox_email_address=inbox_email_address, inbox_id=inbox_id)

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

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = mailslurp_client.CommonOperationsApi(mailslurp_client.ApiClient(configuration))
inbox_email_address = 'inbox_email_address_example' # str | Email address of the inbox we are fetching emails from (optional)
inbox_id = 'inbox_id_example' # str | Id of the inbox we are fetching emails from (optional)

try:
    # Fetch inbox's latest email or if empty wait for email to arrive
    api_response = api_instance.wait_for_latest_email(inbox_email_address=inbox_email_address, inbox_id=inbox_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonOperationsApi->wait_for_latest_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_email_address** | **str**| Email address of the inbox we are fetching emails from | [optional] 
 **inbox_id** | [**str**](.md)| Id of the inbox we are fetching emails from | [optional] 

### Return type

[**Email**](Email.md)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

