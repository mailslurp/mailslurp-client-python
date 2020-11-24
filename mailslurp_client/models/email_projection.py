# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
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
        'attachments': 'list[str]',
        'bcc': 'list[str]',
        'body_md5_hash': 'str',
        'cc': 'list[str]',
        'created_at': 'datetime',
        '_from': 'str',
        'id': 'str',
        'inbox_id': 'str',
        'read': 'bool',
        'subject': 'str',
        'to': 'list[str]'
    }

    attribute_map = {
        'attachments': 'attachments',
        'bcc': 'bcc',
        'body_md5_hash': 'bodyMD5Hash',
        'cc': 'cc',
        'created_at': 'createdAt',
        '_from': 'from',
        'id': 'id',
        'inbox_id': 'inboxId',
        'read': 'read',
        'subject': 'subject',
        'to': 'to'
    }

    def __init__(self, attachments=None, bcc=None, body_md5_hash=None, cc=None, created_at=None, _from=None, id=None, inbox_id=None, read=None, subject=None, to=None, local_vars_configuration=None):  # noqa: E501
        """EmailProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attachments = None
        self._bcc = None
        self._body_md5_hash = None
        self._cc = None
        self._created_at = None
        self.__from = None
        self._id = None
        self._inbox_id = None
        self._read = None
        self._subject = None
        self._to = None
        self.discriminator = None

        if attachments is not None:
            self.attachments = attachments
        if bcc is not None:
            self.bcc = bcc
        if body_md5_hash is not None:
            self.body_md5_hash = body_md5_hash
        if cc is not None:
            self.cc = cc
        self.created_at = created_at
        if _from is not None:
            self._from = _from
        self.id = id
        self.inbox_id = inbox_id
        if read is not None:
            self.read = read
        if subject is not None:
            self.subject = subject
        self.to = to

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

        self._read = read

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
