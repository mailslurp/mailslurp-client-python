# WebhookDeliveryStatusPayload

DELIVERY_STATUS webhook payload. Sent to your webhook url endpoint via HTTP POST when an email delivery status is created. This could be a successful delivery or a delivery failure.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Idempotent message ID. Store this ID locally or in a database to prevent message duplication. | 
**webhook_id** | **str** | ID of webhook entity being triggered | 
**event_name** | **str** | Name of the event type webhook is being triggered for. | 
**webhook_name** | **str** | Name of the webhook being triggered | [optional] 
**id** | **str** | ID of delivery status | 
**user_id** | **str** | User ID of event | 
**sent_id** | **str** | ID of sent email | [optional] 
**remote_mta_ip** | **str** | IP address of the remote Mail Transfer Agent | [optional] 
**inbox_id** | **str** | Id of the inbox | [optional] 
**reporting_mta** | **str** | Mail Transfer Agent reporting delivery status | [optional] 
**recipients** | **list[str]** | Recipients for delivery | [optional] 
**smtp_response** | **str** | SMTP server response message | [optional] 
**smtp_status_code** | **int** | SMTP server status | [optional] 
**processing_time_millis** | **int** | Time in milliseconds for delivery processing | [optional] 
**received** | **datetime** | Time event was received | [optional] 
**subject** | **str** | Email subject | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


