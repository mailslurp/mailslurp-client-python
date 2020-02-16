# coding: utf-8

# flake8: noqa
"""
    MailSlurp API

    ## Introduction  [MailSlurp](https://www.mailslurp.com) is an Email API for developers and QA testers. It let's users: - create emails addresses on demand - receive emails and attachments in code - send templated HTML emails  ## About  This page contains the REST API documentation for MailSlurp. All requests require API Key authentication passed as an `x-api-key` header.  Create an account to [get your free API Key](https://app.mailslurp.com/sign-up/).  ## Resources - 🔑 [Get API Key](https://app.mailslurp.com/sign-up/)                    - 🎓 [Developer Portal](https://www.mailslurp.com/docs/)           - 📦 [Library SDKs](https://www.mailslurp.com/docs/) - ✍️ [Code Examples](https://www.mailslurp.com/examples) - ⚠️ [Report an issue](https://drift.me/mailslurp)  ## Explore    # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from mailslurp_client.models.attachment_meta_data import AttachmentMetaData
from mailslurp_client.models.basic_auth_options import BasicAuthOptions
from mailslurp_client.models.bulk_send_email_options import BulkSendEmailOptions
from mailslurp_client.models.contact_dto import ContactDto
from mailslurp_client.models.contact_projection import ContactProjection
from mailslurp_client.models.create_contact_options import CreateContactOptions
from mailslurp_client.models.create_domain_options import CreateDomainOptions
from mailslurp_client.models.create_group_options import CreateGroupOptions
from mailslurp_client.models.create_template_options import CreateTemplateOptions
from mailslurp_client.models.create_webhook_options import CreateWebhookOptions
from mailslurp_client.models.domain_plus_verification_records_and_status import DomainPlusVerificationRecordsAndStatus
from mailslurp_client.models.domain_preview import DomainPreview
from mailslurp_client.models.email import Email
from mailslurp_client.models.email_analysis import EmailAnalysis
from mailslurp_client.models.email_preview import EmailPreview
from mailslurp_client.models.email_projection import EmailProjection
from mailslurp_client.models.forward_email_options import ForwardEmailOptions
from mailslurp_client.models.group_contacts_dto import GroupContactsDto
from mailslurp_client.models.group_dto import GroupDto
from mailslurp_client.models.group_projection import GroupProjection
from mailslurp_client.models.html_validation_result import HTMLValidationResult
from mailslurp_client.models.inbox import Inbox
from mailslurp_client.models.inbox_projection import InboxProjection
from mailslurp_client.models.json_node import JsonNode
from mailslurp_client.models.match_option import MatchOption
from mailslurp_client.models.match_options import MatchOptions
from mailslurp_client.models.page_contact_projection import PageContactProjection
from mailslurp_client.models.page_email_preview import PageEmailPreview
from mailslurp_client.models.page_email_projection import PageEmailProjection
from mailslurp_client.models.page_group_projection import PageGroupProjection
from mailslurp_client.models.page_inbox_projection import PageInboxProjection
from mailslurp_client.models.page_template_projection import PageTemplateProjection
from mailslurp_client.models.page_webhook_projection import PageWebhookProjection
from mailslurp_client.models.pageable import Pageable
from mailslurp_client.models.send_email_options import SendEmailOptions
from mailslurp_client.models.set_inbox_favourited_options import SetInboxFavouritedOptions
from mailslurp_client.models.sort import Sort
from mailslurp_client.models.template_dto import TemplateDto
from mailslurp_client.models.template_projection import TemplateProjection
from mailslurp_client.models.template_variable import TemplateVariable
from mailslurp_client.models.update_group_contacts import UpdateGroupContacts
from mailslurp_client.models.upload_attachment_options import UploadAttachmentOptions
from mailslurp_client.models.validation_dto import ValidationDto
from mailslurp_client.models.validation_message import ValidationMessage
from mailslurp_client.models.webhook_dto import WebhookDto
from mailslurp_client.models.webhook_projection import WebhookProjection
from mailslurp_client.models.webhook_test_request import WebhookTestRequest
from mailslurp_client.models.webhook_test_response import WebhookTestResponse
from mailslurp_client.models.webhook_test_result import WebhookTestResult
