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


class TrackingPixelProjection(object):
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
        'name': 'str',
        'id': 'str',
        'user_id': 'str',
        'sent_email_id': 'str',
        'inbox_id': 'str',
        'created_at': 'datetime',
        'recipient': 'str',
        'seen': 'bool',
        'seen_at': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'user_id': 'userId',
        'sent_email_id': 'sentEmailId',
        'inbox_id': 'inboxId',
        'created_at': 'createdAt',
        'recipient': 'recipient',
        'seen': 'seen',
        'seen_at': 'seenAt'
    }

    def __init__(self, name=None, id=None, user_id=None, sent_email_id=None, inbox_id=None, created_at=None, recipient=None, seen=None, seen_at=None, local_vars_configuration=None):  # noqa: E501
        """TrackingPixelProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._id = None
        self._user_id = None
        self._sent_email_id = None
        self._inbox_id = None
        self._created_at = None
        self._recipient = None
        self._seen = None
        self._seen_at = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.id = id
        self.user_id = user_id
        if sent_email_id is not None:
            self.sent_email_id = sent_email_id
        if inbox_id is not None:
            self.inbox_id = inbox_id
        self.created_at = created_at
        if recipient is not None:
            self.recipient = recipient
        self.seen = seen
        if seen_at is not None:
            self.seen_at = seen_at

    @property
    def name(self):
        """Gets the name of this TrackingPixelProjection.  # noqa: E501


        :return: The name of this TrackingPixelProjection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrackingPixelProjection.


        :param name: The name of this TrackingPixelProjection.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this TrackingPixelProjection.  # noqa: E501


        :return: The id of this TrackingPixelProjection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrackingPixelProjection.


        :param id: The id of this TrackingPixelProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this TrackingPixelProjection.  # noqa: E501


        :return: The user_id of this TrackingPixelProjection.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TrackingPixelProjection.


        :param user_id: The user_id of this TrackingPixelProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def sent_email_id(self):
        """Gets the sent_email_id of this TrackingPixelProjection.  # noqa: E501


        :return: The sent_email_id of this TrackingPixelProjection.  # noqa: E501
        :rtype: str
        """
        return self._sent_email_id

    @sent_email_id.setter
    def sent_email_id(self, sent_email_id):
        """Sets the sent_email_id of this TrackingPixelProjection.


        :param sent_email_id: The sent_email_id of this TrackingPixelProjection.  # noqa: E501
        :type: str
        """

        self._sent_email_id = sent_email_id

    @property
    def inbox_id(self):
        """Gets the inbox_id of this TrackingPixelProjection.  # noqa: E501


        :return: The inbox_id of this TrackingPixelProjection.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this TrackingPixelProjection.


        :param inbox_id: The inbox_id of this TrackingPixelProjection.  # noqa: E501
        :type: str
        """

        self._inbox_id = inbox_id

    @property
    def created_at(self):
        """Gets the created_at of this TrackingPixelProjection.  # noqa: E501


        :return: The created_at of this TrackingPixelProjection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TrackingPixelProjection.


        :param created_at: The created_at of this TrackingPixelProjection.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def recipient(self):
        """Gets the recipient of this TrackingPixelProjection.  # noqa: E501


        :return: The recipient of this TrackingPixelProjection.  # noqa: E501
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this TrackingPixelProjection.


        :param recipient: The recipient of this TrackingPixelProjection.  # noqa: E501
        :type: str
        """

        self._recipient = recipient

    @property
    def seen(self):
        """Gets the seen of this TrackingPixelProjection.  # noqa: E501


        :return: The seen of this TrackingPixelProjection.  # noqa: E501
        :rtype: bool
        """
        return self._seen

    @seen.setter
    def seen(self, seen):
        """Sets the seen of this TrackingPixelProjection.


        :param seen: The seen of this TrackingPixelProjection.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and seen is None:  # noqa: E501
            raise ValueError("Invalid value for `seen`, must not be `None`")  # noqa: E501

        self._seen = seen

    @property
    def seen_at(self):
        """Gets the seen_at of this TrackingPixelProjection.  # noqa: E501


        :return: The seen_at of this TrackingPixelProjection.  # noqa: E501
        :rtype: datetime
        """
        return self._seen_at

    @seen_at.setter
    def seen_at(self, seen_at):
        """Sets the seen_at of this TrackingPixelProjection.


        :param seen_at: The seen_at of this TrackingPixelProjection.  # noqa: E501
        :type: datetime
        """

        self._seen_at = seen_at

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
        if not isinstance(other, TrackingPixelProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackingPixelProjection):
            return True

        return self.to_dict() != other.to_dict()
