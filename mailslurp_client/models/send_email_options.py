# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class SendEmailOptions(object):
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
        'attachments': 'list[str]',
        'bcc': 'list[str]',
        'body': 'str',
        'cc': 'list[str]',
        'charset': 'str',
        '_from': 'str',
        'is_html': 'bool',
        'reply_to': 'str',
        'send_strategy': 'str',
        'subject': 'str',
        'template': 'str',
        'template_variables': 'object',
        'to': 'list[str]',
        'to_contacts': 'list[str]',
        'to_group': 'str'
    }

    attribute_map = {
        'attachments': 'attachments',
        'bcc': 'bcc',
        'body': 'body',
        'cc': 'cc',
        'charset': 'charset',
        '_from': 'from',
        'is_html': 'isHTML',
        'reply_to': 'replyTo',
        'send_strategy': 'sendStrategy',
        'subject': 'subject',
        'template': 'template',
        'template_variables': 'templateVariables',
        'to': 'to',
        'to_contacts': 'toContacts',
        'to_group': 'toGroup'
    }

    def __init__(self, attachments=None, bcc=None, body=None, cc=None, charset=None, _from=None, is_html=None, reply_to=None, send_strategy=None, subject=None, template=None, template_variables=None, to=None, to_contacts=None, to_group=None, local_vars_configuration=None):  # noqa: E501
        """SendEmailOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attachments = None
        self._bcc = None
        self._body = None
        self._cc = None
        self._charset = None
        self.__from = None
        self._is_html = None
        self._reply_to = None
        self._send_strategy = None
        self._subject = None
        self._template = None
        self._template_variables = None
        self._to = None
        self._to_contacts = None
        self._to_group = None
        self.discriminator = None

        if attachments is not None:
            self.attachments = attachments
        if bcc is not None:
            self.bcc = bcc
        if body is not None:
            self.body = body
        if cc is not None:
            self.cc = cc
        if charset is not None:
            self.charset = charset
        if _from is not None:
            self._from = _from
        if is_html is not None:
            self.is_html = is_html
        if reply_to is not None:
            self.reply_to = reply_to
        if send_strategy is not None:
            self.send_strategy = send_strategy
        if subject is not None:
            self.subject = subject
        if template is not None:
            self.template = template
        if template_variables is not None:
            self.template_variables = template_variables
        if to is not None:
            self.to = to
        if to_contacts is not None:
            self.to_contacts = to_contacts
        if to_group is not None:
            self.to_group = to_group

    @property
    def attachments(self):
        """Gets the attachments of this SendEmailOptions.  # noqa: E501

        Optional list of attachment IDs to send with this email. You must first upload each attachment separately in order to obtain attachment IDs. This way you can reuse attachments with different emails once uploaded.  # noqa: E501

        :return: The attachments of this SendEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this SendEmailOptions.

        Optional list of attachment IDs to send with this email. You must first upload each attachment separately in order to obtain attachment IDs. This way you can reuse attachments with different emails once uploaded.  # noqa: E501

        :param attachments: The attachments of this SendEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._attachments = attachments

    @property
    def bcc(self):
        """Gets the bcc of this SendEmailOptions.  # noqa: E501

        Optional list of bcc destination email addresses  # noqa: E501

        :return: The bcc of this SendEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this SendEmailOptions.

        Optional list of bcc destination email addresses  # noqa: E501

        :param bcc: The bcc of this SendEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._bcc = bcc

    @property
    def body(self):
        """Gets the body of this SendEmailOptions.  # noqa: E501

        Optional contents of email. If body contains HTML then set `isHTML` to true to ensure that email clients render it correctly. You can use moustache template syntax in the email body in conjunction with `toGroup` contact variables or `templateVariables` data. If you need more templating control consider creating a template and using the `template` property instead of the body.  # noqa: E501

        :return: The body of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SendEmailOptions.

        Optional contents of email. If body contains HTML then set `isHTML` to true to ensure that email clients render it correctly. You can use moustache template syntax in the email body in conjunction with `toGroup` contact variables or `templateVariables` data. If you need more templating control consider creating a template and using the `template` property instead of the body.  # noqa: E501

        :param body: The body of this SendEmailOptions.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def cc(self):
        """Gets the cc of this SendEmailOptions.  # noqa: E501

        Optional list of cc destination email addresses  # noqa: E501

        :return: The cc of this SendEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this SendEmailOptions.

        Optional list of cc destination email addresses  # noqa: E501

        :param cc: The cc of this SendEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._cc = cc

    @property
    def charset(self):
        """Gets the charset of this SendEmailOptions.  # noqa: E501

        Optional charset  # noqa: E501

        :return: The charset of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._charset

    @charset.setter
    def charset(self, charset):
        """Sets the charset of this SendEmailOptions.

        Optional charset  # noqa: E501

        :param charset: The charset of this SendEmailOptions.  # noqa: E501
        :type: str
        """

        self._charset = charset

    @property
    def _from(self):
        """Gets the _from of this SendEmailOptions.  # noqa: E501

        Optional from address. If not set the source inbox address will be used for this field. Beware of potential spam penalties when setting this field to an address not used by the inbox. For custom email addresses use a custom domain.  # noqa: E501

        :return: The _from of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this SendEmailOptions.

        Optional from address. If not set the source inbox address will be used for this field. Beware of potential spam penalties when setting this field to an address not used by the inbox. For custom email addresses use a custom domain.  # noqa: E501

        :param _from: The _from of this SendEmailOptions.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def is_html(self):
        """Gets the is_html of this SendEmailOptions.  # noqa: E501

        Optional HTML flag. If true the `content-type` of the email will be `text/html`. Set to true when sending HTML to ensure proper rending on email clients  # noqa: E501

        :return: The is_html of this SendEmailOptions.  # noqa: E501
        :rtype: bool
        """
        return self._is_html

    @is_html.setter
    def is_html(self, is_html):
        """Sets the is_html of this SendEmailOptions.

        Optional HTML flag. If true the `content-type` of the email will be `text/html`. Set to true when sending HTML to ensure proper rending on email clients  # noqa: E501

        :param is_html: The is_html of this SendEmailOptions.  # noqa: E501
        :type: bool
        """

        self._is_html = is_html

    @property
    def reply_to(self):
        """Gets the reply_to of this SendEmailOptions.  # noqa: E501

        Optional replyTo header  # noqa: E501

        :return: The reply_to of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this SendEmailOptions.

        Optional replyTo header  # noqa: E501

        :param reply_to: The reply_to of this SendEmailOptions.  # noqa: E501
        :type: str
        """

        self._reply_to = reply_to

    @property
    def send_strategy(self):
        """Gets the send_strategy of this SendEmailOptions.  # noqa: E501

        Optional strategy to use when sending the email  # noqa: E501

        :return: The send_strategy of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._send_strategy

    @send_strategy.setter
    def send_strategy(self, send_strategy):
        """Sets the send_strategy of this SendEmailOptions.

        Optional strategy to use when sending the email  # noqa: E501

        :param send_strategy: The send_strategy of this SendEmailOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["SINGLE_MESSAGE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and send_strategy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `send_strategy` ({0}), must be one of {1}"  # noqa: E501
                .format(send_strategy, allowed_values)
            )

        self._send_strategy = send_strategy

    @property
    def subject(self):
        """Gets the subject of this SendEmailOptions.  # noqa: E501

        Optional email subject line  # noqa: E501

        :return: The subject of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this SendEmailOptions.

        Optional email subject line  # noqa: E501

        :param subject: The subject of this SendEmailOptions.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def template(self):
        """Gets the template of this SendEmailOptions.  # noqa: E501

        Optional template ID to use for body. Will override body if provided. When using a template make sure you pass the corresponding map of `templateVariables`. You can find which variables are needed by fetching the template itself or viewing it in the dashboard.  # noqa: E501

        :return: The template of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this SendEmailOptions.

        Optional template ID to use for body. Will override body if provided. When using a template make sure you pass the corresponding map of `templateVariables`. You can find which variables are needed by fetching the template itself or viewing it in the dashboard.  # noqa: E501

        :param template: The template of this SendEmailOptions.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def template_variables(self):
        """Gets the template_variables of this SendEmailOptions.  # noqa: E501

        Optional map of template variables. Will replace moustache syntax variables in subject and body or template with the associated values if found.  # noqa: E501

        :return: The template_variables of this SendEmailOptions.  # noqa: E501
        :rtype: object
        """
        return self._template_variables

    @template_variables.setter
    def template_variables(self, template_variables):
        """Sets the template_variables of this SendEmailOptions.

        Optional map of template variables. Will replace moustache syntax variables in subject and body or template with the associated values if found.  # noqa: E501

        :param template_variables: The template_variables of this SendEmailOptions.  # noqa: E501
        :type: object
        """

        self._template_variables = template_variables

    @property
    def to(self):
        """Gets the to of this SendEmailOptions.  # noqa: E501

        List of destination email addresses. Even single recipients must be in array form. Maximum recipients per email depends on your plan. If you need to send many emails try using contacts or contact groups or use a non standard sendStrategy to ensure that spam filters are not triggered (many recipients in one email can affect your spam rating).  # noqa: E501

        :return: The to of this SendEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SendEmailOptions.

        List of destination email addresses. Even single recipients must be in array form. Maximum recipients per email depends on your plan. If you need to send many emails try using contacts or contact groups or use a non standard sendStrategy to ensure that spam filters are not triggered (many recipients in one email can affect your spam rating).  # noqa: E501

        :param to: The to of this SendEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._to = to

    @property
    def to_contacts(self):
        """Gets the to_contacts of this SendEmailOptions.  # noqa: E501

        Optional list of contact IDs to send email to. Manage your contacts via the API or dashboard. When contacts are used the email is sent to each contact separately so they will not see other recipients.  # noqa: E501

        :return: The to_contacts of this SendEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._to_contacts

    @to_contacts.setter
    def to_contacts(self, to_contacts):
        """Sets the to_contacts of this SendEmailOptions.

        Optional list of contact IDs to send email to. Manage your contacts via the API or dashboard. When contacts are used the email is sent to each contact separately so they will not see other recipients.  # noqa: E501

        :param to_contacts: The to_contacts of this SendEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._to_contacts = to_contacts

    @property
    def to_group(self):
        """Gets the to_group of this SendEmailOptions.  # noqa: E501

        Optional contact group ID to send email to. You can create contacts and contact groups in the API or dashboard and use them for email campaigns. When contact groups are used the email is sent to each contact separately so they will not see other recipients  # noqa: E501

        :return: The to_group of this SendEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._to_group

    @to_group.setter
    def to_group(self, to_group):
        """Sets the to_group of this SendEmailOptions.

        Optional contact group ID to send email to. You can create contacts and contact groups in the API or dashboard and use them for email campaigns. When contact groups are used the email is sent to each contact separately so they will not see other recipients  # noqa: E501

        :param to_group: The to_group of this SendEmailOptions.  # noqa: E501
        :type: str
        """

        self._to_group = to_group

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
        if not isinstance(other, SendEmailOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SendEmailOptions):
            return True

        return self.to_dict() != other.to_dict()
