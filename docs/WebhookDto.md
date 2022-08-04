# WebhookDto

Representation of a webhook for an inbox. The URL specified will be using by MailSlurp whenever an email is received by the attached inbox. A webhook entity should have a URL that points to your server. Your server should accept HTTP/S POST requests and return a success 200. MailSlurp will retry your webhooks if they fail. See https://python.api.mailslurp.com/schemas/webhook-payload for the payload schema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the Webhook | 
**user_id** | **str** | User ID of the Webhook | 
**basic_auth** | **bool** | Does webhook expect basic authentication? If true it means you created this webhook with a username and password. MailSlurp will use these in the URL to authenticate itself. | 
**name** | **str** | Name of the webhook | [optional] 
**inbox_id** | **str** | The inbox that the Webhook will be triggered by. If null then webhook triggered at account level | [optional] 
**url** | **str** | URL of your server that the webhook will be sent to. The schema of the JSON that is sent is described by the payloadJsonSchema. | 
**method** | **str** | HTTP method that your server endpoint must listen for | 
**payload_json_schema** | **str** | Deprecated. Fetch JSON Schema for webhook using the getJsonSchemaForWebhookPayload method | 
**created_at** | **datetime** | When the webhook was created | 
**updated_at** | **datetime** |  | 
**event_name** | **str** | Webhook trigger event name | [optional] 
**request_headers** | [**WebhookHeaders**](WebhookHeaders) |  | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


