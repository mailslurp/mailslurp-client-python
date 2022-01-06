# PageExpiredInboxRecordProjection

Paginated expired inbox results. Page index starts at zero. Projection results may omit larger entity fields. For fetching a full entity use the projection ID with individual method calls.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**list[ExpiredInboxRecordProjection]**](ExpiredInboxRecordProjection) |  | [optional] 
**pageable** | [**Pageable**](Pageable) |  | [optional] 
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**last** | **bool** |  | [optional] 
**size** | **int** |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**Sort**](Sort) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


