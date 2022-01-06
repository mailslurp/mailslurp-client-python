# ReplyToEmailOptions

Options for replying to email with API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Body of the reply email you want to send | [optional] 
**_from** | **str** | The from header that should be used. Optional | [optional] 
**reply_to** | **str** | The replyTo header that should be used. Optional | [optional] 
**charset** | **str** | The charset that your message should be sent with. Optional. Default is UTF-8 | [optional] 
**attachments** | **list[str]** | List of uploaded attachments to send with the reply. Optional. | [optional] 
**template_variables** | **dict(str, object)** | Template variables if using a template | [optional] 
**template** | **str** | Template ID to use instead of body. Will use template variable map to fill defined variable slots. | [optional] 
**send_strategy** | **str** | How an email should be sent based on its recipients | [optional] 
**use_inbox_name** | **bool** | Optionally use inbox name as display name for sender email address | [optional] 
**html** | **bool** |  | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


