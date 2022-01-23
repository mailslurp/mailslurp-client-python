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


class WebhookTestResult(object):
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
        'message': 'str',
        'response': 'WebhookTestResponse',
        'request': 'WebhookTestRequest'
    }

    attribute_map = {
        'message': 'message',
        'response': 'response',
        'request': 'request'
    }

    def __init__(self, message=None, response=None, request=None, local_vars_configuration=None):  # noqa: E501
        """WebhookTestResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message = None
        self._response = None
        self._request = None
        self.discriminator = None

        if message is not None:
            self.message = message
        self.response = response
        self.request = request

    @property
    def message(self):
        """Gets the message of this WebhookTestResult.  # noqa: E501


        :return: The message of this WebhookTestResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this WebhookTestResult.


        :param message: The message of this WebhookTestResult.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def response(self):
        """Gets the response of this WebhookTestResult.  # noqa: E501


        :return: The response of this WebhookTestResult.  # noqa: E501
        :rtype: WebhookTestResponse
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this WebhookTestResult.


        :param response: The response of this WebhookTestResult.  # noqa: E501
        :type: WebhookTestResponse
        """
        if self.local_vars_configuration.client_side_validation and response is None:  # noqa: E501
            raise ValueError("Invalid value for `response`, must not be `None`")  # noqa: E501

        self._response = response

    @property
    def request(self):
        """Gets the request of this WebhookTestResult.  # noqa: E501


        :return: The request of this WebhookTestResult.  # noqa: E501
        :rtype: WebhookTestRequest
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this WebhookTestResult.


        :param request: The request of this WebhookTestResult.  # noqa: E501
        :type: WebhookTestRequest
        """
        if self.local_vars_configuration.client_side_validation and request is None:  # noqa: E501
            raise ValueError("Invalid value for `request`, must not be `None`")  # noqa: E501

        self._request = request

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
        if not isinstance(other, WebhookTestResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookTestResult):
            return True

        return self.to_dict() != other.to_dict()
