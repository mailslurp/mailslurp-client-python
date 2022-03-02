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


class UserDto(object):
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
        'api_key': 'str',
        'email_address': 'str',
        'email_address_md5': 'str',
        'created': 'datetime',
        'user_type': 'str',
        'organization': 'str',
        'verified': 'str',
        'has_password': 'bool',
        'is_frozen': 'bool',
        'add_new_contacts': 'bool',
        'sso_provider': 'str',
        'customer_id': 'str',
        'has_onboarded': 'bool',
        'imap_username': 'str',
        'imap_password': 'str',
        'smtp_username': 'str',
        'smtp_password': 'str'
    }

    attribute_map = {
        'id': 'id',
        'api_key': 'apiKey',
        'email_address': 'emailAddress',
        'email_address_md5': 'emailAddressMd5',
        'created': 'created',
        'user_type': 'userType',
        'organization': 'organization',
        'verified': 'verified',
        'has_password': 'hasPassword',
        'is_frozen': 'isFrozen',
        'add_new_contacts': 'addNewContacts',
        'sso_provider': 'ssoProvider',
        'customer_id': 'customerId',
        'has_onboarded': 'hasOnboarded',
        'imap_username': 'imapUsername',
        'imap_password': 'imapPassword',
        'smtp_username': 'smtpUsername',
        'smtp_password': 'smtpPassword'
    }

    def __init__(self, id=None, api_key=None, email_address=None, email_address_md5=None, created=None, user_type=None, organization=None, verified=None, has_password=None, is_frozen=None, add_new_contacts=None, sso_provider=None, customer_id=None, has_onboarded=None, imap_username=None, imap_password=None, smtp_username=None, smtp_password=None, local_vars_configuration=None):  # noqa: E501
        """UserDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._api_key = None
        self._email_address = None
        self._email_address_md5 = None
        self._created = None
        self._user_type = None
        self._organization = None
        self._verified = None
        self._has_password = None
        self._is_frozen = None
        self._add_new_contacts = None
        self._sso_provider = None
        self._customer_id = None
        self._has_onboarded = None
        self._imap_username = None
        self._imap_password = None
        self._smtp_username = None
        self._smtp_password = None
        self.discriminator = None

        self.id = id
        self.api_key = api_key
        self.email_address = email_address
        self.email_address_md5 = email_address_md5
        if created is not None:
            self.created = created
        if user_type is not None:
            self.user_type = user_type
        if organization is not None:
            self.organization = organization
        if verified is not None:
            self.verified = verified
        self.has_password = has_password
        self.is_frozen = is_frozen
        if add_new_contacts is not None:
            self.add_new_contacts = add_new_contacts
        if sso_provider is not None:
            self.sso_provider = sso_provider
        if customer_id is not None:
            self.customer_id = customer_id
        if has_onboarded is not None:
            self.has_onboarded = has_onboarded
        if imap_username is not None:
            self.imap_username = imap_username
        if imap_password is not None:
            self.imap_password = imap_password
        if smtp_username is not None:
            self.smtp_username = smtp_username
        if smtp_password is not None:
            self.smtp_password = smtp_password

    @property
    def id(self):
        """Gets the id of this UserDto.  # noqa: E501


        :return: The id of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserDto.


        :param id: The id of this UserDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def api_key(self):
        """Gets the api_key of this UserDto.  # noqa: E501


        :return: The api_key of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this UserDto.


        :param api_key: The api_key of this UserDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and api_key is None:  # noqa: E501
            raise ValueError("Invalid value for `api_key`, must not be `None`")  # noqa: E501

        self._api_key = api_key

    @property
    def email_address(self):
        """Gets the email_address of this UserDto.  # noqa: E501


        :return: The email_address of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UserDto.


        :param email_address: The email_address of this UserDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def email_address_md5(self):
        """Gets the email_address_md5 of this UserDto.  # noqa: E501


        :return: The email_address_md5 of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._email_address_md5

    @email_address_md5.setter
    def email_address_md5(self, email_address_md5):
        """Sets the email_address_md5 of this UserDto.


        :param email_address_md5: The email_address_md5 of this UserDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email_address_md5 is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address_md5`, must not be `None`")  # noqa: E501

        self._email_address_md5 = email_address_md5

    @property
    def created(self):
        """Gets the created of this UserDto.  # noqa: E501


        :return: The created of this UserDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UserDto.


        :param created: The created of this UserDto.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def user_type(self):
        """Gets the user_type of this UserDto.  # noqa: E501


        :return: The user_type of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this UserDto.


        :param user_type: The user_type of this UserDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["SOLO", "CHILD_SOLO", "CHILD_TEAM"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and user_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `user_type` ({0}), must be one of {1}"  # noqa: E501
                .format(user_type, allowed_values)
            )

        self._user_type = user_type

    @property
    def organization(self):
        """Gets the organization of this UserDto.  # noqa: E501

        Does user belong to an organization  # noqa: E501

        :return: The organization of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this UserDto.

        Does user belong to an organization  # noqa: E501

        :param organization: The organization of this UserDto.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def verified(self):
        """Gets the verified of this UserDto.  # noqa: E501

        Has user accepted an organization invite  # noqa: E501

        :return: The verified of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this UserDto.

        Has user accepted an organization invite  # noqa: E501

        :param verified: The verified of this UserDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["VERIFIED", "PENDING"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and verified not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `verified` ({0}), must be one of {1}"  # noqa: E501
                .format(verified, allowed_values)
            )

        self._verified = verified

    @property
    def has_password(self):
        """Gets the has_password of this UserDto.  # noqa: E501


        :return: The has_password of this UserDto.  # noqa: E501
        :rtype: bool
        """
        return self._has_password

    @has_password.setter
    def has_password(self, has_password):
        """Sets the has_password of this UserDto.


        :param has_password: The has_password of this UserDto.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and has_password is None:  # noqa: E501
            raise ValueError("Invalid value for `has_password`, must not be `None`")  # noqa: E501

        self._has_password = has_password

    @property
    def is_frozen(self):
        """Gets the is_frozen of this UserDto.  # noqa: E501


        :return: The is_frozen of this UserDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this UserDto.


        :param is_frozen: The is_frozen of this UserDto.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_frozen is None:  # noqa: E501
            raise ValueError("Invalid value for `is_frozen`, must not be `None`")  # noqa: E501

        self._is_frozen = is_frozen

    @property
    def add_new_contacts(self):
        """Gets the add_new_contacts of this UserDto.  # noqa: E501


        :return: The add_new_contacts of this UserDto.  # noqa: E501
        :rtype: bool
        """
        return self._add_new_contacts

    @add_new_contacts.setter
    def add_new_contacts(self, add_new_contacts):
        """Sets the add_new_contacts of this UserDto.


        :param add_new_contacts: The add_new_contacts of this UserDto.  # noqa: E501
        :type: bool
        """

        self._add_new_contacts = add_new_contacts

    @property
    def sso_provider(self):
        """Gets the sso_provider of this UserDto.  # noqa: E501


        :return: The sso_provider of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._sso_provider

    @sso_provider.setter
    def sso_provider(self, sso_provider):
        """Sets the sso_provider of this UserDto.


        :param sso_provider: The sso_provider of this UserDto.  # noqa: E501
        :type: str
        """

        self._sso_provider = sso_provider

    @property
    def customer_id(self):
        """Gets the customer_id of this UserDto.  # noqa: E501


        :return: The customer_id of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this UserDto.


        :param customer_id: The customer_id of this UserDto.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def has_onboarded(self):
        """Gets the has_onboarded of this UserDto.  # noqa: E501


        :return: The has_onboarded of this UserDto.  # noqa: E501
        :rtype: bool
        """
        return self._has_onboarded

    @has_onboarded.setter
    def has_onboarded(self, has_onboarded):
        """Sets the has_onboarded of this UserDto.


        :param has_onboarded: The has_onboarded of this UserDto.  # noqa: E501
        :type: bool
        """

        self._has_onboarded = has_onboarded

    @property
    def imap_username(self):
        """Gets the imap_username of this UserDto.  # noqa: E501


        :return: The imap_username of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._imap_username

    @imap_username.setter
    def imap_username(self, imap_username):
        """Sets the imap_username of this UserDto.


        :param imap_username: The imap_username of this UserDto.  # noqa: E501
        :type: str
        """

        self._imap_username = imap_username

    @property
    def imap_password(self):
        """Gets the imap_password of this UserDto.  # noqa: E501


        :return: The imap_password of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._imap_password

    @imap_password.setter
    def imap_password(self, imap_password):
        """Sets the imap_password of this UserDto.


        :param imap_password: The imap_password of this UserDto.  # noqa: E501
        :type: str
        """

        self._imap_password = imap_password

    @property
    def smtp_username(self):
        """Gets the smtp_username of this UserDto.  # noqa: E501


        :return: The smtp_username of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._smtp_username

    @smtp_username.setter
    def smtp_username(self, smtp_username):
        """Sets the smtp_username of this UserDto.


        :param smtp_username: The smtp_username of this UserDto.  # noqa: E501
        :type: str
        """

        self._smtp_username = smtp_username

    @property
    def smtp_password(self):
        """Gets the smtp_password of this UserDto.  # noqa: E501


        :return: The smtp_password of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._smtp_password

    @smtp_password.setter
    def smtp_password(self, smtp_password):
        """Sets the smtp_password of this UserDto.


        :param smtp_password: The smtp_password of this UserDto.  # noqa: E501
        :type: str
        """

        self._smtp_password = smtp_password

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
        if not isinstance(other, UserDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserDto):
            return True

        return self.to_dict() != other.to_dict()
