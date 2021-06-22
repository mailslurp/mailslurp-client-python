# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mailslurp_client
from mailslurp_client.models.webhook_new_contact_payload import WebhookNewContactPayload  # noqa: E501
from mailslurp_client.rest import ApiException

class TestWebhookNewContactPayload(unittest.TestCase):
    """WebhookNewContactPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WebhookNewContactPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.webhook_new_contact_payload.WebhookNewContactPayload()  # noqa: E501
        if include_optional :
            return WebhookNewContactPayload(
                company = '0', 
                contact_id = '0', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                email_addresses = [
                    '0'
                    ], 
                event_name = 'EMAIL_RECEIVED', 
                first_name = '0', 
                group_id = '0', 
                last_name = '0', 
                message_id = '0', 
                meta_data = mailslurp_client.models.json_node.JsonNode(), 
                opt_out = True, 
                primary_email_address = '0', 
                tags = [
                    '0'
                    ], 
                webhook_id = '0', 
                webhook_name = '0'
            )
        else :
            return WebhookNewContactPayload(
                contact_id = '0',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                email_addresses = [
                    '0'
                    ],
                tags = [
                    '0'
                    ],
        )

    def testWebhookNewContactPayload(self):
        """Test WebhookNewContactPayload"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
