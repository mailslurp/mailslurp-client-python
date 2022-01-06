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


class ExportOptions(object):
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
        'output_format': 'str',
        'exclude_previously_exported': 'bool',
        'created_earliest_time': 'datetime',
        'created_oldest_time': 'datetime',
        'filter': 'str',
        'list_separator_token': 'str'
    }

    attribute_map = {
        'output_format': 'outputFormat',
        'exclude_previously_exported': 'excludePreviouslyExported',
        'created_earliest_time': 'createdEarliestTime',
        'created_oldest_time': 'createdOldestTime',
        'filter': 'filter',
        'list_separator_token': 'listSeparatorToken'
    }

    def __init__(self, output_format=None, exclude_previously_exported=None, created_earliest_time=None, created_oldest_time=None, filter=None, list_separator_token=None, local_vars_configuration=None):  # noqa: E501
        """ExportOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._output_format = None
        self._exclude_previously_exported = None
        self._created_earliest_time = None
        self._created_oldest_time = None
        self._filter = None
        self._list_separator_token = None
        self.discriminator = None

        if output_format is not None:
            self.output_format = output_format
        if exclude_previously_exported is not None:
            self.exclude_previously_exported = exclude_previously_exported
        if created_earliest_time is not None:
            self.created_earliest_time = created_earliest_time
        if created_oldest_time is not None:
            self.created_oldest_time = created_oldest_time
        if filter is not None:
            self.filter = filter
        if list_separator_token is not None:
            self.list_separator_token = list_separator_token

    @property
    def output_format(self):
        """Gets the output_format of this ExportOptions.  # noqa: E501


        :return: The output_format of this ExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        """Sets the output_format of this ExportOptions.


        :param output_format: The output_format of this ExportOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["CSV_DEFAULT", "CSV_EXCEL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and output_format not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `output_format` ({0}), must be one of {1}"  # noqa: E501
                .format(output_format, allowed_values)
            )

        self._output_format = output_format

    @property
    def exclude_previously_exported(self):
        """Gets the exclude_previously_exported of this ExportOptions.  # noqa: E501


        :return: The exclude_previously_exported of this ExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_previously_exported

    @exclude_previously_exported.setter
    def exclude_previously_exported(self, exclude_previously_exported):
        """Sets the exclude_previously_exported of this ExportOptions.


        :param exclude_previously_exported: The exclude_previously_exported of this ExportOptions.  # noqa: E501
        :type: bool
        """

        self._exclude_previously_exported = exclude_previously_exported

    @property
    def created_earliest_time(self):
        """Gets the created_earliest_time of this ExportOptions.  # noqa: E501


        :return: The created_earliest_time of this ExportOptions.  # noqa: E501
        :rtype: datetime
        """
        return self._created_earliest_time

    @created_earliest_time.setter
    def created_earliest_time(self, created_earliest_time):
        """Sets the created_earliest_time of this ExportOptions.


        :param created_earliest_time: The created_earliest_time of this ExportOptions.  # noqa: E501
        :type: datetime
        """

        self._created_earliest_time = created_earliest_time

    @property
    def created_oldest_time(self):
        """Gets the created_oldest_time of this ExportOptions.  # noqa: E501


        :return: The created_oldest_time of this ExportOptions.  # noqa: E501
        :rtype: datetime
        """
        return self._created_oldest_time

    @created_oldest_time.setter
    def created_oldest_time(self, created_oldest_time):
        """Sets the created_oldest_time of this ExportOptions.


        :param created_oldest_time: The created_oldest_time of this ExportOptions.  # noqa: E501
        :type: datetime
        """

        self._created_oldest_time = created_oldest_time

    @property
    def filter(self):
        """Gets the filter of this ExportOptions.  # noqa: E501


        :return: The filter of this ExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ExportOptions.


        :param filter: The filter of this ExportOptions.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def list_separator_token(self):
        """Gets the list_separator_token of this ExportOptions.  # noqa: E501


        :return: The list_separator_token of this ExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._list_separator_token

    @list_separator_token.setter
    def list_separator_token(self, list_separator_token):
        """Sets the list_separator_token of this ExportOptions.


        :param list_separator_token: The list_separator_token of this ExportOptions.  # noqa: E501
        :type: str
        """

        self._list_separator_token = list_separator_token

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
        if not isinstance(other, ExportOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExportOptions):
            return True

        return self.to_dict() != other.to_dict()
