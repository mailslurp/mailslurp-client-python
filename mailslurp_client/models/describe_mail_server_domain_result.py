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


class DescribeMailServerDomainResult(object):
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
        'mx_records': 'list[NameServerRecord]',
        'domain': 'str',
        'message': 'str'
    }

    attribute_map = {
        'mx_records': 'mxRecords',
        'domain': 'domain',
        'message': 'message'
    }

    def __init__(self, mx_records=None, domain=None, message=None, local_vars_configuration=None):  # noqa: E501
        """DescribeMailServerDomainResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mx_records = None
        self._domain = None
        self._message = None
        self.discriminator = None

        self.mx_records = mx_records
        self.domain = domain
        self.message = message

    @property
    def mx_records(self):
        """Gets the mx_records of this DescribeMailServerDomainResult.  # noqa: E501


        :return: The mx_records of this DescribeMailServerDomainResult.  # noqa: E501
        :rtype: list[NameServerRecord]
        """
        return self._mx_records

    @mx_records.setter
    def mx_records(self, mx_records):
        """Sets the mx_records of this DescribeMailServerDomainResult.


        :param mx_records: The mx_records of this DescribeMailServerDomainResult.  # noqa: E501
        :type: list[NameServerRecord]
        """
        if self.local_vars_configuration.client_side_validation and mx_records is None:  # noqa: E501
            raise ValueError("Invalid value for `mx_records`, must not be `None`")  # noqa: E501

        self._mx_records = mx_records

    @property
    def domain(self):
        """Gets the domain of this DescribeMailServerDomainResult.  # noqa: E501


        :return: The domain of this DescribeMailServerDomainResult.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DescribeMailServerDomainResult.


        :param domain: The domain of this DescribeMailServerDomainResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and domain is None:  # noqa: E501
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def message(self):
        """Gets the message of this DescribeMailServerDomainResult.  # noqa: E501


        :return: The message of this DescribeMailServerDomainResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DescribeMailServerDomainResult.


        :param message: The message of this DescribeMailServerDomainResult.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, DescribeMailServerDomainResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeMailServerDomainResult):
            return True

        return self.to_dict() != other.to_dict()
