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


class ImapUpdateFlagsOptions(object):
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
        'operation': 'str',
        'flags': 'list[str]',
        'uid_set': 'str',
        'seq_set': 'str'
    }

    attribute_map = {
        'operation': 'operation',
        'flags': 'flags',
        'uid_set': 'uidSet',
        'seq_set': 'seqSet'
    }

    def __init__(self, operation=None, flags=None, uid_set=None, seq_set=None, local_vars_configuration=None):  # noqa: E501
        """ImapUpdateFlagsOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._operation = None
        self._flags = None
        self._uid_set = None
        self._seq_set = None
        self.discriminator = None

        self.operation = operation
        self.flags = flags
        self.uid_set = uid_set
        self.seq_set = seq_set

    @property
    def operation(self):
        """Gets the operation of this ImapUpdateFlagsOptions.  # noqa: E501


        :return: The operation of this ImapUpdateFlagsOptions.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this ImapUpdateFlagsOptions.


        :param operation: The operation of this ImapUpdateFlagsOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and operation is None:  # noqa: E501
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501

        self._operation = operation

    @property
    def flags(self):
        """Gets the flags of this ImapUpdateFlagsOptions.  # noqa: E501


        :return: The flags of this ImapUpdateFlagsOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this ImapUpdateFlagsOptions.


        :param flags: The flags of this ImapUpdateFlagsOptions.  # noqa: E501
        :type: list[str]
        """

        self._flags = flags

    @property
    def uid_set(self):
        """Gets the uid_set of this ImapUpdateFlagsOptions.  # noqa: E501


        :return: The uid_set of this ImapUpdateFlagsOptions.  # noqa: E501
        :rtype: str
        """
        return self._uid_set

    @uid_set.setter
    def uid_set(self, uid_set):
        """Sets the uid_set of this ImapUpdateFlagsOptions.


        :param uid_set: The uid_set of this ImapUpdateFlagsOptions.  # noqa: E501
        :type: str
        """

        self._uid_set = uid_set

    @property
    def seq_set(self):
        """Gets the seq_set of this ImapUpdateFlagsOptions.  # noqa: E501


        :return: The seq_set of this ImapUpdateFlagsOptions.  # noqa: E501
        :rtype: str
        """
        return self._seq_set

    @seq_set.setter
    def seq_set(self, seq_set):
        """Sets the seq_set of this ImapUpdateFlagsOptions.


        :param seq_set: The seq_set of this ImapUpdateFlagsOptions.  # noqa: E501
        :type: str
        """

        self._seq_set = seq_set

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
        if not isinstance(other, ImapUpdateFlagsOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImapUpdateFlagsOptions):
            return True

        return self.to_dict() != other.to_dict()
