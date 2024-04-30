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
from mailslurp_client.api.email_verification_controller_api import EmailVerificationControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestEmailVerificationControllerApi(unittest.TestCase):
    """EmailVerificationControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.email_verification_controller_api.EmailVerificationControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_all_validation_requests(self):
        """Test case for delete_all_validation_requests

        Delete all validation requests  # noqa: E501
        """
        pass

    def test_delete_validation_request(self):
        """Test case for delete_validation_request

        Delete a validation record  # noqa: E501
        """
        pass

    def test_get_validation_requests(self):
        """Test case for get_validation_requests

        Validate a list of email addresses. Per unit billing. See your plan for pricing.  # noqa: E501
        """
        pass

    def test_validate_email_address_list(self):
        """Test case for validate_email_address_list

        Validate a list of email addresses. Per unit billing. See your plan for pricing.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
