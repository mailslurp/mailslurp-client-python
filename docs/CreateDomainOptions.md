# CreateDomainOptions

Options for creating a domain to use with MailSlurp. You must have ownership access to this domain in order to verify it. Domains will not function correctly until the domain has been verified. See https://www.mailslurp.com/guides/custom-domains for help. Domains can be either `HTTP` or `SMTP` type. The type of domain determines which inboxes can be used with it. `SMTP` inboxes use a mail server running `mx.mailslurp.com` while `HTTP` inboxes are handled by AWS SES.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The top level domain you wish to use with MailSlurp. Do not specify subdomain just the top level. So &#x60;test.com&#x60; covers all subdomains such as &#x60;mail.test.com&#x60;. Don&#39;t include a protocol such as &#x60;http://&#x60;. Once added you must complete the verification steps by adding the returned records to your domain. | 
**description** | **str** | Optional description of the domain. | [optional] 
**created_catch_all_inbox** | **bool** | Whether to create a catch all inbox for the domain. Any email sent to an address using your domain that cannot be matched to an existing inbox you created with the domain will be routed to the created catch all inbox. You can access emails using the regular methods on this inbox ID. | [optional] 
**domain_type** | **str** | Type of domain. Dictates type of inbox that can be created with domain. HTTP means inboxes are processed using SES while SMTP inboxes use a custom SMTP mail server. SMTP does not support sending so use HTTP for sending emails. | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


