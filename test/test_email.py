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
import datetime

import mailslurp_client
from mailslurp_client.models.email import Email  # noqa: E501
from mailslurp_client.rest import ApiException

class TestEmail(unittest.TestCase):
    """Email unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Email
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.email.Email()  # noqa: E501
        if include_optional :
            return Email(
                id = '0', 
                user_id = '0', 
                inbox_id = '0', 
                domain_id = '0', 
                to = [
                    '0'
                    ], 
                _from = '0', 
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
                reply_to = '0', 
                cc = [
                    '0'
                    ], 
                bcc = [
                    '0'
                    ], 
                headers = {
                    'key' : '0'
                    }, 
                headers_map = {
                    'key' : [
                        '0'
                        ]
                    }, 
                attachments = [
                    '0'
                    ], 
                subject = '0', 
                body = '0', 
                body_excerpt = '0', 
                body_md5_hash = '0', 
                is_html = True, 
                charset = '0', 
                analysis = mailslurp_client.models.email_analysis.EmailAnalysis(
                    spam_verdict = '0', 
                    virus_verdict = '0', 
                    spf_verdict = '0', 
                    dkim_verdict = '0', 
                    dmarc_verdict = '0', ), 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                read = True, 
                team_access = True, 
                html = True
            )
        else :
            return Email(
                id = '0',
                user_id = '0',
                inbox_id = '0',
                to = [
                    '0'
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                read = True,
                team_access = True,
        )

    def testEmail(self):
        """Test Email"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
