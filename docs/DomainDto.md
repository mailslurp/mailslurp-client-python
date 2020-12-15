# DomainDto

Domain plus verification records and status
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**dkim_tokens** | **list[str]** | DNS records for DKIM approval | [optional] 
**domain** | **str** | Custom domain name | [optional] 
**id** | **str** |  | 
**is_verified** | **bool** | Whether domain has been verified or not. If the domain is not verified after 72 hours there is most likely an issue with the domains DNS records. | [optional] 
**updated_at** | **datetime** |  | 
**user_id** | **str** |  | 
**verification_token** | **str** | A TXT record that you must place in the DNS settings of the domain to complete domain verification | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


