# EmailProjection

A compact representation of a full email. Used in list endpoints to keep response sizes low. Body and attachments are not included. To get all fields of the email use the `getEmail` method with the email projection's ID. See `EmailDto` for documentation on projection properties.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**_from** | **str** |  | [optional] 
**team_access** | **bool** |  | [optional] 
**read** | **bool** |  | [optional] 
**body_md5_hash** | **str** |  | [optional] 
**body_excerpt** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**inbox_id** | **str** |  | [optional] 
**to** | **list[str]** |  | [optional] 
**attachments** | **list[str]** |  | [optional] 
**bcc** | **list[str]** |  | [optional] 
**cc** | **list[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


