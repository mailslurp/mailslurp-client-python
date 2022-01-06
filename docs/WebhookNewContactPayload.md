# WebhookNewContactPayload

NEW_CONTACT webhook payload. Sent to your webhook url endpoint via HTTP POST when an email is received by the inbox that your webhook is attached to that contains a recipient that has not been saved as a contact.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Idempotent message ID. Store this ID locally or in a database to prevent message duplication. | [optional] 
**webhook_id** | **str** | ID of webhook entity being triggered | [optional] 
**webhook_name** | **str** | Name of the webhook being triggered | [optional] 
**event_name** | **str** | Name of the event type webhook is being triggered for. | [optional] 
**contact_id** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**primary_email_address** | **str** |  | [optional] 
**email_addresses** | **list[str]** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**meta_data** | [**object**]() |  | [optional] 
**opt_out** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


