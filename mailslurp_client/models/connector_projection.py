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


class ConnectorProjection(object):
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
        'enabled': 'bool',
        'email_address': 'str',
        'user_id': 'str',
        'inbox_id': 'str',
        'sync_enabled': 'bool',
        'sync_schedule_type': 'str',
        'sync_interval': 'int',
        'created_at': 'datetime',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'email_address': 'emailAddress',
        'user_id': 'userId',
        'inbox_id': 'inboxId',
        'sync_enabled': 'syncEnabled',
        'sync_schedule_type': 'syncScheduleType',
        'sync_interval': 'syncInterval',
        'created_at': 'createdAt',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, enabled=None, email_address=None, user_id=None, inbox_id=None, sync_enabled=None, sync_schedule_type=None, sync_interval=None, created_at=None, name=None, id=None, local_vars_configuration=None):  # noqa: E501
        """ConnectorProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enabled = None
        self._email_address = None
        self._user_id = None
        self._inbox_id = None
        self._sync_enabled = None
        self._sync_schedule_type = None
        self._sync_interval = None
        self._created_at = None
        self._name = None
        self._id = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if email_address is not None:
            self.email_address = email_address
        self.user_id = user_id
        self.inbox_id = inbox_id
        if sync_enabled is not None:
            self.sync_enabled = sync_enabled
        self.sync_schedule_type = sync_schedule_type
        if sync_interval is not None:
            self.sync_interval = sync_interval
        self.created_at = created_at
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def enabled(self):
        """Gets the enabled of this ConnectorProjection.  # noqa: E501


        :return: The enabled of this ConnectorProjection.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ConnectorProjection.


        :param enabled: The enabled of this ConnectorProjection.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def email_address(self):
        """Gets the email_address of this ConnectorProjection.  # noqa: E501


        :return: The email_address of this ConnectorProjection.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this ConnectorProjection.


        :param email_address: The email_address of this ConnectorProjection.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def user_id(self):
        """Gets the user_id of this ConnectorProjection.  # noqa: E501


        :return: The user_id of this ConnectorProjection.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ConnectorProjection.


        :param user_id: The user_id of this ConnectorProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def inbox_id(self):
        """Gets the inbox_id of this ConnectorProjection.  # noqa: E501


        :return: The inbox_id of this ConnectorProjection.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this ConnectorProjection.


        :param inbox_id: The inbox_id of this ConnectorProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and inbox_id is None:  # noqa: E501
            raise ValueError("Invalid value for `inbox_id`, must not be `None`")  # noqa: E501

        self._inbox_id = inbox_id

    @property
    def sync_enabled(self):
        """Gets the sync_enabled of this ConnectorProjection.  # noqa: E501


        :return: The sync_enabled of this ConnectorProjection.  # noqa: E501
        :rtype: bool
        """
        return self._sync_enabled

    @sync_enabled.setter
    def sync_enabled(self, sync_enabled):
        """Sets the sync_enabled of this ConnectorProjection.


        :param sync_enabled: The sync_enabled of this ConnectorProjection.  # noqa: E501
        :type: bool
        """

        self._sync_enabled = sync_enabled

    @property
    def sync_schedule_type(self):
        """Gets the sync_schedule_type of this ConnectorProjection.  # noqa: E501


        :return: The sync_schedule_type of this ConnectorProjection.  # noqa: E501
        :rtype: str
        """
        return self._sync_schedule_type

    @sync_schedule_type.setter
    def sync_schedule_type(self, sync_schedule_type):
        """Sets the sync_schedule_type of this ConnectorProjection.


        :param sync_schedule_type: The sync_schedule_type of this ConnectorProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sync_schedule_type is None:  # noqa: E501
            raise ValueError("Invalid value for `sync_schedule_type`, must not be `None`")  # noqa: E501
        allowed_values = ["INTERVAL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and sync_schedule_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `sync_schedule_type` ({0}), must be one of {1}"  # noqa: E501
                .format(sync_schedule_type, allowed_values)
            )

        self._sync_schedule_type = sync_schedule_type

    @property
    def sync_interval(self):
        """Gets the sync_interval of this ConnectorProjection.  # noqa: E501


        :return: The sync_interval of this ConnectorProjection.  # noqa: E501
        :rtype: int
        """
        return self._sync_interval

    @sync_interval.setter
    def sync_interval(self, sync_interval):
        """Sets the sync_interval of this ConnectorProjection.


        :param sync_interval: The sync_interval of this ConnectorProjection.  # noqa: E501
        :type: int
        """

        self._sync_interval = sync_interval

    @property
    def created_at(self):
        """Gets the created_at of this ConnectorProjection.  # noqa: E501


        :return: The created_at of this ConnectorProjection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ConnectorProjection.


        :param created_at: The created_at of this ConnectorProjection.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this ConnectorProjection.  # noqa: E501


        :return: The name of this ConnectorProjection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectorProjection.


        :param name: The name of this ConnectorProjection.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this ConnectorProjection.  # noqa: E501


        :return: The id of this ConnectorProjection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectorProjection.


        :param id: The id of this ConnectorProjection.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, ConnectorProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectorProjection):
            return True

        return self.to_dict() != other.to_dict()
