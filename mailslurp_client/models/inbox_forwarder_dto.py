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


class InboxForwarderDto(object):
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
        'created_at': 'datetime',
        'field': 'str',
        'forward_to_recipients': 'list[str]',
        'id': 'str',
        'inbox_id': 'str',
        'match': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'field': 'field',
        'forward_to_recipients': 'forwardToRecipients',
        'id': 'id',
        'inbox_id': 'inboxId',
        'match': 'match'
    }

    def __init__(self, created_at=None, field=None, forward_to_recipients=None, id=None, inbox_id=None, match=None, local_vars_configuration=None):  # noqa: E501
        """InboxForwarderDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._field = None
        self._forward_to_recipients = None
        self._id = None
        self._inbox_id = None
        self._match = None
        self.discriminator = None

        self.created_at = created_at
        self.field = field
        self.forward_to_recipients = forward_to_recipients
        self.id = id
        self.inbox_id = inbox_id
        self.match = match

    @property
    def created_at(self):
        """Gets the created_at of this InboxForwarderDto.  # noqa: E501


        :return: The created_at of this InboxForwarderDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InboxForwarderDto.


        :param created_at: The created_at of this InboxForwarderDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def field(self):
        """Gets the field of this InboxForwarderDto.  # noqa: E501


        :return: The field of this InboxForwarderDto.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this InboxForwarderDto.


        :param field: The field of this InboxForwarderDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and field is None:  # noqa: E501
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501
        allowed_values = ["RECIPIENTS", "SENDER", "SUBJECT", "ATTACHMENTS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and field not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `field` ({0}), must be one of {1}"  # noqa: E501
                .format(field, allowed_values)
            )

        self._field = field

    @property
    def forward_to_recipients(self):
        """Gets the forward_to_recipients of this InboxForwarderDto.  # noqa: E501


        :return: The forward_to_recipients of this InboxForwarderDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._forward_to_recipients

    @forward_to_recipients.setter
    def forward_to_recipients(self, forward_to_recipients):
        """Sets the forward_to_recipients of this InboxForwarderDto.


        :param forward_to_recipients: The forward_to_recipients of this InboxForwarderDto.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and forward_to_recipients is None:  # noqa: E501
            raise ValueError("Invalid value for `forward_to_recipients`, must not be `None`")  # noqa: E501

        self._forward_to_recipients = forward_to_recipients

    @property
    def id(self):
        """Gets the id of this InboxForwarderDto.  # noqa: E501


        :return: The id of this InboxForwarderDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InboxForwarderDto.


        :param id: The id of this InboxForwarderDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def inbox_id(self):
        """Gets the inbox_id of this InboxForwarderDto.  # noqa: E501


        :return: The inbox_id of this InboxForwarderDto.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this InboxForwarderDto.


        :param inbox_id: The inbox_id of this InboxForwarderDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and inbox_id is None:  # noqa: E501
            raise ValueError("Invalid value for `inbox_id`, must not be `None`")  # noqa: E501

        self._inbox_id = inbox_id

    @property
    def match(self):
        """Gets the match of this InboxForwarderDto.  # noqa: E501


        :return: The match of this InboxForwarderDto.  # noqa: E501
        :rtype: str
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this InboxForwarderDto.


        :param match: The match of this InboxForwarderDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and match is None:  # noqa: E501
            raise ValueError("Invalid value for `match`, must not be `None`")  # noqa: E501

        self._match = match

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
        if not isinstance(other, InboxForwarderDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InboxForwarderDto):
            return True

        return self.to_dict() != other.to_dict()
