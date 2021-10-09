# mailslurp_client.TrackingControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tracking_pixel**](TrackingControllerApi#create_tracking_pixel) | **POST** /tracking/pixels | Create tracking pixel
[**get_all_tracking_pixels**](TrackingControllerApi#get_all_tracking_pixels) | **GET** /tracking/pixels | Get tracking pixels
[**get_tracking_pixel**](TrackingControllerApi#get_tracking_pixel) | **GET** /tracking/pixels/{id} | Get pixel


# **create_tracking_pixel**
> TrackingPixelDto create_tracking_pixel(create_tracking_pixel_options)

Create tracking pixel

Create a tracking pixel. A tracking pixel is an image that can be embedded in an email. When the email is viewed and the image is seen MailSlurp will mark the pixel as seen. Use tracking pixels to monitor email open events. You can receive open notifications via webhook or by fetching the pixel.

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
    api_instance = mailslurp_client.TrackingControllerApi(api_client)
    create_tracking_pixel_options = mailslurp_client.CreateTrackingPixelOptions() # CreateTrackingPixelOptions | createTrackingPixelOptions

    try:
        # Create tracking pixel
        api_response = api_instance.create_tracking_pixel(create_tracking_pixel_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TrackingControllerApi->create_tracking_pixel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tracking_pixel_options** | [**CreateTrackingPixelOptions**](CreateTrackingPixelOptions)| createTrackingPixelOptions | 

### Return type

[**TrackingPixelDto**](TrackingPixelDto)

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

# **get_all_tracking_pixels**
> PageTrackingPixelProjection get_all_tracking_pixels(before=before, page=page, search_filter=search_filter, since=since, size=size, sort=sort)

Get tracking pixels

List tracking pixels in paginated form

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
    api_instance = mailslurp_client.TrackingControllerApi(api_client)
    before = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at before the given timestamp (optional)
page = 0 # int | Optional page index in list pagination (optional) (default to 0)
search_filter = 'search_filter_example' # str | Optional search filter (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter by created at after the given timestamp (optional)
size = 20 # int | Optional page size in list pagination (optional) (default to 20)
sort = 'ASC' # str | Optional createdAt sort direction ASC or DESC (optional) (default to 'ASC')

    try:
        # Get tracking pixels
        api_response = api_instance.get_all_tracking_pixels(before=before, page=page, search_filter=search_filter, since=since, size=size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TrackingControllerApi->get_all_tracking_pixels: %s\n" % e)
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

### Return type

[**PageTrackingPixelProjection**](PageTrackingPixelProjection)

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

# **get_tracking_pixel**
> TrackingPixelDto get_tracking_pixel(id)

Get pixel

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
    api_instance = mailslurp_client.TrackingControllerApi(api_client)
    id = 'id_example' # str | id

    try:
        # Get pixel
        api_response = api_instance.get_tracking_pixel(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TrackingControllerApi->get_tracking_pixel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**]()| id | 

### Return type

[**TrackingPixelDto**](TrackingPixelDto)

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

