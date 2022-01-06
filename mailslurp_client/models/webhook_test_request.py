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


class WebhookTestRequest(object):
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
        'method': 'str',
        'headers': 'dict(str, str)',
        'payload': 'str'
    }

    attribute_map = {
        'url': 'url',
        'method': 'method',
        'headers': 'headers',
        'payload': 'payload'
    }

    def __init__(self, url=None, method=None, headers=None, payload=None, local_vars_configuration=None):  # noqa: E501
        """WebhookTestRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._method = None
        self._headers = None
        self._payload = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if method is not None:
            self.method = method
        if headers is not None:
            self.headers = headers
        if payload is not None:
            self.payload = payload

    @property
    def url(self):
        """Gets the url of this WebhookTestRequest.  # noqa: E501


        :return: The url of this WebhookTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookTestRequest.


        :param url: The url of this WebhookTestRequest.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def method(self):
        """Gets the method of this WebhookTestRequest.  # noqa: E501


        :return: The method of this WebhookTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this WebhookTestRequest.


        :param method: The method of this WebhookTestRequest.  # noqa: E501
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
    def headers(self):
        """Gets the headers of this WebhookTestRequest.  # noqa: E501


        :return: The headers of this WebhookTestRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this WebhookTestRequest.


        :param headers: The headers of this WebhookTestRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._headers = headers

    @property
    def payload(self):
        """Gets the payload of this WebhookTestRequest.  # noqa: E501


        :return: The payload of this WebhookTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this WebhookTestRequest.


        :param payload: The payload of this WebhookTestRequest.  # noqa: E501
        :type: str
        """

        self._payload = payload

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
        if not isinstance(other, WebhookTestRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookTestRequest):
            return True

        return self.to_dict() != other.to_dict()
