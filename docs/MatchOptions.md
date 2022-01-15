# MatchOptions

Optional filter for matching emails based on fields. For instance filter results to only include emails whose `SUBJECT` value does `CONTAIN` given match value. An example payload would be `{ matches: [{ field: 'SUBJECT', should: 'CONTAIN', value: 'Welcome' }] }`. You can also pass conditions such as `HAS_ATTACHMENT`. If you wish to extract regex matches inside the email content see the `getEmailContentMatch` method in the EmailController.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | [**list[MatchOption]**](MatchOption) | Zero or more match options such as &#x60;{ field: &#39;SUBJECT&#39;, should: &#39;CONTAIN&#39;, value: &#39;Welcome&#39; }&#x60;. Options are additive so if one does not match the email is excluded from results | [optional] 
**conditions** | [**list[ConditionOption]**](ConditionOption) | Zero or more conditions such as &#x60;{ condition: &#39;HAS_ATTACHMENTS&#39;, value: &#39;TRUE&#39; }&#x60;. Note the values are the strings &#x60;TRUE|FALSE&#x60; not booleans. | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


