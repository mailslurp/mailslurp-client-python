# coding: utf-8

"""
    MailSlurp API

    ## Introduction  [MailSlurp](https://www.mailslurp.com) is an Email API for developers and QA testers. It let's users: - create emails addresses on demand - receive emails and attachments in code - send templated HTML emails  ## About  This page contains the REST API documentation for MailSlurp. All requests require API Key authentication passed as an `x-api-key` header.  Create an account to [get your free API Key](https://app.mailslurp.com/sign-up/).  ## Resources - 🔑 [Get API Key](https://app.mailslurp.com/sign-up/)                    - 🎓 [Developer Portal](https://www.mailslurp.com/docs/)           - 📦 [Library SDKs](https://www.mailslurp.com/docs/) - ✍️ [Code Examples](https://www.mailslurp.com/examples) - ⚠️ [Report an issue](https://drift.me/mailslurp)  ## Explore    # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mailslurp_client
from mailslurp_client.models.html_validation_result import HTMLValidationResult  # noqa: E501
from mailslurp_client.rest import ApiException

class TestHTMLValidationResult(unittest.TestCase):
    """HTMLValidationResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HTMLValidationResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.html_validation_result.HTMLValidationResult()  # noqa: E501
        if include_optional :
            return HTMLValidationResult(
                errors = [
                    mailslurp_client.models.validation_message.ValidationMessage(
                        line_number = 56, 
                        message = '0', )
                    ], 
                is_valid = True, 
                warnings = [
                    mailslurp_client.models.validation_message.ValidationMessage(
                        line_number = 56, 
                        message = '0', )
                    ]
            )
        else :
            return HTMLValidationResult(
                errors = [
                    mailslurp_client.models.validation_message.ValidationMessage(
                        line_number = 56, 
                        message = '0', )
                    ],
                is_valid = True,
                warnings = [
                    mailslurp_client.models.validation_message.ValidationMessage(
                        line_number = 56, 
                        message = '0', )
                    ],
        )

    def testHTMLValidationResult(self):
        """Test HTMLValidationResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
