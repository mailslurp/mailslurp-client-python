# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class FlushExpiredInboxesResult(object):
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
        'inbox_ids': 'list[str]',
        'expire_before': 'datetime'
    }

    attribute_map = {
        'inbox_ids': 'inboxIds',
        'expire_before': 'expireBefore'
    }

    def __init__(self, inbox_ids=None, expire_before=None, local_vars_configuration=None):  # noqa: E501
        """FlushExpiredInboxesResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._inbox_ids = None
        self._expire_before = None
        self.discriminator = None

        self.inbox_ids = inbox_ids
        self.expire_before = expire_before

    @property
    def inbox_ids(self):
        """Gets the inbox_ids of this FlushExpiredInboxesResult.  # noqa: E501

        Inbox IDs affected by expiration  # noqa: E501

        :return: The inbox_ids of this FlushExpiredInboxesResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._inbox_ids

    @inbox_ids.setter
    def inbox_ids(self, inbox_ids):
        """Sets the inbox_ids of this FlushExpiredInboxesResult.

        Inbox IDs affected by expiration  # noqa: E501

        :param inbox_ids: The inbox_ids of this FlushExpiredInboxesResult.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and inbox_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `inbox_ids`, must not be `None`")  # noqa: E501

        self._inbox_ids = inbox_ids

    @property
    def expire_before(self):
        """Gets the expire_before of this FlushExpiredInboxesResult.  # noqa: E501

        DateTime to filter inboxes so that those expiring before this time are expired  # noqa: E501

        :return: The expire_before of this FlushExpiredInboxesResult.  # noqa: E501
        :rtype: datetime
        """
        return self._expire_before

    @expire_before.setter
    def expire_before(self, expire_before):
        """Sets the expire_before of this FlushExpiredInboxesResult.

        DateTime to filter inboxes so that those expiring before this time are expired  # noqa: E501

        :param expire_before: The expire_before of this FlushExpiredInboxesResult.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and expire_before is None:  # noqa: E501
            raise ValueError("Invalid value for `expire_before`, must not be `None`")  # noqa: E501

        self._expire_before = expire_before

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
        if not isinstance(other, FlushExpiredInboxesResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FlushExpiredInboxesResult):
            return True

        return self.to_dict() != other.to_dict()
