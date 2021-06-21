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


class MissedEmailProjection(object):
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
        '_from': 'str',
        'id': 'str',
        'subject': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        '_from': 'from',
        'id': 'id',
        'subject': 'subject',
        'user_id': 'userId'
    }

    def __init__(self, created_at=None, _from=None, id=None, subject=None, user_id=None, local_vars_configuration=None):  # noqa: E501
        """MissedEmailProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self.__from = None
        self._id = None
        self._subject = None
        self._user_id = None
        self.discriminator = None

        self.created_at = created_at
        if _from is not None:
            self._from = _from
        self.id = id
        if subject is not None:
            self.subject = subject
        self.user_id = user_id

    @property
    def created_at(self):
        """Gets the created_at of this MissedEmailProjection.  # noqa: E501


        :return: The created_at of this MissedEmailProjection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MissedEmailProjection.


        :param created_at: The created_at of this MissedEmailProjection.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def _from(self):
        """Gets the _from of this MissedEmailProjection.  # noqa: E501


        :return: The _from of this MissedEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this MissedEmailProjection.


        :param _from: The _from of this MissedEmailProjection.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def id(self):
        """Gets the id of this MissedEmailProjection.  # noqa: E501


        :return: The id of this MissedEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MissedEmailProjection.


        :param id: The id of this MissedEmailProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def subject(self):
        """Gets the subject of this MissedEmailProjection.  # noqa: E501


        :return: The subject of this MissedEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this MissedEmailProjection.


        :param subject: The subject of this MissedEmailProjection.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def user_id(self):
        """Gets the user_id of this MissedEmailProjection.  # noqa: E501


        :return: The user_id of this MissedEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this MissedEmailProjection.


        :param user_id: The user_id of this MissedEmailProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

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
        if not isinstance(other, MissedEmailProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MissedEmailProjection):
            return True

        return self.to_dict() != other.to_dict()
