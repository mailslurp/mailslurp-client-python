# WebhookEmailReadPayload

EMAIL_READ webhook payload. Sent to your webhook url endpoint via HTTP POST when an email is read. This happens when an email is requested in full from the API or a user views the email in the dashboard.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Date time of event creation | [optional] 
**email_id** | **str** | ID of the email that was received. Use this ID for fetching the email with the &#x60;EmailController&#x60;. | [optional] 
**email_is_read** | **bool** | Is the email read | [optional] 
**event_name** | **str** | Name of the event type webhook is being triggered for. | [optional] 
**inbox_id** | **str** | Id of the inbox that received an email | [optional] 
**message_id** | **str** | Idempotent message ID. Store this ID locally or in a database to prevent message duplication. | [optional] 
**webhook_id** | **str** | ID of webhook entity being triggered | [optional] 
**webhook_name** | **str** | Name of the webhook being triggered | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


