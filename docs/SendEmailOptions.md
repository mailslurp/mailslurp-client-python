# SendEmailOptions

Options for sending an email message from an inbox. You must provide one of: `to`, `toGroup`, or `toContacts` to send an email. All other parameters are optional.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | **list[str]** | Optional list of attachment IDs to send with this email. You must first upload each attachment separately in order to obtain attachment IDs. This way you can reuse attachments with different emails once uploaded. | [optional] 
**bcc** | **list[str]** | Optional list of bcc destination email addresses | [optional] 
**body** | **str** | Optional contents of email. If body contains HTML then set &#x60;isHTML&#x60; to true to ensure that email clients render it correctly. You can use moustache template syntax in the email body in conjunction with &#x60;toGroup&#x60; contact variables or &#x60;templateVariables&#x60; data. If you need more templating control consider creating a template and using the &#x60;template&#x60; property instead of the body. | [optional] 
**cc** | **list[str]** | Optional list of cc destination email addresses | [optional] 
**charset** | **str** | Optional charset | [optional] 
**_from** | **str** | Optional from address. If not set the source inbox address will be used for this field. Beware of potential spam penalties when setting this field to an address not used by the inbox. For custom email addresses use a custom domain. | [optional] 
**is_html** | **bool** | Optional HTML flag. If true the &#x60;content-type&#x60; of the email will be &#x60;text/html&#x60;. Set to true when sending HTML to ensure proper rending on email clients | [optional] 
**reply_to** | **str** | Optional replyTo header | [optional] 
**send_strategy** | **str** | Optional strategy to use when sending the email | [optional] 
**subject** | **str** | Optional email subject line | [optional] 
**template** | **str** | Optional template ID to use for body. Will override body if provided. When using a template make sure you pass the corresponding map of &#x60;templateVariables&#x60;. You can find which variables are needed by fetching the template itself or viewing it in the dashboard. | [optional] 
**template_variables** | [**object**](.md) | Optional map of template variables. Will replace moustache syntax variables in subject and body or template with the associated values if found. | [optional] 
**to** | **list[str]** | List of destination email addresses. Even single recipients must be in array form. Maximum recipients per email depends on your plan. If you need to send many emails try using contacts or contact groups or use a non standard sendStrategy to ensure that spam filters are not triggered (many recipients in one email can affect your spam rating). | [optional] 
**to_contacts** | **list[str]** | Optional list of contact IDs to send email to. Manage your contacts via the API or dashboard. When contacts are used the email is sent to each contact separately so they will not see other recipients. | [optional] 
**to_group** | **str** | Optional contact group ID to send email to. You can create contacts and contact groups in the API or dashboard and use them for email campaigns. When contact groups are used the email is sent to each contact separately so they will not see other recipients | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


