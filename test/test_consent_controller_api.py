# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails and SMS from dynamically allocated email addresses and phone numbers. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mailslurp_client
from mailslurp_client.api.consent_controller_api import ConsentControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestConsentControllerApi(unittest.TestCase):
    """ConsentControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.consent_controller_api.ConsentControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_sending_consent_for_email_address(self):
        """Test case for check_sending_consent_for_email_address

        """
        pass

    def test_get_opt_in_identities(self):
        """Test case for get_opt_in_identities

        """
        pass

    def test_revoke_opt_in_consent_for_email_address(self):
        """Test case for revoke_opt_in_consent_for_email_address

        """
        pass

    def test_send_opt_in_consent_for_email_address(self):
        """Test case for send_opt_in_consent_for_email_address

        Send a verification code to a user once they have explicitly submitted their email address  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
