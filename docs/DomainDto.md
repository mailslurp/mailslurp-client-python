# DomainDto

Domain plus verification records and status
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**domain** | **str** | Custom domain name | [optional] 
**verification_token** | **str** | Verification tokens | [optional] 
**dkim_tokens** | **list[str]** | Unique token DKIM tokens | [optional] 
**domain_name_records** | [**list[DomainNameRecord]**](DomainNameRecord) | List of DNS domain name records (C, MX, TXT) etc that you must add to the DNS server associated with your domain provider. | [optional] 
**catch_all_inbox_id** | **str** | The optional catch all inbox that will receive emails sent to the domain that cannot be matched. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**domain_type** | **str** | Type of domain. Dictates type of inbox that can be created with domain. HTTP means inboxes are processed using SES while SMTP inboxes use a custom SMTP mail server. SMTP does not support sending so use HTTP for sending emails. | [optional] 
**verified** | **bool** |  | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


