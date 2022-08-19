# FlushExpiredInboxesResult

Result from calling expire on any inboxes that have applicable expiration dates given current time.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbox_ids** | **list[str]** | Inbox IDs affected by expiration | 
**expire_before** | **datetime** | DateTime to filter inboxes so that those expiring before this time are expired | 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


