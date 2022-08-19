# AliasDto

Email alias representation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email_address** | **str** | The alias&#39;s email address for receiving email | 
**masked_email_address** | **str** | The underlying email address that is hidden and will received forwarded email | [optional] 
**user_id** | **str** |  | 
**inbox_id** | **str** | Inbox that is associated with the alias | 
**name** | **str** |  | [optional] 
**use_threads** | **bool** | If alias will generate response threads or not when email are received by it | [optional] 
**is_verified** | **bool** | Has the alias been verified. You must verify an alias if the masked email address has not yet been verified by your account | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


