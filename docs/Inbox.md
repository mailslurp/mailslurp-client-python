# Inbox

Representation of an inbox with an email address. Emails can be sent to or from this email address.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | When was the inbox created | [optional] 
**description** | **str** | Optional description of an inbox for labelling purposes | [optional] 
**email_address** | **str** | The inbox&#39;s email address. Send an email to this address and the inbox will receive and store it for you. To retrieve the email use the Inbox and Email Controller endpoints. | [optional] 
**expires_at** | **datetime** | When, if ever, will the inbox expire and be deleted. If null then this inbox is permanent and the emails in it won&#39;t be deleted. | [optional] 
**favourite** | **bool** | Is the inbox favourited | [optional] 
**id** | **str** | ID of the inbox | [optional] 
**name** | **str** | Optional name of the inbox. Displayed in the dashboard for easier search | [optional] 
**tags** | **list[str]** | Tags that inbox has been tagged with | [optional] 
**user_id** | **str** | ID of user that inbox belongs to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


