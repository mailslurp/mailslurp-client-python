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


class WebhookNewEmailPayload(object):
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
        'inbox_id': 'str',
        'email_id': 'str',
        'created_at': 'datetime',
        'to': 'list[str]',
        '_from': 'str',
        'cc': 'list[str]',
        'bcc': 'list[str]',
        'subject': 'str',
        'attachment_meta_datas': 'list[AttachmentMetaData]'
    }

    attribute_map = {
        'message_id': 'messageId',
        'webhook_id': 'webhookId',
        'event_name': 'eventName',
        'webhook_name': 'webhookName',
        'inbox_id': 'inboxId',
        'email_id': 'emailId',
        'created_at': 'createdAt',
        'to': 'to',
        '_from': 'from',
        'cc': 'cc',
        'bcc': 'bcc',
        'subject': 'subject',
        'attachment_meta_datas': 'attachmentMetaDatas'
    }

    def __init__(self, message_id=None, webhook_id=None, event_name=None, webhook_name=None, inbox_id=None, email_id=None, created_at=None, to=None, _from=None, cc=None, bcc=None, subject=None, attachment_meta_datas=None, local_vars_configuration=None):  # noqa: E501
        """WebhookNewEmailPayload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message_id = None
        self._webhook_id = None
        self._event_name = None
        self._webhook_name = None
        self._inbox_id = None
        self._email_id = None
        self._created_at = None
        self._to = None
        self.__from = None
        self._cc = None
        self._bcc = None
        self._subject = None
        self._attachment_meta_datas = None
        self.discriminator = None

        if message_id is not None:
            self.message_id = message_id
        if webhook_id is not None:
            self.webhook_id = webhook_id
        if event_name is not None:
            self.event_name = event_name
        if webhook_name is not None:
            self.webhook_name = webhook_name
        if inbox_id is not None:
            self.inbox_id = inbox_id
        if email_id is not None:
            self.email_id = email_id
        if created_at is not None:
            self.created_at = created_at
        if to is not None:
            self.to = to
        if _from is not None:
            self._from = _from
        if cc is not None:
            self.cc = cc
        if bcc is not None:
            self.bcc = bcc
        if subject is not None:
            self.subject = subject
        if attachment_meta_datas is not None:
            self.attachment_meta_datas = attachment_meta_datas

    @property
    def message_id(self):
        """Gets the message_id of this WebhookNewEmailPayload.  # noqa: E501

        Idempotent message ID. Store this ID locally or in a database to prevent message duplication.  # noqa: E501

        :return: The message_id of this WebhookNewEmailPayload.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this WebhookNewEmailPayload.

        Idempotent message ID. Store this ID locally or in a database to prevent message duplication.  # noqa: E501

        :param message_id: The message_id of this WebhookNewEmailPayload.  # noqa: E501
        :type: str
        """

        self._message_id = message_id

    @property
    def webhook_id(self):
        """Gets the webhook_id of this WebhookNewEmailPayload.  # noqa: E501

        ID of webhook entity being triggered  # noqa: E501

        :return: The webhook_id of this WebhookNewEmailPayload.  # noqa: E501
        :rtype: str
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this WebhookNewEmailPayload.

        ID of webhook entity being triggered  # noqa: E501

        :param webhook_id: The webhook_id of this WebhookNewEmailPayload.  # noqa: E501
        :type: str
        """

        self._webhook_id = webhook_id

    @property
    def event_name(self):
        """Gets the event_name of this WebhookNewEmailPayload.  # noqa: E501

        Name of the event type webhook is being triggered for.  # noqa: E501

        :return: The event_name of this WebhookNewEmailPayload.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this WebhookNewEmailPayload.

        Name of the event type webhook is being triggered for.  # noqa: E501

        :param event_name: The event_name of this WebhookNewEmailPayload.  # noqa: E501
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
    def webhook_name(self):
        """Gets the webhook_name of this WebhookNewEmailPayload.  # noqa: E501

        Name of the webhook being triggered  # noqa: E501

        :return: The webhook_name of this WebhookNewEmailPayload.  # noqa: E501
        :rtype: str
        """
        return self._webhook_name

    @webhook_name.setter
    def webhook_name(self, webhook_name):
        """Sets the webhook_name of this WebhookNewEmailPayload.

        Name of the webhook being triggered  # noqa: E501

        :param webhook_name: The webhook_name of this WebhookNewEmailPayload.  # noqa: E501
        :type: str
        """

        self._webhook_name = webhook_name

    @property
    def inbox_id(self):
        """Gets the inbox_id of this WebhookNewEmailPayload.  # noqa: E501

        Id of the inbox that received an email  # noqa: E501

        :return: The inbox_id of this WebhookNewEmailPayload.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this WebhookNewEmailPayload.

        Id of the inbox that received an email  # noqa: E501

        :param inbox_id: The inbox_id of this WebhookNewEmailPayload.  # noqa: E501
        :type: str
        """

        self._inbox_id = inbox_id

    @property
    def email_id(self):
        """Gets the email_id of this WebhookNewEmailPayload.  # noqa: E501

        ID of the email that was received. Use this ID for fetching the email with the `EmailController`.  # noqa: E501

        :return: The email_id of this WebhookNewEmailPayload.  # noqa: E501
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        """Sets the email_id of this WebhookNewEmailPayload.

        ID of the email that was received. Use this ID for fetching the email with the `EmailController`.  # noqa: E501

        :param email_id: The email_id of this WebhookNewEmailPayload.  # noqa: E501
        :type: str
        """

        self._email_id = email_id

    @property
    def created_at(self):
        """Gets the created_at of this WebhookNewEmailPayload.  # noqa: E501

        Date time of event creation  # noqa: E501

        :return: The created_at of this WebhookNewEmailPayload.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WebhookNewEmailPayload.

        Date time of event creation  # noqa: E501

        :param created_at: The created_at of this WebhookNewEmailPayload.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def to(self):
        """Gets the to of this WebhookNewEmailPayload.  # noqa: E501

        List of `To` recipient email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :return: The to of this WebhookNewEmailPayload.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this WebhookNewEmailPayload.

        List of `To` recipient email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :param to: The to of this WebhookNewEmailPayload.  # noqa: E501
        :type: list[str]
        """

        self._to = to

    @property
    def _from(self):
        """Gets the _from of this WebhookNewEmailPayload.  # noqa: E501

        Who the email was sent from. An email address - see fromName for the sender name.  # noqa: E501

        :return: The _from of this WebhookNewEmailPayload.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this WebhookNewEmailPayload.

        Who the email was sent from. An email address - see fromName for the sender name.  # noqa: E501

        :param _from: The _from of this WebhookNewEmailPayload.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def cc(self):
        """Gets the cc of this WebhookNewEmailPayload.  # noqa: E501

        List of `CC` recipients email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :return: The cc of this WebhookNewEmailPayload.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this WebhookNewEmailPayload.

        List of `CC` recipients email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :param cc: The cc of this WebhookNewEmailPayload.  # noqa: E501
        :type: list[str]
        """

        self._cc = cc

    @property
    def bcc(self):
        """Gets the bcc of this WebhookNewEmailPayload.  # noqa: E501

        List of `BCC` recipients email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :return: The bcc of this WebhookNewEmailPayload.  # noqa: E501
        :rtype: list[str]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this WebhookNewEmailPayload.

        List of `BCC` recipients email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :param bcc: The bcc of this WebhookNewEmailPayload.  # noqa: E501
        :type: list[str]
        """

        self._bcc = bcc

    @property
    def subject(self):
        """Gets the subject of this WebhookNewEmailPayload.  # noqa: E501

        The subject line of the email message as specified by SMTP subject header  # noqa: E501

        :return: The subject of this WebhookNewEmailPayload.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this WebhookNewEmailPayload.

        The subject line of the email message as specified by SMTP subject header  # noqa: E501

        :param subject: The subject of this WebhookNewEmailPayload.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def attachment_meta_datas(self):
        """Gets the attachment_meta_datas of this WebhookNewEmailPayload.  # noqa: E501

        List of attachment meta data objects if attachments present  # noqa: E501

        :return: The attachment_meta_datas of this WebhookNewEmailPayload.  # noqa: E501
        :rtype: list[AttachmentMetaData]
        """
        return self._attachment_meta_datas

    @attachment_meta_datas.setter
    def attachment_meta_datas(self, attachment_meta_datas):
        """Sets the attachment_meta_datas of this WebhookNewEmailPayload.

        List of attachment meta data objects if attachments present  # noqa: E501

        :param attachment_meta_datas: The attachment_meta_datas of this WebhookNewEmailPayload.  # noqa: E501
        :type: list[AttachmentMetaData]
        """

        self._attachment_meta_datas = attachment_meta_datas

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
        if not isinstance(other, WebhookNewEmailPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookNewEmailPayload):
            return True

        return self.to_dict() != other.to_dict()
