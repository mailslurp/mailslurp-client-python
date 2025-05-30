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
import datetime

import mailslurp_client
from mailslurp_client.models.email_preview import EmailPreview  # noqa: E501
from mailslurp_client.rest import ApiException

class TestEmailPreview(unittest.TestCase):
    """EmailPreview unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EmailPreview
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.email_preview.EmailPreview()  # noqa: E501
        if include_optional :
            return EmailPreview(
                id = '0', 
                inbox_id = '0', 
                domain_id = '0', 
                subject = '0', 
                to = [
                    '0'
                    ], 
                _from = '0', 
                bcc = [
                    '0'
                    ], 
                cc = [
                    '0'
                    ], 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                read = True, 
                attachments = [
                    '0'
                    ], 
                thread_id = '0', 
                message_id = '0', 
                in_reply_to = '0', 
                sender = mailslurp_client.models.sender.Sender(
                    raw_value = '0', 
                    email_address = '0', 
                    name = '0', ), 
                recipients = mailslurp_client.models.email_recipients.EmailRecipients(
                    to = [
                        mailslurp_client.models.recipient.Recipient(
                            raw_value = '0', 
                            email_address = '0', 
                            name = '0', )
                        ], 
                    cc = [
                        mailslurp_client.models.recipient.Recipient(
                            raw_value = '0', 
                            email_address = '0', 
                            name = '0', )
                        ], 
                    bcc = [
                        mailslurp_client.models.recipient.Recipient(
                            raw_value = '0', 
                            email_address = '0', 
                            name = '0', )
                        ], ), 
                favourite = True, 
                body_part_content_types = [
                    '0'
                    ], 
                plus_address = '0', 
                size_bytes = 56
            )
        else :
            return EmailPreview(
                id = '0',
                to = [
                    '0'
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                read = True,
        )

    def testEmailPreview(self):
        """Test EmailPreview"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
