# CreateDomainOptions

Options for creating a domain to use with MailSlurp. You must have ownership access to this domain in order to verify it. Domains will not function correctly until the domain has been verified. See https://www.mailslurp.com/guides/custom-domains for help. Domains can be either `HTTP` or `SMTP` type. The type of domain determines which inboxes can be used with it. `SMTP` inboxes use a mail server running `mx.mailslurp.com` while `HTTP` inboxes are handled by AWS SES.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_catch_all_inbox** | **bool** | Whether to create a catch all inbox for the domain. Any email sent to an address using your domain that cannot be matched to an existing inbox you created with the domain will be routed to the created catch all inbox. You can access emails using the regular methods on this inbox ID. | [optional] 
**description** | **str** | Optional description of the domain. | [optional] 
**domain** | **str** | The top level domain you wish to use with MailSlurp. Do not specify subdomain just the top level. So &#x60;test.com&#x60; covers all subdomains such as &#x60;mail.test.com&#x60;. Don&#39;t include a protocol such as &#x60;http://&#x60;. Once added you must complete the verification steps by adding the returned records to your domain. | [optional] 
**domain_type** | **str** | Domain type to create. HTTP or SMTP domain. HTTP domain uses MailSlurps SES MX records. SMTP uses a custom SMTP server MX record. SMTP domains can only be used with SMTP inboxes. SMTP inboxes are more reliable for public inbound emails while HTTP inboxes are more suitable for testing. | [optional] 

[[Back to Model list]](../README#documentation-for-models) [[Back to API list]](../README#documentation-for-api-endpoints) [[Back to README]](../README)


