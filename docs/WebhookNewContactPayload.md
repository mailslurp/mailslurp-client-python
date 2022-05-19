# WebhookNewContactPayload

NEW_CONTACT webhook payload. Sent to your webhook url endpoint via HTTP POST when an email is received by the inbox that your webhook is attached to that contains a recipient that has not been saved as a contact.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Idempotent message ID. Store this ID locally or in a database to prevent message duplication. | 
**webhook_id** | **str** | ID of webhook entity being triggered | 
**webhook_name** | **str** | Name of the webhook being triggered | [optional] 
**event_name** | **str** | Name of the event type webhook is being triggered for. | 
**contact_id** | **str** |  | 
**group_id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**primary_email_address** | **str** |  | [optional] 
**email_addresses** | **list[str]** |  | 
**tags** | **list[str]** |  | 
**meta_data** | [**object**]() |  | [optional] 
**opt_out** | **bool** |  | [optional] 
**created_at** | **datetime** |  | 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


