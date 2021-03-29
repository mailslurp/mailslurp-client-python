# Email

Email model (also referred to as EmailDto). Represents an email that was received by an inbox. If you want the original SMTP message see the `getRawEmail` endpoint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**EmailAnalysis**](EmailAnalysis.md) |  | [optional] 
**attachments** | **list[str]** | List of IDs of attachments found in the email. Use these IDs with the Inbox and Email Controllers to download attachments and attachment meta data such as filesize, name, extension. | [optional] 
**bcc** | **list[str]** | List of &#x60;BCC&#x60; recipients email was addressed to | [optional] 
**body** | **str** | The body of the email message | [optional] 
**body_md5_hash** | **str** | A hash signature of the email message | [optional] 
**cc** | **list[str]** | List of &#x60;CC&#x60; recipients email was addressed to | [optional] 
**charset** | **str** | Detected character set of the email body such as UTF-8 | [optional] 
**created_at** | **datetime** | When was the email received by MailSlurp | [optional] 
**_from** | **str** | Who the email was sent from | [optional] 
**headers** | **dict(str, str)** |  | [optional] 
**id** | **str** | ID of the email | [optional] 
**inbox_id** | **str** | ID of the inbox that received the email | [optional] 
**is_html** | **bool** | Was HTML sent in the email body | [optional] 
**read** | **bool** | Has the email been viewed ever. This means viewed in the dashboard or requested via the full email entity endpoints | [optional] 
**reply_to** | **str** | The replyTo field on the received email | [optional] 
**subject** | **str** | The subject line of the email message | [optional] 
**team_access** | **bool** | Can the email be accessed by organization team members | [optional] 
**to** | **list[str]** | List of &#x60;To&#x60; recipients email was addressed to | [optional] 
**updated_at** | **datetime** | When was the email last updated | [optional] 
**user_id** | **str** | ID of user that email belongs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


