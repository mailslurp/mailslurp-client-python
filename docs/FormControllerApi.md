# mailslurp_client.FormControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_form**](FormControllerApi#submit_form) | **POST** /forms | Submit a form to be parsed and sent as an email to an address determined by the form fields


# **submit_form**
> str submit_form(to=to, subject=subject, redirect_to=redirect_to, email_address=email_address, success_message=success_message, spam_check=spam_check, other_parameters=other_parameters)

Submit a form to be parsed and sent as an email to an address determined by the form fields

This endpoint allows you to submit HTML forms and receive the field values and files via email.   #### Parameters The endpoint looks for special meta parameters in the form fields OR in the URL request parameters. The meta parameters can be used to specify the behaviour of the email.   You must provide at-least a `_to` email address to tell the endpoint where the form should be emailed. These can be submitted as hidden HTML input fields with the corresponding `name` attributes or as URL query parameters such as `?_to=test@example.com`  The endpoint takes all other form fields that are named and includes them in the message body of the email. Files are sent as attachments.  #### Submitting This endpoint accepts form submission via POST method. It accepts `application/x-www-form-urlencoded`, and `multipart/form-data` content-types.  #### HTML Example ```html <form    action=\"https://api.mailslurp.com/forms\"   method=\"post\" >   <input name=\"_to\" type=\"hidden\" value=\"test@example.com\"/>   <textarea name=\"feedback\"></textarea>   <button type=\"submit\">Submit</button> </form> ```  #### URL Example ```html <form    action=\"https://api.mailslurp.com/forms?_to=test@example.com\"   method=\"post\" >   <textarea name=\"feedback\"></textarea>   <button type=\"submit\">Submit</button> </form> ```    The email address is specified by a `_to` field OR is extracted from an email alias specified by a `_toAlias` field (see the alias controller for more information).  Endpoint accepts .  You can specify a content type in HTML forms using the `enctype` attribute, for instance: `<form enctype=\"multipart/form-data\">`.  

### Example

* Api Key Authentication (API_KEY):
```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = mailslurp_client.Configuration(
    host = "http://localhost:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API_KEY
configuration = mailslurp_client.Configuration(
    host = "http://localhost:8080",
    api_key = {
        'x-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with mailslurp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailslurp_client.FormControllerApi(api_client)
    to = 'test@example.com' # str | The email address that submitted form should be sent to. (optional)
subject = 'My form submission' # str | Optional subject of the email that will be sent. (optional)
redirect_to = 'https://mysite.com/form-success' # str | Optional URL to redirect form submitter to after submission. If not present user will see a success message. (optional)
email_address = 'test@example.com' # str | Email address of the submitting user. Include this if you wish to record the submitters email address and reply to it later. (optional)
success_message = 'Thanks for submitting' # str | Optional success message to display if no _redirectTo present. (optional)
spam_check = 'spam_check_example' # str | Optional but recommended field that catches spammers out. Include as a hidden form field but LEAVE EMPTY. Spam-bots will usually fill every field. If the _spamCheck field is filled the form submission will be ignored. (optional)
other_parameters = 'other_parameters_example' # str | All other parameters or fields will be accepted and attached to the sent email. This includes files and any HTML form field with a name. These fields will become the body of the email that is sent. (optional)

    try:
        # Submit a form to be parsed and sent as an email to an address determined by the form fields
        api_response = api_instance.submit_form(to=to, subject=subject, redirect_to=redirect_to, email_address=email_address, success_message=success_message, spam_check=spam_check, other_parameters=other_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormControllerApi->submit_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to** | **str**| The email address that submitted form should be sent to. | [optional] 
 **subject** | **str**| Optional subject of the email that will be sent. | [optional] 
 **redirect_to** | **str**| Optional URL to redirect form submitter to after submission. If not present user will see a success message. | [optional] 
 **email_address** | **str**| Email address of the submitting user. Include this if you wish to record the submitters email address and reply to it later. | [optional] 
 **success_message** | **str**| Optional success message to display if no _redirectTo present. | [optional] 
 **spam_check** | **str**| Optional but recommended field that catches spammers out. Include as a hidden form field but LEAVE EMPTY. Spam-bots will usually fill every field. If the _spamCheck field is filled the form submission will be ignored. | [optional] 
 **other_parameters** | **str**| All other parameters or fields will be accepted and attached to the sent email. This includes files and any HTML form field with a name. These fields will become the body of the email that is sent. | [optional] 

### Return type

**str**

### Authorization

[API_KEY](../README#API_KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to Model list]](../README#documentation-for-models) [[Back to README]](../README)

