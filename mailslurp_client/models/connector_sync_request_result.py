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


class ConnectorSyncRequestResult(object):
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
        'sync_result': 'ConnectorSyncResult',
        'exception': 'str',
        'event_id': 'str'
    }

    attribute_map = {
        'sync_result': 'syncResult',
        'exception': 'exception',
        'event_id': 'eventId'
    }

    def __init__(self, sync_result=None, exception=None, event_id=None, local_vars_configuration=None):  # noqa: E501
        """ConnectorSyncRequestResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sync_result = None
        self._exception = None
        self._event_id = None
        self.discriminator = None

        if sync_result is not None:
            self.sync_result = sync_result
        if exception is not None:
            self.exception = exception
        if event_id is not None:
            self.event_id = event_id

    @property
    def sync_result(self):
        """Gets the sync_result of this ConnectorSyncRequestResult.  # noqa: E501


        :return: The sync_result of this ConnectorSyncRequestResult.  # noqa: E501
        :rtype: ConnectorSyncResult
        """
        return self._sync_result

    @sync_result.setter
    def sync_result(self, sync_result):
        """Sets the sync_result of this ConnectorSyncRequestResult.


        :param sync_result: The sync_result of this ConnectorSyncRequestResult.  # noqa: E501
        :type: ConnectorSyncResult
        """

        self._sync_result = sync_result

    @property
    def exception(self):
        """Gets the exception of this ConnectorSyncRequestResult.  # noqa: E501


        :return: The exception of this ConnectorSyncRequestResult.  # noqa: E501
        :rtype: str
        """
        return self._exception

    @exception.setter
    def exception(self, exception):
        """Sets the exception of this ConnectorSyncRequestResult.


        :param exception: The exception of this ConnectorSyncRequestResult.  # noqa: E501
        :type: str
        """

        self._exception = exception

    @property
    def event_id(self):
        """Gets the event_id of this ConnectorSyncRequestResult.  # noqa: E501


        :return: The event_id of this ConnectorSyncRequestResult.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this ConnectorSyncRequestResult.


        :param event_id: The event_id of this ConnectorSyncRequestResult.  # noqa: E501
        :type: str
        """

        self._event_id = event_id

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
        if not isinstance(other, ConnectorSyncRequestResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectorSyncRequestResult):
            return True

        return self.to_dict() != other.to_dict()
