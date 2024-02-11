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


class ExpiredInboxRecordProjection(object):
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
        'user_id': 'str',
        'email_address': 'str',
        'created_at': 'datetime',
        'id': 'str'
    }

    attribute_map = {
        'user_id': 'userId',
        'email_address': 'emailAddress',
        'created_at': 'createdAt',
        'id': 'id'
    }

    def __init__(self, user_id=None, email_address=None, created_at=None, id=None, local_vars_configuration=None):  # noqa: E501
        """ExpiredInboxRecordProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._email_address = None
        self._created_at = None
        self._id = None
        self.discriminator = None

        self.user_id = user_id
        self.email_address = email_address
        self.created_at = created_at
        self.id = id

    @property
    def user_id(self):
        """Gets the user_id of this ExpiredInboxRecordProjection.  # noqa: E501


        :return: The user_id of this ExpiredInboxRecordProjection.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ExpiredInboxRecordProjection.


        :param user_id: The user_id of this ExpiredInboxRecordProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def email_address(self):
        """Gets the email_address of this ExpiredInboxRecordProjection.  # noqa: E501


        :return: The email_address of this ExpiredInboxRecordProjection.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this ExpiredInboxRecordProjection.


        :param email_address: The email_address of this ExpiredInboxRecordProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def created_at(self):
        """Gets the created_at of this ExpiredInboxRecordProjection.  # noqa: E501


        :return: The created_at of this ExpiredInboxRecordProjection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ExpiredInboxRecordProjection.


        :param created_at: The created_at of this ExpiredInboxRecordProjection.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this ExpiredInboxRecordProjection.  # noqa: E501


        :return: The id of this ExpiredInboxRecordProjection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExpiredInboxRecordProjection.


        :param id: The id of this ExpiredInboxRecordProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, ExpiredInboxRecordProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExpiredInboxRecordProjection):
            return True

        return self.to_dict() != other.to_dict()
