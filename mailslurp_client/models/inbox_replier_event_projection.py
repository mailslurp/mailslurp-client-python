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


class InboxReplierEventProjection(object):
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
        'message': 'str',
        'id': 'str',
        'status': 'str',
        'user_id': 'str',
        'recipients': 'list[str]',
        'email_id': 'str',
        'inbox_id': 'str',
        'created_at': 'datetime',
        'sent_id': 'str',
        'replier_id': 'str'
    }

    attribute_map = {
        'message': 'message',
        'id': 'id',
        'status': 'status',
        'user_id': 'userId',
        'recipients': 'recipients',
        'email_id': 'emailId',
        'inbox_id': 'inboxId',
        'created_at': 'createdAt',
        'sent_id': 'sentId',
        'replier_id': 'replierId'
    }

    def __init__(self, message=None, id=None, status=None, user_id=None, recipients=None, email_id=None, inbox_id=None, created_at=None, sent_id=None, replier_id=None, local_vars_configuration=None):  # noqa: E501
        """InboxReplierEventProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message = None
        self._id = None
        self._status = None
        self._user_id = None
        self._recipients = None
        self._email_id = None
        self._inbox_id = None
        self._created_at = None
        self._sent_id = None
        self._replier_id = None
        self.discriminator = None

        self.message = message
        self.id = id
        self.status = status
        self.user_id = user_id
        self.recipients = recipients
        self.email_id = email_id
        self.inbox_id = inbox_id
        self.created_at = created_at
        self.sent_id = sent_id
        self.replier_id = replier_id

    @property
    def message(self):
        """Gets the message of this InboxReplierEventProjection.  # noqa: E501


        :return: The message of this InboxReplierEventProjection.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InboxReplierEventProjection.


        :param message: The message of this InboxReplierEventProjection.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def id(self):
        """Gets the id of this InboxReplierEventProjection.  # noqa: E501


        :return: The id of this InboxReplierEventProjection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InboxReplierEventProjection.


        :param id: The id of this InboxReplierEventProjection.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this InboxReplierEventProjection.  # noqa: E501


        :return: The status of this InboxReplierEventProjection.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InboxReplierEventProjection.


        :param status: The status of this InboxReplierEventProjection.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"SUCCESS", "FAILURE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def user_id(self):
        """Gets the user_id of this InboxReplierEventProjection.  # noqa: E501


        :return: The user_id of this InboxReplierEventProjection.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this InboxReplierEventProjection.


        :param user_id: The user_id of this InboxReplierEventProjection.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def recipients(self):
        """Gets the recipients of this InboxReplierEventProjection.  # noqa: E501


        :return: The recipients of this InboxReplierEventProjection.  # noqa: E501
        :rtype: list[str]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this InboxReplierEventProjection.


        :param recipients: The recipients of this InboxReplierEventProjection.  # noqa: E501
        :type: list[str]
        """

        self._recipients = recipients

    @property
    def email_id(self):
        """Gets the email_id of this InboxReplierEventProjection.  # noqa: E501


        :return: The email_id of this InboxReplierEventProjection.  # noqa: E501
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        """Sets the email_id of this InboxReplierEventProjection.


        :param email_id: The email_id of this InboxReplierEventProjection.  # noqa: E501
        :type: str
        """

        self._email_id = email_id

    @property
    def inbox_id(self):
        """Gets the inbox_id of this InboxReplierEventProjection.  # noqa: E501


        :return: The inbox_id of this InboxReplierEventProjection.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this InboxReplierEventProjection.


        :param inbox_id: The inbox_id of this InboxReplierEventProjection.  # noqa: E501
        :type: str
        """

        self._inbox_id = inbox_id

    @property
    def created_at(self):
        """Gets the created_at of this InboxReplierEventProjection.  # noqa: E501


        :return: The created_at of this InboxReplierEventProjection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InboxReplierEventProjection.


        :param created_at: The created_at of this InboxReplierEventProjection.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def sent_id(self):
        """Gets the sent_id of this InboxReplierEventProjection.  # noqa: E501


        :return: The sent_id of this InboxReplierEventProjection.  # noqa: E501
        :rtype: str
        """
        return self._sent_id

    @sent_id.setter
    def sent_id(self, sent_id):
        """Sets the sent_id of this InboxReplierEventProjection.


        :param sent_id: The sent_id of this InboxReplierEventProjection.  # noqa: E501
        :type: str
        """

        self._sent_id = sent_id

    @property
    def replier_id(self):
        """Gets the replier_id of this InboxReplierEventProjection.  # noqa: E501


        :return: The replier_id of this InboxReplierEventProjection.  # noqa: E501
        :rtype: str
        """
        return self._replier_id

    @replier_id.setter
    def replier_id(self, replier_id):
        """Sets the replier_id of this InboxReplierEventProjection.


        :param replier_id: The replier_id of this InboxReplierEventProjection.  # noqa: E501
        :type: str
        """

        self._replier_id = replier_id

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
        if not isinstance(other, InboxReplierEventProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InboxReplierEventProjection):
            return True

        return self.to_dict() != other.to_dict()
