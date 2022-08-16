# WebhookNewSmsPayload

NEW_SMS webhook payload. Sent to your webhook url endpoint via HTTP POST when an sms is received by the phone number that your webhook is attached to. Use the SMS ID to fetch the full SMS details.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Idempotent message ID. Store this ID locally or in a database to prevent message duplication. | 
**webhook_id** | **str** | ID of webhook entity being triggered | 
**event_name** | **str** | Name of the event type webhook is being triggered for. | 
**webhook_name** | **str** | Name of the webhook being triggered | [optional] 
**sms_id** | **str** | ID of SMS message | 
**user_id** | **str** | User ID of event | 
**phone_number** | **str** | ID of phone number receiving SMS | 
**to_number** | **str** | Recipient phone number | 
**from_number** | **str** | Sender phone number | 
**body** | **str** | SMS message body | 
**read** | **bool** | SMS has been read | 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


