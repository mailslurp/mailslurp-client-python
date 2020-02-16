# EmailPreview

Preview of an email message. For full message call the email endpoints with the provided email id.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | **list[str]** | List of IDs of attachments found in the email. Use these IDs with the Inbox and Email Controllers to download attachments and attachment meta data such as filesize, name, extension. | [optional] 
**bcc** | **list[str]** | List of &#x60;BCC&#x60; recipients email was addressed to | [optional] 
**cc** | **list[str]** | List of &#x60;CC&#x60; recipients email was addressed to | [optional] 
**created_at** | **datetime** | When was the email received by MailSlurp | [optional] 
**id** | **str** | ID of the email | [optional] 
**read** | **bool** | Has the email been viewed ever | [optional] 
**subject** | **str** | The subject line of the email message | [optional] 
**to** | **list[str]** | List of &#x60;To&#x60; recipients email was addressed to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


