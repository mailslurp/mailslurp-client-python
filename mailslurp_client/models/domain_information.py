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


class DomainInformation(object):
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
        'domain_name': 'str',
        'verified': 'bool',
        'domain_type': 'str'
    }

    attribute_map = {
        'domain_name': 'domainName',
        'verified': 'verified',
        'domain_type': 'domainType'
    }

    def __init__(self, domain_name=None, verified=None, domain_type=None, local_vars_configuration=None):  # noqa: E501
        """DomainInformation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._domain_name = None
        self._verified = None
        self._domain_type = None
        self.discriminator = None

        self.domain_name = domain_name
        self.verified = verified
        self.domain_type = domain_type

    @property
    def domain_name(self):
        """Gets the domain_name of this DomainInformation.  # noqa: E501


        :return: The domain_name of this DomainInformation.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DomainInformation.


        :param domain_name: The domain_name of this DomainInformation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and domain_name is None:  # noqa: E501
            raise ValueError("Invalid value for `domain_name`, must not be `None`")  # noqa: E501

        self._domain_name = domain_name

    @property
    def verified(self):
        """Gets the verified of this DomainInformation.  # noqa: E501


        :return: The verified of this DomainInformation.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this DomainInformation.


        :param verified: The verified of this DomainInformation.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and verified is None:  # noqa: E501
            raise ValueError("Invalid value for `verified`, must not be `None`")  # noqa: E501

        self._verified = verified

    @property
    def domain_type(self):
        """Gets the domain_type of this DomainInformation.  # noqa: E501

        Type of domain. Dictates type of inbox that can be created with domain. HTTP means inboxes are processed using SES while SMTP inboxes use a custom SMTP mail server. SMTP does not support sending so use HTTP for sending emails.  # noqa: E501

        :return: The domain_type of this DomainInformation.  # noqa: E501
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this DomainInformation.

        Type of domain. Dictates type of inbox that can be created with domain. HTTP means inboxes are processed using SES while SMTP inboxes use a custom SMTP mail server. SMTP does not support sending so use HTTP for sending emails.  # noqa: E501

        :param domain_type: The domain_type of this DomainInformation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and domain_type is None:  # noqa: E501
            raise ValueError("Invalid value for `domain_type`, must not be `None`")  # noqa: E501
        allowed_values = ["HTTP_INBOX", "SMTP_DOMAIN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and domain_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `domain_type` ({0}), must be one of {1}"  # noqa: E501
                .format(domain_type, allowed_values)
            )

        self._domain_type = domain_type

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
        if not isinstance(other, DomainInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DomainInformation):
            return True

        return self.to_dict() != other.to_dict()
