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


class VerifyEmailAddressOptions(object):
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
        'mail_server_domain': 'str',
        'email_address': 'str',
        'sender_email_address': 'str',
        'port': 'int'
    }

    attribute_map = {
        'mail_server_domain': 'mailServerDomain',
        'email_address': 'emailAddress',
        'sender_email_address': 'senderEmailAddress',
        'port': 'port'
    }

    def __init__(self, mail_server_domain=None, email_address=None, sender_email_address=None, port=None, local_vars_configuration=None):  # noqa: E501
        """VerifyEmailAddressOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mail_server_domain = None
        self._email_address = None
        self._sender_email_address = None
        self._port = None
        self.discriminator = None

        if mail_server_domain is not None:
            self.mail_server_domain = mail_server_domain
        self.email_address = email_address
        if sender_email_address is not None:
            self.sender_email_address = sender_email_address
        if port is not None:
            self.port = port

    @property
    def mail_server_domain(self):
        """Gets the mail_server_domain of this VerifyEmailAddressOptions.  # noqa: E501


        :return: The mail_server_domain of this VerifyEmailAddressOptions.  # noqa: E501
        :rtype: str
        """
        return self._mail_server_domain

    @mail_server_domain.setter
    def mail_server_domain(self, mail_server_domain):
        """Sets the mail_server_domain of this VerifyEmailAddressOptions.


        :param mail_server_domain: The mail_server_domain of this VerifyEmailAddressOptions.  # noqa: E501
        :type: str
        """

        self._mail_server_domain = mail_server_domain

    @property
    def email_address(self):
        """Gets the email_address of this VerifyEmailAddressOptions.  # noqa: E501


        :return: The email_address of this VerifyEmailAddressOptions.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this VerifyEmailAddressOptions.


        :param email_address: The email_address of this VerifyEmailAddressOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def sender_email_address(self):
        """Gets the sender_email_address of this VerifyEmailAddressOptions.  # noqa: E501


        :return: The sender_email_address of this VerifyEmailAddressOptions.  # noqa: E501
        :rtype: str
        """
        return self._sender_email_address

    @sender_email_address.setter
    def sender_email_address(self, sender_email_address):
        """Sets the sender_email_address of this VerifyEmailAddressOptions.


        :param sender_email_address: The sender_email_address of this VerifyEmailAddressOptions.  # noqa: E501
        :type: str
        """

        self._sender_email_address = sender_email_address

    @property
    def port(self):
        """Gets the port of this VerifyEmailAddressOptions.  # noqa: E501


        :return: The port of this VerifyEmailAddressOptions.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this VerifyEmailAddressOptions.


        :param port: The port of this VerifyEmailAddressOptions.  # noqa: E501
        :type: int
        """

        self._port = port

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
        if not isinstance(other, VerifyEmailAddressOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VerifyEmailAddressOptions):
            return True

        return self.to_dict() != other.to_dict()
