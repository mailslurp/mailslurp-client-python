# PageSentEmailProjection

Paginated sent email results. Page index starts at zero. Projection results may omit larger entity fields. For fetching a full sent email entity use the projection ID with individual method calls.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**list[SentEmailProjection]**](SentEmailProjection) | Collection of items | 
**pageable** | [**PageableObject**](PageableObject) |  | [optional] 
**total** | **int** |  | [optional] 
**size** | **int** | Size of page requested | 
**number** | **int** | Page number starting at 0 | 
**number_of_elements** | **int** | Number of items returned | 
**total_pages** | **int** | Total number of pages available | 
**total_elements** | **int** | Total number of items available for querying | 
**last** | **bool** |  | [optional] 
**sort** | [**Sort**](Sort) |  | [optional] 
**first** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


