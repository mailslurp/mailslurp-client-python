# EmailProjection

A compact representation of a full email. Used in list endpoints to keep response sizes low. Body and attachments are not included. To get all fields of the email use the `getEmail` method with the email projection's ID. See `EmailDto` for documentation on projection properties.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**_from** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**inbox_id** | **str** |  | 
**to** | **list[str]** |  | 
**attachments** | **list[str]** |  | [optional] 
**created_at** | **datetime** |  | 
**bcc** | **list[str]** |  | [optional] 
**cc** | **list[str]** |  | [optional] 
**team_access** | **bool** |  | [optional] 
**read** | **bool** |  | [optional] 
**body_md5_hash** | **str** |  | [optional] 
**body_excerpt** | **str** |  | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


