# WebhookNewContactPayload

NEW_CONTACT webhook payload. Sent to your webhook url endpoint via HTTP POST when an email is received by the inbox that your webhook is attached to that contains a recipient that has not been saved as a contact.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | **str** |  | [optional] 
**contact_id** | **str** |  | 
**created_at** | **datetime** |  | 
**email_addresses** | **list[str]** |  | 
**event_name** | **str** | Name of the event type webhook is being triggered for. | [optional] 
**first_name** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**message_id** | **str** | Idempotent message ID. Store this ID locally or in a database to prevent message duplication. | [optional] 
**meta_data** | [**object**]() |  | [optional] 
**opt_out** | **bool** |  | [optional] 
**primary_email_address** | **str** |  | [optional] 
**tags** | **list[str]** |  | 
**webhook_id** | **str** | ID of webhook entity being triggered | [optional] 
**webhook_name** | **str** | Name of the webhook being triggered | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


