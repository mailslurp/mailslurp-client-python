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


class EmailProjection(object):
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
        'recipients': 'EmailRecipients',
        'sender': 'Sender',
        'attachments': 'list[str]',
        'inbox_id': 'str',
        'created_at': 'datetime',
        'to': 'list[str]',
        'cc': 'list[str]',
        'bcc': 'list[str]',
        'message_id': 'str',
        'domain_id': 'str',
        'favourite': 'bool',
        'plus_address': 'str',
        'size_bytes': 'int',
        'in_reply_to': 'str',
        'read': 'bool',
        'body_excerpt': 'str',
        'text_excerpt': 'str',
        'body_part_content_types': 'list[str]',
        'body_md5_hash': 'str',
        'team_access': 'bool',
        'subject': 'str',
        'id': 'str',
        'thread_id': 'str',
        '_from': 'str'
    }

    attribute_map = {
        'recipients': 'recipients',
        'sender': 'sender',
        'attachments': 'attachments',
        'inbox_id': 'inboxId',
        'created_at': 'createdAt',
        'to': 'to',
        'cc': 'cc',
        'bcc': 'bcc',
        'message_id': 'messageId',
        'domain_id': 'domainId',
        'favourite': 'favourite',
        'plus_address': 'plusAddress',
        'size_bytes': 'sizeBytes',
        'in_reply_to': 'inReplyTo',
        'read': 'read',
        'body_excerpt': 'bodyExcerpt',
        'text_excerpt': 'textExcerpt',
        'body_part_content_types': 'bodyPartContentTypes',
        'body_md5_hash': 'bodyMD5Hash',
        'team_access': 'teamAccess',
        'subject': 'subject',
        'id': 'id',
        'thread_id': 'threadId',
        '_from': 'from'
    }

    def __init__(self, recipients=None, sender=None, attachments=None, inbox_id=None, created_at=None, to=None, cc=None, bcc=None, message_id=None, domain_id=None, favourite=None, plus_address=None, size_bytes=None, in_reply_to=None, read=None, body_excerpt=None, text_excerpt=None, body_part_content_types=None, body_md5_hash=None, team_access=None, subject=None, id=None, thread_id=None, _from=None, local_vars_configuration=None):  # noqa: E501
        """EmailProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._recipients = None
        self._sender = None
        self._attachments = None
        self._inbox_id = None
        self._created_at = None
        self._to = None
        self._cc = None
        self._bcc = None
        self._message_id = None
        self._domain_id = None
        self._favourite = None
        self._plus_address = None
        self._size_bytes = None
        self._in_reply_to = None
        self._read = None
        self._body_excerpt = None
        self._text_excerpt = None
        self._body_part_content_types = None
        self._body_md5_hash = None
        self._team_access = None
        self._subject = None
        self._id = None
        self._thread_id = None
        self.__from = None
        self.discriminator = None

        self.recipients = recipients
        self.sender = sender
        self.attachments = attachments
        self.inbox_id = inbox_id
        self.created_at = created_at
        self.to = to
        self.cc = cc
        self.bcc = bcc
        self.message_id = message_id
        self.domain_id = domain_id
        self.favourite = favourite
        self.plus_address = plus_address
        self.size_bytes = size_bytes
        self.in_reply_to = in_reply_to
        self.read = read
        self.body_excerpt = body_excerpt
        self.text_excerpt = text_excerpt
        self.body_part_content_types = body_part_content_types
        self.body_md5_hash = body_md5_hash
        self.team_access = team_access
        self.subject = subject
        self.id = id
        self.thread_id = thread_id
        self._from = _from

    @property
    def recipients(self):
        """Gets the recipients of this EmailProjection.  # noqa: E501


        :return: The recipients of this EmailProjection.  # noqa: E501
        :rtype: EmailRecipients
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this EmailProjection.


        :param recipients: The recipients of this EmailProjection.  # noqa: E501
        :type: EmailRecipients
        """

        self._recipients = recipients

    @property
    def sender(self):
        """Gets the sender of this EmailProjection.  # noqa: E501


        :return: The sender of this EmailProjection.  # noqa: E501
        :rtype: Sender
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this EmailProjection.


        :param sender: The sender of this EmailProjection.  # noqa: E501
        :type: Sender
        """

        self._sender = sender

    @property
    def attachments(self):
        """Gets the attachments of this EmailProjection.  # noqa: E501


        :return: The attachments of this EmailProjection.  # noqa: E501
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this EmailProjection.


        :param attachments: The attachments of this EmailProjection.  # noqa: E501
        :type: list[str]
        """

        self._attachments = attachments

    @property
    def inbox_id(self):
        """Gets the inbox_id of this EmailProjection.  # noqa: E501


        :return: The inbox_id of this EmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this EmailProjection.


        :param inbox_id: The inbox_id of this EmailProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and inbox_id is None:  # noqa: E501
            raise ValueError("Invalid value for `inbox_id`, must not be `None`")  # noqa: E501

        self._inbox_id = inbox_id

    @property
    def created_at(self):
        """Gets the created_at of this EmailProjection.  # noqa: E501


        :return: The created_at of this EmailProjection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EmailProjection.


        :param created_at: The created_at of this EmailProjection.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def to(self):
        """Gets the to of this EmailProjection.  # noqa: E501


        :return: The to of this EmailProjection.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this EmailProjection.


        :param to: The to of this EmailProjection.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def cc(self):
        """Gets the cc of this EmailProjection.  # noqa: E501


        :return: The cc of this EmailProjection.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this EmailProjection.


        :param cc: The cc of this EmailProjection.  # noqa: E501
        :type: list[str]
        """

        self._cc = cc

    @property
    def bcc(self):
        """Gets the bcc of this EmailProjection.  # noqa: E501


        :return: The bcc of this EmailProjection.  # noqa: E501
        :rtype: list[str]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this EmailProjection.


        :param bcc: The bcc of this EmailProjection.  # noqa: E501
        :type: list[str]
        """

        self._bcc = bcc

    @property
    def message_id(self):
        """Gets the message_id of this EmailProjection.  # noqa: E501


        :return: The message_id of this EmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this EmailProjection.


        :param message_id: The message_id of this EmailProjection.  # noqa: E501
        :type: str
        """

        self._message_id = message_id

    @property
    def domain_id(self):
        """Gets the domain_id of this EmailProjection.  # noqa: E501


        :return: The domain_id of this EmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this EmailProjection.


        :param domain_id: The domain_id of this EmailProjection.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def favourite(self):
        """Gets the favourite of this EmailProjection.  # noqa: E501


        :return: The favourite of this EmailProjection.  # noqa: E501
        :rtype: bool
        """
        return self._favourite

    @favourite.setter
    def favourite(self, favourite):
        """Sets the favourite of this EmailProjection.


        :param favourite: The favourite of this EmailProjection.  # noqa: E501
        :type: bool
        """

        self._favourite = favourite

    @property
    def plus_address(self):
        """Gets the plus_address of this EmailProjection.  # noqa: E501


        :return: The plus_address of this EmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._plus_address

    @plus_address.setter
    def plus_address(self, plus_address):
        """Sets the plus_address of this EmailProjection.


        :param plus_address: The plus_address of this EmailProjection.  # noqa: E501
        :type: str
        """

        self._plus_address = plus_address

    @property
    def size_bytes(self):
        """Gets the size_bytes of this EmailProjection.  # noqa: E501


        :return: The size_bytes of this EmailProjection.  # noqa: E501
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this EmailProjection.


        :param size_bytes: The size_bytes of this EmailProjection.  # noqa: E501
        :type: int
        """

        self._size_bytes = size_bytes

    @property
    def in_reply_to(self):
        """Gets the in_reply_to of this EmailProjection.  # noqa: E501


        :return: The in_reply_to of this EmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._in_reply_to

    @in_reply_to.setter
    def in_reply_to(self, in_reply_to):
        """Sets the in_reply_to of this EmailProjection.


        :param in_reply_to: The in_reply_to of this EmailProjection.  # noqa: E501
        :type: str
        """

        self._in_reply_to = in_reply_to

    @property
    def read(self):
        """Gets the read of this EmailProjection.  # noqa: E501


        :return: The read of this EmailProjection.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this EmailProjection.


        :param read: The read of this EmailProjection.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and read is None:  # noqa: E501
            raise ValueError("Invalid value for `read`, must not be `None`")  # noqa: E501

        self._read = read

    @property
    def body_excerpt(self):
        """Gets the body_excerpt of this EmailProjection.  # noqa: E501


        :return: The body_excerpt of this EmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._body_excerpt

    @body_excerpt.setter
    def body_excerpt(self, body_excerpt):
        """Sets the body_excerpt of this EmailProjection.


        :param body_excerpt: The body_excerpt of this EmailProjection.  # noqa: E501
        :type: str
        """

        self._body_excerpt = body_excerpt

    @property
    def text_excerpt(self):
        """Gets the text_excerpt of this EmailProjection.  # noqa: E501


        :return: The text_excerpt of this EmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._text_excerpt

    @text_excerpt.setter
    def text_excerpt(self, text_excerpt):
        """Sets the text_excerpt of this EmailProjection.


        :param text_excerpt: The text_excerpt of this EmailProjection.  # noqa: E501
        :type: str
        """

        self._text_excerpt = text_excerpt

    @property
    def body_part_content_types(self):
        """Gets the body_part_content_types of this EmailProjection.  # noqa: E501


        :return: The body_part_content_types of this EmailProjection.  # noqa: E501
        :rtype: list[str]
        """
        return self._body_part_content_types

    @body_part_content_types.setter
    def body_part_content_types(self, body_part_content_types):
        """Sets the body_part_content_types of this EmailProjection.


        :param body_part_content_types: The body_part_content_types of this EmailProjection.  # noqa: E501
        :type: list[str]
        """

        self._body_part_content_types = body_part_content_types

    @property
    def body_md5_hash(self):
        """Gets the body_md5_hash of this EmailProjection.  # noqa: E501


        :return: The body_md5_hash of this EmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._body_md5_hash

    @body_md5_hash.setter
    def body_md5_hash(self, body_md5_hash):
        """Sets the body_md5_hash of this EmailProjection.


        :param body_md5_hash: The body_md5_hash of this EmailProjection.  # noqa: E501
        :type: str
        """

        self._body_md5_hash = body_md5_hash

    @property
    def team_access(self):
        """Gets the team_access of this EmailProjection.  # noqa: E501


        :return: The team_access of this EmailProjection.  # noqa: E501
        :rtype: bool
        """
        return self._team_access

    @team_access.setter
    def team_access(self, team_access):
        """Sets the team_access of this EmailProjection.


        :param team_access: The team_access of this EmailProjection.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and team_access is None:  # noqa: E501
            raise ValueError("Invalid value for `team_access`, must not be `None`")  # noqa: E501

        self._team_access = team_access

    @property
    def subject(self):
        """Gets the subject of this EmailProjection.  # noqa: E501


        :return: The subject of this EmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this EmailProjection.


        :param subject: The subject of this EmailProjection.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def id(self):
        """Gets the id of this EmailProjection.  # noqa: E501


        :return: The id of this EmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmailProjection.


        :param id: The id of this EmailProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def thread_id(self):
        """Gets the thread_id of this EmailProjection.  # noqa: E501


        :return: The thread_id of this EmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        """Sets the thread_id of this EmailProjection.


        :param thread_id: The thread_id of this EmailProjection.  # noqa: E501
        :type: str
        """

        self._thread_id = thread_id

    @property
    def _from(self):
        """Gets the _from of this EmailProjection.  # noqa: E501


        :return: The _from of this EmailProjection.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this EmailProjection.


        :param _from: The _from of this EmailProjection.  # noqa: E501
        :type: str
        """

        self.__from = _from

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
        if not isinstance(other, EmailProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailProjection):
            return True

        return self.to_dict() != other.to_dict()
