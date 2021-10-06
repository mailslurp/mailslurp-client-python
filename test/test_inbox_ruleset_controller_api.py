# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mailslurp_client
from mailslurp_client.api.inbox_ruleset_controller_api import InboxRulesetControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestInboxRulesetControllerApi(unittest.TestCase):
    """InboxRulesetControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.inbox_ruleset_controller_api.InboxRulesetControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_new_inbox_ruleset(self):
        """Test case for create_new_inbox_ruleset

        Create an inbox ruleset  # noqa: E501
        """
        pass

    def test_delete_inbox_ruleset(self):
        """Test case for delete_inbox_ruleset

        Delete an inbox ruleset  # noqa: E501
        """
        pass

    def test_delete_inbox_rulesets(self):
        """Test case for delete_inbox_rulesets

        Delete inbox rulesets  # noqa: E501
        """
        pass

    def test_get_inbox_ruleset(self):
        """Test case for get_inbox_ruleset

        Get an inbox ruleset  # noqa: E501
        """
        pass

    def test_get_inbox_rulesets(self):
        """Test case for get_inbox_rulesets

        List inbox rulesets  # noqa: E501
        """
        pass

    def test_test_inbox_ruleset(self):
        """Test case for test_inbox_ruleset

        Test an inbox ruleset  # noqa: E501
        """
        pass

    def test_test_inbox_rulesets_for_inbox(self):
        """Test case for test_inbox_rulesets_for_inbox

        Test inbox rulesets for inbox  # noqa: E501
        """
        pass

    def test_test_new_inbox_ruleset(self):
        """Test case for test_new_inbox_ruleset

        Test new inbox ruleset  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
