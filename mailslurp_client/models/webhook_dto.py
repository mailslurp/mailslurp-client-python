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


class WebhookDto(object):
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
        'basic_auth': 'bool',
        'created_at': 'datetime',
        'id': 'str',
        'inbox_id': 'str',
        'method': 'str',
        'name': 'str',
        'payload_json_schema': 'str',
        'updated_at': 'datetime',
        'url': 'str'
    }

    attribute_map = {
        'basic_auth': 'basicAuth',
        'created_at': 'createdAt',
        'id': 'id',
        'inbox_id': 'inboxId',
        'method': 'method',
        'name': 'name',
        'payload_json_schema': 'payloadJsonSchema',
        'updated_at': 'updatedAt',
        'url': 'url'
    }

    def __init__(self, basic_auth=None, created_at=None, id=None, inbox_id=None, method=None, name=None, payload_json_schema=None, updated_at=None, url=None, local_vars_configuration=None):  # noqa: E501
        """WebhookDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._basic_auth = None
        self._created_at = None
        self._id = None
        self._inbox_id = None
        self._method = None
        self._name = None
        self._payload_json_schema = None
        self._updated_at = None
        self._url = None
        self.discriminator = None

        if basic_auth is not None:
            self.basic_auth = basic_auth
        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if inbox_id is not None:
            self.inbox_id = inbox_id
        if method is not None:
            self.method = method
        if name is not None:
            self.name = name
        if payload_json_schema is not None:
            self.payload_json_schema = payload_json_schema
        self.updated_at = updated_at
        if url is not None:
            self.url = url

    @property
    def basic_auth(self):
        """Gets the basic_auth of this WebhookDto.  # noqa: E501

        Does webhook expect basic authentication? If true it means you created this webhook with a username and password. MailSlurp will use these in the URL to authenticate itself.  # noqa: E501

        :return: The basic_auth of this WebhookDto.  # noqa: E501
        :rtype: bool
        """
        return self._basic_auth

    @basic_auth.setter
    def basic_auth(self, basic_auth):
        """Sets the basic_auth of this WebhookDto.

        Does webhook expect basic authentication? If true it means you created this webhook with a username and password. MailSlurp will use these in the URL to authenticate itself.  # noqa: E501

        :param basic_auth: The basic_auth of this WebhookDto.  # noqa: E501
        :type: bool
        """

        self._basic_auth = basic_auth

    @property
    def created_at(self):
        """Gets the created_at of this WebhookDto.  # noqa: E501

        When the webhook was created  # noqa: E501

        :return: The created_at of this WebhookDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WebhookDto.

        When the webhook was created  # noqa: E501

        :param created_at: The created_at of this WebhookDto.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this WebhookDto.  # noqa: E501

        ID of the Webhook  # noqa: E501

        :return: The id of this WebhookDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookDto.

        ID of the Webhook  # noqa: E501

        :param id: The id of this WebhookDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def inbox_id(self):
        """Gets the inbox_id of this WebhookDto.  # noqa: E501

        The inbox that the Webhook will be triggered by  # noqa: E501

        :return: The inbox_id of this WebhookDto.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this WebhookDto.

        The inbox that the Webhook will be triggered by  # noqa: E501

        :param inbox_id: The inbox_id of this WebhookDto.  # noqa: E501
        :type: str
        """

        self._inbox_id = inbox_id

    @property
    def method(self):
        """Gets the method of this WebhookDto.  # noqa: E501

        HTTP method that your server endpoint must listen for  # noqa: E501

        :return: The method of this WebhookDto.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this WebhookDto.

        HTTP method that your server endpoint must listen for  # noqa: E501

        :param method: The method of this WebhookDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "TRACE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def name(self):
        """Gets the name of this WebhookDto.  # noqa: E501

        Name of the webhook  # noqa: E501

        :return: The name of this WebhookDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebhookDto.

        Name of the webhook  # noqa: E501

        :param name: The name of this WebhookDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def payload_json_schema(self):
        """Gets the payload_json_schema of this WebhookDto.  # noqa: E501

        JSON Schema for the payload that will be sent to your URL via the HTTP method described.  # noqa: E501

        :return: The payload_json_schema of this WebhookDto.  # noqa: E501
        :rtype: str
        """
        return self._payload_json_schema

    @payload_json_schema.setter
    def payload_json_schema(self, payload_json_schema):
        """Sets the payload_json_schema of this WebhookDto.

        JSON Schema for the payload that will be sent to your URL via the HTTP method described.  # noqa: E501

        :param payload_json_schema: The payload_json_schema of this WebhookDto.  # noqa: E501
        :type: str
        """

        self._payload_json_schema = payload_json_schema

    @property
    def updated_at(self):
        """Gets the updated_at of this WebhookDto.  # noqa: E501


        :return: The updated_at of this WebhookDto.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this WebhookDto.


        :param updated_at: The updated_at of this WebhookDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def url(self):
        """Gets the url of this WebhookDto.  # noqa: E501

        URL of your server that the webhook will be sent to. The schema of the JSON that is sent is described by the payloadJsonSchema.  # noqa: E501

        :return: The url of this WebhookDto.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookDto.

        URL of your server that the webhook will be sent to. The schema of the JSON that is sent is described by the payloadJsonSchema.  # noqa: E501

        :param url: The url of this WebhookDto.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, WebhookDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookDto):
            return True

        return self.to_dict() != other.to_dict()