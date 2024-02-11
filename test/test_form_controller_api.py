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
from mailslurp_client.api.form_controller_api import FormControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestFormControllerApi(unittest.TestCase):
    """FormControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.form_controller_api.FormControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_submit_form(self):
        """Test case for submit_form

        Submit a form to be parsed and sent as an email to an address determined by the form fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
