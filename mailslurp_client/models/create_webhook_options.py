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


class CreateWebhookOptions(object):
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
        'url': 'str',
        'basic_auth': 'BasicAuthOptions',
        'name': 'str',
        'event_name': 'str',
        'include_headers': 'WebhookHeaders',
        'request_body_template': 'str',
        'ai_transform_id': 'str',
        'use_static_ip_range': 'bool',
        'ignore_insecure_ssl_certificates': 'bool',
        'tags': 'list[str]'
    }

    attribute_map = {
        'url': 'url',
        'basic_auth': 'basicAuth',
        'name': 'name',
        'event_name': 'eventName',
        'include_headers': 'includeHeaders',
        'request_body_template': 'requestBodyTemplate',
        'ai_transform_id': 'aiTransformId',
        'use_static_ip_range': 'useStaticIpRange',
        'ignore_insecure_ssl_certificates': 'ignoreInsecureSslCertificates',
        'tags': 'tags'
    }

    def __init__(self, url=None, basic_auth=None, name=None, event_name=None, include_headers=None, request_body_template=None, ai_transform_id=None, use_static_ip_range=False, ignore_insecure_ssl_certificates=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """CreateWebhookOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._basic_auth = None
        self._name = None
        self._event_name = None
        self._include_headers = None
        self._request_body_template = None
        self._ai_transform_id = None
        self._use_static_ip_range = None
        self._ignore_insecure_ssl_certificates = None
        self._tags = None
        self.discriminator = None

        self.url = url
        self.basic_auth = basic_auth
        self.name = name
        self.event_name = event_name
        if include_headers is not None:
            self.include_headers = include_headers
        self.request_body_template = request_body_template
        self.ai_transform_id = ai_transform_id
        self.use_static_ip_range = use_static_ip_range
        self.ignore_insecure_ssl_certificates = ignore_insecure_ssl_certificates
        self.tags = tags

    @property
    def url(self):
        """Gets the url of this CreateWebhookOptions.  # noqa: E501

        Public URL on your server that MailSlurp can post WebhookNotification payload to when an email is received or an event is trigger. The payload of the submitted JSON is dependent on the webhook event type. See docs.mailslurp.com/webhooks for event payload documentation.  # noqa: E501

        :return: The url of this CreateWebhookOptions.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateWebhookOptions.

        Public URL on your server that MailSlurp can post WebhookNotification payload to when an email is received or an event is trigger. The payload of the submitted JSON is dependent on the webhook event type. See docs.mailslurp.com/webhooks for event payload documentation.  # noqa: E501

        :param url: The url of this CreateWebhookOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def basic_auth(self):
        """Gets the basic_auth of this CreateWebhookOptions.  # noqa: E501


        :return: The basic_auth of this CreateWebhookOptions.  # noqa: E501
        :rtype: BasicAuthOptions
        """
        return self._basic_auth

    @basic_auth.setter
    def basic_auth(self, basic_auth):
        """Sets the basic_auth of this CreateWebhookOptions.


        :param basic_auth: The basic_auth of this CreateWebhookOptions.  # noqa: E501
        :type: BasicAuthOptions
        """

        self._basic_auth = basic_auth

    @property
    def name(self):
        """Gets the name of this CreateWebhookOptions.  # noqa: E501

        Optional name for the webhook  # noqa: E501

        :return: The name of this CreateWebhookOptions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateWebhookOptions.

        Optional name for the webhook  # noqa: E501

        :param name: The name of this CreateWebhookOptions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def event_name(self):
        """Gets the event_name of this CreateWebhookOptions.  # noqa: E501

        Optional webhook event name. Default is `EMAIL_RECEIVED` and is triggered when an email is received by the inbox associated with the webhook. Payload differ according to the webhook event name.  # noqa: E501

        :return: The event_name of this CreateWebhookOptions.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this CreateWebhookOptions.

        Optional webhook event name. Default is `EMAIL_RECEIVED` and is triggered when an email is received by the inbox associated with the webhook. Payload differ according to the webhook event name.  # noqa: E501

        :param event_name: The event_name of this CreateWebhookOptions.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"EMAIL_RECEIVED", "NEW_AI_TRANSFORM_RESULT", "NEW_EMAIL", "NEW_CONTACT", "NEW_ATTACHMENT", "EMAIL_OPENED", "EMAIL_READ", "DELIVERY_STATUS", "BOUNCE", "BOUNCE_RECIPIENT", "NEW_SMS", "NEW_GUEST_USER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and event_name not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `event_name` ({0}), must be one of {1}"  # noqa: E501
                .format(event_name, allowed_values)
            )

        self._event_name = event_name

    @property
    def include_headers(self):
        """Gets the include_headers of this CreateWebhookOptions.  # noqa: E501


        :return: The include_headers of this CreateWebhookOptions.  # noqa: E501
        :rtype: WebhookHeaders
        """
        return self._include_headers

    @include_headers.setter
    def include_headers(self, include_headers):
        """Sets the include_headers of this CreateWebhookOptions.


        :param include_headers: The include_headers of this CreateWebhookOptions.  # noqa: E501
        :type: WebhookHeaders
        """

        self._include_headers = include_headers

    @property
    def request_body_template(self):
        """Gets the request_body_template of this CreateWebhookOptions.  # noqa: E501

        Template for the JSON body of the webhook request that will be sent to your server. Use Moustache style `{{variableName}}` templating to use parts of the standard webhook payload for the given event.  # noqa: E501

        :return: The request_body_template of this CreateWebhookOptions.  # noqa: E501
        :rtype: str
        """
        return self._request_body_template

    @request_body_template.setter
    def request_body_template(self, request_body_template):
        """Sets the request_body_template of this CreateWebhookOptions.

        Template for the JSON body of the webhook request that will be sent to your server. Use Moustache style `{{variableName}}` templating to use parts of the standard webhook payload for the given event.  # noqa: E501

        :param request_body_template: The request_body_template of this CreateWebhookOptions.  # noqa: E501
        :type: str
        """

        self._request_body_template = request_body_template

    @property
    def ai_transform_id(self):
        """Gets the ai_transform_id of this CreateWebhookOptions.  # noqa: E501

        AI Transform ID to apply to the webhook event and send a payload matching transform output schema  # noqa: E501

        :return: The ai_transform_id of this CreateWebhookOptions.  # noqa: E501
        :rtype: str
        """
        return self._ai_transform_id

    @ai_transform_id.setter
    def ai_transform_id(self, ai_transform_id):
        """Sets the ai_transform_id of this CreateWebhookOptions.

        AI Transform ID to apply to the webhook event and send a payload matching transform output schema  # noqa: E501

        :param ai_transform_id: The ai_transform_id of this CreateWebhookOptions.  # noqa: E501
        :type: str
        """

        self._ai_transform_id = ai_transform_id

    @property
    def use_static_ip_range(self):
        """Gets the use_static_ip_range of this CreateWebhookOptions.  # noqa: E501

        Use static IP range when calling webhook endpoint  # noqa: E501

        :return: The use_static_ip_range of this CreateWebhookOptions.  # noqa: E501
        :rtype: bool
        """
        return self._use_static_ip_range

    @use_static_ip_range.setter
    def use_static_ip_range(self, use_static_ip_range):
        """Sets the use_static_ip_range of this CreateWebhookOptions.

        Use static IP range when calling webhook endpoint  # noqa: E501

        :param use_static_ip_range: The use_static_ip_range of this CreateWebhookOptions.  # noqa: E501
        :type: bool
        """

        self._use_static_ip_range = use_static_ip_range

    @property
    def ignore_insecure_ssl_certificates(self):
        """Gets the ignore_insecure_ssl_certificates of this CreateWebhookOptions.  # noqa: E501

        Ignore insecure SSL certificates when sending request. Useful for self-signed certs.  # noqa: E501

        :return: The ignore_insecure_ssl_certificates of this CreateWebhookOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_insecure_ssl_certificates

    @ignore_insecure_ssl_certificates.setter
    def ignore_insecure_ssl_certificates(self, ignore_insecure_ssl_certificates):
        """Sets the ignore_insecure_ssl_certificates of this CreateWebhookOptions.

        Ignore insecure SSL certificates when sending request. Useful for self-signed certs.  # noqa: E501

        :param ignore_insecure_ssl_certificates: The ignore_insecure_ssl_certificates of this CreateWebhookOptions.  # noqa: E501
        :type: bool
        """

        self._ignore_insecure_ssl_certificates = ignore_insecure_ssl_certificates

    @property
    def tags(self):
        """Gets the tags of this CreateWebhookOptions.  # noqa: E501

        Optional list of tags  # noqa: E501

        :return: The tags of this CreateWebhookOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateWebhookOptions.

        Optional list of tags  # noqa: E501

        :param tags: The tags of this CreateWebhookOptions.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, CreateWebhookOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateWebhookOptions):
            return True

        return self.to_dict() != other.to_dict()
