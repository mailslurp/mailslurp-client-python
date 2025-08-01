# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails and SMS from dynamically allocated email addresses and phone numbers. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class SentEmailProjection(object):
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
        'id': 'str',
        'recipients': 'EmailRecipients',
        '_from': 'str',
        'sender': 'Sender',
        'subject': 'str',
        'attachments': 'list[str]',
        'inbox_id': 'str',
        'user_id': 'str',
        'created_at': 'datetime',
        'to': 'list[str]',
        'cc': 'list[str]',
        'bcc': 'list[str]',
        'message_id': 'str',
        'in_reply_to': 'str',
        'body_excerpt': 'str',
        'text_excerpt': 'str',
        'body_md5_hash': 'str',
        'virtual_send': 'bool',
        'thread_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'recipients': 'recipients',
        '_from': 'from',
        'sender': 'sender',
        'subject': 'subject',
        'attachments': 'attachments',
        'inbox_id': 'inboxId',
        'user_id': 'userId',
        'created_at': 'createdAt',
        'to': 'to',
        'cc': 'cc',
        'bcc': 'bcc',
        'message_id': 'messageId',
        'in_reply_to': 'inReplyTo',
        'body_excerpt': 'bodyExcerpt',
        'text_excerpt': 'textExcerpt',
        'body_md5_hash': 'bodyMD5Hash',
        'virtual_send': 'virtualSend',
        'thread_id': 'threadId'
    }

    def __init__(self, id=None, recipients=None, _from=None, sender=None, subject=None, attachments=None, inbox_id=None, user_id=None, created_at=None, to=None, cc=None, bcc=None, message_id=None, in_reply_to=None, body_excerpt=None, text_excerpt=None, body_md5_hash=None, virtual_send=None, thread_id=None, local_vars_configuration=None):  # noqa: E501
        """SentEmailProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._recipients = None
        self.__from = None
        self._sender = None
        self._subject = None
        self._attachments = None
        self._inbox_id = None
        self._user_id = None
        self._created_at = None
        self._to = None
        self._cc = None
        self._bcc = None
        self._message_id = None
        self._in_reply_to = None
        self._body_excerpt = None
        self._text_excerpt = None
        self._body_md5_hash = None
        self._virtual_send = None
        self._thread_id = None
        self.discriminator = None

        self.id = id
        self.recipients = recipients
        self._from = _from
        self.sender = sender
        self.subject = subject
        self.attachments = attachments
        self.inbox_id = inbox_id
        self.user_id = user_id
        self.created_at = created_at
        if to is not None:
            self.to = to
        if cc is not None:
            self.cc = cc
        if bcc is not None:
            self.bcc = bcc
        self.message_id = message_id
        self.in_reply_to = in_reply_to
        self.body_excerpt = body_excerpt
        self.text_excerpt = text_excerpt
        self.body_md5_hash = body_md5_hash
        self.virtual_send = virtual_send
        self.thread_id = thread_id

    @property
    def id(self):
        """Gets the id of this SentEmailProjection.  # noqa: E501


        :return: The id of this SentEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SentEmailProjection.


        :param id: The id of this SentEmailProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def recipients(self):
        """Gets the recipients of this SentEmailProjection.  # noqa: E501


        :return: The recipients of this SentEmailProjection.  # noqa: E501
        :rtype: EmailRecipients
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this SentEmailProjection.


        :param recipients: The recipients of this SentEmailProjection.  # noqa: E501
        :type: EmailRecipients
        """

        self._recipients = recipients

    @property
    def _from(self):
        """Gets the _from of this SentEmailProjection.  # noqa: E501


        :return: The _from of this SentEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this SentEmailProjection.


        :param _from: The _from of this SentEmailProjection.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def sender(self):
        """Gets the sender of this SentEmailProjection.  # noqa: E501


        :return: The sender of this SentEmailProjection.  # noqa: E501
        :rtype: Sender
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this SentEmailProjection.


        :param sender: The sender of this SentEmailProjection.  # noqa: E501
        :type: Sender
        """

        self._sender = sender

    @property
    def subject(self):
        """Gets the subject of this SentEmailProjection.  # noqa: E501


        :return: The subject of this SentEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this SentEmailProjection.


        :param subject: The subject of this SentEmailProjection.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def attachments(self):
        """Gets the attachments of this SentEmailProjection.  # noqa: E501


        :return: The attachments of this SentEmailProjection.  # noqa: E501
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this SentEmailProjection.


        :param attachments: The attachments of this SentEmailProjection.  # noqa: E501
        :type: list[str]
        """

        self._attachments = attachments

    @property
    def inbox_id(self):
        """Gets the inbox_id of this SentEmailProjection.  # noqa: E501


        :return: The inbox_id of this SentEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this SentEmailProjection.


        :param inbox_id: The inbox_id of this SentEmailProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and inbox_id is None:  # noqa: E501
            raise ValueError("Invalid value for `inbox_id`, must not be `None`")  # noqa: E501

        self._inbox_id = inbox_id

    @property
    def user_id(self):
        """Gets the user_id of this SentEmailProjection.  # noqa: E501


        :return: The user_id of this SentEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SentEmailProjection.


        :param user_id: The user_id of this SentEmailProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def created_at(self):
        """Gets the created_at of this SentEmailProjection.  # noqa: E501


        :return: The created_at of this SentEmailProjection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SentEmailProjection.


        :param created_at: The created_at of this SentEmailProjection.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def to(self):
        """Gets the to of this SentEmailProjection.  # noqa: E501


        :return: The to of this SentEmailProjection.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SentEmailProjection.


        :param to: The to of this SentEmailProjection.  # noqa: E501
        :type: list[str]
        """

        self._to = to

    @property
    def cc(self):
        """Gets the cc of this SentEmailProjection.  # noqa: E501


        :return: The cc of this SentEmailProjection.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this SentEmailProjection.


        :param cc: The cc of this SentEmailProjection.  # noqa: E501
        :type: list[str]
        """

        self._cc = cc

    @property
    def bcc(self):
        """Gets the bcc of this SentEmailProjection.  # noqa: E501


        :return: The bcc of this SentEmailProjection.  # noqa: E501
        :rtype: list[str]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this SentEmailProjection.


        :param bcc: The bcc of this SentEmailProjection.  # noqa: E501
        :type: list[str]
        """

        self._bcc = bcc

    @property
    def message_id(self):
        """Gets the message_id of this SentEmailProjection.  # noqa: E501


        :return: The message_id of this SentEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this SentEmailProjection.


        :param message_id: The message_id of this SentEmailProjection.  # noqa: E501
        :type: str
        """

        self._message_id = message_id

    @property
    def in_reply_to(self):
        """Gets the in_reply_to of this SentEmailProjection.  # noqa: E501


        :return: The in_reply_to of this SentEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._in_reply_to

    @in_reply_to.setter
    def in_reply_to(self, in_reply_to):
        """Sets the in_reply_to of this SentEmailProjection.


        :param in_reply_to: The in_reply_to of this SentEmailProjection.  # noqa: E501
        :type: str
        """

        self._in_reply_to = in_reply_to

    @property
    def body_excerpt(self):
        """Gets the body_excerpt of this SentEmailProjection.  # noqa: E501


        :return: The body_excerpt of this SentEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._body_excerpt

    @body_excerpt.setter
    def body_excerpt(self, body_excerpt):
        """Sets the body_excerpt of this SentEmailProjection.


        :param body_excerpt: The body_excerpt of this SentEmailProjection.  # noqa: E501
        :type: str
        """

        self._body_excerpt = body_excerpt

    @property
    def text_excerpt(self):
        """Gets the text_excerpt of this SentEmailProjection.  # noqa: E501


        :return: The text_excerpt of this SentEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._text_excerpt

    @text_excerpt.setter
    def text_excerpt(self, text_excerpt):
        """Sets the text_excerpt of this SentEmailProjection.


        :param text_excerpt: The text_excerpt of this SentEmailProjection.  # noqa: E501
        :type: str
        """

        self._text_excerpt = text_excerpt

    @property
    def body_md5_hash(self):
        """Gets the body_md5_hash of this SentEmailProjection.  # noqa: E501


        :return: The body_md5_hash of this SentEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._body_md5_hash

    @body_md5_hash.setter
    def body_md5_hash(self, body_md5_hash):
        """Sets the body_md5_hash of this SentEmailProjection.


        :param body_md5_hash: The body_md5_hash of this SentEmailProjection.  # noqa: E501
        :type: str
        """

        self._body_md5_hash = body_md5_hash

    @property
    def virtual_send(self):
        """Gets the virtual_send of this SentEmailProjection.  # noqa: E501


        :return: The virtual_send of this SentEmailProjection.  # noqa: E501
        :rtype: bool
        """
        return self._virtual_send

    @virtual_send.setter
    def virtual_send(self, virtual_send):
        """Sets the virtual_send of this SentEmailProjection.


        :param virtual_send: The virtual_send of this SentEmailProjection.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and virtual_send is None:  # noqa: E501
            raise ValueError("Invalid value for `virtual_send`, must not be `None`")  # noqa: E501

        self._virtual_send = virtual_send

    @property
    def thread_id(self):
        """Gets the thread_id of this SentEmailProjection.  # noqa: E501


        :return: The thread_id of this SentEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        """Sets the thread_id of this SentEmailProjection.


        :param thread_id: The thread_id of this SentEmailProjection.  # noqa: E501
        :type: str
        """

        self._thread_id = thread_id

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
        if not isinstance(other, SentEmailProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SentEmailProjection):
            return True

        return self.to_dict() != other.to_dict()
