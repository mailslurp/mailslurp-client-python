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
from mailslurp_client.api.alias_controller_api import AliasControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestAliasControllerApi(unittest.TestCase):
    """AliasControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.alias_controller_api.AliasControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_alias(self):
        """Test case for create_alias

        Create an email alias. Must be verified by clicking link inside verification email that will be sent to the address. Once verified the alias will be active.  # noqa: E501
        """
        pass

    def test_delete_alias(self):
        """Test case for delete_alias

        Delete an email alias  # noqa: E501
        """
        pass

    def test_get_alias(self):
        """Test case for get_alias

        Get an email alias  # noqa: E501
        """
        pass

    def test_get_alias_emails(self):
        """Test case for get_alias_emails

        Get emails for an alias  # noqa: E501
        """
        pass

    def test_get_alias_threads(self):
        """Test case for get_alias_threads

        Get threads created for an alias  # noqa: E501
        """
        pass

    def test_get_aliases(self):
        """Test case for get_aliases

        Get all email aliases you have created  # noqa: E501
        """
        pass

    def test_reply_to_alias_email(self):
        """Test case for reply_to_alias_email

        Reply to an email  # noqa: E501
        """
        pass

    def test_send_alias_email(self):
        """Test case for send_alias_email

        Send an email from an alias inbox  # noqa: E501
        """
        pass

    def test_update_alias(self):
        """Test case for update_alias

        Update an email alias  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
