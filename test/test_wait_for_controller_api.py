# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mailslurp_client
from mailslurp_client.api.wait_for_controller_api import WaitForControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestWaitForControllerApi(unittest.TestCase):
    """WaitForControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.wait_for_controller_api.WaitForControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_wait_for(self):
        """Test case for wait_for

        Wait for conditions to be met  # noqa: E501
        """
        pass

    def test_wait_for_email_count(self):
        """Test case for wait_for_email_count

        Wait for and return count number of emails   # noqa: E501
        """
        pass

    def test_wait_for_latest_email(self):
        """Test case for wait_for_latest_email

        Fetch inbox's latest email or if empty wait for an email to arrive  # noqa: E501
        """
        pass

    def test_wait_for_matching_email(self):
        """Test case for wait_for_matching_email

        Wait or return list of emails that match simple matching patterns  # noqa: E501
        """
        pass

    def test_wait_for_matching_first_email(self):
        """Test case for wait_for_matching_first_email

        Wait for or return the first email that matches proved MatchOptions array  # noqa: E501
        """
        pass

    def test_wait_for_nth_email(self):
        """Test case for wait_for_nth_email

        Wait for or fetch the email with a given index in the inbox specified  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
