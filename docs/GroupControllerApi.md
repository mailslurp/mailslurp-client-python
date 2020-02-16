# mailslurp_client.GroupControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contacts_to_group**](GroupControllerApi.md#add_contacts_to_group) | **PUT** /groups/{groupId}/contacts | Add contacts to a group
[**create_group**](GroupControllerApi.md#create_group) | **POST** /groups | Create a group
[**delete_group**](GroupControllerApi.md#delete_group) | **DELETE** /groups/{groupId} | Delete group
[**get_all_groups**](GroupControllerApi.md#get_all_groups) | **GET** /groups/paginated | Get all Contact Groups in paginated format
[**get_group**](GroupControllerApi.md#get_group) | **GET** /groups/{groupId} | Get group
[**get_group_with_contacts**](GroupControllerApi.md#get_group_with_contacts) | **GET** /groups/{groupId}/contacts | Get group and contacts belonging to it
[**get_groups**](GroupControllerApi.md#get_groups) | **GET** /groups | Get all groups
[**remove_contacts_from_group**](GroupControllerApi.md#remove_contacts_from_group) | **DELETE** /groups/{groupId}/contacts | Remove contacts from a group


# **add_contacts_to_group**
> GroupContactsDto add_contacts_to_group(group_id, update_group_contacts_option)

Add contacts to a group

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
    api_instance = mailslurp_client.GroupControllerApi(api_client)
    group_id = 'group_id_example' # str | groupId
update_group_contacts_option = mailslurp_client.UpdateGroupContacts() # UpdateGroupContacts | updateGroupContactsOption

    try:
        # Add contacts to a group
        api_response = api_instance.add_contacts_to_group(group_id, update_group_contacts_option)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupControllerApi->add_contacts_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)| groupId | 
 **update_group_contacts_option** | [**UpdateGroupContacts**](UpdateGroupContacts.md)| updateGroupContactsOption | 

### Return type

[**GroupContactsDto**](GroupContactsDto.md)

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

# **create_group**
> GroupDto create_group(create_group_options)

Create a group

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
    api_instance = mailslurp_client.GroupControllerApi(api_client)
    create_group_options = mailslurp_client.CreateGroupOptions() # CreateGroupOptions | createGroupOptions

    try:
        # Create a group
        api_response = api_instance.create_group(create_group_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupControllerApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_group_options** | [**CreateGroupOptions**](CreateGroupOptions.md)| createGroupOptions | 

### Return type

[**GroupDto**](GroupDto.md)

### Authorization

[API_KEY](../README.md#API_KEY)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group_id)

Delete group

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
    api_instance = mailslurp_client.GroupControllerApi(api_client)
    group_id = 'group_id_example' # str | groupId

    try:
        # Delete group
        api_instance.delete_group(group_id)
    except ApiException as e:
        print("Exception when calling GroupControllerApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)| groupId | 

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

# **get_all_groups**
> PageGroupProjection get_all_groups(page=page, size=size, sort=sort)

Get all Contact Groups in paginated format

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
    api_instance = mailslurp_client.GroupControllerApi(api_client)
    page = 0 # int | Optional page index in inbox list pagination (optional) (default to 0)
size = 20 # int | Optional page size in inbox list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')

    try:
        # Get all Contact Groups in paginated format
        api_response = api_instance.get_all_groups(page=page, size=size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupControllerApi->get_all_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Optional page index in inbox list pagination | [optional] [default to 0]
 **size** | **int**| Optional page size in inbox list pagination | [optional] [default to 20]
 **sort** | **str**| Optional createdAt sort direction ASC or DESC | [optional] [default to &#39;ASC&#39;]

### Return type

[**PageGroupProjection**](PageGroupProjection.md)

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

# **get_group**
> GroupDto get_group(group_id)

Get group

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
    api_instance = mailslurp_client.GroupControllerApi(api_client)
    group_id = 'group_id_example' # str | groupId

    try:
        # Get group
        api_response = api_instance.get_group(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupControllerApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)| groupId | 

### Return type

[**GroupDto**](GroupDto.md)

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

# **get_group_with_contacts**
> GroupContactsDto get_group_with_contacts(group_id)

Get group and contacts belonging to it

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
    api_instance = mailslurp_client.GroupControllerApi(api_client)
    group_id = 'group_id_example' # str | groupId

    try:
        # Get group and contacts belonging to it
        api_response = api_instance.get_group_with_contacts(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupControllerApi->get_group_with_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)| groupId | 

### Return type

[**GroupContactsDto**](GroupContactsDto.md)

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

# **get_groups**
> list[GroupProjection] get_groups()

Get all groups

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
    api_instance = mailslurp_client.GroupControllerApi(api_client)
    
    try:
        # Get all groups
        api_response = api_instance.get_groups()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupControllerApi->get_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GroupProjection]**](GroupProjection.md)

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

# **remove_contacts_from_group**
> GroupContactsDto remove_contacts_from_group(group_id, update_group_contacts_option)

Remove contacts from a group

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
    api_instance = mailslurp_client.GroupControllerApi(api_client)
    group_id = 'group_id_example' # str | groupId
update_group_contacts_option = mailslurp_client.UpdateGroupContacts() # UpdateGroupContacts | updateGroupContactsOption

    try:
        # Remove contacts from a group
        api_response = api_instance.remove_contacts_from_group(group_id, update_group_contacts_option)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupControllerApi->remove_contacts_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)| groupId | 
 **update_group_contacts_option** | [**UpdateGroupContacts**](UpdateGroupContacts.md)| updateGroupContactsOption | 

### Return type

[**GroupContactsDto**](GroupContactsDto.md)

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

