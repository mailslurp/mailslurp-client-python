# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class InboxRulesetTestOptions(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'test_target': 'str'
    }

    attribute_map = {
        'test_target': 'testTarget'
    }

    def __init__(self, test_target=None, local_vars_configuration=None):  # noqa: E501
        """InboxRulesetTestOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._test_target = None
        self.discriminator = None

        self.test_target = test_target

    @property
    def test_target(self):
        """Gets the test_target of this InboxRulesetTestOptions.  # noqa: E501


        :return: The test_target of this InboxRulesetTestOptions.  # noqa: E501
        :rtype: str
        """
        return self._test_target

    @test_target.setter
    def test_target(self, test_target):
        """Sets the test_target of this InboxRulesetTestOptions.


        :param test_target: The test_target of this InboxRulesetTestOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and test_target is None:  # noqa: E501
            raise ValueError("Invalid value for `test_target`, must not be `None`")  # noqa: E501

        self._test_target = test_target

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InboxRulesetTestOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InboxRulesetTestOptions):
            return True

        return self.to_dict() != other.to_dict()