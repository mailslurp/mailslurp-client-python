# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class ExpirationDefaults(object):
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
        'can_permanent_inbox': 'bool',
        'default_expiration_millis': 'int',
        'default_expires_at': 'datetime',
        'max_expiration_millis': 'int',
        'next_inbox_allows_permanent': 'bool'
    }

    attribute_map = {
        'can_permanent_inbox': 'canPermanentInbox',
        'default_expiration_millis': 'defaultExpirationMillis',
        'default_expires_at': 'defaultExpiresAt',
        'max_expiration_millis': 'maxExpirationMillis',
        'next_inbox_allows_permanent': 'nextInboxAllowsPermanent'
    }

    def __init__(self, can_permanent_inbox=None, default_expiration_millis=None, default_expires_at=None, max_expiration_millis=None, next_inbox_allows_permanent=None, local_vars_configuration=None):  # noqa: E501
        """ExpirationDefaults - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._can_permanent_inbox = None
        self._default_expiration_millis = None
        self._default_expires_at = None
        self._max_expiration_millis = None
        self._next_inbox_allows_permanent = None
        self.discriminator = None

        self.can_permanent_inbox = can_permanent_inbox
        if default_expiration_millis is not None:
            self.default_expiration_millis = default_expiration_millis
        if default_expires_at is not None:
            self.default_expires_at = default_expires_at
        if max_expiration_millis is not None:
            self.max_expiration_millis = max_expiration_millis
        self.next_inbox_allows_permanent = next_inbox_allows_permanent

    @property
    def can_permanent_inbox(self):
        """Gets the can_permanent_inbox of this ExpirationDefaults.  # noqa: E501


        :return: The can_permanent_inbox of this ExpirationDefaults.  # noqa: E501
        :rtype: bool
        """
        return self._can_permanent_inbox

    @can_permanent_inbox.setter
    def can_permanent_inbox(self, can_permanent_inbox):
        """Sets the can_permanent_inbox of this ExpirationDefaults.


        :param can_permanent_inbox: The can_permanent_inbox of this ExpirationDefaults.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and can_permanent_inbox is None:  # noqa: E501
            raise ValueError("Invalid value for `can_permanent_inbox`, must not be `None`")  # noqa: E501

        self._can_permanent_inbox = can_permanent_inbox

    @property
    def default_expiration_millis(self):
        """Gets the default_expiration_millis of this ExpirationDefaults.  # noqa: E501


        :return: The default_expiration_millis of this ExpirationDefaults.  # noqa: E501
        :rtype: int
        """
        return self._default_expiration_millis

    @default_expiration_millis.setter
    def default_expiration_millis(self, default_expiration_millis):
        """Sets the default_expiration_millis of this ExpirationDefaults.


        :param default_expiration_millis: The default_expiration_millis of this ExpirationDefaults.  # noqa: E501
        :type: int
        """

        self._default_expiration_millis = default_expiration_millis

    @property
    def default_expires_at(self):
        """Gets the default_expires_at of this ExpirationDefaults.  # noqa: E501


        :return: The default_expires_at of this ExpirationDefaults.  # noqa: E501
        :rtype: datetime
        """
        return self._default_expires_at

    @default_expires_at.setter
    def default_expires_at(self, default_expires_at):
        """Sets the default_expires_at of this ExpirationDefaults.


        :param default_expires_at: The default_expires_at of this ExpirationDefaults.  # noqa: E501
        :type: datetime
        """

        self._default_expires_at = default_expires_at

    @property
    def max_expiration_millis(self):
        """Gets the max_expiration_millis of this ExpirationDefaults.  # noqa: E501


        :return: The max_expiration_millis of this ExpirationDefaults.  # noqa: E501
        :rtype: int
        """
        return self._max_expiration_millis

    @max_expiration_millis.setter
    def max_expiration_millis(self, max_expiration_millis):
        """Sets the max_expiration_millis of this ExpirationDefaults.


        :param max_expiration_millis: The max_expiration_millis of this ExpirationDefaults.  # noqa: E501
        :type: int
        """

        self._max_expiration_millis = max_expiration_millis

    @property
    def next_inbox_allows_permanent(self):
        """Gets the next_inbox_allows_permanent of this ExpirationDefaults.  # noqa: E501


        :return: The next_inbox_allows_permanent of this ExpirationDefaults.  # noqa: E501
        :rtype: bool
        """
        return self._next_inbox_allows_permanent

    @next_inbox_allows_permanent.setter
    def next_inbox_allows_permanent(self, next_inbox_allows_permanent):
        """Sets the next_inbox_allows_permanent of this ExpirationDefaults.


        :param next_inbox_allows_permanent: The next_inbox_allows_permanent of this ExpirationDefaults.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and next_inbox_allows_permanent is None:  # noqa: E501
            raise ValueError("Invalid value for `next_inbox_allows_permanent`, must not be `None`")  # noqa: E501

        self._next_inbox_allows_permanent = next_inbox_allows_permanent

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
        if not isinstance(other, ExpirationDefaults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExpirationDefaults):
            return True

        return self.to_dict() != other.to_dict()
