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


class UnknownMissedEmailProjection(object):
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
        '_from': 'str',
        'created_at': 'datetime',
        'subject': 'str',
        'to': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        '_from': 'from',
        'created_at': 'createdAt',
        'subject': 'subject',
        'to': 'to'
    }

    def __init__(self, id=None, _from=None, created_at=None, subject=None, to=None, local_vars_configuration=None):  # noqa: E501
        """UnknownMissedEmailProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self.__from = None
        self._created_at = None
        self._subject = None
        self._to = None
        self.discriminator = None

        self.id = id
        if _from is not None:
            self._from = _from
        self.created_at = created_at
        if subject is not None:
            self.subject = subject
        if to is not None:
            self.to = to

    @property
    def id(self):
        """Gets the id of this UnknownMissedEmailProjection.  # noqa: E501


        :return: The id of this UnknownMissedEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UnknownMissedEmailProjection.


        :param id: The id of this UnknownMissedEmailProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def _from(self):
        """Gets the _from of this UnknownMissedEmailProjection.  # noqa: E501


        :return: The _from of this UnknownMissedEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this UnknownMissedEmailProjection.


        :param _from: The _from of this UnknownMissedEmailProjection.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def created_at(self):
        """Gets the created_at of this UnknownMissedEmailProjection.  # noqa: E501


        :return: The created_at of this UnknownMissedEmailProjection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UnknownMissedEmailProjection.


        :param created_at: The created_at of this UnknownMissedEmailProjection.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def subject(self):
        """Gets the subject of this UnknownMissedEmailProjection.  # noqa: E501


        :return: The subject of this UnknownMissedEmailProjection.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this UnknownMissedEmailProjection.


        :param subject: The subject of this UnknownMissedEmailProjection.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def to(self):
        """Gets the to of this UnknownMissedEmailProjection.  # noqa: E501


        :return: The to of this UnknownMissedEmailProjection.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this UnknownMissedEmailProjection.


        :param to: The to of this UnknownMissedEmailProjection.  # noqa: E501
        :type: list[str]
        """

        self._to = to

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
        if not isinstance(other, UnknownMissedEmailProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnknownMissedEmailProjection):
            return True

        return self.to_dict() != other.to_dict()
