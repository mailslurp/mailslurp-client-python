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
from mailslurp_client.api.webhook_controller_api import WebhookControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestWebhookControllerApi(unittest.TestCase):
    """WebhookControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.webhook_controller_api.WebhookControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_webhook(self):
        """Test case for create_webhook

        Attach a WebHook URL to an inbox  # noqa: E501
        """
        pass

    def test_delete_webhook(self):
        """Test case for delete_webhook

        Delete and disable a Webhook for an Inbox  # noqa: E501
        """
        pass

    def test_get_all_webhooks(self):
        """Test case for get_all_webhooks

        List Webhooks Paginated  # noqa: E501
        """
        pass

    def test_get_webhook(self):
        """Test case for get_webhook

        Get a webhook for an Inbox  # noqa: E501
        """
        pass

    def test_get_webhooks(self):
        """Test case for get_webhooks

        Get all Webhooks for an Inbox  # noqa: E501
        """
        pass

    def test_send_test_data(self):
        """Test case for send_test_data

        Send webhook test data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
