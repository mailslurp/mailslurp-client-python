# EmailAnalysis

Analysis result for email. Each verdict property is a string PASS|FAIL|GRAY or dynamic error message
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dkim_verdict** | **str** | Verdict of DomainKeys Identified Mail analysis | [optional] 
**dmarc_verdict** | **str** | Verdict of Domain-based Message Authentication Reporting and Conformance analysis | [optional] 
**spam_verdict** | **str** | Verdict of spam ranking analysis | [optional] 
**spf_verdict** | **str** | Verdict of Send Policy Framework record spoofing analysis | [optional] 
**virus_verdict** | **str** | Verdict of virus scan analysis | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


