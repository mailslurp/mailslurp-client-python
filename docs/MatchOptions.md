# MatchOptions

Optional filter for matching emails based on fields. For instance filter results to only include emails whose `SUBJECT` value does `CONTAIN` given match value. An example payload would be `{ matches: [{ field: 'SUBJECT', should: 'CONTAIN', value: 'Welcome' }] }`. If you wish to extract regex matches inside the email content see the `getEmailContentMatch` method in the EmailController.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | [**list[MatchOption]**](MatchOption) | 1 or more match options. Options are additive so if one does not match the email is excluded from results | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


