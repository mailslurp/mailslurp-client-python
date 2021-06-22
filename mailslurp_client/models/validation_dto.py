# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class ValidationDto(object):
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
        'email_id': 'str',
        'html': 'HTMLValidationResult'
    }

    attribute_map = {
        'email_id': 'emailId',
        'html': 'html'
    }

    def __init__(self, email_id=None, html=None, local_vars_configuration=None):  # noqa: E501
        """ValidationDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email_id = None
        self._html = None
        self.discriminator = None

        if email_id is not None:
            self.email_id = email_id
        if html is not None:
            self.html = html

    @property
    def email_id(self):
        """Gets the email_id of this ValidationDto.  # noqa: E501

        ID of the email validated  # noqa: E501

        :return: The email_id of this ValidationDto.  # noqa: E501
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        """Sets the email_id of this ValidationDto.

        ID of the email validated  # noqa: E501

        :param email_id: The email_id of this ValidationDto.  # noqa: E501
        :type: str
        """

        self._email_id = email_id

    @property
    def html(self):
        """Gets the html of this ValidationDto.  # noqa: E501


        :return: The html of this ValidationDto.  # noqa: E501
        :rtype: HTMLValidationResult
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this ValidationDto.


        :param html: The html of this ValidationDto.  # noqa: E501
        :type: HTMLValidationResult
        """

        self._html = html

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
        if not isinstance(other, ValidationDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValidationDto):
            return True

        return self.to_dict() != other.to_dict()
