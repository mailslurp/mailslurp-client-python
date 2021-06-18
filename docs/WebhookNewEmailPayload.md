# WebhookNewEmailPayload

NEW_EMAIL webhook payload
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_meta_datas** | [**list[AttachmentMetaData]**](AttachmentMetaData) | List of attachment meta data objects if attachments present | [optional] 
**bcc** | **list[str]** | List of &#x60;BCC&#x60; recipients email was addressed to | [optional] 
**cc** | **list[str]** | List of &#x60;CC&#x60; recipients email was addressed to | [optional] 
**created_at** | **datetime** | Date time of event creation | [optional] 
**email_id** | **str** | ID of the email that was received. Use this ID for fetching the email with the &#x60;EmailController&#x60;. | [optional] 
**event_name** | **str** | Name of the event type webhook is being triggered for. | [optional] 
**_from** | **str** | Who the email was sent from | [optional] 
**inbox_id** | **str** | Id of the inbox that received an email | [optional] 
**message_id** | **str** | Idempotent message ID. Store this ID locally or in a database to prevent message duplication. | [optional] 
**subject** | **str** | The subject line of the email message | [optional] 
**to** | **list[str]** | List of &#x60;To&#x60; recipients that email was addressed to | [optional] 
**webhook_id** | **str** | ID of webhook entity being triggered | [optional] 
**webhook_name** | **str** | Name of the webhook being triggered | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


