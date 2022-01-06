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


class CreateAliasOptions(object):
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
        'email_address': 'str',
        'inbox_id': 'str',
        'name': 'str',
        'use_threads': 'bool'
    }

    attribute_map = {
        'email_address': 'emailAddress',
        'inbox_id': 'inboxId',
        'name': 'name',
        'use_threads': 'useThreads'
    }

    def __init__(self, email_address=None, inbox_id=None, name=None, use_threads=None, local_vars_configuration=None):  # noqa: E501
        """CreateAliasOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email_address = None
        self._inbox_id = None
        self._name = None
        self._use_threads = None
        self.discriminator = None

        if email_address is not None:
            self.email_address = email_address
        if inbox_id is not None:
            self.inbox_id = inbox_id
        if name is not None:
            self.name = name
        if use_threads is not None:
            self.use_threads = use_threads

    @property
    def email_address(self):
        """Gets the email_address of this CreateAliasOptions.  # noqa: E501

        Email address to be hidden behind alias. Emails sent to the alias email address will be forwarded to this address. If you want to enable replies set useThreads true and the reply-to for the email will allow outbound communication via a thread.  # noqa: E501

        :return: The email_address of this CreateAliasOptions.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CreateAliasOptions.

        Email address to be hidden behind alias. Emails sent to the alias email address will be forwarded to this address. If you want to enable replies set useThreads true and the reply-to for the email will allow outbound communication via a thread.  # noqa: E501

        :param email_address: The email_address of this CreateAliasOptions.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def inbox_id(self):
        """Gets the inbox_id of this CreateAliasOptions.  # noqa: E501

        Optional inbox ID to attach to alias. Null by default means an a new inbox will be created for the alias. Use a custom inbox to control what email address the alias uses. To use custom email addresses create a domain and an inbox, the use the inbox ID with this call. Emails received by this inbox will be forwarded to the alias email address  # noqa: E501

        :return: The inbox_id of this CreateAliasOptions.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this CreateAliasOptions.

        Optional inbox ID to attach to alias. Null by default means an a new inbox will be created for the alias. Use a custom inbox to control what email address the alias uses. To use custom email addresses create a domain and an inbox, the use the inbox ID with this call. Emails received by this inbox will be forwarded to the alias email address  # noqa: E501

        :param inbox_id: The inbox_id of this CreateAliasOptions.  # noqa: E501
        :type: str
        """

        self._inbox_id = inbox_id

    @property
    def name(self):
        """Gets the name of this CreateAliasOptions.  # noqa: E501

        Optional name for alias  # noqa: E501

        :return: The name of this CreateAliasOptions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAliasOptions.

        Optional name for alias  # noqa: E501

        :param name: The name of this CreateAliasOptions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def use_threads(self):
        """Gets the use_threads of this CreateAliasOptions.  # noqa: E501

        Enable threads options. If true emails will be sent with a unique reply-to thread address. This means you can reply to the forwarded email and it will be sent to the recipients via your alias address. That way a thread conversation is preserved.  # noqa: E501

        :return: The use_threads of this CreateAliasOptions.  # noqa: E501
        :rtype: bool
        """
        return self._use_threads

    @use_threads.setter
    def use_threads(self, use_threads):
        """Sets the use_threads of this CreateAliasOptions.

        Enable threads options. If true emails will be sent with a unique reply-to thread address. This means you can reply to the forwarded email and it will be sent to the recipients via your alias address. That way a thread conversation is preserved.  # noqa: E501

        :param use_threads: The use_threads of this CreateAliasOptions.  # noqa: E501
        :type: bool
        """

        self._use_threads = use_threads

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
        if not isinstance(other, CreateAliasOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateAliasOptions):
            return True

        return self.to_dict() != other.to_dict()
