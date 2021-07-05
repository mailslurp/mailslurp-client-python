# PageSentEmailProjection

Paginated sent email results. Page index starts at zero. Projection results may omit larger entity fields. For fetching a full sent email entity use the projection ID with individual method calls.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**list[SentEmailProjection]**](SentEmailProjection) | Collection of items | [optional] 
**empty** | **bool** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number** | **int** | Page number starting at 0 | [optional] 
**number_of_elements** | **int** | Number of items returned | [optional] 
**pageable** | [**Pageable**](Pageable) |  | [optional] 
**size** | **int** | Size of page requested | [optional] 
**sort** | [**Sort**](Sort) |  | [optional] 
**total_elements** | **int** | Total number of items available for querying | [optional] 
**total_pages** | **int** | Total number of pages available | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


