# ReplyToAliasEmailOptions

Options for replying to an alias email using the alias inbox
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | **list[str]** | List of uploaded attachments to send with the reply. Optional. | [optional] 
**body** | **str** | Body of the reply email you want to send | [optional] 
**charset** | **str** | The charset that your message should be sent with. Optional. Default is UTF-8 | [optional] 
**is_html** | **bool** | Is the reply HTML | [optional] 
**send_strategy** | **str** | When to send the email. Typically immediately | [optional] 
**template** | **str** | Template ID to use instead of body. Will use template variable map to fill defined variable slots. | [optional] 
**template_variables** | [**object**]() | Template variables if using a template | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


