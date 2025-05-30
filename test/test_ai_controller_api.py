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
from mailslurp_client.api.ai_controller_api import AIControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestAIControllerApi(unittest.TestCase):
    """AIControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.ai_controller_api.AIControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_generate_structured_content_from_attachment(self):
        """Test case for generate_structured_content_from_attachment

        Generate structured content for an attachment  # noqa: E501
        """
        pass

    def test_generate_structured_content_from_email(self):
        """Test case for generate_structured_content_from_email

        Generate structured content for an email  # noqa: E501
        """
        pass

    def test_validate_structured_output_schema(self):
        """Test case for validate_structured_output_schema

        Validate structured content schema  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
