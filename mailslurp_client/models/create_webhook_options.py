# coding: utf-8

"""
    MailSlurp API

    ## Introduction  [MailSlurp](https://www.mailslurp.com) is an Email API for developers and QA testers. It let's users: - create emails addresses on demand - receive emails and attachments in code - send templated HTML emails  ## About  This page contains the REST API documentation for MailSlurp. All requests require API Key authentication passed as an `x-api-key` header.  Create an account to [get your free API Key](https://app.mailslurp.com/sign-up/).  ## Resources - 🔑 [Get API Key](https://app.mailslurp.com/sign-up/)                    - 🎓 [Developer Portal](https://www.mailslurp.com/docs/)           - 📦 [Library SDKs](https://www.mailslurp.com/docs/) - ✍️ [Code Examples](https://www.mailslurp.com/examples) - ⚠️ [Report an issue](https://drift.me/mailslurp)  ## Explore    # noqa: E501

    The version of the OpenAPI document: 6.5.2
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
        'basic_auth': 'BasicAuthOptions',
        'name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'basic_auth': 'basicAuth',
        'name': 'name',
        'url': 'url'
    }

    def __init__(self, basic_auth=None, name=None, url=None, local_vars_configuration=None):  # noqa: E501
        """CreateWebhookOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._basic_auth = None
        self._name = None
        self._url = None
        self.discriminator = None

        if basic_auth is not None:
            self.basic_auth = basic_auth
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url

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
    def url(self):
        """Gets the url of this CreateWebhookOptions.  # noqa: E501

        Public URL on your server that MailSlurp can post WebhookNotification payload to when an email is received. The payload of the submitted JSON is described by https://api.mailslurp.com/schemas/webhook-payload  # noqa: E501

        :return: The url of this CreateWebhookOptions.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateWebhookOptions.

        Public URL on your server that MailSlurp can post WebhookNotification payload to when an email is received. The payload of the submitted JSON is described by https://api.mailslurp.com/schemas/webhook-payload  # noqa: E501

        :param url: The url of this CreateWebhookOptions.  # noqa: E501
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
        if not isinstance(other, CreateWebhookOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateWebhookOptions):
            return True

        return self.to_dict() != other.to_dict()
