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


class ImapServerFetchItem(object):
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
        'content': 'str',
        'id': 'str',
        'uid': 'int',
        'seq_num': 'int',
        'read': 'bool'
    }

    attribute_map = {
        'content': 'content',
        'id': 'id',
        'uid': 'uid',
        'seq_num': 'seqNum',
        'read': 'read'
    }

    def __init__(self, content=None, id=None, uid=None, seq_num=None, read=None, local_vars_configuration=None):  # noqa: E501
        """ImapServerFetchItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content = None
        self._id = None
        self._uid = None
        self._seq_num = None
        self._read = None
        self.discriminator = None

        self.content = content
        self.id = id
        self.uid = uid
        self.seq_num = seq_num
        self.read = read

    @property
    def content(self):
        """Gets the content of this ImapServerFetchItem.  # noqa: E501

        Content of the email  # noqa: E501

        :return: The content of this ImapServerFetchItem.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ImapServerFetchItem.

        Content of the email  # noqa: E501

        :param content: The content of this ImapServerFetchItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def id(self):
        """Gets the id of this ImapServerFetchItem.  # noqa: E501

        ID of the email  # noqa: E501

        :return: The id of this ImapServerFetchItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImapServerFetchItem.

        ID of the email  # noqa: E501

        :param id: The id of this ImapServerFetchItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def uid(self):
        """Gets the uid of this ImapServerFetchItem.  # noqa: E501

        UID of the email  # noqa: E501

        :return: The uid of this ImapServerFetchItem.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ImapServerFetchItem.

        UID of the email  # noqa: E501

        :param uid: The uid of this ImapServerFetchItem.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def seq_num(self):
        """Gets the seq_num of this ImapServerFetchItem.  # noqa: E501

        Sequence number of the email  # noqa: E501

        :return: The seq_num of this ImapServerFetchItem.  # noqa: E501
        :rtype: int
        """
        return self._seq_num

    @seq_num.setter
    def seq_num(self, seq_num):
        """Sets the seq_num of this ImapServerFetchItem.

        Sequence number of the email  # noqa: E501

        :param seq_num: The seq_num of this ImapServerFetchItem.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and seq_num is None:  # noqa: E501
            raise ValueError("Invalid value for `seq_num`, must not be `None`")  # noqa: E501

        self._seq_num = seq_num

    @property
    def read(self):
        """Gets the read of this ImapServerFetchItem.  # noqa: E501

        Read status of the email  # noqa: E501

        :return: The read of this ImapServerFetchItem.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this ImapServerFetchItem.

        Read status of the email  # noqa: E501

        :param read: The read of this ImapServerFetchItem.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and read is None:  # noqa: E501
            raise ValueError("Invalid value for `read`, must not be `None`")  # noqa: E501

        self._read = read

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
        if not isinstance(other, ImapServerFetchItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImapServerFetchItem):
            return True

        return self.to_dict() != other.to_dict()
