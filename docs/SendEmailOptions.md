# SendEmailOptions

Options for sending an email message from an inbox. Must supply either list of `to` email addresses or `toGroups` list of Contact Group IDs.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | **list[str]** | Optional list of attachment IDs to send with this email. You must first upload each attachment separately in order to obtain attachment IDs | [optional] 
**bcc** | **list[str]** | Optional list of bcc destination email addresses | [optional] 
**body** | **str** | Contents of email. If body contains HTML then set &#x60;isHTML&#x60; to true. You can use moustache template syntax in the body in conjunction with &#x60;toGroup&#x60; contact variables or &#x60;templateVariables&#x60; data. | [optional] 
**cc** | **list[str]** | Optional list of cc destination email addresses | [optional] 
**charset** | **str** | Optional charset | [optional] 
**_from** | **str** | Optional from address. If not set source inbox address will be used | [optional] 
**is_html** | **bool** | Optional HTML flag. If true the &#x60;content-type&#x60; of the email will be &#x60;text/html&#x60; | [optional] 
**reply_to** | **str** | Optional replyTo header | [optional] 
**subject** | **str** | Optional email subject line | [optional] 
**template** | **str** | Optional template ID to use for body. Will override body if provided | [optional] 
**template_variables** | [**object**](.md) | Optional map of template variables. Will replace moustache syntax variables in subject and body or template with the associated values | [optional] 
**to** | **list[str]** | List of destination email addresses. Even single recipients must be in array form. Max 100 recipients. | [optional] 
**to_contacts** | **list[str]** | Optional list of contact IDs to send email to | [optional] 
**to_group** | **str** | Optional contact group ID to send email to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


