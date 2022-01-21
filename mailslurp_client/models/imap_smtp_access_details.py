# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class ImapSmtpAccessDetails(object):
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
        'smtp_server_host': 'str',
        'smtp_server_port': 'int',
        'smtp_username': 'str',
        'smtp_password': 'str',
        'imap_server_host': 'str',
        'imap_server_port': 'int',
        'imap_username': 'str',
        'imap_password': 'str'
    }

    attribute_map = {
        'smtp_server_host': 'smtpServerHost',
        'smtp_server_port': 'smtpServerPort',
        'smtp_username': 'smtpUsername',
        'smtp_password': 'smtpPassword',
        'imap_server_host': 'imapServerHost',
        'imap_server_port': 'imapServerPort',
        'imap_username': 'imapUsername',
        'imap_password': 'imapPassword'
    }

    def __init__(self, smtp_server_host=None, smtp_server_port=None, smtp_username=None, smtp_password=None, imap_server_host=None, imap_server_port=None, imap_username=None, imap_password=None, local_vars_configuration=None):  # noqa: E501
        """ImapSmtpAccessDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._smtp_server_host = None
        self._smtp_server_port = None
        self._smtp_username = None
        self._smtp_password = None
        self._imap_server_host = None
        self._imap_server_port = None
        self._imap_username = None
        self._imap_password = None
        self.discriminator = None

        self.smtp_server_host = smtp_server_host
        self.smtp_server_port = smtp_server_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.imap_server_host = imap_server_host
        self.imap_server_port = imap_server_port
        self.imap_username = imap_username
        self.imap_password = imap_password

    @property
    def smtp_server_host(self):
        """Gets the smtp_server_host of this ImapSmtpAccessDetails.  # noqa: E501


        :return: The smtp_server_host of this ImapSmtpAccessDetails.  # noqa: E501
        :rtype: str
        """
        return self._smtp_server_host

    @smtp_server_host.setter
    def smtp_server_host(self, smtp_server_host):
        """Sets the smtp_server_host of this ImapSmtpAccessDetails.


        :param smtp_server_host: The smtp_server_host of this ImapSmtpAccessDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and smtp_server_host is None:  # noqa: E501
            raise ValueError("Invalid value for `smtp_server_host`, must not be `None`")  # noqa: E501

        self._smtp_server_host = smtp_server_host

    @property
    def smtp_server_port(self):
        """Gets the smtp_server_port of this ImapSmtpAccessDetails.  # noqa: E501


        :return: The smtp_server_port of this ImapSmtpAccessDetails.  # noqa: E501
        :rtype: int
        """
        return self._smtp_server_port

    @smtp_server_port.setter
    def smtp_server_port(self, smtp_server_port):
        """Sets the smtp_server_port of this ImapSmtpAccessDetails.


        :param smtp_server_port: The smtp_server_port of this ImapSmtpAccessDetails.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and smtp_server_port is None:  # noqa: E501
            raise ValueError("Invalid value for `smtp_server_port`, must not be `None`")  # noqa: E501

        self._smtp_server_port = smtp_server_port

    @property
    def smtp_username(self):
        """Gets the smtp_username of this ImapSmtpAccessDetails.  # noqa: E501


        :return: The smtp_username of this ImapSmtpAccessDetails.  # noqa: E501
        :rtype: str
        """
        return self._smtp_username

    @smtp_username.setter
    def smtp_username(self, smtp_username):
        """Sets the smtp_username of this ImapSmtpAccessDetails.


        :param smtp_username: The smtp_username of this ImapSmtpAccessDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and smtp_username is None:  # noqa: E501
            raise ValueError("Invalid value for `smtp_username`, must not be `None`")  # noqa: E501

        self._smtp_username = smtp_username

    @property
    def smtp_password(self):
        """Gets the smtp_password of this ImapSmtpAccessDetails.  # noqa: E501


        :return: The smtp_password of this ImapSmtpAccessDetails.  # noqa: E501
        :rtype: str
        """
        return self._smtp_password

    @smtp_password.setter
    def smtp_password(self, smtp_password):
        """Sets the smtp_password of this ImapSmtpAccessDetails.


        :param smtp_password: The smtp_password of this ImapSmtpAccessDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and smtp_password is None:  # noqa: E501
            raise ValueError("Invalid value for `smtp_password`, must not be `None`")  # noqa: E501

        self._smtp_password = smtp_password

    @property
    def imap_server_host(self):
        """Gets the imap_server_host of this ImapSmtpAccessDetails.  # noqa: E501


        :return: The imap_server_host of this ImapSmtpAccessDetails.  # noqa: E501
        :rtype: str
        """
        return self._imap_server_host

    @imap_server_host.setter
    def imap_server_host(self, imap_server_host):
        """Sets the imap_server_host of this ImapSmtpAccessDetails.


        :param imap_server_host: The imap_server_host of this ImapSmtpAccessDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and imap_server_host is None:  # noqa: E501
            raise ValueError("Invalid value for `imap_server_host`, must not be `None`")  # noqa: E501

        self._imap_server_host = imap_server_host

    @property
    def imap_server_port(self):
        """Gets the imap_server_port of this ImapSmtpAccessDetails.  # noqa: E501


        :return: The imap_server_port of this ImapSmtpAccessDetails.  # noqa: E501
        :rtype: int
        """
        return self._imap_server_port

    @imap_server_port.setter
    def imap_server_port(self, imap_server_port):
        """Sets the imap_server_port of this ImapSmtpAccessDetails.


        :param imap_server_port: The imap_server_port of this ImapSmtpAccessDetails.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and imap_server_port is None:  # noqa: E501
            raise ValueError("Invalid value for `imap_server_port`, must not be `None`")  # noqa: E501

        self._imap_server_port = imap_server_port

    @property
    def imap_username(self):
        """Gets the imap_username of this ImapSmtpAccessDetails.  # noqa: E501


        :return: The imap_username of this ImapSmtpAccessDetails.  # noqa: E501
        :rtype: str
        """
        return self._imap_username

    @imap_username.setter
    def imap_username(self, imap_username):
        """Sets the imap_username of this ImapSmtpAccessDetails.


        :param imap_username: The imap_username of this ImapSmtpAccessDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and imap_username is None:  # noqa: E501
            raise ValueError("Invalid value for `imap_username`, must not be `None`")  # noqa: E501

        self._imap_username = imap_username

    @property
    def imap_password(self):
        """Gets the imap_password of this ImapSmtpAccessDetails.  # noqa: E501


        :return: The imap_password of this ImapSmtpAccessDetails.  # noqa: E501
        :rtype: str
        """
        return self._imap_password

    @imap_password.setter
    def imap_password(self, imap_password):
        """Sets the imap_password of this ImapSmtpAccessDetails.


        :param imap_password: The imap_password of this ImapSmtpAccessDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and imap_password is None:  # noqa: E501
            raise ValueError("Invalid value for `imap_password`, must not be `None`")  # noqa: E501

        self._imap_password = imap_password

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
        if not isinstance(other, ImapSmtpAccessDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImapSmtpAccessDetails):
            return True

        return self.to_dict() != other.to_dict()