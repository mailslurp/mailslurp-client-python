# PageEmailPreview

Paginated email preview results. EmailProjections and EmailPreviews are essentially the same but have legacy naming issues. Page index starts at zero. Projection results may omit larger entity fields. For fetching a full entity use the projection ID with individual method calls. For emails there are several methods for fetching message bodies and attachments.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**list[EmailPreview]**](EmailPreview) |  | [optional] 
**pageable** | [**Pageable**](Pageable) |  | [optional] 
**last** | **bool** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**Sort**](Sort) |  | [optional] 
**first** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**empty** | **bool** |  | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


