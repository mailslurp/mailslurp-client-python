# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: d1659dc1567a5b62f65d0612107a50aace03e085
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class DomainDto(object):
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
        'created_at': 'datetime',
        'domain': 'str',
        'id': 'str',
        'is_verified': 'bool',
        'updated_at': 'datetime',
        'user_id': 'str',
        'verification_token': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'domain': 'domain',
        'id': 'id',
        'is_verified': 'isVerified',
        'updated_at': 'updatedAt',
        'user_id': 'userId',
        'verification_token': 'verificationToken'
    }

    def __init__(self, created_at=None, domain=None, id=None, is_verified=None, updated_at=None, user_id=None, verification_token=None, local_vars_configuration=None):  # noqa: E501
        """DomainDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._domain = None
        self._id = None
        self._is_verified = None
        self._updated_at = None
        self._user_id = None
        self._verification_token = None
        self.discriminator = None

        self.created_at = created_at
        self.domain = domain
        self.id = id
        self.is_verified = is_verified
        self.updated_at = updated_at
        self.user_id = user_id
        self.verification_token = verification_token

    @property
    def created_at(self):
        """Gets the created_at of this DomainDto.  # noqa: E501


        :return: The created_at of this DomainDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DomainDto.


        :param created_at: The created_at of this DomainDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def domain(self):
        """Gets the domain of this DomainDto.  # noqa: E501


        :return: The domain of this DomainDto.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DomainDto.


        :param domain: The domain of this DomainDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and domain is None:  # noqa: E501
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def id(self):
        """Gets the id of this DomainDto.  # noqa: E501


        :return: The id of this DomainDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainDto.


        :param id: The id of this DomainDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_verified(self):
        """Gets the is_verified of this DomainDto.  # noqa: E501


        :return: The is_verified of this DomainDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_verified

    @is_verified.setter
    def is_verified(self, is_verified):
        """Sets the is_verified of this DomainDto.


        :param is_verified: The is_verified of this DomainDto.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_verified is None:  # noqa: E501
            raise ValueError("Invalid value for `is_verified`, must not be `None`")  # noqa: E501

        self._is_verified = is_verified

    @property
    def updated_at(self):
        """Gets the updated_at of this DomainDto.  # noqa: E501


        :return: The updated_at of this DomainDto.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DomainDto.


        :param updated_at: The updated_at of this DomainDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def user_id(self):
        """Gets the user_id of this DomainDto.  # noqa: E501


        :return: The user_id of this DomainDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DomainDto.


        :param user_id: The user_id of this DomainDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def verification_token(self):
        """Gets the verification_token of this DomainDto.  # noqa: E501


        :return: The verification_token of this DomainDto.  # noqa: E501
        :rtype: str
        """
        return self._verification_token

    @verification_token.setter
    def verification_token(self, verification_token):
        """Sets the verification_token of this DomainDto.


        :param verification_token: The verification_token of this DomainDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and verification_token is None:  # noqa: E501
            raise ValueError("Invalid value for `verification_token`, must not be `None`")  # noqa: E501

        self._verification_token = verification_token

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
        if not isinstance(other, DomainDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DomainDto):
            return True

        return self.to_dict() != other.to_dict()