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


class ContactProjection(object):
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
        'group_id': 'str',
        'created_at': 'datetime',
        'first_name': 'str',
        'last_name': 'str',
        'company': 'str',
        'email_addresses': 'list[str]',
        'opt_out': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'groupId',
        'created_at': 'createdAt',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'company': 'company',
        'email_addresses': 'emailAddresses',
        'opt_out': 'optOut'
    }

    def __init__(self, id=None, group_id=None, created_at=None, first_name=None, last_name=None, company=None, email_addresses=None, opt_out=None, local_vars_configuration=None):  # noqa: E501
        """ContactProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._group_id = None
        self._created_at = None
        self._first_name = None
        self._last_name = None
        self._company = None
        self._email_addresses = None
        self._opt_out = None
        self.discriminator = None

        self.id = id
        self.group_id = group_id
        self.created_at = created_at
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.email_addresses = email_addresses
        self.opt_out = opt_out

    @property
    def id(self):
        """Gets the id of this ContactProjection.  # noqa: E501


        :return: The id of this ContactProjection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContactProjection.


        :param id: The id of this ContactProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def group_id(self):
        """Gets the group_id of this ContactProjection.  # noqa: E501


        :return: The group_id of this ContactProjection.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ContactProjection.


        :param group_id: The group_id of this ContactProjection.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def created_at(self):
        """Gets the created_at of this ContactProjection.  # noqa: E501


        :return: The created_at of this ContactProjection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ContactProjection.


        :param created_at: The created_at of this ContactProjection.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def first_name(self):
        """Gets the first_name of this ContactProjection.  # noqa: E501


        :return: The first_name of this ContactProjection.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ContactProjection.


        :param first_name: The first_name of this ContactProjection.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this ContactProjection.  # noqa: E501


        :return: The last_name of this ContactProjection.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ContactProjection.


        :param last_name: The last_name of this ContactProjection.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def company(self):
        """Gets the company of this ContactProjection.  # noqa: E501


        :return: The company of this ContactProjection.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this ContactProjection.


        :param company: The company of this ContactProjection.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def email_addresses(self):
        """Gets the email_addresses of this ContactProjection.  # noqa: E501


        :return: The email_addresses of this ContactProjection.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_addresses

    @email_addresses.setter
    def email_addresses(self, email_addresses):
        """Sets the email_addresses of this ContactProjection.


        :param email_addresses: The email_addresses of this ContactProjection.  # noqa: E501
        :type: list[str]
        """

        self._email_addresses = email_addresses

    @property
    def opt_out(self):
        """Gets the opt_out of this ContactProjection.  # noqa: E501


        :return: The opt_out of this ContactProjection.  # noqa: E501
        :rtype: bool
        """
        return self._opt_out

    @opt_out.setter
    def opt_out(self, opt_out):
        """Sets the opt_out of this ContactProjection.


        :param opt_out: The opt_out of this ContactProjection.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and opt_out is None:  # noqa: E501
            raise ValueError("Invalid value for `opt_out`, must not be `None`")  # noqa: E501

        self._opt_out = opt_out

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
        if not isinstance(other, ContactProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContactProjection):
            return True

        return self.to_dict() != other.to_dict()
