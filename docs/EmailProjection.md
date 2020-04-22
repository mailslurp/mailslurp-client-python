# EmailProjection

A compact representation of a full email. Used in list endpoints to keep response sizes low. Body and attachments are not included. To get all fields of the email use the `getEmail` method with the email projection's ID. See `EmailDto` for documentation on projection properties.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | **list[str]** |  | [optional] 
**bcc** | **list[str]** |  | [optional] 
**cc** | **list[str]** |  | [optional] 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**inbox_id** | **str** |  | 
**read** | **bool** |  | [optional] 
**subject** | **str** |  | [optional] 
**to** | **list[str]** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


