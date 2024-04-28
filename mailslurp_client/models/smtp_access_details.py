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


class SmtpAccessDetails(object):
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
        'secure_smtp_server_host': 'str',
        'secure_smtp_server_port': 'int',
        'secure_smtp_username': 'str',
        'secure_smtp_password': 'str',
        'smtp_server_host': 'str',
        'smtp_server_port': 'int',
        'smtp_username': 'str',
        'smtp_password': 'str',
        'mail_from_domain': 'str'
    }

    attribute_map = {
        'secure_smtp_server_host': 'secureSmtpServerHost',
        'secure_smtp_server_port': 'secureSmtpServerPort',
        'secure_smtp_username': 'secureSmtpUsername',
        'secure_smtp_password': 'secureSmtpPassword',
        'smtp_server_host': 'smtpServerHost',
        'smtp_server_port': 'smtpServerPort',
        'smtp_username': 'smtpUsername',
        'smtp_password': 'smtpPassword',
        'mail_from_domain': 'mailFromDomain'
    }

    def __init__(self, secure_smtp_server_host=None, secure_smtp_server_port=None, secure_smtp_username=None, secure_smtp_password=None, smtp_server_host=None, smtp_server_port=None, smtp_username=None, smtp_password=None, mail_from_domain=None, local_vars_configuration=None):  # noqa: E501
        """SmtpAccessDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._secure_smtp_server_host = None
        self._secure_smtp_server_port = None
        self._secure_smtp_username = None
        self._secure_smtp_password = None
        self._smtp_server_host = None
        self._smtp_server_port = None
        self._smtp_username = None
        self._smtp_password = None
        self._mail_from_domain = None
        self.discriminator = None

        self.secure_smtp_server_host = secure_smtp_server_host
        self.secure_smtp_server_port = secure_smtp_server_port
        self.secure_smtp_username = secure_smtp_username
        self.secure_smtp_password = secure_smtp_password
        self.smtp_server_host = smtp_server_host
        self.smtp_server_port = smtp_server_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.mail_from_domain = mail_from_domain

    @property
    def secure_smtp_server_host(self):
        """Gets the secure_smtp_server_host of this SmtpAccessDetails.  # noqa: E501

        Secure TLS SMTP server host domain  # noqa: E501

        :return: The secure_smtp_server_host of this SmtpAccessDetails.  # noqa: E501
        :rtype: str
        """
        return self._secure_smtp_server_host

    @secure_smtp_server_host.setter
    def secure_smtp_server_host(self, secure_smtp_server_host):
        """Sets the secure_smtp_server_host of this SmtpAccessDetails.

        Secure TLS SMTP server host domain  # noqa: E501

        :param secure_smtp_server_host: The secure_smtp_server_host of this SmtpAccessDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and secure_smtp_server_host is None:  # noqa: E501
            raise ValueError("Invalid value for `secure_smtp_server_host`, must not be `None`")  # noqa: E501

        self._secure_smtp_server_host = secure_smtp_server_host

    @property
    def secure_smtp_server_port(self):
        """Gets the secure_smtp_server_port of this SmtpAccessDetails.  # noqa: E501

        Secure TLS SMTP server host port  # noqa: E501

        :return: The secure_smtp_server_port of this SmtpAccessDetails.  # noqa: E501
        :rtype: int
        """
        return self._secure_smtp_server_port

    @secure_smtp_server_port.setter
    def secure_smtp_server_port(self, secure_smtp_server_port):
        """Sets the secure_smtp_server_port of this SmtpAccessDetails.

        Secure TLS SMTP server host port  # noqa: E501

        :param secure_smtp_server_port: The secure_smtp_server_port of this SmtpAccessDetails.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and secure_smtp_server_port is None:  # noqa: E501
            raise ValueError("Invalid value for `secure_smtp_server_port`, must not be `None`")  # noqa: E501

        self._secure_smtp_server_port = secure_smtp_server_port

    @property
    def secure_smtp_username(self):
        """Gets the secure_smtp_username of this SmtpAccessDetails.  # noqa: E501

        Secure TLS SMTP username for login  # noqa: E501

        :return: The secure_smtp_username of this SmtpAccessDetails.  # noqa: E501
        :rtype: str
        """
        return self._secure_smtp_username

    @secure_smtp_username.setter
    def secure_smtp_username(self, secure_smtp_username):
        """Sets the secure_smtp_username of this SmtpAccessDetails.

        Secure TLS SMTP username for login  # noqa: E501

        :param secure_smtp_username: The secure_smtp_username of this SmtpAccessDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and secure_smtp_username is None:  # noqa: E501
            raise ValueError("Invalid value for `secure_smtp_username`, must not be `None`")  # noqa: E501

        self._secure_smtp_username = secure_smtp_username

    @property
    def secure_smtp_password(self):
        """Gets the secure_smtp_password of this SmtpAccessDetails.  # noqa: E501

        Secure TLS SMTP password for login  # noqa: E501

        :return: The secure_smtp_password of this SmtpAccessDetails.  # noqa: E501
        :rtype: str
        """
        return self._secure_smtp_password

    @secure_smtp_password.setter
    def secure_smtp_password(self, secure_smtp_password):
        """Sets the secure_smtp_password of this SmtpAccessDetails.

        Secure TLS SMTP password for login  # noqa: E501

        :param secure_smtp_password: The secure_smtp_password of this SmtpAccessDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and secure_smtp_password is None:  # noqa: E501
            raise ValueError("Invalid value for `secure_smtp_password`, must not be `None`")  # noqa: E501

        self._secure_smtp_password = secure_smtp_password

    @property
    def smtp_server_host(self):
        """Gets the smtp_server_host of this SmtpAccessDetails.  # noqa: E501

        SMTP server host domain  # noqa: E501

        :return: The smtp_server_host of this SmtpAccessDetails.  # noqa: E501
        :rtype: str
        """
        return self._smtp_server_host

    @smtp_server_host.setter
    def smtp_server_host(self, smtp_server_host):
        """Sets the smtp_server_host of this SmtpAccessDetails.

        SMTP server host domain  # noqa: E501

        :param smtp_server_host: The smtp_server_host of this SmtpAccessDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and smtp_server_host is None:  # noqa: E501
            raise ValueError("Invalid value for `smtp_server_host`, must not be `None`")  # noqa: E501

        self._smtp_server_host = smtp_server_host

    @property
    def smtp_server_port(self):
        """Gets the smtp_server_port of this SmtpAccessDetails.  # noqa: E501

        SMTP server host port  # noqa: E501

        :return: The smtp_server_port of this SmtpAccessDetails.  # noqa: E501
        :rtype: int
        """
        return self._smtp_server_port

    @smtp_server_port.setter
    def smtp_server_port(self, smtp_server_port):
        """Sets the smtp_server_port of this SmtpAccessDetails.

        SMTP server host port  # noqa: E501

        :param smtp_server_port: The smtp_server_port of this SmtpAccessDetails.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and smtp_server_port is None:  # noqa: E501
            raise ValueError("Invalid value for `smtp_server_port`, must not be `None`")  # noqa: E501

        self._smtp_server_port = smtp_server_port

    @property
    def smtp_username(self):
        """Gets the smtp_username of this SmtpAccessDetails.  # noqa: E501

        SMTP username for login  # noqa: E501

        :return: The smtp_username of this SmtpAccessDetails.  # noqa: E501
        :rtype: str
        """
        return self._smtp_username

    @smtp_username.setter
    def smtp_username(self, smtp_username):
        """Sets the smtp_username of this SmtpAccessDetails.

        SMTP username for login  # noqa: E501

        :param smtp_username: The smtp_username of this SmtpAccessDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and smtp_username is None:  # noqa: E501
            raise ValueError("Invalid value for `smtp_username`, must not be `None`")  # noqa: E501

        self._smtp_username = smtp_username

    @property
    def smtp_password(self):
        """Gets the smtp_password of this SmtpAccessDetails.  # noqa: E501

        SMTP password for login  # noqa: E501

        :return: The smtp_password of this SmtpAccessDetails.  # noqa: E501
        :rtype: str
        """
        return self._smtp_password

    @smtp_password.setter
    def smtp_password(self, smtp_password):
        """Sets the smtp_password of this SmtpAccessDetails.

        SMTP password for login  # noqa: E501

        :param smtp_password: The smtp_password of this SmtpAccessDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and smtp_password is None:  # noqa: E501
            raise ValueError("Invalid value for `smtp_password`, must not be `None`")  # noqa: E501

        self._smtp_password = smtp_password

    @property
    def mail_from_domain(self):
        """Gets the mail_from_domain of this SmtpAccessDetails.  # noqa: E501

        Mail from domain or SMTP HELO value  # noqa: E501

        :return: The mail_from_domain of this SmtpAccessDetails.  # noqa: E501
        :rtype: str
        """
        return self._mail_from_domain

    @mail_from_domain.setter
    def mail_from_domain(self, mail_from_domain):
        """Sets the mail_from_domain of this SmtpAccessDetails.

        Mail from domain or SMTP HELO value  # noqa: E501

        :param mail_from_domain: The mail_from_domain of this SmtpAccessDetails.  # noqa: E501
        :type: str
        """

        self._mail_from_domain = mail_from_domain

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
        if not isinstance(other, SmtpAccessDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmtpAccessDetails):
            return True

        return self.to_dict() != other.to_dict()