# SentEmailDto

Sent email details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of sent email | 
**user_id** | **str** | User ID | 
**inbox_id** | **str** | Inbox ID email was sent from | 
**domain_id** | **str** | Domain ID | [optional] 
**to** | **list[str]** | Recipients email was sent to | [optional] 
**_from** | **str** |  | [optional] 
**reply_to** | **str** |  | [optional] 
**cc** | **list[str]** |  | [optional] 
**bcc** | **list[str]** |  | [optional] 
**attachments** | **list[str]** | Array of IDs of attachments that were sent with this email | [optional] 
**subject** | **str** |  | [optional] 
**body_md5_hash** | **str** | MD5 Hash | [optional] 
**body** | **str** |  | [optional] 
**to_contacts** | **list[str]** |  | [optional] 
**to_group** | **str** |  | [optional] 
**charset** | **str** |  | [optional] 
**is_html** | **bool** |  | [optional] 
**sent_at** | **datetime** |  | 
**pixel_ids** | **list[str]** |  | [optional] 
**message_id** | **str** |  | [optional] 
**message_ids** | **list[str]** |  | [optional] 
**virtual_send** | **bool** |  | [optional] 
**template_id** | **str** |  | [optional] 
**template_variables** | **dict(str, object)** |  | [optional] 
**html** | **bool** |  | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


