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


class Sender(object):
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
        'raw_value': 'str',
        'email_address': 'str',
        'name': 'str'
    }

    attribute_map = {
        'raw_value': 'rawValue',
        'email_address': 'emailAddress',
        'name': 'name'
    }

    def __init__(self, raw_value=None, email_address=None, name=None, local_vars_configuration=None):  # noqa: E501
        """Sender - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._raw_value = None
        self._email_address = None
        self._name = None
        self.discriminator = None

        self.raw_value = raw_value
        self.email_address = email_address
        if name is not None:
            self.name = name

    @property
    def raw_value(self):
        """Gets the raw_value of this Sender.  # noqa: E501


        :return: The raw_value of this Sender.  # noqa: E501
        :rtype: str
        """
        return self._raw_value

    @raw_value.setter
    def raw_value(self, raw_value):
        """Sets the raw_value of this Sender.


        :param raw_value: The raw_value of this Sender.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and raw_value is None:  # noqa: E501
            raise ValueError("Invalid value for `raw_value`, must not be `None`")  # noqa: E501

        self._raw_value = raw_value

    @property
    def email_address(self):
        """Gets the email_address of this Sender.  # noqa: E501


        :return: The email_address of this Sender.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this Sender.


        :param email_address: The email_address of this Sender.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def name(self):
        """Gets the name of this Sender.  # noqa: E501


        :return: The name of this Sender.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Sender.


        :param name: The name of this Sender.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, Sender):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Sender):
            return True

        return self.to_dict() != other.to_dict()
