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


class WebhookResultEntity(object):
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
        'http_method': 'str',
        'id': 'str',
        'inbox_id': 'str',
        'message_id': 'str',
        'response_body_extract': 'str',
        'response_status': 'int',
        'response_time_millis': 'int',
        'result_type': 'str',
        'updated_at': 'datetime',
        'user_id': 'str',
        'webhook_event': 'str',
        'webhook_id': 'str',
        'webhook_url': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'http_method': 'httpMethod',
        'id': 'id',
        'inbox_id': 'inboxId',
        'message_id': 'messageId',
        'response_body_extract': 'responseBodyExtract',
        'response_status': 'responseStatus',
        'response_time_millis': 'responseTimeMillis',
        'result_type': 'resultType',
        'updated_at': 'updatedAt',
        'user_id': 'userId',
        'webhook_event': 'webhookEvent',
        'webhook_id': 'webhookId',
        'webhook_url': 'webhookUrl'
    }

    def __init__(self, created_at=None, http_method=None, id=None, inbox_id=None, message_id=None, response_body_extract=None, response_status=None, response_time_millis=None, result_type=None, updated_at=None, user_id=None, webhook_event=None, webhook_id=None, webhook_url=None, local_vars_configuration=None):  # noqa: E501
        """WebhookResultEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._http_method = None
        self._id = None
        self._inbox_id = None
        self._message_id = None
        self._response_body_extract = None
        self._response_status = None
        self._response_time_millis = None
        self._result_type = None
        self._updated_at = None
        self._user_id = None
        self._webhook_event = None
        self._webhook_id = None
        self._webhook_url = None
        self.discriminator = None

        self.created_at = created_at
        self.http_method = http_method
        if id is not None:
            self.id = id
        self.inbox_id = inbox_id
        self.message_id = message_id
        if response_body_extract is not None:
            self.response_body_extract = response_body_extract
        if response_status is not None:
            self.response_status = response_status
        self.response_time_millis = response_time_millis
        if result_type is not None:
            self.result_type = result_type
        self.updated_at = updated_at
        self.user_id = user_id
        self.webhook_event = webhook_event
        self.webhook_id = webhook_id
        self.webhook_url = webhook_url

    @property
    def created_at(self):
        """Gets the created_at of this WebhookResultEntity.  # noqa: E501


        :return: The created_at of this WebhookResultEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WebhookResultEntity.


        :param created_at: The created_at of this WebhookResultEntity.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def http_method(self):
        """Gets the http_method of this WebhookResultEntity.  # noqa: E501


        :return: The http_method of this WebhookResultEntity.  # noqa: E501
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this WebhookResultEntity.


        :param http_method: The http_method of this WebhookResultEntity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and http_method is None:  # noqa: E501
            raise ValueError("Invalid value for `http_method`, must not be `None`")  # noqa: E501
        allowed_values = ["GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "TRACE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and http_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `http_method` ({0}), must be one of {1}"  # noqa: E501
                .format(http_method, allowed_values)
            )

        self._http_method = http_method

    @property
    def id(self):
        """Gets the id of this WebhookResultEntity.  # noqa: E501


        :return: The id of this WebhookResultEntity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookResultEntity.


        :param id: The id of this WebhookResultEntity.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def inbox_id(self):
        """Gets the inbox_id of this WebhookResultEntity.  # noqa: E501


        :return: The inbox_id of this WebhookResultEntity.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this WebhookResultEntity.


        :param inbox_id: The inbox_id of this WebhookResultEntity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and inbox_id is None:  # noqa: E501
            raise ValueError("Invalid value for `inbox_id`, must not be `None`")  # noqa: E501

        self._inbox_id = inbox_id

    @property
    def message_id(self):
        """Gets the message_id of this WebhookResultEntity.  # noqa: E501


        :return: The message_id of this WebhookResultEntity.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this WebhookResultEntity.


        :param message_id: The message_id of this WebhookResultEntity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message_id is None:  # noqa: E501
            raise ValueError("Invalid value for `message_id`, must not be `None`")  # noqa: E501

        self._message_id = message_id

    @property
    def response_body_extract(self):
        """Gets the response_body_extract of this WebhookResultEntity.  # noqa: E501


        :return: The response_body_extract of this WebhookResultEntity.  # noqa: E501
        :rtype: str
        """
        return self._response_body_extract

    @response_body_extract.setter
    def response_body_extract(self, response_body_extract):
        """Sets the response_body_extract of this WebhookResultEntity.


        :param response_body_extract: The response_body_extract of this WebhookResultEntity.  # noqa: E501
        :type: str
        """

        self._response_body_extract = response_body_extract

    @property
    def response_status(self):
        """Gets the response_status of this WebhookResultEntity.  # noqa: E501


        :return: The response_status of this WebhookResultEntity.  # noqa: E501
        :rtype: int
        """
        return self._response_status

    @response_status.setter
    def response_status(self, response_status):
        """Sets the response_status of this WebhookResultEntity.


        :param response_status: The response_status of this WebhookResultEntity.  # noqa: E501
        :type: int
        """

        self._response_status = response_status

    @property
    def response_time_millis(self):
        """Gets the response_time_millis of this WebhookResultEntity.  # noqa: E501


        :return: The response_time_millis of this WebhookResultEntity.  # noqa: E501
        :rtype: int
        """
        return self._response_time_millis

    @response_time_millis.setter
    def response_time_millis(self, response_time_millis):
        """Sets the response_time_millis of this WebhookResultEntity.


        :param response_time_millis: The response_time_millis of this WebhookResultEntity.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and response_time_millis is None:  # noqa: E501
            raise ValueError("Invalid value for `response_time_millis`, must not be `None`")  # noqa: E501

        self._response_time_millis = response_time_millis

    @property
    def result_type(self):
        """Gets the result_type of this WebhookResultEntity.  # noqa: E501


        :return: The result_type of this WebhookResultEntity.  # noqa: E501
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """Sets the result_type of this WebhookResultEntity.


        :param result_type: The result_type of this WebhookResultEntity.  # noqa: E501
        :type: str
        """
        allowed_values = ["BAD_RESPONSE", "EXCEPTION", "SUCCESS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and result_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `result_type` ({0}), must be one of {1}"  # noqa: E501
                .format(result_type, allowed_values)
            )

        self._result_type = result_type

    @property
    def updated_at(self):
        """Gets the updated_at of this WebhookResultEntity.  # noqa: E501


        :return: The updated_at of this WebhookResultEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this WebhookResultEntity.


        :param updated_at: The updated_at of this WebhookResultEntity.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def user_id(self):
        """Gets the user_id of this WebhookResultEntity.  # noqa: E501


        :return: The user_id of this WebhookResultEntity.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this WebhookResultEntity.


        :param user_id: The user_id of this WebhookResultEntity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def webhook_event(self):
        """Gets the webhook_event of this WebhookResultEntity.  # noqa: E501


        :return: The webhook_event of this WebhookResultEntity.  # noqa: E501
        :rtype: str
        """
        return self._webhook_event

    @webhook_event.setter
    def webhook_event(self, webhook_event):
        """Sets the webhook_event of this WebhookResultEntity.


        :param webhook_event: The webhook_event of this WebhookResultEntity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and webhook_event is None:  # noqa: E501
            raise ValueError("Invalid value for `webhook_event`, must not be `None`")  # noqa: E501
        allowed_values = ["EMAIL_RECEIVED", "NEW_EMAIL", "NEW_CONTACT", "NEW_ATTACHMENT", "EMAIL_OPENED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and webhook_event not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `webhook_event` ({0}), must be one of {1}"  # noqa: E501
                .format(webhook_event, allowed_values)
            )

        self._webhook_event = webhook_event

    @property
    def webhook_id(self):
        """Gets the webhook_id of this WebhookResultEntity.  # noqa: E501


        :return: The webhook_id of this WebhookResultEntity.  # noqa: E501
        :rtype: str
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this WebhookResultEntity.


        :param webhook_id: The webhook_id of this WebhookResultEntity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and webhook_id is None:  # noqa: E501
            raise ValueError("Invalid value for `webhook_id`, must not be `None`")  # noqa: E501

        self._webhook_id = webhook_id

    @property
    def webhook_url(self):
        """Gets the webhook_url of this WebhookResultEntity.  # noqa: E501


        :return: The webhook_url of this WebhookResultEntity.  # noqa: E501
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        """Sets the webhook_url of this WebhookResultEntity.


        :param webhook_url: The webhook_url of this WebhookResultEntity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and webhook_url is None:  # noqa: E501
            raise ValueError("Invalid value for `webhook_url`, must not be `None`")  # noqa: E501

        self._webhook_url = webhook_url

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
        if not isinstance(other, WebhookResultEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookResultEntity):
            return True

        return self.to_dict() != other.to_dict()
