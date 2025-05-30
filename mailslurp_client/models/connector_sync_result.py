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


class ConnectorSyncResult(object):
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
        'email_sync_count': 'int',
        'logs': 'list[str]',
        'email_ids': 'list[str]'
    }

    attribute_map = {
        'email_sync_count': 'emailSyncCount',
        'logs': 'logs',
        'email_ids': 'emailIds'
    }

    def __init__(self, email_sync_count=None, logs=None, email_ids=None, local_vars_configuration=None):  # noqa: E501
        """ConnectorSyncResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email_sync_count = None
        self._logs = None
        self._email_ids = None
        self.discriminator = None

        self.email_sync_count = email_sync_count
        if logs is not None:
            self.logs = logs
        if email_ids is not None:
            self.email_ids = email_ids

    @property
    def email_sync_count(self):
        """Gets the email_sync_count of this ConnectorSyncResult.  # noqa: E501


        :return: The email_sync_count of this ConnectorSyncResult.  # noqa: E501
        :rtype: int
        """
        return self._email_sync_count

    @email_sync_count.setter
    def email_sync_count(self, email_sync_count):
        """Sets the email_sync_count of this ConnectorSyncResult.


        :param email_sync_count: The email_sync_count of this ConnectorSyncResult.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and email_sync_count is None:  # noqa: E501
            raise ValueError("Invalid value for `email_sync_count`, must not be `None`")  # noqa: E501

        self._email_sync_count = email_sync_count

    @property
    def logs(self):
        """Gets the logs of this ConnectorSyncResult.  # noqa: E501


        :return: The logs of this ConnectorSyncResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this ConnectorSyncResult.


        :param logs: The logs of this ConnectorSyncResult.  # noqa: E501
        :type: list[str]
        """

        self._logs = logs

    @property
    def email_ids(self):
        """Gets the email_ids of this ConnectorSyncResult.  # noqa: E501


        :return: The email_ids of this ConnectorSyncResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_ids

    @email_ids.setter
    def email_ids(self, email_ids):
        """Sets the email_ids of this ConnectorSyncResult.


        :param email_ids: The email_ids of this ConnectorSyncResult.  # noqa: E501
        :type: list[str]
        """

        self._email_ids = email_ids

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
        if not isinstance(other, ConnectorSyncResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectorSyncResult):
            return True

        return self.to_dict() != other.to_dict()
