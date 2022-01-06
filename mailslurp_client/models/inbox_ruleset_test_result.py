# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class InboxRulesetTestResult(object):
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
        'ruleset_matches': 'dict(str, bool)',
        'matches': 'bool'
    }

    attribute_map = {
        'ruleset_matches': 'rulesetMatches',
        'matches': 'matches'
    }

    def __init__(self, ruleset_matches=None, matches=None, local_vars_configuration=None):  # noqa: E501
        """InboxRulesetTestResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ruleset_matches = None
        self._matches = None
        self.discriminator = None

        if ruleset_matches is not None:
            self.ruleset_matches = ruleset_matches
        if matches is not None:
            self.matches = matches

    @property
    def ruleset_matches(self):
        """Gets the ruleset_matches of this InboxRulesetTestResult.  # noqa: E501

        Map of inbox ruleset ID to boolean of if target matches  # noqa: E501

        :return: The ruleset_matches of this InboxRulesetTestResult.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._ruleset_matches

    @ruleset_matches.setter
    def ruleset_matches(self, ruleset_matches):
        """Sets the ruleset_matches of this InboxRulesetTestResult.

        Map of inbox ruleset ID to boolean of if target matches  # noqa: E501

        :param ruleset_matches: The ruleset_matches of this InboxRulesetTestResult.  # noqa: E501
        :type: dict(str, bool)
        """

        self._ruleset_matches = ruleset_matches

    @property
    def matches(self):
        """Gets the matches of this InboxRulesetTestResult.  # noqa: E501


        :return: The matches of this InboxRulesetTestResult.  # noqa: E501
        :rtype: bool
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this InboxRulesetTestResult.


        :param matches: The matches of this InboxRulesetTestResult.  # noqa: E501
        :type: bool
        """

        self._matches = matches

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
        if not isinstance(other, InboxRulesetTestResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InboxRulesetTestResult):
            return True

        return self.to_dict() != other.to_dict()
