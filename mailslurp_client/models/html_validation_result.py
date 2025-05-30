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


class HTMLValidationResult(object):
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
        'is_valid': 'bool',
        'infos': 'list[ValidationMessage]',
        'errors': 'list[ValidationMessage]',
        'warnings': 'list[ValidationMessage]'
    }

    attribute_map = {
        'is_valid': 'isValid',
        'infos': 'infos',
        'errors': 'errors',
        'warnings': 'warnings'
    }

    def __init__(self, is_valid=None, infos=None, errors=None, warnings=None, local_vars_configuration=None):  # noqa: E501
        """HTMLValidationResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_valid = None
        self._infos = None
        self._errors = None
        self._warnings = None
        self.discriminator = None

        self.is_valid = is_valid
        self.infos = infos
        self.errors = errors
        self.warnings = warnings

    @property
    def is_valid(self):
        """Gets the is_valid of this HTMLValidationResult.  # noqa: E501

        Is HTML validation result valid  # noqa: E501

        :return: The is_valid of this HTMLValidationResult.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this HTMLValidationResult.

        Is HTML validation result valid  # noqa: E501

        :param is_valid: The is_valid of this HTMLValidationResult.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_valid is None:  # noqa: E501
            raise ValueError("Invalid value for `is_valid`, must not be `None`")  # noqa: E501

        self._is_valid = is_valid

    @property
    def infos(self):
        """Gets the infos of this HTMLValidationResult.  # noqa: E501

        Optional infos resulting from HTML validation  # noqa: E501

        :return: The infos of this HTMLValidationResult.  # noqa: E501
        :rtype: list[ValidationMessage]
        """
        return self._infos

    @infos.setter
    def infos(self, infos):
        """Sets the infos of this HTMLValidationResult.

        Optional infos resulting from HTML validation  # noqa: E501

        :param infos: The infos of this HTMLValidationResult.  # noqa: E501
        :type: list[ValidationMessage]
        """
        if self.local_vars_configuration.client_side_validation and infos is None:  # noqa: E501
            raise ValueError("Invalid value for `infos`, must not be `None`")  # noqa: E501

        self._infos = infos

    @property
    def errors(self):
        """Gets the errors of this HTMLValidationResult.  # noqa: E501

        Optional errors resulting from HTML validation  # noqa: E501

        :return: The errors of this HTMLValidationResult.  # noqa: E501
        :rtype: list[ValidationMessage]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this HTMLValidationResult.

        Optional errors resulting from HTML validation  # noqa: E501

        :param errors: The errors of this HTMLValidationResult.  # noqa: E501
        :type: list[ValidationMessage]
        """
        if self.local_vars_configuration.client_side_validation and errors is None:  # noqa: E501
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors

    @property
    def warnings(self):
        """Gets the warnings of this HTMLValidationResult.  # noqa: E501

        Optional warnings resulting from HTML validation  # noqa: E501

        :return: The warnings of this HTMLValidationResult.  # noqa: E501
        :rtype: list[ValidationMessage]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this HTMLValidationResult.

        Optional warnings resulting from HTML validation  # noqa: E501

        :param warnings: The warnings of this HTMLValidationResult.  # noqa: E501
        :type: list[ValidationMessage]
        """
        if self.local_vars_configuration.client_side_validation and warnings is None:  # noqa: E501
            raise ValueError("Invalid value for `warnings`, must not be `None`")  # noqa: E501

        self._warnings = warnings

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
        if not isinstance(other, HTMLValidationResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HTMLValidationResult):
            return True

        return self.to_dict() != other.to_dict()
