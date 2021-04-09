# CreateWebhookOptions

Options for creating a webhook. Webhooks can be attached to inboxes and MailSlurp will POST a webhook payload to the URL specified whenever the inbox receives an email. Webhooks are great for processing many inbound emails.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_auth** | [**BasicAuthOptions**](BasicAuthOptions.md) |  | [optional] 
**name** | **str** | Optional name for the webhook | [optional] 
**url** | **str** | Public URL on your server that MailSlurp can post WebhookNotification payload to when an email is received. The payload of the submitted JSON is described by https://api.mailslurp.com/schemas/webhook-payload | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


