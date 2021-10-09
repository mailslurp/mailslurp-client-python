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


class BouncedEmailDto(object):
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
        'bounce_mta': 'str',
        'bounce_recipients': 'list[str]',
        'bounce_sub_type': 'str',
        'bounce_type': 'str',
        'created_at': 'datetime',
        'id': 'str',
        'notification_type': 'str',
        'sender': 'str',
        'sent_to_recipients': 'list[str]',
        'user_id': 'str'
    }

    attribute_map = {
        'bounce_mta': 'bounceMta',
        'bounce_recipients': 'bounceRecipients',
        'bounce_sub_type': 'bounceSubType',
        'bounce_type': 'bounceType',
        'created_at': 'createdAt',
        'id': 'id',
        'notification_type': 'notificationType',
        'sender': 'sender',
        'sent_to_recipients': 'sentToRecipients',
        'user_id': 'userId'
    }

    def __init__(self, bounce_mta=None, bounce_recipients=None, bounce_sub_type=None, bounce_type=None, created_at=None, id=None, notification_type=None, sender=None, sent_to_recipients=None, user_id=None, local_vars_configuration=None):  # noqa: E501
        """BouncedEmailDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bounce_mta = None
        self._bounce_recipients = None
        self._bounce_sub_type = None
        self._bounce_type = None
        self._created_at = None
        self._id = None
        self._notification_type = None
        self._sender = None
        self._sent_to_recipients = None
        self._user_id = None
        self.discriminator = None

        if bounce_mta is not None:
            self.bounce_mta = bounce_mta
        if bounce_recipients is not None:
            self.bounce_recipients = bounce_recipients
        if bounce_sub_type is not None:
            self.bounce_sub_type = bounce_sub_type
        if bounce_type is not None:
            self.bounce_type = bounce_type
        self.created_at = created_at
        if id is not None:
            self.id = id
        self.notification_type = notification_type
        self.sender = sender
        if sent_to_recipients is not None:
            self.sent_to_recipients = sent_to_recipients
        self.user_id = user_id

    @property
    def bounce_mta(self):
        """Gets the bounce_mta of this BouncedEmailDto.  # noqa: E501


        :return: The bounce_mta of this BouncedEmailDto.  # noqa: E501
        :rtype: str
        """
        return self._bounce_mta

    @bounce_mta.setter
    def bounce_mta(self, bounce_mta):
        """Sets the bounce_mta of this BouncedEmailDto.


        :param bounce_mta: The bounce_mta of this BouncedEmailDto.  # noqa: E501
        :type: str
        """

        self._bounce_mta = bounce_mta

    @property
    def bounce_recipients(self):
        """Gets the bounce_recipients of this BouncedEmailDto.  # noqa: E501


        :return: The bounce_recipients of this BouncedEmailDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._bounce_recipients

    @bounce_recipients.setter
    def bounce_recipients(self, bounce_recipients):
        """Sets the bounce_recipients of this BouncedEmailDto.


        :param bounce_recipients: The bounce_recipients of this BouncedEmailDto.  # noqa: E501
        :type: list[str]
        """

        self._bounce_recipients = bounce_recipients

    @property
    def bounce_sub_type(self):
        """Gets the bounce_sub_type of this BouncedEmailDto.  # noqa: E501


        :return: The bounce_sub_type of this BouncedEmailDto.  # noqa: E501
        :rtype: str
        """
        return self._bounce_sub_type

    @bounce_sub_type.setter
    def bounce_sub_type(self, bounce_sub_type):
        """Sets the bounce_sub_type of this BouncedEmailDto.


        :param bounce_sub_type: The bounce_sub_type of this BouncedEmailDto.  # noqa: E501
        :type: str
        """

        self._bounce_sub_type = bounce_sub_type

    @property
    def bounce_type(self):
        """Gets the bounce_type of this BouncedEmailDto.  # noqa: E501


        :return: The bounce_type of this BouncedEmailDto.  # noqa: E501
        :rtype: str
        """
        return self._bounce_type

    @bounce_type.setter
    def bounce_type(self, bounce_type):
        """Sets the bounce_type of this BouncedEmailDto.


        :param bounce_type: The bounce_type of this BouncedEmailDto.  # noqa: E501
        :type: str
        """

        self._bounce_type = bounce_type

    @property
    def created_at(self):
        """Gets the created_at of this BouncedEmailDto.  # noqa: E501


        :return: The created_at of this BouncedEmailDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BouncedEmailDto.


        :param created_at: The created_at of this BouncedEmailDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this BouncedEmailDto.  # noqa: E501


        :return: The id of this BouncedEmailDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BouncedEmailDto.


        :param id: The id of this BouncedEmailDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def notification_type(self):
        """Gets the notification_type of this BouncedEmailDto.  # noqa: E501


        :return: The notification_type of this BouncedEmailDto.  # noqa: E501
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this BouncedEmailDto.


        :param notification_type: The notification_type of this BouncedEmailDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and notification_type is None:  # noqa: E501
            raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

        self._notification_type = notification_type

    @property
    def sender(self):
        """Gets the sender of this BouncedEmailDto.  # noqa: E501


        :return: The sender of this BouncedEmailDto.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this BouncedEmailDto.


        :param sender: The sender of this BouncedEmailDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sender is None:  # noqa: E501
            raise ValueError("Invalid value for `sender`, must not be `None`")  # noqa: E501

        self._sender = sender

    @property
    def sent_to_recipients(self):
        """Gets the sent_to_recipients of this BouncedEmailDto.  # noqa: E501


        :return: The sent_to_recipients of this BouncedEmailDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._sent_to_recipients

    @sent_to_recipients.setter
    def sent_to_recipients(self, sent_to_recipients):
        """Sets the sent_to_recipients of this BouncedEmailDto.


        :param sent_to_recipients: The sent_to_recipients of this BouncedEmailDto.  # noqa: E501
        :type: list[str]
        """

        self._sent_to_recipients = sent_to_recipients

    @property
    def user_id(self):
        """Gets the user_id of this BouncedEmailDto.  # noqa: E501


        :return: The user_id of this BouncedEmailDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BouncedEmailDto.


        :param user_id: The user_id of this BouncedEmailDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

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
        if not isinstance(other, BouncedEmailDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BouncedEmailDto):
            return True

        return self.to_dict() != other.to_dict()
