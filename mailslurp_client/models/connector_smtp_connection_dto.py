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


class ConnectorSmtpConnectionDto(object):
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
        'connector_id': 'str',
        'smtp_host': 'str',
        'smtp_port': 'int',
        'smtp_username': 'str',
        'smtp_password': 'str',
        'smtp_ssl': 'bool',
        'enabled': 'bool',
        'created_at': 'datetime',
        'id': 'str'
    }

    attribute_map = {
        'connector_id': 'connectorId',
        'smtp_host': 'smtpHost',
        'smtp_port': 'smtpPort',
        'smtp_username': 'smtpUsername',
        'smtp_password': 'smtpPassword',
        'smtp_ssl': 'smtpSsl',
        'enabled': 'enabled',
        'created_at': 'createdAt',
        'id': 'id'
    }

    def __init__(self, connector_id=None, smtp_host=None, smtp_port=None, smtp_username=None, smtp_password=None, smtp_ssl=None, enabled=None, created_at=None, id=None, local_vars_configuration=None):  # noqa: E501
        """ConnectorSmtpConnectionDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._connector_id = None
        self._smtp_host = None
        self._smtp_port = None
        self._smtp_username = None
        self._smtp_password = None
        self._smtp_ssl = None
        self._enabled = None
        self._created_at = None
        self._id = None
        self.discriminator = None

        self.connector_id = connector_id
        if smtp_host is not None:
            self.smtp_host = smtp_host
        if smtp_port is not None:
            self.smtp_port = smtp_port
        if smtp_username is not None:
            self.smtp_username = smtp_username
        if smtp_password is not None:
            self.smtp_password = smtp_password
        if smtp_ssl is not None:
            self.smtp_ssl = smtp_ssl
        if enabled is not None:
            self.enabled = enabled
        self.created_at = created_at
        self.id = id

    @property
    def connector_id(self):
        """Gets the connector_id of this ConnectorSmtpConnectionDto.  # noqa: E501


        :return: The connector_id of this ConnectorSmtpConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this ConnectorSmtpConnectionDto.


        :param connector_id: The connector_id of this ConnectorSmtpConnectionDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and connector_id is None:  # noqa: E501
            raise ValueError("Invalid value for `connector_id`, must not be `None`")  # noqa: E501

        self._connector_id = connector_id

    @property
    def smtp_host(self):
        """Gets the smtp_host of this ConnectorSmtpConnectionDto.  # noqa: E501


        :return: The smtp_host of this ConnectorSmtpConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._smtp_host

    @smtp_host.setter
    def smtp_host(self, smtp_host):
        """Sets the smtp_host of this ConnectorSmtpConnectionDto.


        :param smtp_host: The smtp_host of this ConnectorSmtpConnectionDto.  # noqa: E501
        :type: str
        """

        self._smtp_host = smtp_host

    @property
    def smtp_port(self):
        """Gets the smtp_port of this ConnectorSmtpConnectionDto.  # noqa: E501


        :return: The smtp_port of this ConnectorSmtpConnectionDto.  # noqa: E501
        :rtype: int
        """
        return self._smtp_port

    @smtp_port.setter
    def smtp_port(self, smtp_port):
        """Sets the smtp_port of this ConnectorSmtpConnectionDto.


        :param smtp_port: The smtp_port of this ConnectorSmtpConnectionDto.  # noqa: E501
        :type: int
        """

        self._smtp_port = smtp_port

    @property
    def smtp_username(self):
        """Gets the smtp_username of this ConnectorSmtpConnectionDto.  # noqa: E501


        :return: The smtp_username of this ConnectorSmtpConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._smtp_username

    @smtp_username.setter
    def smtp_username(self, smtp_username):
        """Sets the smtp_username of this ConnectorSmtpConnectionDto.


        :param smtp_username: The smtp_username of this ConnectorSmtpConnectionDto.  # noqa: E501
        :type: str
        """

        self._smtp_username = smtp_username

    @property
    def smtp_password(self):
        """Gets the smtp_password of this ConnectorSmtpConnectionDto.  # noqa: E501


        :return: The smtp_password of this ConnectorSmtpConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._smtp_password

    @smtp_password.setter
    def smtp_password(self, smtp_password):
        """Sets the smtp_password of this ConnectorSmtpConnectionDto.


        :param smtp_password: The smtp_password of this ConnectorSmtpConnectionDto.  # noqa: E501
        :type: str
        """

        self._smtp_password = smtp_password

    @property
    def smtp_ssl(self):
        """Gets the smtp_ssl of this ConnectorSmtpConnectionDto.  # noqa: E501


        :return: The smtp_ssl of this ConnectorSmtpConnectionDto.  # noqa: E501
        :rtype: bool
        """
        return self._smtp_ssl

    @smtp_ssl.setter
    def smtp_ssl(self, smtp_ssl):
        """Sets the smtp_ssl of this ConnectorSmtpConnectionDto.


        :param smtp_ssl: The smtp_ssl of this ConnectorSmtpConnectionDto.  # noqa: E501
        :type: bool
        """

        self._smtp_ssl = smtp_ssl

    @property
    def enabled(self):
        """Gets the enabled of this ConnectorSmtpConnectionDto.  # noqa: E501


        :return: The enabled of this ConnectorSmtpConnectionDto.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ConnectorSmtpConnectionDto.


        :param enabled: The enabled of this ConnectorSmtpConnectionDto.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def created_at(self):
        """Gets the created_at of this ConnectorSmtpConnectionDto.  # noqa: E501


        :return: The created_at of this ConnectorSmtpConnectionDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ConnectorSmtpConnectionDto.


        :param created_at: The created_at of this ConnectorSmtpConnectionDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this ConnectorSmtpConnectionDto.  # noqa: E501


        :return: The id of this ConnectorSmtpConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectorSmtpConnectionDto.


        :param id: The id of this ConnectorSmtpConnectionDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, ConnectorSmtpConnectionDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectorSmtpConnectionDto):
            return True

        return self.to_dict() != other.to_dict()
