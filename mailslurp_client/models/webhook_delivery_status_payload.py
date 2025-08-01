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


class WebhookDeliveryStatusPayload(object):
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
        'id': 'str',
        'user_id': 'str',
        'sent_id': 'str',
        'remote_mta_ip': 'str',
        'inbox_id': 'str',
        'reporting_mta': 'str',
        'recipients': 'list[str]',
        'smtp_response': 'str',
        'smtp_status_code': 'int',
        'processing_time_millis': 'int',
        'received': 'datetime',
        'subject': 'str'
    }

    attribute_map = {
        'message_id': 'messageId',
        'webhook_id': 'webhookId',
        'event_name': 'eventName',
        'webhook_name': 'webhookName',
        'id': 'id',
        'user_id': 'userId',
        'sent_id': 'sentId',
        'remote_mta_ip': 'remoteMtaIp',
        'inbox_id': 'inboxId',
        'reporting_mta': 'reportingMta',
        'recipients': 'recipients',
        'smtp_response': 'smtpResponse',
        'smtp_status_code': 'smtpStatusCode',
        'processing_time_millis': 'processingTimeMillis',
        'received': 'received',
        'subject': 'subject'
    }

    def __init__(self, message_id=None, webhook_id=None, event_name=None, webhook_name=None, id=None, user_id=None, sent_id=None, remote_mta_ip=None, inbox_id=None, reporting_mta=None, recipients=None, smtp_response=None, smtp_status_code=None, processing_time_millis=None, received=None, subject=None, local_vars_configuration=None):  # noqa: E501
        """WebhookDeliveryStatusPayload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message_id = None
        self._webhook_id = None
        self._event_name = None
        self._webhook_name = None
        self._id = None
        self._user_id = None
        self._sent_id = None
        self._remote_mta_ip = None
        self._inbox_id = None
        self._reporting_mta = None
        self._recipients = None
        self._smtp_response = None
        self._smtp_status_code = None
        self._processing_time_millis = None
        self._received = None
        self._subject = None
        self.discriminator = None

        self.message_id = message_id
        self.webhook_id = webhook_id
        self.event_name = event_name
        self.webhook_name = webhook_name
        self.id = id
        self.user_id = user_id
        self.sent_id = sent_id
        self.remote_mta_ip = remote_mta_ip
        self.inbox_id = inbox_id
        self.reporting_mta = reporting_mta
        self.recipients = recipients
        self.smtp_response = smtp_response
        self.smtp_status_code = smtp_status_code
        self.processing_time_millis = processing_time_millis
        self.received = received
        self.subject = subject

    @property
    def message_id(self):
        """Gets the message_id of this WebhookDeliveryStatusPayload.  # noqa: E501

        Idempotent message ID. Store this ID locally or in a database to prevent message duplication.  # noqa: E501

        :return: The message_id of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this WebhookDeliveryStatusPayload.

        Idempotent message ID. Store this ID locally or in a database to prevent message duplication.  # noqa: E501

        :param message_id: The message_id of this WebhookDeliveryStatusPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message_id is None:  # noqa: E501
            raise ValueError("Invalid value for `message_id`, must not be `None`")  # noqa: E501

        self._message_id = message_id

    @property
    def webhook_id(self):
        """Gets the webhook_id of this WebhookDeliveryStatusPayload.  # noqa: E501

        ID of webhook entity being triggered  # noqa: E501

        :return: The webhook_id of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: str
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this WebhookDeliveryStatusPayload.

        ID of webhook entity being triggered  # noqa: E501

        :param webhook_id: The webhook_id of this WebhookDeliveryStatusPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and webhook_id is None:  # noqa: E501
            raise ValueError("Invalid value for `webhook_id`, must not be `None`")  # noqa: E501

        self._webhook_id = webhook_id

    @property
    def event_name(self):
        """Gets the event_name of this WebhookDeliveryStatusPayload.  # noqa: E501

        Name of the event type webhook is being triggered for.  # noqa: E501

        :return: The event_name of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this WebhookDeliveryStatusPayload.

        Name of the event type webhook is being triggered for.  # noqa: E501

        :param event_name: The event_name of this WebhookDeliveryStatusPayload.  # noqa: E501
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
        """Gets the webhook_name of this WebhookDeliveryStatusPayload.  # noqa: E501

        Name of the webhook being triggered  # noqa: E501

        :return: The webhook_name of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: str
        """
        return self._webhook_name

    @webhook_name.setter
    def webhook_name(self, webhook_name):
        """Sets the webhook_name of this WebhookDeliveryStatusPayload.

        Name of the webhook being triggered  # noqa: E501

        :param webhook_name: The webhook_name of this WebhookDeliveryStatusPayload.  # noqa: E501
        :type: str
        """

        self._webhook_name = webhook_name

    @property
    def id(self):
        """Gets the id of this WebhookDeliveryStatusPayload.  # noqa: E501

        ID of delivery status  # noqa: E501

        :return: The id of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookDeliveryStatusPayload.

        ID of delivery status  # noqa: E501

        :param id: The id of this WebhookDeliveryStatusPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this WebhookDeliveryStatusPayload.  # noqa: E501

        User ID of event  # noqa: E501

        :return: The user_id of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this WebhookDeliveryStatusPayload.

        User ID of event  # noqa: E501

        :param user_id: The user_id of this WebhookDeliveryStatusPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def sent_id(self):
        """Gets the sent_id of this WebhookDeliveryStatusPayload.  # noqa: E501

        ID of sent email  # noqa: E501

        :return: The sent_id of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: str
        """
        return self._sent_id

    @sent_id.setter
    def sent_id(self, sent_id):
        """Sets the sent_id of this WebhookDeliveryStatusPayload.

        ID of sent email  # noqa: E501

        :param sent_id: The sent_id of this WebhookDeliveryStatusPayload.  # noqa: E501
        :type: str
        """

        self._sent_id = sent_id

    @property
    def remote_mta_ip(self):
        """Gets the remote_mta_ip of this WebhookDeliveryStatusPayload.  # noqa: E501

        IP address of the remote Mail Transfer Agent  # noqa: E501

        :return: The remote_mta_ip of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: str
        """
        return self._remote_mta_ip

    @remote_mta_ip.setter
    def remote_mta_ip(self, remote_mta_ip):
        """Sets the remote_mta_ip of this WebhookDeliveryStatusPayload.

        IP address of the remote Mail Transfer Agent  # noqa: E501

        :param remote_mta_ip: The remote_mta_ip of this WebhookDeliveryStatusPayload.  # noqa: E501
        :type: str
        """

        self._remote_mta_ip = remote_mta_ip

    @property
    def inbox_id(self):
        """Gets the inbox_id of this WebhookDeliveryStatusPayload.  # noqa: E501

        Id of the inbox  # noqa: E501

        :return: The inbox_id of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this WebhookDeliveryStatusPayload.

        Id of the inbox  # noqa: E501

        :param inbox_id: The inbox_id of this WebhookDeliveryStatusPayload.  # noqa: E501
        :type: str
        """

        self._inbox_id = inbox_id

    @property
    def reporting_mta(self):
        """Gets the reporting_mta of this WebhookDeliveryStatusPayload.  # noqa: E501

        Mail Transfer Agent reporting delivery status  # noqa: E501

        :return: The reporting_mta of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: str
        """
        return self._reporting_mta

    @reporting_mta.setter
    def reporting_mta(self, reporting_mta):
        """Sets the reporting_mta of this WebhookDeliveryStatusPayload.

        Mail Transfer Agent reporting delivery status  # noqa: E501

        :param reporting_mta: The reporting_mta of this WebhookDeliveryStatusPayload.  # noqa: E501
        :type: str
        """

        self._reporting_mta = reporting_mta

    @property
    def recipients(self):
        """Gets the recipients of this WebhookDeliveryStatusPayload.  # noqa: E501

        Recipients for delivery  # noqa: E501

        :return: The recipients of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: list[str]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this WebhookDeliveryStatusPayload.

        Recipients for delivery  # noqa: E501

        :param recipients: The recipients of this WebhookDeliveryStatusPayload.  # noqa: E501
        :type: list[str]
        """

        self._recipients = recipients

    @property
    def smtp_response(self):
        """Gets the smtp_response of this WebhookDeliveryStatusPayload.  # noqa: E501

        SMTP server response message  # noqa: E501

        :return: The smtp_response of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: str
        """
        return self._smtp_response

    @smtp_response.setter
    def smtp_response(self, smtp_response):
        """Sets the smtp_response of this WebhookDeliveryStatusPayload.

        SMTP server response message  # noqa: E501

        :param smtp_response: The smtp_response of this WebhookDeliveryStatusPayload.  # noqa: E501
        :type: str
        """

        self._smtp_response = smtp_response

    @property
    def smtp_status_code(self):
        """Gets the smtp_status_code of this WebhookDeliveryStatusPayload.  # noqa: E501

        SMTP server status  # noqa: E501

        :return: The smtp_status_code of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: int
        """
        return self._smtp_status_code

    @smtp_status_code.setter
    def smtp_status_code(self, smtp_status_code):
        """Sets the smtp_status_code of this WebhookDeliveryStatusPayload.

        SMTP server status  # noqa: E501

        :param smtp_status_code: The smtp_status_code of this WebhookDeliveryStatusPayload.  # noqa: E501
        :type: int
        """

        self._smtp_status_code = smtp_status_code

    @property
    def processing_time_millis(self):
        """Gets the processing_time_millis of this WebhookDeliveryStatusPayload.  # noqa: E501

        Time in milliseconds for delivery processing  # noqa: E501

        :return: The processing_time_millis of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: int
        """
        return self._processing_time_millis

    @processing_time_millis.setter
    def processing_time_millis(self, processing_time_millis):
        """Sets the processing_time_millis of this WebhookDeliveryStatusPayload.

        Time in milliseconds for delivery processing  # noqa: E501

        :param processing_time_millis: The processing_time_millis of this WebhookDeliveryStatusPayload.  # noqa: E501
        :type: int
        """

        self._processing_time_millis = processing_time_millis

    @property
    def received(self):
        """Gets the received of this WebhookDeliveryStatusPayload.  # noqa: E501

        Time event was received  # noqa: E501

        :return: The received of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: datetime
        """
        return self._received

    @received.setter
    def received(self, received):
        """Sets the received of this WebhookDeliveryStatusPayload.

        Time event was received  # noqa: E501

        :param received: The received of this WebhookDeliveryStatusPayload.  # noqa: E501
        :type: datetime
        """

        self._received = received

    @property
    def subject(self):
        """Gets the subject of this WebhookDeliveryStatusPayload.  # noqa: E501

        Email subject  # noqa: E501

        :return: The subject of this WebhookDeliveryStatusPayload.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this WebhookDeliveryStatusPayload.

        Email subject  # noqa: E501

        :param subject: The subject of this WebhookDeliveryStatusPayload.  # noqa: E501
        :type: str
        """

        self._subject = subject

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
        if not isinstance(other, WebhookDeliveryStatusPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookDeliveryStatusPayload):
            return True

        return self.to_dict() != other.to_dict()
