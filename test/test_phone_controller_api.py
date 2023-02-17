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
from mailslurp_client.api.phone_controller_api import PhoneControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestPhoneControllerApi(unittest.TestCase):
    """PhoneControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.phone_controller_api.PhoneControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_emergency_address(self):
        """Test case for create_emergency_address

        """
        pass

    def test_delete_emergency_address(self):
        """Test case for delete_emergency_address

        """
        pass

    def test_delete_phone_number(self):
        """Test case for delete_phone_number

        """
        pass

    def test_get_emergency_address(self):
        """Test case for get_emergency_address

        """
        pass

    def test_get_emergency_addresses(self):
        """Test case for get_emergency_addresses

        """
        pass

    def test_get_phone_number(self):
        """Test case for get_phone_number

        """
        pass

    def test_get_phone_numbers(self):
        """Test case for get_phone_numbers

        """
        pass

    def test_get_phone_plans(self):
        """Test case for get_phone_plans

        """
        pass

    def test_test_phone_number_send_sms(self):
        """Test case for test_phone_number_send_sms

        """
        pass


if __name__ == '__main__':
    unittest.main()
