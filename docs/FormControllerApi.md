# mailslurp_client.FormControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_form**](FormControllerApi.md#submit_form) | **POST** /forms | Submit a form to be parsed and sent as an email to an address determined by the form fields


# **submit_form**
> str submit_form(email_address=email_address, redirect_to=redirect_to, spam_check=spam_check, subject=subject, success_message=success_message, to=to, to_alias=to_alias, other_parameters=other_parameters)

Submit a form to be parsed and sent as an email to an address determined by the form fields

This endpoint allows you to submit HTML forms and receive the field values and files via email.   #### Parameters The endpoint looks for special meta parameters in the form fields OR in the URL request parameters. The meta parameters can be used to specify the behaviour of the email.   You must provide at-least a `_to` email address or a `_toAlias` email alias ID to tell the endpoint where the form should be emailed. These can be submitted as hidden HTML input fields with the corresponding `name` attributes or as URL query parameters such as `?_to=test@example.com`  The endpoint takes all other form fields that are named and includes them in the message body of the email. Files are sent as attachments.  #### Submitting This endpoint accepts form submission via POST method. It accepts `application/x-www-form-urlencoded`, and `multipart/form-data` content-types.  #### HTML Example ```html <form    action=\"https://api.mailslurp.com/forms\"   method=\"post\" >   <input name=\"_to\" type=\"hidden\" value=\"test@example.com\"/>   <textarea name=\"feedback\"></textarea>   <button type=\"submit\">Submit</button> </form> ```  #### URL Example ```html <form    action=\"https://api.mailslurp.com/forms?_toAlias=test@example.com\"   method=\"post\" >   <textarea name=\"feedback\"></textarea>   <button type=\"submit\">Submit</button> </form> ```    The email address is specified by a `_to` field OR is extracted from an email alias specified by a `_toAlias` field (see the alias controller for more information).  Endpoint accepts .  You can specify a content type in HTML forms using the `enctype` attribute, for instance: `<form enctype=\"multipart/form-data\">`.  

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
    api_instance = mailslurp_client.FormControllerApi(api_client)
    email_address = 'email_address_example' # str | Email address of the submitting user. Include this if you wish to record the submitters email address and reply to it later. (optional)
redirect_to = 'redirect_to_example' # str | Optional URL to redirect form submitter to after submission. If not present user will see a success message. (optional)
spam_check = 'spam_check_example' # str | Optional but recommended field that catches spammers out. Include as a hidden form field but LEAVE EMPTY. Spam-bots will usually fill every field. If the _spamCheck field is filled the form submission will be ignored. (optional)
subject = 'subject_example' # str | Optional subject of the email that will be sent. (optional)
success_message = 'success_message_example' # str | Optional success message to display if no _redirectTo present. (optional)
to = 'to_example' # str | The email address that submitted form should be sent to. Either this or _toAlias must be present for a form to be successfully submitted.. (optional)
to_alias = 'to_alias_example' # str | ID of an email alias to that form should be sent to. Aliases must be created before submission and can be used to hide an email address and reduce spam. (optional)
other_parameters = 'other_parameters_example' # str | All other parameters or fields will be accepted and attached to the sent email. This includes files and any HTML form field with a name. These fields will become the body of the email that is sent. (optional)

    try:
        # Submit a form to be parsed and sent as an email to an address determined by the form fields
        api_response = api_instance.submit_form(email_address=email_address, redirect_to=redirect_to, spam_check=spam_check, subject=subject, success_message=success_message, to=to, to_alias=to_alias, other_parameters=other_parameters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormControllerApi->submit_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | **str**| Email address of the submitting user. Include this if you wish to record the submitters email address and reply to it later. | [optional] 
 **redirect_to** | **str**| Optional URL to redirect form submitter to after submission. If not present user will see a success message. | [optional] 
 **spam_check** | **str**| Optional but recommended field that catches spammers out. Include as a hidden form field but LEAVE EMPTY. Spam-bots will usually fill every field. If the _spamCheck field is filled the form submission will be ignored. | [optional] 
 **subject** | **str**| Optional subject of the email that will be sent. | [optional] 
 **success_message** | **str**| Optional success message to display if no _redirectTo present. | [optional] 
 **to** | **str**| The email address that submitted form should be sent to. Either this or _toAlias must be present for a form to be successfully submitted.. | [optional] 
 **to_alias** | **str**| ID of an email alias to that form should be sent to. Aliases must be created before submission and can be used to hide an email address and reduce spam. | [optional] 
 **other_parameters** | **str**| All other parameters or fields will be accepted and attached to the sent email. This includes files and any HTML form field with a name. These fields will become the body of the email that is sent. | [optional] 

### Return type

**str**

### Authorization

[API_KEY](../README.md#API_KEY)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
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

