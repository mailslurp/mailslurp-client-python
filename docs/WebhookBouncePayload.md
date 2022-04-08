# WebhookBouncePayload

EMAIL_READ webhook payload. Sent to your webhook url endpoint via HTTP POST when an email is read. This happens when an email is requested in full from the API or a user views the email in the dashboard.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Idempotent message ID. Store this ID locally or in a database to prevent message duplication. | 
**webhook_id** | **str** | ID of webhook entity being triggered | 
**event_name** | **str** | Name of the event type webhook is being triggered for. | 
**webhook_name** | **str** | Name of the webhook being triggered | [optional] 
**bounce_id** | **str** | ID of the bounce email record. Use the ID with the bounce controller to view more information | 
**sent_to_recipients** | **list[str]** |  | [optional] 
**sender** | **str** |  | 
**bounce_recipients** | **list[str]** | Email addresses that resulted in a bounce or email being rejected. Please save these recipients and avoid emailing them in the future to maintain your reputation. | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


