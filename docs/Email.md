# Email

Email entity (also known as EmailDto). When an SMTP email message is received by MailSlurp it is parsed. The body and attachments are written to disk and the fields such as to, from, subject etc are stored in a database. The `body` contains the email content. If you want the original SMTP message see the `getRawEmail` endpoints. The attachments can be fetched using the AttachmentController
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the email entity | 
**user_id** | **str** | ID of user that email belongs to | 
**inbox_id** | **str** | ID of the inbox that received the email | 
**domain_id** | **str** | ID of the domain that received the email | [optional] 
**to** | **list[str]** | List of &#x60;To&#x60; recipient email addresses that the email was addressed to. See recipients object for names. | 
**_from** | **str** | Who the email was sent from. An email address - see fromName for the sender name. | [optional] 
**sender** | [**Sender**](Sender) |  | [optional] 
**recipients** | [**EmailRecipients**](EmailRecipients) |  | [optional] 
**reply_to** | **str** | The &#x60;replyTo&#x60; field on the received email message | [optional] 
**cc** | **list[str]** | List of &#x60;CC&#x60; recipients email addresses that the email was addressed to. See recipients object for names. | [optional] 
**bcc** | **list[str]** | List of &#x60;BCC&#x60; recipients email addresses that the email was addressed to. See recipients object for names. | [optional] 
**headers** | **dict(str, str)** | Collection of SMTP headers attached to email | [optional] 
**attachments** | **list[str]** | List of IDs of attachments found in the email. Use these IDs with the Inbox and Email Controllers to download attachments and attachment meta data such as filesize, name, extension. | [optional] 
**subject** | **str** | The subject line of the email message as specified by SMTP subject header | [optional] 
**body** | **str** | The body of the email message as text parsed from the SMTP message body (does not include attachments). Fetch the raw content to access the SMTP message and use the attachments property to access attachments. The body is stored separately to the email entity so the body is not returned in paginated results only in full single email or wait requests. | [optional] 
**body_excerpt** | **str** | An excerpt of the body of the email message for quick preview . | [optional] 
**body_md5_hash** | **str** | A hash signature of the email message using MD5. Useful for comparing emails without fetching full body. | [optional] 
**is_html** | **bool** | Is the email body content type HTML? | [optional] 
**charset** | **str** | Detected character set of the email body such as UTF-8 | [optional] 
**analysis** | [**EmailAnalysis**](EmailAnalysis) |  | [optional] 
**created_at** | **datetime** | When was the email received by MailSlurp | 
**updated_at** | **datetime** | When was the email last updated | 
**read** | **bool** | Read flag. Has the email ever been viewed in the dashboard or fetched via the API with a hydrated body? If so the email is marked as read. Paginated results do not affect read status. Read status is different to email opened event as it depends on your own account accessing the email. Email opened is determined by tracking pixels sent to other uses if enable during sending. You can listened for both email read and email opened events using webhooks. | 
**team_access** | **bool** | Can the email be accessed by organization team members | 
**html** | **bool** |  | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


