# EmailPreview

Preview of an email message. For full message (including body and attachments) call the `getEmail` or other email endpoints with the provided email ID.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | **list[str]** | List of IDs of attachments found in the email. Use these IDs with the Inbox and Email Controllers to download attachments and attachment meta data such as filesize, name, extension. | [optional] 
**bcc** | **list[str]** | List of &#x60;BCC&#x60; recipients email was addressed to | [optional] 
**cc** | **list[str]** | List of &#x60;CC&#x60; recipients email was addressed to | [optional] 
**created_at** | **datetime** | When was the email received by MailSlurp | [optional] 
**_from** | **str** | Who the email was sent from | [optional] 
**id** | **str** | ID of the email | [optional] 
**read** | **bool** | Has the email been viewed ever. This means viewed in the dashboard or requested via the full email entity endpoints | [optional] 
**subject** | **str** | The subject line of the email message | [optional] 
**to** | **list[str]** | List of &#x60;To&#x60; recipients email was addressed to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


