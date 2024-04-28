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


class UserInfoDto(object):
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
        'id': 'str',
        'email_address': 'str',
        'account_state': 'str',
        'subscription_type': 'str',
        'account_type': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'email_address': 'emailAddress',
        'account_state': 'accountState',
        'subscription_type': 'subscriptionType',
        'account_type': 'accountType',
        'created_at': 'createdAt'
    }

    def __init__(self, id=None, email_address=None, account_state=None, subscription_type=None, account_type=None, created_at=None, local_vars_configuration=None):  # noqa: E501
        """UserInfoDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email_address = None
        self._account_state = None
        self._subscription_type = None
        self._account_type = None
        self._created_at = None
        self.discriminator = None

        self.id = id
        self.email_address = email_address
        self.account_state = account_state
        if subscription_type is not None:
            self.subscription_type = subscription_type
        self.account_type = account_type
        self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this UserInfoDto.  # noqa: E501


        :return: The id of this UserInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserInfoDto.


        :param id: The id of this UserInfoDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email_address(self):
        """Gets the email_address of this UserInfoDto.  # noqa: E501


        :return: The email_address of this UserInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UserInfoDto.


        :param email_address: The email_address of this UserInfoDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def account_state(self):
        """Gets the account_state of this UserInfoDto.  # noqa: E501


        :return: The account_state of this UserInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._account_state

    @account_state.setter
    def account_state(self, account_state):
        """Sets the account_state of this UserInfoDto.


        :param account_state: The account_state of this UserInfoDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_state is None:  # noqa: E501
            raise ValueError("Invalid value for `account_state`, must not be `None`")  # noqa: E501
        allowed_values = ["FROZEN", "ACTIVE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and account_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `account_state` ({0}), must be one of {1}"  # noqa: E501
                .format(account_state, allowed_values)
            )

        self._account_state = account_state

    @property
    def subscription_type(self):
        """Gets the subscription_type of this UserInfoDto.  # noqa: E501


        :return: The subscription_type of this UserInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type):
        """Sets the subscription_type of this UserInfoDto.


        :param subscription_type: The subscription_type of this UserInfoDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["PRO_MONTHLY", "STARTER", "PRO", "TEAM", "ENTERPRISE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and subscription_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `subscription_type` ({0}), must be one of {1}"  # noqa: E501
                .format(subscription_type, allowed_values)
            )

        self._subscription_type = subscription_type

    @property
    def account_type(self):
        """Gets the account_type of this UserInfoDto.  # noqa: E501


        :return: The account_type of this UserInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this UserInfoDto.


        :param account_type: The account_type of this UserInfoDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_type is None:  # noqa: E501
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501
        allowed_values = ["SOLO", "CHILD_SOLO", "CHILD_TEAM", "CHILD_ADMIN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and account_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def created_at(self):
        """Gets the created_at of this UserInfoDto.  # noqa: E501


        :return: The created_at of this UserInfoDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserInfoDto.


        :param created_at: The created_at of this UserInfoDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

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
        if not isinstance(other, UserInfoDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserInfoDto):
            return True

        return self.to_dict() != other.to_dict()
