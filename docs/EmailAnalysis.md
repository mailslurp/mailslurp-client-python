# EmailAnalysis

Analysis result for email. Each verdict property is a string PASS|FAIL|GRAY or dynamic error message
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spam_verdict** | **str** | Verdict of spam ranking analysis | [optional] 
**virus_verdict** | **str** | Verdict of virus scan analysis | [optional] 
**spf_verdict** | **str** | Verdict of Send Policy Framework record spoofing analysis | [optional] 
**dkim_verdict** | **str** | Verdict of DomainKeys Identified Mail analysis | [optional] 
**dmarc_verdict** | **str** | Verdict of Domain-based Message Authentication Reporting and Conformance analysis | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


