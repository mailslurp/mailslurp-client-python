# WebhookNewAttachmentPayload

NEW_ATTACHMENT webhook payload
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_id** | **str** | ID of attachment. Use the &#x60;AttachmentController&#x60; to | [optional] 
**content_length** | **int** | Size of attachment in bytes | [optional] 
**content_type** | **str** | Content type of attachment such as &#39;image/png&#39; or &#39;application/pdf | [optional] 
**event_name** | **str** | Name of the event type webhook is being triggered for. | [optional] 
**message_id** | **str** | Idempotent message ID. Store this ID locally or in a database to prevent message duplication. | [optional] 
**name** | **str** | Filename of the attachment if present | [optional] 
**webhook_id** | **str** | ID of webhook entity being triggered | [optional] 
**webhook_name** | **str** | Name of the webhook being triggered | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


