# WebhookNewAttachmentPayload

NEW_ATTACHMENT webhook payload. Sent to your webhook url endpoint via HTTP POST when an email is received by the inbox that your webhook is attached to that contains an attachment. You can use the attachmentId to download the attachment.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Idempotent message ID. Store this ID locally or in a database to prevent message duplication. | 
**webhook_id** | **str** | ID of webhook entity being triggered | 
**webhook_name** | **str** | Name of the webhook being triggered | [optional] 
**event_name** | **str** | Name of the event type webhook is being triggered for. | 
**attachment_id** | **str** | ID of attachment. Use the &#x60;AttachmentController&#x60; to | 
**name** | **str** | Filename of the attachment if present | 
**content_type** | **str** | Content type of attachment such as &#39;image/png&#39; or &#39;application/pdf | 
**content_length** | **int** | Size of attachment in bytes | 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


