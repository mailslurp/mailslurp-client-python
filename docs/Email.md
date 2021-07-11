# Email

Email entity (also known as EmailDto). When an SMTP email message is received by MailSlurp it is parsed. The body and attachments are written to disk and the fields such as to, from, subject etc are stored in a database. The `body` contains the email content. If you want the original SMTP message see the `getRawEmail` endpoints. The attachments can be fetched using the AttachmentController
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**EmailAnalysis**](EmailAnalysis) |  | [optional] 
**attachments** | **list[str]** | List of IDs of attachments found in the email. Use these IDs with the Inbox and Email Controllers to download attachments and attachment meta data such as filesize, name, extension. | [optional] 
**bcc** | **list[str]** | List of &#x60;BCC&#x60; recipients email was addressed to | [optional] 
**body** | **str** | The body of the email message | [optional] 
**body_excerpt** | **str** | An excerpt of the body of the email message | [optional] 
**body_md5_hash** | **str** | A hash signature of the email message | [optional] 
**cc** | **list[str]** | List of &#x60;CC&#x60; recipients email was addressed to | [optional] 
**charset** | **str** | Detected character set of the email body such as UTF-8 | [optional] 
**created_at** | **datetime** | When was the email received by MailSlurp | [optional] 
**_from** | **str** | Who the email was sent from | [optional] 
**headers** | **dict(str, str)** | Collection of SMTP headers attached to email | [optional] 
**id** | **str** | ID of the email entity | [optional] 
**inbox_id** | **str** | ID of the inbox that received the email | [optional] 
**is_html** | **bool** | Is the email body HTML | [optional] 
**read** | **bool** | Read flag. Has the email ever been viewed in the dashboard or fetched via the API? If so the email is marked as read. | [optional] 
**reply_to** | **str** | The &#x60;replyTo&#x60; field on the received email message | [optional] 
**subject** | **str** | The subject line of the email message | [optional] 
**team_access** | **bool** | Can the email be accessed by organization team members | [optional] 
**to** | **list[str]** | List of &#x60;To&#x60; recipients that email was addressed to | [optional] 
**updated_at** | **datetime** | When was the email last updated | [optional] 
**user_id** | **str** | ID of user that email belongs to | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


