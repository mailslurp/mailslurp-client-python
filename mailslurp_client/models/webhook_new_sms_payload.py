# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails and SMS from dynamically allocated email addresses and phone numbers. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class WebhookNewSmsPayload(object):
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
        'message_id': 'str',
        'webhook_id': 'str',
        'event_name': 'str',
        'webhook_name': 'str',
        'sms_id': 'str',
        'user_id': 'str',
        'phone_number': 'str',
        'to_number': 'str',
        'from_number': 'str',
        'body': 'str',
        'read': 'bool'
    }

    attribute_map = {
        'message_id': 'messageId',
        'webhook_id': 'webhookId',
        'event_name': 'eventName',
        'webhook_name': 'webhookName',
        'sms_id': 'smsId',
        'user_id': 'userId',
        'phone_number': 'phoneNumber',
        'to_number': 'toNumber',
        'from_number': 'fromNumber',
        'body': 'body',
        'read': 'read'
    }

    def __init__(self, message_id=None, webhook_id=None, event_name=None, webhook_name=None, sms_id=None, user_id=None, phone_number=None, to_number=None, from_number=None, body=None, read=None, local_vars_configuration=None):  # noqa: E501
        """WebhookNewSmsPayload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message_id = None
        self._webhook_id = None
        self._event_name = None
        self._webhook_name = None
        self._sms_id = None
        self._user_id = None
        self._phone_number = None
        self._to_number = None
        self._from_number = None
        self._body = None
        self._read = None
        self.discriminator = None

        self.message_id = message_id
        self.webhook_id = webhook_id
        self.event_name = event_name
        self.webhook_name = webhook_name
        self.sms_id = sms_id
        self.user_id = user_id
        self.phone_number = phone_number
        self.to_number = to_number
        self.from_number = from_number
        self.body = body
        self.read = read

    @property
    def message_id(self):
        """Gets the message_id of this WebhookNewSmsPayload.  # noqa: E501

        Idempotent message ID. Store this ID locally or in a database to prevent message duplication.  # noqa: E501

        :return: The message_id of this WebhookNewSmsPayload.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this WebhookNewSmsPayload.

        Idempotent message ID. Store this ID locally or in a database to prevent message duplication.  # noqa: E501

        :param message_id: The message_id of this WebhookNewSmsPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message_id is None:  # noqa: E501
            raise ValueError("Invalid value for `message_id`, must not be `None`")  # noqa: E501

        self._message_id = message_id

    @property
    def webhook_id(self):
        """Gets the webhook_id of this WebhookNewSmsPayload.  # noqa: E501

        ID of webhook entity being triggered  # noqa: E501

        :return: The webhook_id of this WebhookNewSmsPayload.  # noqa: E501
        :rtype: str
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this WebhookNewSmsPayload.

        ID of webhook entity being triggered  # noqa: E501

        :param webhook_id: The webhook_id of this WebhookNewSmsPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and webhook_id is None:  # noqa: E501
            raise ValueError("Invalid value for `webhook_id`, must not be `None`")  # noqa: E501

        self._webhook_id = webhook_id

    @property
    def event_name(self):
        """Gets the event_name of this WebhookNewSmsPayload.  # noqa: E501

        Name of the event type webhook is being triggered for.  # noqa: E501

        :return: The event_name of this WebhookNewSmsPayload.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this WebhookNewSmsPayload.

        Name of the event type webhook is being triggered for.  # noqa: E501

        :param event_name: The event_name of this WebhookNewSmsPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and event_name is None:  # noqa: E501
            raise ValueError("Invalid value for `event_name`, must not be `None`")  # noqa: E501
        allowed_values = ["EMAIL_RECEIVED", "NEW_AI_TRANSFORM_RESULT", "NEW_EMAIL", "NEW_CONTACT", "NEW_ATTACHMENT", "EMAIL_OPENED", "EMAIL_READ", "DELIVERY_STATUS", "BOUNCE", "BOUNCE_RECIPIENT", "NEW_SMS", "NEW_GUEST_USER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and event_name not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `event_name` ({0}), must be one of {1}"  # noqa: E501
                .format(event_name, allowed_values)
            )

        self._event_name = event_name

    @property
    def webhook_name(self):
        """Gets the webhook_name of this WebhookNewSmsPayload.  # noqa: E501

        Name of the webhook being triggered  # noqa: E501

        :return: The webhook_name of this WebhookNewSmsPayload.  # noqa: E501
        :rtype: str
        """
        return self._webhook_name

    @webhook_name.setter
    def webhook_name(self, webhook_name):
        """Sets the webhook_name of this WebhookNewSmsPayload.

        Name of the webhook being triggered  # noqa: E501

        :param webhook_name: The webhook_name of this WebhookNewSmsPayload.  # noqa: E501
        :type: str
        """

        self._webhook_name = webhook_name

    @property
    def sms_id(self):
        """Gets the sms_id of this WebhookNewSmsPayload.  # noqa: E501

        ID of SMS message  # noqa: E501

        :return: The sms_id of this WebhookNewSmsPayload.  # noqa: E501
        :rtype: str
        """
        return self._sms_id

    @sms_id.setter
    def sms_id(self, sms_id):
        """Sets the sms_id of this WebhookNewSmsPayload.

        ID of SMS message  # noqa: E501

        :param sms_id: The sms_id of this WebhookNewSmsPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sms_id is None:  # noqa: E501
            raise ValueError("Invalid value for `sms_id`, must not be `None`")  # noqa: E501

        self._sms_id = sms_id

    @property
    def user_id(self):
        """Gets the user_id of this WebhookNewSmsPayload.  # noqa: E501

        User ID of event  # noqa: E501

        :return: The user_id of this WebhookNewSmsPayload.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this WebhookNewSmsPayload.

        User ID of event  # noqa: E501

        :param user_id: The user_id of this WebhookNewSmsPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def phone_number(self):
        """Gets the phone_number of this WebhookNewSmsPayload.  # noqa: E501

        ID of phone number receiving SMS  # noqa: E501

        :return: The phone_number of this WebhookNewSmsPayload.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this WebhookNewSmsPayload.

        ID of phone number receiving SMS  # noqa: E501

        :param phone_number: The phone_number of this WebhookNewSmsPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and phone_number is None:  # noqa: E501
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def to_number(self):
        """Gets the to_number of this WebhookNewSmsPayload.  # noqa: E501

        Recipient phone number  # noqa: E501

        :return: The to_number of this WebhookNewSmsPayload.  # noqa: E501
        :rtype: str
        """
        return self._to_number

    @to_number.setter
    def to_number(self, to_number):
        """Sets the to_number of this WebhookNewSmsPayload.

        Recipient phone number  # noqa: E501

        :param to_number: The to_number of this WebhookNewSmsPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and to_number is None:  # noqa: E501
            raise ValueError("Invalid value for `to_number`, must not be `None`")  # noqa: E501

        self._to_number = to_number

    @property
    def from_number(self):
        """Gets the from_number of this WebhookNewSmsPayload.  # noqa: E501

        Sender phone number  # noqa: E501

        :return: The from_number of this WebhookNewSmsPayload.  # noqa: E501
        :rtype: str
        """
        return self._from_number

    @from_number.setter
    def from_number(self, from_number):
        """Sets the from_number of this WebhookNewSmsPayload.

        Sender phone number  # noqa: E501

        :param from_number: The from_number of this WebhookNewSmsPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and from_number is None:  # noqa: E501
            raise ValueError("Invalid value for `from_number`, must not be `None`")  # noqa: E501

        self._from_number = from_number

    @property
    def body(self):
        """Gets the body of this WebhookNewSmsPayload.  # noqa: E501

        SMS message body  # noqa: E501

        :return: The body of this WebhookNewSmsPayload.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this WebhookNewSmsPayload.

        SMS message body  # noqa: E501

        :param body: The body of this WebhookNewSmsPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and body is None:  # noqa: E501
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def read(self):
        """Gets the read of this WebhookNewSmsPayload.  # noqa: E501

        SMS has been read  # noqa: E501

        :return: The read of this WebhookNewSmsPayload.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this WebhookNewSmsPayload.

        SMS has been read  # noqa: E501

        :param read: The read of this WebhookNewSmsPayload.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and read is None:  # noqa: E501
            raise ValueError("Invalid value for `read`, must not be `None`")  # noqa: E501

        self._read = read

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
        if not isinstance(other, WebhookNewSmsPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookNewSmsPayload):
            return True

        return self.to_dict() != other.to_dict()
