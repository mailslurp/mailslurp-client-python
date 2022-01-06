# WebhookNewEmailPayload

NEW_EMAIL webhook payload. Sent to your webhook url endpoint via HTTP POST when an email is received by the inbox that your webhook is attached to. Use the email ID to fetch the full email body or attachments.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Idempotent message ID. Store this ID locally or in a database to prevent message duplication. | [optional] 
**webhook_id** | **str** | ID of webhook entity being triggered | [optional] 
**event_name** | **str** | Name of the event type webhook is being triggered for. | [optional] 
**webhook_name** | **str** | Name of the webhook being triggered | [optional] 
**inbox_id** | **str** | Id of the inbox that received an email | [optional] 
**email_id** | **str** | ID of the email that was received. Use this ID for fetching the email with the &#x60;EmailController&#x60;. | [optional] 
**created_at** | **datetime** | Date time of event creation | [optional] 
**to** | **list[str]** | List of &#x60;To&#x60; recipient email addresses that the email was addressed to. See recipients object for names. | [optional] 
**_from** | **str** | Who the email was sent from. An email address - see fromName for the sender name. | [optional] 
**cc** | **list[str]** | List of &#x60;CC&#x60; recipients email addresses that the email was addressed to. See recipients object for names. | [optional] 
**bcc** | **list[str]** | List of &#x60;BCC&#x60; recipients email addresses that the email was addressed to. See recipients object for names. | [optional] 
**subject** | **str** | The subject line of the email message as specified by SMTP subject header | [optional] 
**attachment_meta_datas** | [**list[AttachmentMetaData]**](AttachmentMetaData) | List of attachment meta data objects if attachments present | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


