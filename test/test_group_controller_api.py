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
from mailslurp_client.api.group_controller_api import GroupControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestGroupControllerApi(unittest.TestCase):
    """GroupControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.group_controller_api.GroupControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_contacts_to_group(self):
        """Test case for add_contacts_to_group

        Add contacts to a group  # noqa: E501
        """
        pass

    def test_create_group(self):
        """Test case for create_group

        Create a group  # noqa: E501
        """
        pass

    def test_delete_group(self):
        """Test case for delete_group

        Delete group  # noqa: E501
        """
        pass

    def test_get_all_groups(self):
        """Test case for get_all_groups

        Get all Contact Groups in paginated format  # noqa: E501
        """
        pass

    def test_get_group(self):
        """Test case for get_group

        Get group  # noqa: E501
        """
        pass

    def test_get_group_with_contacts(self):
        """Test case for get_group_with_contacts

        Get group and contacts belonging to it  # noqa: E501
        """
        pass

    def test_get_group_with_contacts_paginated(self):
        """Test case for get_group_with_contacts_paginated

        Get group and paginated contacts belonging to it  # noqa: E501
        """
        pass

    def test_get_groups(self):
        """Test case for get_groups

        Get all groups  # noqa: E501
        """
        pass

    def test_remove_contacts_from_group(self):
        """Test case for remove_contacts_from_group

        Remove contacts from a group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
