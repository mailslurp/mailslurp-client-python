# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class WebhookNewContactPayload(object):
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
        'company': 'str',
        'contact_id': 'str',
        'created_at': 'datetime',
        'email_addresses': 'list[str]',
        'event_name': 'str',
        'first_name': 'str',
        'group_id': 'str',
        'last_name': 'str',
        'message_id': 'str',
        'meta_data': 'object',
        'opt_out': 'bool',
        'primary_email_address': 'str',
        'tags': 'list[str]',
        'webhook_id': 'str',
        'webhook_name': 'str'
    }

    attribute_map = {
        'company': 'company',
        'contact_id': 'contactId',
        'created_at': 'createdAt',
        'email_addresses': 'emailAddresses',
        'event_name': 'eventName',
        'first_name': 'firstName',
        'group_id': 'groupId',
        'last_name': 'lastName',
        'message_id': 'messageId',
        'meta_data': 'metaData',
        'opt_out': 'optOut',
        'primary_email_address': 'primaryEmailAddress',
        'tags': 'tags',
        'webhook_id': 'webhookId',
        'webhook_name': 'webhookName'
    }

    def __init__(self, company=None, contact_id=None, created_at=None, email_addresses=None, event_name=None, first_name=None, group_id=None, last_name=None, message_id=None, meta_data=None, opt_out=None, primary_email_address=None, tags=None, webhook_id=None, webhook_name=None, local_vars_configuration=None):  # noqa: E501
        """WebhookNewContactPayload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._company = None
        self._contact_id = None
        self._created_at = None
        self._email_addresses = None
        self._event_name = None
        self._first_name = None
        self._group_id = None
        self._last_name = None
        self._message_id = None
        self._meta_data = None
        self._opt_out = None
        self._primary_email_address = None
        self._tags = None
        self._webhook_id = None
        self._webhook_name = None
        self.discriminator = None

        if company is not None:
            self.company = company
        self.contact_id = contact_id
        self.created_at = created_at
        self.email_addresses = email_addresses
        if event_name is not None:
            self.event_name = event_name
        if first_name is not None:
            self.first_name = first_name
        if group_id is not None:
            self.group_id = group_id
        if last_name is not None:
            self.last_name = last_name
        if message_id is not None:
            self.message_id = message_id
        if meta_data is not None:
            self.meta_data = meta_data
        if opt_out is not None:
            self.opt_out = opt_out
        if primary_email_address is not None:
            self.primary_email_address = primary_email_address
        self.tags = tags
        if webhook_id is not None:
            self.webhook_id = webhook_id
        if webhook_name is not None:
            self.webhook_name = webhook_name

    @property
    def company(self):
        """Gets the company of this WebhookNewContactPayload.  # noqa: E501


        :return: The company of this WebhookNewContactPayload.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this WebhookNewContactPayload.


        :param company: The company of this WebhookNewContactPayload.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def contact_id(self):
        """Gets the contact_id of this WebhookNewContactPayload.  # noqa: E501


        :return: The contact_id of this WebhookNewContactPayload.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this WebhookNewContactPayload.


        :param contact_id: The contact_id of this WebhookNewContactPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and contact_id is None:  # noqa: E501
            raise ValueError("Invalid value for `contact_id`, must not be `None`")  # noqa: E501

        self._contact_id = contact_id

    @property
    def created_at(self):
        """Gets the created_at of this WebhookNewContactPayload.  # noqa: E501


        :return: The created_at of this WebhookNewContactPayload.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WebhookNewContactPayload.


        :param created_at: The created_at of this WebhookNewContactPayload.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def email_addresses(self):
        """Gets the email_addresses of this WebhookNewContactPayload.  # noqa: E501


        :return: The email_addresses of this WebhookNewContactPayload.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_addresses

    @email_addresses.setter
    def email_addresses(self, email_addresses):
        """Sets the email_addresses of this WebhookNewContactPayload.


        :param email_addresses: The email_addresses of this WebhookNewContactPayload.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and email_addresses is None:  # noqa: E501
            raise ValueError("Invalid value for `email_addresses`, must not be `None`")  # noqa: E501

        self._email_addresses = email_addresses

    @property
    def event_name(self):
        """Gets the event_name of this WebhookNewContactPayload.  # noqa: E501

        Name of the event type webhook is being triggered for.  # noqa: E501

        :return: The event_name of this WebhookNewContactPayload.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this WebhookNewContactPayload.

        Name of the event type webhook is being triggered for.  # noqa: E501

        :param event_name: The event_name of this WebhookNewContactPayload.  # noqa: E501
        :type: str
        """
        allowed_values = ["EMAIL_RECEIVED", "NEW_EMAIL", "NEW_CONTACT", "NEW_ATTACHMENT", "EMAIL_OPENED", "EMAIL_READ"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and event_name not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `event_name` ({0}), must be one of {1}"  # noqa: E501
                .format(event_name, allowed_values)
            )

        self._event_name = event_name

    @property
    def first_name(self):
        """Gets the first_name of this WebhookNewContactPayload.  # noqa: E501


        :return: The first_name of this WebhookNewContactPayload.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this WebhookNewContactPayload.


        :param first_name: The first_name of this WebhookNewContactPayload.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def group_id(self):
        """Gets the group_id of this WebhookNewContactPayload.  # noqa: E501


        :return: The group_id of this WebhookNewContactPayload.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this WebhookNewContactPayload.


        :param group_id: The group_id of this WebhookNewContactPayload.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def last_name(self):
        """Gets the last_name of this WebhookNewContactPayload.  # noqa: E501


        :return: The last_name of this WebhookNewContactPayload.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this WebhookNewContactPayload.


        :param last_name: The last_name of this WebhookNewContactPayload.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def message_id(self):
        """Gets the message_id of this WebhookNewContactPayload.  # noqa: E501

        Idempotent message ID. Store this ID locally or in a database to prevent message duplication.  # noqa: E501

        :return: The message_id of this WebhookNewContactPayload.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this WebhookNewContactPayload.

        Idempotent message ID. Store this ID locally or in a database to prevent message duplication.  # noqa: E501

        :param message_id: The message_id of this WebhookNewContactPayload.  # noqa: E501
        :type: str
        """

        self._message_id = message_id

    @property
    def meta_data(self):
        """Gets the meta_data of this WebhookNewContactPayload.  # noqa: E501


        :return: The meta_data of this WebhookNewContactPayload.  # noqa: E501
        :rtype: object
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this WebhookNewContactPayload.


        :param meta_data: The meta_data of this WebhookNewContactPayload.  # noqa: E501
        :type: object
        """

        self._meta_data = meta_data

    @property
    def opt_out(self):
        """Gets the opt_out of this WebhookNewContactPayload.  # noqa: E501


        :return: The opt_out of this WebhookNewContactPayload.  # noqa: E501
        :rtype: bool
        """
        return self._opt_out

    @opt_out.setter
    def opt_out(self, opt_out):
        """Sets the opt_out of this WebhookNewContactPayload.


        :param opt_out: The opt_out of this WebhookNewContactPayload.  # noqa: E501
        :type: bool
        """

        self._opt_out = opt_out

    @property
    def primary_email_address(self):
        """Gets the primary_email_address of this WebhookNewContactPayload.  # noqa: E501


        :return: The primary_email_address of this WebhookNewContactPayload.  # noqa: E501
        :rtype: str
        """
        return self._primary_email_address

    @primary_email_address.setter
    def primary_email_address(self, primary_email_address):
        """Sets the primary_email_address of this WebhookNewContactPayload.


        :param primary_email_address: The primary_email_address of this WebhookNewContactPayload.  # noqa: E501
        :type: str
        """

        self._primary_email_address = primary_email_address

    @property
    def tags(self):
        """Gets the tags of this WebhookNewContactPayload.  # noqa: E501


        :return: The tags of this WebhookNewContactPayload.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WebhookNewContactPayload.


        :param tags: The tags of this WebhookNewContactPayload.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def webhook_id(self):
        """Gets the webhook_id of this WebhookNewContactPayload.  # noqa: E501

        ID of webhook entity being triggered  # noqa: E501

        :return: The webhook_id of this WebhookNewContactPayload.  # noqa: E501
        :rtype: str
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this WebhookNewContactPayload.

        ID of webhook entity being triggered  # noqa: E501

        :param webhook_id: The webhook_id of this WebhookNewContactPayload.  # noqa: E501
        :type: str
        """

        self._webhook_id = webhook_id

    @property
    def webhook_name(self):
        """Gets the webhook_name of this WebhookNewContactPayload.  # noqa: E501

        Name of the webhook being triggered  # noqa: E501

        :return: The webhook_name of this WebhookNewContactPayload.  # noqa: E501
        :rtype: str
        """
        return self._webhook_name

    @webhook_name.setter
    def webhook_name(self, webhook_name):
        """Sets the webhook_name of this WebhookNewContactPayload.

        Name of the webhook being triggered  # noqa: E501

        :param webhook_name: The webhook_name of this WebhookNewContactPayload.  # noqa: E501
        :type: str
        """

        self._webhook_name = webhook_name

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
        if not isinstance(other, WebhookNewContactPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookNewContactPayload):
            return True

        return self.to_dict() != other.to_dict()
