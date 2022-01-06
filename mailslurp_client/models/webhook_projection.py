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


class WebhookProjection(object):
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
        'name': 'str',
        'id': 'str',
        'url': 'str',
        'inbox_id': 'str',
        'event_name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'url': 'url',
        'inbox_id': 'inboxId',
        'event_name': 'eventName',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, name=None, id=None, url=None, inbox_id=None, event_name=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """WebhookProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._id = None
        self._url = None
        self._inbox_id = None
        self._event_name = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if inbox_id is not None:
            self.inbox_id = inbox_id
        if event_name is not None:
            self.event_name = event_name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def name(self):
        """Gets the name of this WebhookProjection.  # noqa: E501


        :return: The name of this WebhookProjection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebhookProjection.


        :param name: The name of this WebhookProjection.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this WebhookProjection.  # noqa: E501


        :return: The id of this WebhookProjection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookProjection.


        :param id: The id of this WebhookProjection.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this WebhookProjection.  # noqa: E501


        :return: The url of this WebhookProjection.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookProjection.


        :param url: The url of this WebhookProjection.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def inbox_id(self):
        """Gets the inbox_id of this WebhookProjection.  # noqa: E501


        :return: The inbox_id of this WebhookProjection.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this WebhookProjection.


        :param inbox_id: The inbox_id of this WebhookProjection.  # noqa: E501
        :type: str
        """

        self._inbox_id = inbox_id

    @property
    def event_name(self):
        """Gets the event_name of this WebhookProjection.  # noqa: E501


        :return: The event_name of this WebhookProjection.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this WebhookProjection.


        :param event_name: The event_name of this WebhookProjection.  # noqa: E501
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
    def created_at(self):
        """Gets the created_at of this WebhookProjection.  # noqa: E501


        :return: The created_at of this WebhookProjection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WebhookProjection.


        :param created_at: The created_at of this WebhookProjection.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this WebhookProjection.  # noqa: E501


        :return: The updated_at of this WebhookProjection.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this WebhookProjection.


        :param updated_at: The updated_at of this WebhookProjection.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, WebhookProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookProjection):
            return True

        return self.to_dict() != other.to_dict()
