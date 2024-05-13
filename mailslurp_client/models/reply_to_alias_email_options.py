# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class ReplyToAliasEmailOptions(object):
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
        'body': 'str',
        'is_html': 'bool',
        'charset': 'str',
        'attachments': 'list[str]',
        'template_variables': 'dict(str, object)',
        'template': 'str',
        'send_strategy': 'str',
        'custom_headers': 'dict(str, str)',
        'use_inbox_name': 'bool',
        'html': 'bool'
    }

    attribute_map = {
        'body': 'body',
        'is_html': 'isHTML',
        'charset': 'charset',
        'attachments': 'attachments',
        'template_variables': 'templateVariables',
        'template': 'template',
        'send_strategy': 'sendStrategy',
        'custom_headers': 'customHeaders',
        'use_inbox_name': 'useInboxName',
        'html': 'html'
    }

    def __init__(self, body=None, is_html=None, charset=None, attachments=None, template_variables=None, template=None, send_strategy=None, custom_headers=None, use_inbox_name=None, html=None, local_vars_configuration=None):  # noqa: E501
        """ReplyToAliasEmailOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._body = None
        self._is_html = None
        self._charset = None
        self._attachments = None
        self._template_variables = None
        self._template = None
        self._send_strategy = None
        self._custom_headers = None
        self._use_inbox_name = None
        self._html = None
        self.discriminator = None

        self.body = body
        self.is_html = is_html
        self.charset = charset
        self.attachments = attachments
        self.template_variables = template_variables
        self.template = template
        self.send_strategy = send_strategy
        self.custom_headers = custom_headers
        self.use_inbox_name = use_inbox_name
        if html is not None:
            self.html = html

    @property
    def body(self):
        """Gets the body of this ReplyToAliasEmailOptions.  # noqa: E501

        Body of the reply email you want to send  # noqa: E501

        :return: The body of this ReplyToAliasEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ReplyToAliasEmailOptions.

        Body of the reply email you want to send  # noqa: E501

        :param body: The body of this ReplyToAliasEmailOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and body is None:  # noqa: E501
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def is_html(self):
        """Gets the is_html of this ReplyToAliasEmailOptions.  # noqa: E501

        Is the reply HTML  # noqa: E501

        :return: The is_html of this ReplyToAliasEmailOptions.  # noqa: E501
        :rtype: bool
        """
        return self._is_html

    @is_html.setter
    def is_html(self, is_html):
        """Sets the is_html of this ReplyToAliasEmailOptions.

        Is the reply HTML  # noqa: E501

        :param is_html: The is_html of this ReplyToAliasEmailOptions.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_html is None:  # noqa: E501
            raise ValueError("Invalid value for `is_html`, must not be `None`")  # noqa: E501

        self._is_html = is_html

    @property
    def charset(self):
        """Gets the charset of this ReplyToAliasEmailOptions.  # noqa: E501

        The charset that your message should be sent with. Optional. Default is UTF-8  # noqa: E501

        :return: The charset of this ReplyToAliasEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._charset

    @charset.setter
    def charset(self, charset):
        """Sets the charset of this ReplyToAliasEmailOptions.

        The charset that your message should be sent with. Optional. Default is UTF-8  # noqa: E501

        :param charset: The charset of this ReplyToAliasEmailOptions.  # noqa: E501
        :type: str
        """

        self._charset = charset

    @property
    def attachments(self):
        """Gets the attachments of this ReplyToAliasEmailOptions.  # noqa: E501

        List of uploaded attachments to send with the reply. Optional.  # noqa: E501

        :return: The attachments of this ReplyToAliasEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this ReplyToAliasEmailOptions.

        List of uploaded attachments to send with the reply. Optional.  # noqa: E501

        :param attachments: The attachments of this ReplyToAliasEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._attachments = attachments

    @property
    def template_variables(self):
        """Gets the template_variables of this ReplyToAliasEmailOptions.  # noqa: E501

        Template variables if using a template  # noqa: E501

        :return: The template_variables of this ReplyToAliasEmailOptions.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._template_variables

    @template_variables.setter
    def template_variables(self, template_variables):
        """Sets the template_variables of this ReplyToAliasEmailOptions.

        Template variables if using a template  # noqa: E501

        :param template_variables: The template_variables of this ReplyToAliasEmailOptions.  # noqa: E501
        :type: dict(str, object)
        """

        self._template_variables = template_variables

    @property
    def template(self):
        """Gets the template of this ReplyToAliasEmailOptions.  # noqa: E501

        Template ID to use instead of body. Will use template variable map to fill defined variable slots.  # noqa: E501

        :return: The template of this ReplyToAliasEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this ReplyToAliasEmailOptions.

        Template ID to use instead of body. Will use template variable map to fill defined variable slots.  # noqa: E501

        :param template: The template of this ReplyToAliasEmailOptions.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def send_strategy(self):
        """Gets the send_strategy of this ReplyToAliasEmailOptions.  # noqa: E501

        How an email should be sent based on its recipients  # noqa: E501

        :return: The send_strategy of this ReplyToAliasEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._send_strategy

    @send_strategy.setter
    def send_strategy(self, send_strategy):
        """Sets the send_strategy of this ReplyToAliasEmailOptions.

        How an email should be sent based on its recipients  # noqa: E501

        :param send_strategy: The send_strategy of this ReplyToAliasEmailOptions.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"SINGLE_MESSAGE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and send_strategy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `send_strategy` ({0}), must be one of {1}"  # noqa: E501
                .format(send_strategy, allowed_values)
            )

        self._send_strategy = send_strategy

    @property
    def custom_headers(self):
        """Gets the custom_headers of this ReplyToAliasEmailOptions.  # noqa: E501

        Optional custom headers  # noqa: E501

        :return: The custom_headers of this ReplyToAliasEmailOptions.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_headers

    @custom_headers.setter
    def custom_headers(self, custom_headers):
        """Sets the custom_headers of this ReplyToAliasEmailOptions.

        Optional custom headers  # noqa: E501

        :param custom_headers: The custom_headers of this ReplyToAliasEmailOptions.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_headers = custom_headers

    @property
    def use_inbox_name(self):
        """Gets the use_inbox_name of this ReplyToAliasEmailOptions.  # noqa: E501

        Optionally use inbox name as display name for sender email address  # noqa: E501

        :return: The use_inbox_name of this ReplyToAliasEmailOptions.  # noqa: E501
        :rtype: bool
        """
        return self._use_inbox_name

    @use_inbox_name.setter
    def use_inbox_name(self, use_inbox_name):
        """Sets the use_inbox_name of this ReplyToAliasEmailOptions.

        Optionally use inbox name as display name for sender email address  # noqa: E501

        :param use_inbox_name: The use_inbox_name of this ReplyToAliasEmailOptions.  # noqa: E501
        :type: bool
        """

        self._use_inbox_name = use_inbox_name

    @property
    def html(self):
        """Gets the html of this ReplyToAliasEmailOptions.  # noqa: E501


        :return: The html of this ReplyToAliasEmailOptions.  # noqa: E501
        :rtype: bool
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this ReplyToAliasEmailOptions.


        :param html: The html of this ReplyToAliasEmailOptions.  # noqa: E501
        :type: bool
        """

        self._html = html

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
        if not isinstance(other, ReplyToAliasEmailOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReplyToAliasEmailOptions):
            return True

        return self.to_dict() != other.to_dict()
