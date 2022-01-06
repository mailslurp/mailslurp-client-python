# WebhookEmailOpenedPayload

EMAIL_OPENED webhook payload. Sent to your webhook url endpoint via HTTP POST when an email containing a tracking pixel is opened and the pixel image is loaded by a reader.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Idempotent message ID. Store this ID locally or in a database to prevent message duplication. | [optional] 
**webhook_id** | **str** | ID of webhook entity being triggered | [optional] 
**event_name** | **str** | Name of the event type webhook is being triggered for. | [optional] 
**webhook_name** | **str** | Name of the webhook being triggered | [optional] 
**inbox_id** | **str** | Id of the inbox that received an email | [optional] 
**pixel_id** | **str** | ID of the tracking pixel | [optional] 
**sent_email_id** | **str** | ID of sent email | [optional] 
**recipient** | **str** | Email address for the recipient of the tracking pixel | [optional] 
**created_at** | **datetime** | Date time of event creation | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


