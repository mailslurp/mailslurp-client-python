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


class InboxRulesetDto(object):
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
        'action': 'str',
        'created_at': 'datetime',
        'handler': 'str',
        'id': 'str',
        'inbox_id': 'str',
        'scope': 'str',
        'target': 'str'
    }

    attribute_map = {
        'action': 'action',
        'created_at': 'createdAt',
        'handler': 'handler',
        'id': 'id',
        'inbox_id': 'inboxId',
        'scope': 'scope',
        'target': 'target'
    }

    def __init__(self, action=None, created_at=None, handler=None, id=None, inbox_id=None, scope=None, target=None, local_vars_configuration=None):  # noqa: E501
        """InboxRulesetDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._created_at = None
        self._handler = None
        self._id = None
        self._inbox_id = None
        self._scope = None
        self._target = None
        self.discriminator = None

        self.action = action
        self.created_at = created_at
        self.handler = handler
        self.id = id
        self.inbox_id = inbox_id
        self.scope = scope
        self.target = target

    @property
    def action(self):
        """Gets the action of this InboxRulesetDto.  # noqa: E501


        :return: The action of this InboxRulesetDto.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this InboxRulesetDto.


        :param action: The action of this InboxRulesetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and action is None:  # noqa: E501
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["BLOCK", "ALLOW", "FILTER_REMOVE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and action not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def created_at(self):
        """Gets the created_at of this InboxRulesetDto.  # noqa: E501


        :return: The created_at of this InboxRulesetDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InboxRulesetDto.


        :param created_at: The created_at of this InboxRulesetDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def handler(self):
        """Gets the handler of this InboxRulesetDto.  # noqa: E501


        :return: The handler of this InboxRulesetDto.  # noqa: E501
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        """Sets the handler of this InboxRulesetDto.


        :param handler: The handler of this InboxRulesetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and handler is None:  # noqa: E501
            raise ValueError("Invalid value for `handler`, must not be `None`")  # noqa: E501
        allowed_values = ["EXCEPTION"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and handler not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `handler` ({0}), must be one of {1}"  # noqa: E501
                .format(handler, allowed_values)
            )

        self._handler = handler

    @property
    def id(self):
        """Gets the id of this InboxRulesetDto.  # noqa: E501


        :return: The id of this InboxRulesetDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InboxRulesetDto.


        :param id: The id of this InboxRulesetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def inbox_id(self):
        """Gets the inbox_id of this InboxRulesetDto.  # noqa: E501


        :return: The inbox_id of this InboxRulesetDto.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this InboxRulesetDto.


        :param inbox_id: The inbox_id of this InboxRulesetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and inbox_id is None:  # noqa: E501
            raise ValueError("Invalid value for `inbox_id`, must not be `None`")  # noqa: E501

        self._inbox_id = inbox_id

    @property
    def scope(self):
        """Gets the scope of this InboxRulesetDto.  # noqa: E501


        :return: The scope of this InboxRulesetDto.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this InboxRulesetDto.


        :param scope: The scope of this InboxRulesetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and scope is None:  # noqa: E501
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501
        allowed_values = ["RECEIVING_EMAILS", "SENDING_EMAILS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and scope not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def target(self):
        """Gets the target of this InboxRulesetDto.  # noqa: E501


        :return: The target of this InboxRulesetDto.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this InboxRulesetDto.


        :param target: The target of this InboxRulesetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and target is None:  # noqa: E501
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

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
        if not isinstance(other, InboxRulesetDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InboxRulesetDto):
            return True

        return self.to_dict() != other.to_dict()