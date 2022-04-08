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


class EmailRecipients(object):
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
        'to': 'list[Recipient]',
        'cc': 'list[Recipient]',
        'bcc': 'list[Recipient]'
    }

    attribute_map = {
        'to': 'to',
        'cc': 'cc',
        'bcc': 'bcc'
    }

    def __init__(self, to=None, cc=None, bcc=None, local_vars_configuration=None):  # noqa: E501
        """EmailRecipients - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._to = None
        self._cc = None
        self._bcc = None
        self.discriminator = None

        if to is not None:
            self.to = to
        if cc is not None:
            self.cc = cc
        if bcc is not None:
            self.bcc = bcc

    @property
    def to(self):
        """Gets the to of this EmailRecipients.  # noqa: E501


        :return: The to of this EmailRecipients.  # noqa: E501
        :rtype: list[Recipient]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this EmailRecipients.


        :param to: The to of this EmailRecipients.  # noqa: E501
        :type: list[Recipient]
        """

        self._to = to

    @property
    def cc(self):
        """Gets the cc of this EmailRecipients.  # noqa: E501


        :return: The cc of this EmailRecipients.  # noqa: E501
        :rtype: list[Recipient]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this EmailRecipients.


        :param cc: The cc of this EmailRecipients.  # noqa: E501
        :type: list[Recipient]
        """

        self._cc = cc

    @property
    def bcc(self):
        """Gets the bcc of this EmailRecipients.  # noqa: E501


        :return: The bcc of this EmailRecipients.  # noqa: E501
        :rtype: list[Recipient]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this EmailRecipients.


        :param bcc: The bcc of this EmailRecipients.  # noqa: E501
        :type: list[Recipient]
        """

        self._bcc = bcc

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
        if not isinstance(other, EmailRecipients):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailRecipients):
            return True

        return self.to_dict() != other.to_dict()
