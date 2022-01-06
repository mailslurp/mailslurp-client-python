# SentEmailDto

Sent email details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of sent email | [optional] 
**user_id** | **str** | User ID | [optional] 
**inbox_id** | **str** | Inbox ID email was sent from | [optional] 
**to** | **list[str]** | Recipients email was sent to | [optional] 
**_from** | **str** |  | [optional] 
**reply_to** | **str** |  | [optional] 
**cc** | **list[str]** |  | [optional] 
**bcc** | **list[str]** |  | [optional] 
**attachments** | **list[str]** | Array of IDs of attachments that were sent with this email | [optional] 
**subject** | **str** |  | [optional] 
**body_md5_hash** | **str** | MD5 Hash | [optional] 
**body** | **str** |  | [optional] 
**charset** | **str** |  | [optional] 
**sent_at** | **datetime** |  | [optional] 
**pixel_ids** | **list[str]** |  | [optional] 
**html** | **bool** |  | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


