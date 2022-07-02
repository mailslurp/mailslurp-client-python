# WebhookBounceRecipientPayload

BOUNCE_RECIPIENT webhook payload. Sent to your webhook url endpoint via HTTP POST when an email caused a bounce to occur for a recipient. Save the recipient to a ban list of your server and avoid email them again.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Idempotent message ID. Store this ID locally or in a database to prevent message duplication. | 
**webhook_id** | **str** | ID of webhook entity being triggered | 
**event_name** | **str** | Name of the event type webhook is being triggered for. | 
**webhook_name** | **str** | Name of the webhook being triggered | [optional] 
**recipient** | **str** | Email address that caused a bounce. Make note of the address and try not to message it again to preserve your reputation. | 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


