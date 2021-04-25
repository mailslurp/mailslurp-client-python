# WebhookDto

Representation of a webhook for an inbox. The URL specified will be using by MailSlurp whenever an email is received by the attached inbox.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_auth** | **bool** | Does webhook expect basic authentication? If true it means you created this webhook with a username and password. MailSlurp will use these in the URL to authenticate itself. | [optional] 
**created_at** | **datetime** | When the webhook was created | [optional] 
**id** | **str** | ID of the Webhook | [optional] 
**inbox_id** | **str** | The inbox that the Webhook will be triggered by | [optional] 
**method** | **str** | HTTP method that your server endpoint must listen for | [optional] 
**name** | **str** | Name of the webhook | [optional] 
**payload_json_schema** | **str** | JSON Schema for the payload that will be sent to your URL via the HTTP method described. | [optional] 
**updated_at** | **datetime** |  | 
**url** | **str** | URL of your server that the webhook will be sent to. The schema of the JSON that is sent is described by the payloadJsonSchema. | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


