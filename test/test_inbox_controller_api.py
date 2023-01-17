# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mailslurp_client
from mailslurp_client.api.inbox_controller_api import InboxControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestInboxControllerApi(unittest.TestCase):
    """InboxControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.inbox_controller_api.InboxControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_scheduled_job(self):
        """Test case for cancel_scheduled_job

        Cancel a scheduled email job  # noqa: E501
        """
        pass

    def test_create_inbox(self):
        """Test case for create_inbox

        Create an inbox email address. An inbox has a real email address and can send and receive emails. Inboxes can be either `SMTP` or `HTTP` inboxes.  # noqa: E501
        """
        pass

    def test_create_inbox_ruleset(self):
        """Test case for create_inbox_ruleset

        Create an inbox ruleset  # noqa: E501
        """
        pass

    def test_create_inbox_with_defaults(self):
        """Test case for create_inbox_with_defaults

        Create an inbox with default options. Uses MailSlurp domain pool address and is private.  # noqa: E501
        """
        pass

    def test_create_inbox_with_options(self):
        """Test case for create_inbox_with_options

        Create an inbox with options. Extended options for inbox creation.  # noqa: E501
        """
        pass

    def test_delete_all_inbox_emails(self):
        """Test case for delete_all_inbox_emails

        Delete all emails in a given inboxes.  # noqa: E501
        """
        pass

    def test_delete_all_inboxes(self):
        """Test case for delete_all_inboxes

        Delete all inboxes  # noqa: E501
        """
        pass

    def test_delete_inbox(self):
        """Test case for delete_inbox

        Delete inbox  # noqa: E501
        """
        pass

    def test_does_inbox_exist(self):
        """Test case for does_inbox_exist

        Does inbox exist  # noqa: E501
        """
        pass

    def test_flush_expired(self):
        """Test case for flush_expired

        Remove expired inboxes  # noqa: E501
        """
        pass

    def test_get_all_inboxes(self):
        """Test case for get_all_inboxes

        List All Inboxes Paginated  # noqa: E501
        """
        pass

    def test_get_all_scheduled_jobs(self):
        """Test case for get_all_scheduled_jobs

        Get all scheduled email sending jobs for account  # noqa: E501
        """
        pass

    def test_get_delivery_statuses_by_inbox_id(self):
        """Test case for get_delivery_statuses_by_inbox_id

        """
        pass

    def test_get_emails(self):
        """Test case for get_emails

        Get emails in an Inbox. This method is not idempotent as it allows retries and waits if you want certain conditions to be met before returning. For simple listing and sorting of known emails use the email controller instead.  # noqa: E501
        """
        pass

    def test_get_imap_smtp_access(self):
        """Test case for get_imap_smtp_access

        """
        pass

    def test_get_inbox(self):
        """Test case for get_inbox

        Get Inbox. Returns properties of an inbox.  # noqa: E501
        """
        pass

    def test_get_inbox_by_email_address(self):
        """Test case for get_inbox_by_email_address

        Search for an inbox with the provided email address  # noqa: E501
        """
        pass

    def test_get_inbox_by_name(self):
        """Test case for get_inbox_by_name

        Search for an inbox with the given name  # noqa: E501
        """
        pass

    def test_get_inbox_count(self):
        """Test case for get_inbox_count

        Get total inbox count  # noqa: E501
        """
        pass

    def test_get_inbox_email_count(self):
        """Test case for get_inbox_email_count

        Get email count in inbox  # noqa: E501
        """
        pass

    def test_get_inbox_emails_paginated(self):
        """Test case for get_inbox_emails_paginated

        Get inbox emails paginated  # noqa: E501
        """
        pass

    def test_get_inbox_ids(self):
        """Test case for get_inbox_ids

        Get all inbox IDs  # noqa: E501
        """
        pass

    def test_get_inbox_sent_emails(self):
        """Test case for get_inbox_sent_emails

        Get Inbox Sent Emails  # noqa: E501
        """
        pass

    def test_get_inbox_tags(self):
        """Test case for get_inbox_tags

        Get inbox tags  # noqa: E501
        """
        pass

    def test_get_inboxes(self):
        """Test case for get_inboxes

        List Inboxes and email addresses  # noqa: E501
        """
        pass

    def test_get_latest_email_in_inbox(self):
        """Test case for get_latest_email_in_inbox

        Get latest email in an inbox. Use `WaitForController` to get emails that may not have arrived yet.  # noqa: E501
        """
        pass

    def test_get_organization_inboxes(self):
        """Test case for get_organization_inboxes

        List Organization Inboxes Paginated  # noqa: E501
        """
        pass

    def test_get_scheduled_job(self):
        """Test case for get_scheduled_job

        Get a scheduled email job  # noqa: E501
        """
        pass

    def test_get_scheduled_jobs_by_inbox_id(self):
        """Test case for get_scheduled_jobs_by_inbox_id

        Get all scheduled email sending jobs for the inbox  # noqa: E501
        """
        pass

    def test_list_inbox_rulesets(self):
        """Test case for list_inbox_rulesets

        List inbox rulesets  # noqa: E501
        """
        pass

    def test_list_inbox_tracking_pixels(self):
        """Test case for list_inbox_tracking_pixels

        List inbox tracking pixels  # noqa: E501
        """
        pass

    def test_send_email(self):
        """Test case for send_email

        Send Email  # noqa: E501
        """
        pass

    def test_send_email_and_confirm(self):
        """Test case for send_email_and_confirm

        Send email and return sent confirmation  # noqa: E501
        """
        pass

    def test_send_email_with_queue(self):
        """Test case for send_email_with_queue

        Send email with queue  # noqa: E501
        """
        pass

    def test_send_smtp_envelope(self):
        """Test case for send_smtp_envelope

        Send email using an SMTP mail envelope and message body and return sent confirmation  # noqa: E501
        """
        pass

    def test_send_test_email(self):
        """Test case for send_test_email

        Send a test email to inbox  # noqa: E501
        """
        pass

    def test_send_with_schedule(self):
        """Test case for send_with_schedule

        Send email with with delay or schedule  # noqa: E501
        """
        pass

    def test_set_inbox_favourited(self):
        """Test case for set_inbox_favourited

        Set inbox favourited state  # noqa: E501
        """
        pass

    def test_update_inbox(self):
        """Test case for update_inbox

        Update Inbox. Change name and description. Email address is not editable.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
