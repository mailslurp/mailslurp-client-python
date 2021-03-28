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
from mailslurp_client.api.expired_controller_api import ExpiredControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestExpiredControllerApi(unittest.TestCase):
    """ExpiredControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.expired_controller_api.ExpiredControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_expiration_defaults(self):
        """Test case for get_expiration_defaults

        Get default expiration settings  # noqa: E501
        """
        pass

    def test_get_expired_inbox_by_inbox_id(self):
        """Test case for get_expired_inbox_by_inbox_id

        Get expired inbox record for a previously existing inbox  # noqa: E501
        """
        pass

    def test_get_expired_inbox_record(self):
        """Test case for get_expired_inbox_record

        Get an expired inbox record  # noqa: E501
        """
        pass

    def test_get_expired_inboxes(self):
        """Test case for get_expired_inboxes

        List records of expired inboxes  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()