# WebhookNewContactPayload

NEW_CONTACT webhook payload. Sent to your webhook url endpoint via HTTP POST when an email is received by the inbox that your webhook is attached to that contains a recipient that has not been saved as a contact.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Idempotent message ID. Store this ID locally or in a database to prevent message duplication. | 
**webhook_id** | **str** | ID of webhook entity being triggered | 
**webhook_name** | **str** | Name of the webhook being triggered | [optional] 
**event_name** | **str** | Name of the event type webhook is being triggered for. | 
**contact_id** | **str** | Contact ID | 
**group_id** | **str** | Contact group ID | [optional] 
**first_name** | **str** | Contact first name | [optional] 
**last_name** | **str** | Contact last name | [optional] 
**company** | **str** | Contact company name | [optional] 
**primary_email_address** | **str** | Primary email address for contact | [optional] 
**email_addresses** | **list[str]** | Email addresses for contact | 
**tags** | **list[str]** | Tags for contact | 
**meta_data** | [**object**]() |  | [optional] 
**opt_out** | **bool** | Has contact opted out of emails | 
**created_at** | **datetime** | Date time of event creation | 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


