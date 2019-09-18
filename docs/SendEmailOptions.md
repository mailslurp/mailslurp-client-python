# SendEmailOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | **list[str]** | Optional list of attachment IDs to send with this email. You must first upload each attachment separately in order to obtain attachment IDs | [optional] 
**bcc** | **list[str]** | Optional list of bcc destination email addresses | [optional] 
**body** | **str** | Contents of email. If HTML set isHTML to true. You can use moustache templates here if you provide a templateVariables option | [optional] 
**cc** | **list[str]** | Optional list of cc destination email addresses | [optional] 
**charset** | **str** | Optional charset | [optional] 
**_from** | **str** | Optional from address. If not set source inbox address will be used | [optional] 
**html** | **bool** |  | [optional] 
**reply_to** | **str** | Optional replyTo header | [optional] 
**subject** | **str** | Optional email subject line | [optional] 
**template_variables** | [**object**](.md) | Optional map of template variables. Will replace moustache syntax variables in subject or body with the associated values | [optional] 
**to** | **list[str]** | List of destination email addresses. Even single recipients must be in array form. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


