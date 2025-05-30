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


class ServerEndpoints(object):
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
        'host': 'str',
        'port': 'int',
        'tls': 'bool',
        'alt_ports': 'list[int]'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port',
        'tls': 'tls',
        'alt_ports': 'altPorts'
    }

    def __init__(self, host=None, port=None, tls=None, alt_ports=None, local_vars_configuration=None):  # noqa: E501
        """ServerEndpoints - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._host = None
        self._port = None
        self._tls = None
        self._alt_ports = None
        self.discriminator = None

        self.host = host
        self.port = port
        self.tls = tls
        self.alt_ports = alt_ports

    @property
    def host(self):
        """Gets the host of this ServerEndpoints.  # noqa: E501


        :return: The host of this ServerEndpoints.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ServerEndpoints.


        :param host: The host of this ServerEndpoints.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and host is None:  # noqa: E501
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def port(self):
        """Gets the port of this ServerEndpoints.  # noqa: E501


        :return: The port of this ServerEndpoints.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ServerEndpoints.


        :param port: The port of this ServerEndpoints.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def tls(self):
        """Gets the tls of this ServerEndpoints.  # noqa: E501


        :return: The tls of this ServerEndpoints.  # noqa: E501
        :rtype: bool
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this ServerEndpoints.


        :param tls: The tls of this ServerEndpoints.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and tls is None:  # noqa: E501
            raise ValueError("Invalid value for `tls`, must not be `None`")  # noqa: E501

        self._tls = tls

    @property
    def alt_ports(self):
        """Gets the alt_ports of this ServerEndpoints.  # noqa: E501


        :return: The alt_ports of this ServerEndpoints.  # noqa: E501
        :rtype: list[int]
        """
        return self._alt_ports

    @alt_ports.setter
    def alt_ports(self, alt_ports):
        """Sets the alt_ports of this ServerEndpoints.


        :param alt_ports: The alt_ports of this ServerEndpoints.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and alt_ports is None:  # noqa: E501
            raise ValueError("Invalid value for `alt_ports`, must not be `None`")  # noqa: E501

        self._alt_ports = alt_ports

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
        if not isinstance(other, ServerEndpoints):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServerEndpoints):
            return True

        return self.to_dict() != other.to_dict()
