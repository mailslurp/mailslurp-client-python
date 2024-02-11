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
from mailslurp_client.models.reply_for_sms import ReplyForSms  # noqa: E501
from mailslurp_client.rest import ApiException

class TestReplyForSms(unittest.TestCase):
    """ReplyForSms unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReplyForSms
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.reply_for_sms.ReplyForSms()  # noqa: E501
        if include_optional :
            return ReplyForSms(
                reply = mailslurp_client.models.sent_sms_dto.SentSmsDto(
                    id = '0', 
                    user_id = '0', 
                    phone_number = '0', 
                    from_number = '0', 
                    to_number = '0', 
                    body = '0', 
                    sid = '0', 
                    reply_to_sid = '0', 
                    reply_to_id = '0', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else :
            return ReplyForSms(
        )

    def testReplyForSms(self):
        """Test ReplyForSms"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()